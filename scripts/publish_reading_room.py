#!/usr/bin/env python3
"""Publish TYLER episode scripts to the okemily.com reading room (IDUNA /api/v1/tyler/episodes).

The reading room is create-only: POST /api/v1/tyler/episodes with tyler.write, one row per slug, no
update and no delete. So this script is built to be run, checked, and re-run safely:

  * It derives every episode's metadata from episodes/*.md (and EPISODES.md for titles), using the
    same convention the first ten episodes were published with (body = the file with its leading
    H1/H2/H3 header block and first '---' stripped). `--selftest` proves that convention still holds by
    fetching the live bodies of those ten and comparing them byte for byte.
  * It asks the server which slugs already exist and skips them. Re-running publishes only what is new.
  * It posts in publication order (oldest first) because the room's index is "most recently published
    first"; the newest episode therefore sits at the top.
  * It verifies each post (GET the episode back and compare) and, with --verify-public, fetches the
    public page.

Usage (credentials come from the environment, never from this file):

    export IDUNA_BASE_URL=http://localhost:18080     # kubectl port-forward -n emily svc/iduna 18080:8080
    export IDUNA_AGENT_NAME=EMILY-PRIME              # any agent holding tyler.write
    export IDUNA_AGENT_SECRET=...                    # the agent's secret (do not print it)

    scripts/publish_reading_room.py --dry-run                 # print what would be published
    scripts/publish_reading_room.py --selftest                # compare against the 10 live episodes
    scripts/publish_reading_room.py --publish --limit 1       # publish one, check it, stop
    scripts/publish_reading_room.py --publish --verify-public # publish everything new

Only the Python standard library is used.
"""
import argparse
import html
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EP_DIR = os.path.join(REPO, 'episodes')
REGISTRY = os.path.join(REPO, 'EPISODES.md')
PUBLIC = 'https://okemily.com'

# The ten episodes published on 2026-08-06 (before this script existed): file -> slug already live.
LEGACY_SLUGS = {
    'x00_the_custody_of_a_duck.md': 'the-custody-of-a-duck',
    'x01_the_long_quiet.md': 'the-long-quiet',
    'x02_recruitment_drive.md': 'recruitment-drive',
    'x03_the_band_name.md': 'the-band-name',
    'x04_ask_the_frog_not_the_tree.md': 'ask-the-frog-not-the-tree',
    's00e-1_the_determination.md': 'the-determination',
    's00e00_pontiac.md': 'pontiac',
    's00e01_neptune.md': 'neptune',
    's00e02_arrival.md': 'arrival',
    's00e03_july4.md': 'july-4',
}

# --------------------------------------------------------------------------------------- parsing


def strip_header(text):
    """Drop the leading H1/H2/H3 (or bold Build) header block through the first '---' line."""
    lines = text.split('\n')
    for i, line in enumerate(lines[:12]):
        if line.strip() == '---':
            pre = lines[:i]
            if all((not x.strip()) or x.startswith('#') or x.startswith('**Build') for x in pre):
                return '\n'.join(lines[i + 1:]).strip()
            break
    return text.strip()


