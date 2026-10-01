#!/usr/bin/env python3
"""Render VH01's MODE_TYLER cold-open beats to committed SHANKPIT assets.

LABELED STOPGAP (founder standing rule, 2026-10-01: core deps are PARENA-first): Piper (a local ONNX
TTS run as a subprocess) and the numpy resampler below only exist to unblock the demo. The real work
is a PARENA-native synthesis + resample stack (PARENA stdlib/media/resample.prn, tracked in
EMILY/BACKLOG.md); when that lands this script is retired and its outputs are re-pinned. The engine
side (SHANKPIT's audio_clip_from_pcm16 seam, the PARENA voice_mod decisions) does not change.

What it does, from vh01_beats.tsv (the ONE source of truth for the spoken French AND the HUD
subtitles -- they cannot diverge):
  1. (unless --no-render) renders each spoken line with Piper into --piper-out (needs TYLER_TTS_HOME,
     default ~/.local/share/tyler-tts). Piper is NOT deterministic (the same line rendered twice
     differs ~10% in length), which is why the results are COMMITTED, never rendered in CI.
  2. resamples every clip to 22050 Hz mono PCM16 (the engine's device rate): 44100 Hz sources (Tyler's
     fr_FR-tom-medium) get a 63-tap Kaiser-windowed-sinc low-pass at 10 kHz then 2:1 decimation;
     22050 Hz sources (Hana's fr_FR-siwis-medium) pass through unchanged.
  3. writes SHANKPIT/assets/tyler_vo/vh01_b{beat}_{actor}.wav + MANIFEST.sha256 (sha256, bytes,
     duration per clip).
  4. writes SHANKPIT/packages/simulation/tyler_voice_lines.h: the lines table (beat, speaker,
     offset_ms, dur_ms, file), the per-beat clip length g_tyler_voice_clip_ms[] (== max(offset+dur),
     tested), and the HUD subtitle string for every beat (accent-stripped French + [EN: gloss]).
Usage: render_vh01.py [--shankpit DIR] [--piper-out DIR] [--no-render]
"""
import argparse, hashlib, math, os, subprocess, sys, unicodedata, wave

GAP_MS = 300          # silence between two spoken lines inside one beat
RATE = 22050          # engine device rate
BEATS = 8
SUBTITLE_MAX = 200    # TYLER_COLDOPEN_SUBTITLE_LEN in SHANKPIT's tyler_coldopen.h
VOICE = {"tyler": "fr_FR-tom-medium", "hana": "fr_FR-siwis-medium"}
SPEAKER_ENUM = {"tyler": "TYLER_ACTOR_TYLER", "hana": "TYLER_ACTOR_HANA"}

here = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("--shankpit", default=os.path.join(here, "..", "..", "SHANKPIT"))
ap.add_argument("--piper-out", default=None)
ap.add_argument("--no-render", action="store_true", help="reuse the Piper WAVs already in --piper-out")
args = ap.parse_args()
home = os.environ.get("TYLER_TTS_HOME", os.path.expanduser("~/.local/share/tyler-tts"))
piper_out = args.piper_out or os.path.join(home, "out")
shank = os.path.abspath(args.shankpit)
vo_dir = os.path.join(shank, "assets", "tyler_vo")
hdr_path = os.path.join(shank, "packages", "simulation", "tyler_voice_lines.h")
os.makedirs(piper_out, exist_ok=True)
os.makedirs(vo_dir, exist_ok=True)

# ---------------------------------------------------------------- the script table
tsv_path = os.path.join(here, "vh01_beats.tsv")
tsv_bytes = open(tsv_path, "rb").read()
rows = []
for ln in tsv_bytes.decode("utf-8").splitlines():
    if ln.startswith("#") or not ln.strip():
        continue
    b, actor, hold, fr, en = (ln.split("\t") + [""])[:5]
    rows.append({"beat": int(b), "actor": actor, "hold_ms": int(hold), "fr": fr, "en": en})

