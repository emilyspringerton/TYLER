#!/usr/bin/env python3
"""Batch-run MoneyPrinterTurbo over TYLER episode scripts. Stdlib only, sequential, resumable.

  mpt_batch.py --dry-run                      # list what would run, write payloads, no API calls
  mpt_batch.py --glob 'episodes/s0[1-3]*.md'  # a subset
  mpt_batch.py --limit 10 --min-free-gb 3     # stop early; refuse to run when disk is low

Per episode <stem> (full filename stem, so s02e06_* duplicates don't collide):
  compiled/<stem>/mpt_payload.json   request sent
  compiled/<stem>/mpt_state.json     {task_id, state: submitted|complete|failed, ...}  (resume key)
  compiled/<stem>/alternates/*.mp4   copied from MPT's storage/tasks/<task_id>/
If compiled/<stem>/narration.txt exists it is sent as video_script (exact narration); otherwise only
a topic is sent and MPT's own LLM writes the narration. Real MPT API: POST /videos, GET /tasks/<id>
(state: 1 complete, -1 failed, 4 processing); port 8990 (8080 is IDUNA)."""
import argparse, glob, json, os, re, shutil, sys, time, urllib.request

TYLER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MPT_STORAGE = "/home/fatbaby/MoneyPrinterTurbo/storage/tasks"

def topic_for(text, stem):
    m = re.search(r"^\*\*MPT_TOPIC:\*\*\s*(.+)$", text, re.M)
    if m: return m.group(1).strip()
    def f(k):
        m = re.search(rf"^\*\*{k}:\*\*\s*(.+)$", text, re.M); return m.group(1).strip() if m else ""
    title = re.sub(r"^\d+\s*—\s*", "", f("EPISODE")) or re.sub(r"^#+\s*", "", text.splitlines()[0])
    return f"A documentary episode: {title}. Location: {f('LOCATION') or 'unknown'}. {f('TIMELINE POSITION')}".strip()

def payload(topic, script, a):
    p = {"video_subject": topic, "video_language": "en", "voice_name": a.voice, "video_aspect": a.aspect,
         "video_count": a.count, "subtitle_enabled": True, "subtitle_font_name": "Anton",
         "subtitle_font_size": 60, "subtitle_color": "#FFFFFF", "subtitle_stroke_color": "#000000",
         "subtitle_stroke_width": 1.5, "bgm_type": "random", "bgm_volume": 0.1,
         "video_clip_duration": 4, "video_terms": "documentary, urban, night, candid footage, film noir"}
    if script: p["video_script"] = script
    return p

def call(api, path, body=None):
    req = urllib.request.Request(api + path, data=None if body is None else json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r: return json.load(r)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--glob", default="episodes/*.md"); ap.add_argument("--api", default="http://127.0.0.1:8990/api/v1")
    ap.add_argument("--voice", default="en-GB-RyanNeural-Male"); ap.add_argument("--aspect", default="9:16")
    ap.add_argument("--count", type=int, default=1); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--min-free-gb", type=float, default=3.0); ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--retry-failed", action="store_true")
    a = ap.parse_args()
    files = sorted(glob.glob(os.path.join(TYLER, a.glob))); done = ran = 0
    for f in files:
        stem = os.path.basename(f)[:-3]; out = os.path.join(TYLER, "compiled", stem)
        sp = os.path.join(out, "mpt_state.json")
        st = json.load(open(sp)) if os.path.exists(sp) else {}
        if st.get("state") == "complete" or (st.get("state") == "failed" and not a.retry_failed):
            done += 1; continue
        if a.limit and ran >= a.limit: break
        text = open(f, encoding="utf-8").read(); nar = os.path.join(out, "narration.txt")
        script = open(nar, encoding="utf-8").read() if os.path.exists(nar) else ""
        p = payload(topic_for(text, stem), script, a)
        if a.dry_run:
            print(f"[dry] {stem}: {'script' if script else 'topic'} | {p['video_subject'][:80]}"); ran += 1; continue
        os.makedirs(os.path.join(out, "alternates"), exist_ok=True)
        json.dump(p, open(os.path.join(out, "mpt_payload.json"), "w"), indent=1, ensure_ascii=False)
        free = shutil.disk_usage(MPT_STORAGE if os.path.isdir(MPT_STORAGE) else "/").free / 2**30
        if free < a.min_free_gb: print(f"STOP: {free:.1f}GB free < {a.min_free_gb}GB"); break
        try:
            tid = call(a.api, "/videos", p)["data"]["task_id"]
            st = {"task_id": tid, "state": "submitted"}; json.dump(st, open(sp, "w"))
            t0 = time.time(); r = {}
            while time.time() - t0 < a.timeout:
                time.sleep(10); r = call(a.api, f"/tasks/{tid}")["data"]
                if r.get("state") in (1, -1): break
                print(f"  {stem} progress {r.get('progress')}%")
            if r.get("state") == 1:
                n = 0
                for v in glob.glob(os.path.join(MPT_STORAGE, tid, "final-*.mp4")):
                    shutil.copy(v, os.path.join(out, "alternates")); n += 1
                st.update(state="complete", videos=n)
            else: st.update(state="failed", detail=str(r)[:300])
        except Exception as e: st = {"state": "failed", "detail": repr(e)}
        json.dump(st, open(sp, "w")); ran += 1; print(f"{stem}: {st['state']}")
    print(f"episodes matched={len(files)} skipped(already done/failed)={done} processed={ran}")
main()
