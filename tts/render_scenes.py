#!/usr/bin/env python3
"""Render every MODE_TYLER scene's French VO at BUILD time (CI). Nothing this writes is committed.

LABELED STOPGAP (core deps are PARENA-first): Piper (local ONNX TTS, subprocess) + the numpy
resampler exist only to unblock the demo; the real stack is PARENA-native synthesis (tracked in
EMILY/BACKLOG.md). When that lands this script retires and the engine side does not change.

For each scene in scenes/*.tsv (the ONE source of truth for spoken French + HUD subtitles):
  1. validates the TSV and builds each beat's subtitle (accent-stripped French + [EN: gloss]);
  2. DRIFT CHECK: every beat's subtitle must appear verbatim in SHANKPIT's committed
     packages/simulation/<scene c file> -- so every scene's HUD text is French and matches the VO;
  3. (unless --check-only) renders each spoken row with Piper, resamples to 22050 Hz mono PCM16,
     writes <out-assets>/<scene>_b<beat>_<actor>.wav + one MANIFEST.sha256 (sha256, bytes, dur_ms);
  4. writes <out-headers>/tyler_voice_<scene>.h: lines table + per-beat clip length.
Usage (CI):  render_scenes.py --shankpit . --voices-dir DIR --out-assets assets/tyler_vo \
                              --out-headers packages/simulation/gen
Local, no Piper:  render_scenes.py --shankpit ../SHANKPIT --check-only
"""
import argparse, hashlib, os, subprocess, sys, tempfile, unicodedata, wave

GAP_MS, RATE, BEATS, SUBTITLE_MAX = 300, 22050, 8, 200
V_TOM, V_SIWIS = "fr_FR-tom-medium", "fr_FR-siwis-medium"
SCENES = [  # id, tsv, SHANKPIT C file that carries the subtitles, voice per scripted slot
    dict(id="vh01", c="tyler_coldopen.c",        voices={"tyler": V_TOM,   "hana": V_SIWIS}),
    dict(id="e03",  c="tyler_e03_coldopen.c",    voices={"tyler": V_TOM,   "hana": V_SIWIS}),
    dict(id="fb01", c="tyler_fb01_coldopen.c",   voices={"tyler": V_TOM,   "hana": V_SIWIS}),
    dict(id="vh02", c="tyler_vh02_coldopen.c",   voices={"tyler": V_SIWIS, "hana": V_TOM}),  # Cam / the sound guy
    dict(id="vh03", c="tyler_vh03_coldopen.c",   voices={"tyler": V_SIWIS, "hana": V_TOM}),  # Cam / the sound guy (+PA, +radio)
    dict(id="vh04", c="tyler_vh04_coldopen.c",   voices={"tyler": V_SIWIS, "hana": V_TOM}),  # Cam / the Auditor
]
SPEAKER_ENUM = {"tyler": "TYLER_ACTOR_TYLER", "hana": "TYLER_ACTOR_HANA"}

here = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("--shankpit", required=True, help="SHANKPIT checkout (for the subtitle drift check)")
ap.add_argument("--check-only", action="store_true", help="validate + drift-check only; no Piper, no outputs")
ap.add_argument("--voices-dir", help="dir holding fr_FR-tom-medium.onnx / fr_FR-siwis-medium.onnx")
ap.add_argument("--out-assets", default="assets/tyler_vo")
ap.add_argument("--out-headers", default="packages/simulation/gen")
args = ap.parse_args()
sim = os.path.join(os.path.abspath(args.shankpit), "packages", "simulation")

def ascii_fold(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).replace("’", "'")

def load(scene):
    rows = []
    path = os.path.join(here, "scenes", scene["id"] + ".tsv")
    for ln in open(path, encoding="utf-8").read().splitlines():
        if ln.startswith("#") or not ln.strip():
            continue
        b, actor, hold, fr, en = (ln.split("\t") + [""])[:5]
        if actor not in ("tyler", "hana", "-"):
            sys.exit(f"{path}: bad actor {actor!r}")
        rows.append({"beat": int(b), "actor": actor, "hold_ms": int(hold), "fr": fr, "en": en})
    return rows, open(path, "rb").read()

def subtitles(scene, rows):
    csrc = open(os.path.join(sim, scene["c"]), encoding="utf-8").read()
    out = []
    for b in range(BEATS):
        br = [r for r in rows if r["beat"] == b]
        if not br:
            sys.exit(f"{scene['id']}: beat {b} has no row")
        fr = " / ".join(ascii_fold(r["fr"]) for r in br)
        en = " / ".join(r["en"] for r in br if r["en"])
        s = fr + (f" [EN: {en}]" if en else "")
        if len(s) >= SUBTITLE_MAX:
            sys.exit(f"{scene['id']} beat {b}: subtitle is {len(s)} chars (max {SUBTITLE_MAX - 1}): {s}")
        if not all(ord(c) < 128 and c not in '"\\' for c in s):
            sys.exit(f"{scene['id']} beat {b}: non-ASCII / quote / backslash in subtitle: {s!r}")
        if s not in csrc:
            sys.exit(f"DRIFT: {scene['id']} beat {b} subtitle not found in {scene['c']}:\n  {s}")
        out.append(s)
    return out

