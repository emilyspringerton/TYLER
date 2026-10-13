# TYLER voice (MODE_TYLER)

`scenes/<scene>.tsv` is the single source for the spoken French and the HUD subtitles of every
SHANKPIT MODE_TYLER scene (vh01, e03, fb01, vh02). `render_scenes.py` renders them with Piper
(a labeled stopgap) **at SHANKPIT build time, in CI** -- nothing it writes is committed.

    render_scenes.py --shankpit ../SHANKPIT --check-only   # no Piper: validate + subtitle drift check
    # CI: SHANKPIT's release.yml checks this repo out and runs the full render.

The drift check fails if a scene's subtitle in SHANKPIT's `tyler_*_coldopen.c` no longer matches the
TSV's accent-stripped French + `[EN: ...]`. Edit the TSV and the C table together.