def slugify(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = s.lower().replace("'", '').replace('’', '')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def registry_titles():
    titles = {}
    with open(REGISTRY, encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^\|\s*([A-Z0-9-]+)\s*\|\s*(.+?)\s*\|.*?(episodes/[^\s|]+\.md)', line)
            if m:
                t = re.sub(r'\s*\((Cold Open[^)]*|Cold Open, Pilot)\)\s*$', '', m.group(2)).strip().strip('"').strip()
                titles[os.path.basename(m.group(3))] = t
    return titles


def parse_build(text):
    for line in text.split('\n')[:14]:
        m = re.search(r'Build\s+(\d{4})', line)
        if m:
            return m.group(1)
    m = re.search(r'Build[: ]+\**\s*(\d{4})', text[:6000])
    return m.group(1) if m else ''


def parse_quoted_title(text):
    lines = text.split('\n')[:6]
    for line in lines[1:4]:
        m = re.match(r'^##\s+"(.+?)"', line)
        if m:
            return m.group(1)
    for line in lines[:2]:
        m = re.search(r'"(.+?)"', line)
        if m:
            return m.group(1)
    return ''


def title_for(fn, text, reg):
    lines = text.split('\n')[:6]
    if fn.startswith('vh') and len(lines) > 1:  # keep the English gloss: "Le Seuil" ("The Threshold")
        m = re.match(r'^##\s+"(.+?)"(?:\s+\("?(.+?)"?\))?\s*$', lines[1])
        if m:
            return m.group(1) + (' (%s)' % m.group(2) if m.group(2) else '')
    t = parse_quoted_title(text)
    if not t or (t == t.upper() and any(c.isalpha() for c in t)):
        t = reg.get(fn) or t
        if t == t.upper() and any(c.isalpha() for c in t):
            t = t.title()
    return t


def group_series_tag(fn):
    b = fn[:-3]
    if b.startswith('s00'):
        m = re.match(r's00e(-?\d+)_', b)
        return 'SERIES X', 'S00E-1' if m.group(1) == '-1' else 'S00E%s' % m.group(1).zfill(2)
    m = re.match(r's06b_e(\d+)_', b)
    if m:
        return 'SEASON 6 (TAKE 2)', 'S6BE%s' % m.group(1)
    m = re.match(r's(\d{2})e(\d{2})_', b)
    if m:
        return 'SEASON %d' % int(m.group(1)), 'S%sE%s' % (m.group(1), m.group(2))
    m = re.match(r'nl(\d+)_', b)
    if m:
        return 'NEVER_LAND', 'NLE%s' % m.group(1)
    m = re.match(r'vh(\d+)_', b)
    if m:
        return 'VALHANNA', 'VH%s · COLD OPEN' % m.group(1)
    if b.startswith('x'):
        return 'SERIES X', 'INTERLUDE, UNNUMBERED'
    raise ValueError('unrecognised episode file: ' + fn)


def sort_key(fn, build):
    if fn.startswith('x'):
        return (0, int(re.match(r'x(\d+)', fn).group(1)), 0, 0)
    m = re.match(r's(\d{2})e(\d{2})_', fn)
    if m and not fn.startswith('s00'):
        return (1, int(m.group(1)), int(m.group(2)), int(build or 0))
    if fn.startswith('nl'):
        return (2, 0, int(re.match(r'nl(\d+)', fn).group(1)), 0)
    if fn.startswith('s06b'):
        return (3, 0, int(re.match(r's06b_e(\d+)', fn).group(1)), 0)
    if fn.startswith('vh'):
        return (4, 0, int(re.match(r'vh(\d+)', fn).group(1)), 0)
    if fn.startswith('s00'):
        return (5, 0, 0, 0)
    raise ValueError(fn)


def load_episodes():
    """Every episode file as a reading-room record, in publication order."""
    reg = registry_titles()
    out = []
    for fn in sorted(os.listdir(EP_DIR)):
        if not fn.endswith('.md'):
            continue
        with open(os.path.join(EP_DIR, fn), encoding='utf-8') as f:
            text = f.read()
        series, tag = group_series_tag(fn)
        build = parse_build(text)
        title = title_for(fn, text, reg)
        flagged = 'Not Canon Unless Promoted' in text[:600]
        if fn.endswith('coldopen_x2_experimental.md'):
            code = fn[:6].upper()
            tag = '%s · COLD OPEN x2 (EXPERIMENTAL; NOT CANON UNLESS PROMOTED)' % code
            series = 'SEASON %d' % int(fn[1:3])
            title = re.sub(r'\s*—.*$', '', title_for(fn, text, reg)) or title
            title = '%s — Memory Render Variant' % re.sub(r'\s*—\s*Memory Render Variant\s*$', '', title)
        elif fn == 's02e06_the_ramp.md':
            tag = 'S02E06 · INFRASTRUCTURE LAYER'
        elif fn.startswith('x') and flagged:
            tag = 'INTERLUDE, UNNUMBERED (NOT CANON UNLESS PROMOTED)'
        if fn in LEGACY_SLUGS:
            slug = LEGACY_SLUGS[fn]
            code = ''
        else:
            code = re.match(r'(s\d{2}e\d{2}|s06b_e\d+|nl\d+|vh\d+|x\d+)_', fn[:-3]).group(1).replace('_', '-')
        if fn in LEGACY_SLUGS:
            pass  # slug and code were fixed above
        elif fn.endswith('coldopen_x2_experimental.md'):
            slug = '%s-cold-open-x2-experimental' % code
        elif fn == 's02e06_the_ramp.md':
            slug = 's02e06-the-ramp'
        else:
            slug = '%s-%s' % (code, slugify(re.sub(r'\s*\(.*\)$', '', title) if fn.startswith('vh') else title))
        out.append(dict(file=fn, slug=slug, title=title, series=series, episode_tag=tag, build=build,
                        body=strip_header(text), _key=sort_key(fn, build)))
    out.sort(key=lambda d: d['_key'])
    slugs = [d['slug'] for d in out]
    dups = sorted({s for s in slugs if slugs.count(s) > 1})
    if dups:
        raise SystemExit('duplicate slugs: %s' % dups)
    bad = [s for s in slugs if not re.match(r'^[a-z0-9-]+$', s)]
    if bad:
        raise SystemExit('invalid slugs: %s' % bad)
    return out


# ------------------------------------------------------------------------------------------- API


class Api:
    def __init__(self, base):
        self.base = base.rstrip('/')
        self.token = None

    def _req(self, method, path, payload=None, auth=False, timeout=60):
        data = json.dumps(payload).encode() if payload is not None else None
        req = urllib.request.Request(self.base + path, data=data, method=method)
        if payload is not None:
            req.add_header('Content-Type', 'application/json')
        if auth:
            req.add_header('Authorization', 'Bearer ' + self.token)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, json.loads(r.read() or b'{}')
        except urllib.error.HTTPError as e:
            raw = e.read()
            try:
                return e.code, json.loads(raw or b'{}')
            except ValueError:
                return e.code, {'error': raw[:200].decode('utf-8', 'replace')}

    def login(self):
        name, secret = os.environ.get('IDUNA_AGENT_NAME'), os.environ.get('IDUNA_AGENT_SECRET')
        if not name or not secret:
            raise SystemExit('IDUNA_AGENT_NAME / IDUNA_AGENT_SECRET not set')
        code, body = self._req('POST', '/api/v1/auth/agent', {'agent_name': name, 'agent_secret': secret})
        if code != 200 or 'access_token' not in body:
            raise SystemExit('IDUNA auth failed: HTTP %s' % code)
        self.token = body['access_token']

    def live_slugs(self):
        code, body = self._req('GET', '/api/v1/tyler/episodes')
        if code != 200:
            raise SystemExit('could not list episodes: HTTP %s' % code)
        return {e['slug']: e for e in body['episodes']}

    def get(self, slug):
        return self._req('GET', '/api/v1/tyler/episodes/' + slug)

    def post(self, ep):
        payload = {k: ep[k] for k in ('slug', 'title', 'series', 'episode_tag', 'build', 'body')}
        return self._req('POST', '/api/v1/tyler/episodes', payload, auth=True, timeout=120)


def public_ok(slug, title):
    url = '%s/tyler/%s/' % (PUBLIC, slug)
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            page = r.read().decode('utf-8', 'replace')
            snippet = (title[:30].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                       .replace('"', '&#34;').replace("'", '&#39;'))  # Go html/template escaping
            return r.status == 200 and snippet in page
    except Exception:
        return False


# ------------------------------------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dry-run', action='store_true', help='print the publication list and exit')
    ap.add_argument('--selftest', action='store_true', help='compare the ten legacy episodes with the live room')
    ap.add_argument('--publish', action='store_true', help='post every episode the room does not have yet')
    ap.add_argument('--limit', type=int, default=0, help='stop after posting N episodes')
    ap.add_argument('--verify-public', action='store_true', help='also fetch each public page after posting')
    ap.add_argument('--base', default=os.environ.get('IDUNA_BASE_URL', PUBLIC))
    args = ap.parse_args()

    eps = load_episodes()
    api = Api(args.base)

    if args.selftest:
        live = api.live_slugs()
        bad = 0
        for ep in eps:
            if ep['file'] in LEGACY_SLUGS:
                code, d = api.get(ep['slug'])
                same = code == 200 and d.get('body') == ep['body'] and d.get('build') == ep['build']
                print('%-24s %s' % (ep['slug'], 'OK' if same else 'DIFFERS'))
                bad += 0 if same else 1
        print('selftest: %d of %d legacy episodes differ' % (bad, len(LEGACY_SLUGS)))
        return 1 if bad else 0

    if args.dry_run or not args.publish:
        try:
            live = api.live_slugs()
        except Exception as e:  # offline dry run is fine
            live = {}
            print('(could not reach the room: %s)' % e)
        todo = [e for e in eps if e['slug'] not in live]
        for i, e in enumerate(todo, 1):
            print('%3d %-48s %-18s %-30s %s %6d  %s' % (i, e['slug'], e['series'], e['episode_tag'][:30], e['build'],
                                                        len(e['body']), e['title'][:50]))
        print('%d episode files, %d already live, %d to publish' % (len(eps), len(eps) - len(todo), len(todo)))
        return 0

    api.login()
    live = api.live_slugs()
    todo = [e for e in eps if e['slug'] not in live]
    print('%d episode files, %d already live, %d to publish' % (len(eps), len(eps) - len(todo), len(todo)))
    posted = 0
    for ep in todo:
        if args.limit and posted >= args.limit:
            break
        for attempt in range(1, 4):
            code, resp = api.post(ep)
            if code == 200:
                break
            if code == 409:  # already exists (e.g. a retry after a timeout that actually succeeded)
                break
            if code in (401, 403):
                api.login()
            if code >= 500 or code in (401, 403, 0):
                time.sleep(2 * attempt)
                gcode, got = api.get(ep['slug'])  # did the failed attempt create it anyway?
                if gcode == 200:
                    code = 200
                    break
                continue
            raise SystemExit('POST %s -> HTTP %s %s' % (ep['slug'], code, resp))
        else:
            raise SystemExit('gave up on %s after 3 attempts' % ep['slug'])
        gcode, got = api.get(ep['slug'])
        if gcode != 200 or got.get('body') != ep['body']:
            raise SystemExit('verification FAILED for %s (HTTP %s)' % (ep['slug'], gcode))
        pub = ''
        if args.verify_public:
            time.sleep(0.3)
            pub = ' public=OK' if public_ok(ep['slug'], ep['title']) else ' public=MISSING'
        posted += 1
        print('[%3d/%d] %s  %s%s' % (posted, len(todo), ep['slug'], 'published' if code == 200 else 'exists', pub), flush=True)
        time.sleep(0.25)
    print('done: %d posted' % posted)
    return 0


if __name__ == '__main__':
    sys.exit(main())