# ----------------------------------------------------------- Piper + resample (stopgap)
def piper_render(voice, text, dst):
    model = os.path.join(args.voices_dir, voice + ".onnx")
    subprocess.run([sys.executable, "-m", "piper", "-m", model, "-f", dst],
                   input=text.encode(), check=True, capture_output=True)

def read_mono16(path):
    import numpy as np
    w = wave.open(path)
    assert w.getnchannels() == 1 and w.getsampwidth() == 2, f"{path}: need mono PCM16"
    rate, raw = w.getframerate(), w.readframes(w.getnframes())
    w.close()
    return rate, np.frombuffer(raw, dtype="<i2").astype(np.float64)

def to_22050(rate, x):
    import numpy as np
    if rate == RATE:
        return x
    if rate != 2 * RATE:
        sys.exit(f"unsupported source rate {rate}")
    n = np.arange(63) - 31.0
    h = np.sinc(2.0 * 10000.0 / rate * n) * np.kaiser(63, 8.6)
    return np.convolve(x, h / h.sum(), mode="same")[::2]

def write_wav(path, x):
    import numpy as np
    pcm = np.clip(np.rint(x), -32768, 32767).astype("<i2")
    w = wave.open(path, "wb")
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE)
    w.writeframes(pcm.tobytes()); w.close()
    return len(pcm)

manifest = []
for sc in SCENES:
    rows, tsv_bytes = load(sc)
    subs = subtitles(sc, rows)
    print(f"{sc['id']}: {len(rows)} rows, {BEATS} subtitles OK (French, match {sc['c']})")
    if args.check_only:
        continue
    if not args.voices_dir:
        sys.exit("--voices-dir required unless --check-only")
    os.makedirs(args.out_assets, exist_ok=True)
    os.makedirs(args.out_headers, exist_ok=True)
    lines, beat_end, used = [], [0] * BEATS, {}
    with tempfile.TemporaryDirectory() as tmp:
        for i, row in enumerate(r for r in rows if r["actor"] != "-"):
            raw = os.path.join(tmp, f"{i}.wav")
            piper_render(sc["voices"][row["actor"]], row["fr"], raw)
            rate, x = read_mono16(raw)
            k = used.get((row["beat"], row["actor"]), 0)
            used[(row["beat"], row["actor"])] = k + 1
            name = f"{sc['id']}_b{row['beat']}_{row['actor']}" + (f"_{k}" if k else "") + ".wav"
            out = os.path.join(args.out_assets, name)
            n = write_wav(out, to_22050(rate, x))
            dur = round(1000.0 * n / RATE)
            off = 0 if beat_end[row["beat"]] == 0 else beat_end[row["beat"]] + GAP_MS
            beat_end[row["beat"]] = off + dur
            sha = hashlib.sha256(open(out, "rb").read()).hexdigest()
            lines.append({**row, "file": f"assets/tyler_vo/{name}", "offset": off, "dur": dur})
            manifest.append(f"{sha}  {os.path.getsize(out)}  {dur}  {name}")
            print(f"  beat {row['beat']} {row['actor']:5} {dur:5}ms offset={off:5} hold={row['hold_ms']} "
                  f"{'OK ' if beat_end[row['beat']] <= row['hold_ms'] else 'OVER'} {name}")
    S = sc["id"]
    with open(os.path.join(args.out_headers, f"tyler_voice_{S}.h"), "w") as h:
        h.write(f"/* GENERATED at build time by TYLER/tts/render_scenes.py from scenes/{S}.tsv (tsv_sha256 "
                f"{hashlib.sha256(tsv_bytes).hexdigest()}). Not committed; do not edit. */\n")
        h.write(f"static const unsigned int g_tyler_{S}_voice_clip_ms[{BEATS}] = {{ "
                + ", ".join(map(str, beat_end)) + " };\n")
        h.write(f"#define TYLER_{S.upper()}_VOICE_LINE_COUNT {len(lines)}\n")
        h.write(f"#define TYLER_{S.upper()}_VOICE_LINES_INIT {{ \\\n")
        h.write(", \\\n".join('    { %d, %s, %d, %d, "%s" }' % (l["beat"], SPEAKER_ENUM[l["actor"]], l["offset"], l["dur"], l["file"])
                              for l in lines))
        h.write(" \\\n}\n")

if not args.check_only:
    with open(os.path.join(args.out_assets, "MANIFEST.sha256"), "w") as m:
        m.write("# sha256  bytes  dur_ms  file  -- generated at build time by TYLER/tts/render_scenes.py\n")
        m.write("\n".join(manifest) + "\n")
    print("rendered", len(manifest), "clips ->", args.out_assets)