def ascii_fold(s):
    """Accent-stripped copy for the engine's ASCII HUD font (e -> e, c -> c)."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return s.replace("’", "'")

# ---------------------------------------------------------------- Piper + resample (stopgap)
def piper_render(row, idx):
    f = os.path.join(piper_out, f"beat{row['beat']}_{row['actor']}_{idx}.wav")
    if args.no_render:
        if not os.path.exists(f):
            sys.exit(f"--no-render: missing {f}")
        return f
    env = dict(os.environ, PYTHONPATH=os.path.join(home, "pylib"))
    subprocess.run([sys.executable, "-m", "piper", "-m",
                    os.path.join(home, "voices", VOICE[row["actor"]] + ".onnx"), "-f", f],
                   input=row["fr"].encode(), env=env, check=True, capture_output=True)
    return f

def read_mono16(path):
    w = wave.open(path)
    assert w.getnchannels() == 1 and w.getsampwidth() == 2, f"{path}: need mono PCM16"
    rate, n = w.getframerate(), w.getnframes()
    raw = w.readframes(n)
    w.close()
    import numpy as np
    return rate, np.frombuffer(raw, dtype="<i2").astype(np.float64)

def to_22050(rate, x):
    import numpy as np
    if rate == RATE:
        return x
    if rate != 2 * RATE:
        sys.exit(f"unsupported source rate {rate} (only {RATE} and {2 * RATE})")
    taps, fc = 63, 10000.0
    n = np.arange(taps) - (taps - 1) / 2.0
    h = np.sinc(2.0 * fc / rate * n) * np.kaiser(taps, 8.6)
    h /= h.sum()
    y = np.convolve(x, h, mode="same")
    return y[::2]

def write_wav(path, x):
    import numpy as np
    pcm = np.clip(np.rint(x), -32768, 32767).astype("<i2")
    w = wave.open(path, "wb")
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE)
    w.writeframes(pcm.tobytes())
    w.close()
    return len(pcm)

def sha256_file(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()

# ---------------------------------------------------------------- build the lines table
lines = []               # one per spoken row
beat_end = [0] * BEATS   # per-beat end of the last spoken line (offset + dur)
spoken_idx = 0
for row in rows:
    if row["actor"] == "-":
        continue
    src = piper_render(row, spoken_idx)
    spoken_idx += 1
    rate, x = read_mono16(src)
    y = to_22050(rate, x)
    name = f"vh01_b{row['beat']}_{row['actor']}.wav"
    out = os.path.join(vo_dir, name)
    n = write_wav(out, y)
    dur = round(1000.0 * n / RATE)
    offset = 0 if beat_end[row["beat"]] == 0 else beat_end[row["beat"]] + GAP_MS
    beat_end[row["beat"]] = offset + dur
    lines.append({**row, "file": f"assets/tyler_vo/{name}", "offset": offset, "dur": dur,
                  "bytes": os.path.getsize(out), "sha": sha256_file(out), "src_rate": rate})
    ok = "OK " if beat_end[row["beat"]] <= row["hold_ms"] else "OVER"
    print(f"beat {row['beat']} {row['actor']:5} src={rate:5}Hz dur={dur:5}ms offset={offset:5} hold={row['hold_ms']} {ok} {name}")

# ---------------------------------------------------------------- subtitles (same rows as the VO)
subs = []
for b in range(BEATS):
    br = [r for r in rows if r["beat"] == b]
    if not br:
        sys.exit(f"beat {b} has no row in {tsv_path}")
    fr = " / ".join(ascii_fold(r["fr"]) for r in br)
    en = " / ".join(r["en"] for r in br if r["en"])
    s = fr + (f" [EN: {en}]" if en else "")
    if len(s) >= SUBTITLE_MAX:
        sys.exit(f"beat {b} subtitle is {len(s)} chars, TYLER_COLDOPEN_SUBTITLE_LEN is {SUBTITLE_MAX}")
    if not all(ord(c) < 128 and c not in '"\\' for c in s):
        sys.exit(f"beat {b} subtitle has a non-ASCII or quote/backslash character: {s!r}")
    subs.append(s)

# ---------------------------------------------------------------- emit the header + manifest
def c_ms(v):
    return f"{v}"

with open(hdr_path, "w") as h:
    h.write("/* Generated by TYLER/tts/render_vh01.py from TYLER/tts/vh01_beats.tsv -- do not edit by hand.\n"
            " * Piper (a LABELED STOPGAP generator) produced the clips under assets/tyler_vo/; they are committed\n"
            " * assets (Piper is not deterministic -- never re-render in CI). The lines table, the per-beat clip\n"
            " * lengths and the HUD subtitles all come from the same TSV rows, so the subtitles can never\n"
            " * contradict what is spoken. tsv_sha256: " + hashlib.sha256(tsv_bytes).hexdigest() + " */\n\n")
    h.write("/* Per-beat length of the spoken audio = max(offset_ms + dur_ms) of that beat's lines (0 = silent).\n"
            " * tyler_coldopen.c stretches each beat's hold to fit it (PARENA tyler/voice-mod). */\n")
    h.write("static const unsigned int g_tyler_voice_clip_ms[%d] = { %s };\n\n" % (BEATS, ", ".join(c_ms(v) for v in beat_end)))
    h.write("#define TYLER_VOICE_LINE_COUNT %d\n\n" % len(lines))
    h.write("/* { beat, speaker, offset_ms into the beat, dur_ms, committed asset path (cwd-relative) } */\n")
    h.write("#define TYLER_VOICE_LINES_INIT { \\\n")
    h.write(", \\\n".join('    { %d, %s, %d, %d, "%s" }' % (l["beat"], SPEAKER_ENUM[l["actor"]], l["offset"], l["dur"], l["file"]) for l in lines))
    h.write(" \\\n}\n\n")
    h.write("/* HUD subtitle per beat: accent-stripped French [EN: gloss]. */\n")
    for b, s in enumerate(subs):
        h.write('#define TYLER_SUBTITLE_%d "%s"\n' % (b, s))

with open(os.path.join(vo_dir, "MANIFEST.sha256"), "w") as m:
    m.write("# sha256  bytes  dur_ms  file  -- generated by TYLER/tts/render_vh01.py; verified by SHANKPIT's make test-tyler-vo\n")
    for l in lines:
        m.write(f"{l['sha']}  {l['bytes']}  {l['dur']}  {os.path.basename(l['file'])}\n")

print("header:", hdr_path)
print("clip_ms:", beat_end)
print("total clip bytes:", sum(l["bytes"] for l in lines))
