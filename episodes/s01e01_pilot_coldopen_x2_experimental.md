# TYLER — S01E01, COLD OPEN (x2 / EXPERIMENTAL)
## "Just a Normal Night" — Memory Render Variant
### Build 0007 | GPT-2-Assisted Draft | Not Canon Unless Promoted

---

**PRODUCTION NOTE, READ BEFORE THE SCRIPT:**

Founder, real-time (2026-08-09): *"do the cold open with the normal s1e0 he just smiled and came
in original pilot episode - but use the gpt2 api inference to help you write it - it can only
handle output of characters up to like 512 tokens out but i would do 256 at a time seems good but
start smaller like 16 so the context locks in cleanly"* → *"then amp up the tokens up until you
get to the 200-300 range."*

This is the same cold open as `s01e01_pilot.md` — same beats, same "he smiled" reveal, same
coin-flip button — restaged around a real technical constraint instead of hiding it: the fine-tuned
GPT-2 checkpoint (`gpt2-alpine-c`, served via `emily gpt2 generate` / `POST :8088/generate`) was
called five times against a growing prompt, ramping `max_tokens` 16 → 32 → 64 → 128 → 256 per the
founder's own spec, each output appended and fed back in as the next call's context. The seed
prompt was the real cold open's own "he showed up asking for a glass of water like he lived here
... he just smiled and came in."

**What actually came back is reproduced verbatim in the RENDER inserts below, unedited.** The
small checkpoint holds the thread for the first two calls, then drifts — by the 128- and 256-token
passes it's produced something about a "watermelon" with a jaw and legs that nobody asked for. That
drift is not a bug to paper over here; it's the actual, honest output of doing exactly what was
asked, at the scale that was asked, on the hardware that's actually available (server-side hard
cap 512 tokens, ~4 min/call on this box right now — a known, accepted constraint, not something
fixed in this pass). The experiment is staged as an in-universe **Emily OS memory render** —
Layer 4 attempting to reconstruct the cold open from degraded archival footage, gets more
confident-sounding and less coherent the longer it's allowed to run. That's a real property of
small language models wearing a costume the show already has a place for: Emily OS never explains
herself, and "at least one impossible detail treated as unremarkable" is a standing writer's-room
rule (`CLAUDE.md` Consistency Check). Nobody in-frame reacts to the render glitching. That's the
joke and the honesty at the same time.

---

## COLD OPEN (x2) — [00:00–01:30 + RENDER INSERTS]

*Runtime: 90 seconds, plus four RENDER inserts that can be cut in, cut around, or left as a
DVD-extra-style alternate track depending on how S1E0 vs. S1E1 ultimately gets sequenced.*

---

**[00:00–00:10] — HANDHELD CHAOS, TOO REAL — same as broadcast cut**

```
INT. HALLWAY — DETROIT APARTMENT — NIGHT
```

SHAKY CAMERA pushes through a dim hallway. A cheap LAV MIC crackles.

**PRODUCER (O.S.)**
Keep rolling. Keep rolling. Don't—don't get close—

The furniture is half-shifted, a table on its side. Nobody reacts like it's strange. A soft NEON
GLOW bleeds from the kitchen, impossible, pooling where light shouldn't pool.

**LOWER THIRD (DOC UI):**
```
TUESDAY // "JUST A NORMAL NIGHT" — x2 RENDER TRACK
```

**ON SCREEN (tiny, like a system log, new for this cut):**
```
EMILY OS: RENDER ATTEMPT 1/5 — SOURCE: DEGRADED
CONTEXT WINDOW: 16 TOKENS
```

---

**[RENDER INSERT #1 — 3 seconds, hard cut to black with white system text]**

```
ON SCREEN:
```
> He had a large empty glass, just a few small bottles. He dropped the
> glass on the ground, then turned it over. The water poured slowly in, but eventually the
> water was clean.

**LOWER THIRD:**
```
RENDER 1/5 — 16 TOKENS — HOLDING
```

*(This is the actual model output, unedited. It's wrong about almost everything — there's no
dropped glass in the real interview — but it's wrong in the right shape: a glass, water, someone
arriving. The render is reaching for the real memory and almost touching it.)*

---

**[00:10–00:25] — INTERVIEW: THE DENIAL — same as broadcast cut**

```
INT. LIVING ROOM — LATER (INTERVIEW SETUP)
```

CUT TO: A calm sit-down interview. This is **SUBJECT #1** — the exhausted serenity of someone who
stopped trying to explain things years ago.

**SUBJECT #1**
He showed up asking for a glass of water
like he lived here.
Then he asked what year it was.

*(beat)*

Like—politely. Like it was my fault.

**PRODUCER (O.S.)**
And you let him in?

**SUBJECT #1**
*(longer pause than expected)*
…Yeah.

*(even longer pause)*

Because he smiled.

**ON SCREEN (tiny, like a system log):**
```
PRESSURE ↑
EMILY OS: RENDER ATTEMPT 2/5 — CONTEXT WINDOW: 32 TOKENS
```

---

**[RENDER INSERT #2 — 4 seconds]**

> glass on the ground, then turned it over. The water poured slowly in, but eventually the water
> was clean. "Is that the Watermelon?" asked the man with the big

**LOWER THIRD:**
```
RENDER 2/5 — 32 TOKENS — A NAME IS FORMING. IT IS THE WRONG NAME.
```

---

**[00:25–00:40] — THE FIRST RECEIPT — same as broadcast cut**

HARD CUT: Security cam footage. Grainy, overexposed. Timestamp reads **1901**. A crowded city
street, period dress, horse-drawn carts — and there, against the flow of pedestrians, a man in a
classic suit, calm eyes, unhurried.

He turns toward the camera. Directly. Like he knew where it was. He tips his hat.

**SUBJECT #1 (V.O.)**
That's him.

**PRODUCER (V.O.)**
That's impossible.

**SUBJECT #1 (V.O.)**
Yeah.

**ON SCREEN:**
```
MIGRATION EVENT DETECTED
EMILY OS: RENDER ATTEMPT 3/5 — CONTEXT WINDOW: 64 TOKENS — CONFIDENCE RISING
```

---

**[RENDER INSERT #3 — 6 seconds, the render is starting to look proud of itself]**

> lidded glasses. "Yes, that is the watermelon. Its
> spill has a watermelon flavor. No
> other word for it, but I know its taste. Its
> sweet, but its fruit flavour is very sweet.

**LOWER THIRD:**
```
RENDER 3/5 — 64 TOKENS — THE SYSTEM IS NOW CERTAIN. THE SYSTEM IS NOW WRONG.
```

*(Nobody on camera acknowledges this. Standing writer's-room rule: Emily OS never explains
herself. She also, apparently, never apologizes.)*

---

**[00:40–00:55] — TYLER ENTERS LIKE A RUMOR — same as broadcast cut**

```
INT. KITCHEN — SAME APARTMENT — CONTINUOUS
```

Back to handheld. **TYLER** stands at the sink, washing his hands. He looks ordinary. He could be
from any decade between 1890 and 2040 without adjustment. He dries his hands too carefully.

He glances at the camera without turning fully.

**TYLER**
You're early.

**CAMERA OP**
Who are you?

Tyler dries the last finger. Sets the towel down. Turns.

**TYLER**
Depends who's asking.

He smiles. The smile is gentle and practiced.

**TYLER (CONT.)**
Is this the cut where you make me the villain?

**ON SCREEN (quiet):**
```
AH SHOCK: LISTINGS SPIKE
EMILY OS: RENDER ATTEMPT 4/5 — CONTEXT WINDOW: 128 TOKENS — DRIFT DETECTED, CONTINUING ANYWAY
```

---

**[RENDER INSERT #4 — 8 seconds]**

> "When
> are you going to get them?"
>
> "Not yet. If I need to, I'll get them tomorrow."
>
> At this, Zidane
> started to move, moving. He held the stone with one hand. He held it
> askew, until almost all the stones stopped moving.

**LOWER THIRD:**
```
RENDER 4/5 — 128 TOKENS — WHO IS ZIDANE
```

*(Nobody in the show's universe knows who Zidane is either. That's fine. Not every render has to
resolve. This is a documentary about a man who won't stay in his own year, being narrated by a
system that won't stay on its own topic. They deserve each other.)*

---

**[00:55–01:25] — FACTIONS + THE IMPOSSIBLE ACT — same as broadcast cut**

A door opens. Someone STEPS IN — clean suit, calm posture. The room's temperature changes. Not
metaphorically.

**SUIT**
We can end this quietly.

**TYLER**
You've never ended anything.

*(beat)*

You only rename it.

**ON SCREEN:**
```
CONFLICT ↑
EMILY OS: RENDER ATTEMPT 5/5 — CONTEXT WINDOW: 256 TOKENS — FINAL PASS
```

Tyler pulls a coin from his jacket. Flips it. It hangs one beat longer than physics allows. The
date on its face changes every time the lens focuses, always half a second too late.

**CAMERA OP (whisper)**
What the—

**TYLER**
Shh.

He looks straight into the lens.

**TYLER**
If you keep filming, you become part of it.

*(a beat)*

But you're going to keep filming.

---

**[RENDER INSERT #5 — 11 seconds, the longest render, the one that breaks all the way]**

> "Might as well get the watermelon,"
> said the man. Zidane
> came to the stone with the other hand and laid
> him down on the ground. A deep breath broke out from the
> watermelon's mouth that, just a few drops at a
> time, broke the watermelon's jaw
> away. "Whoa, it's going to hurt really good."
>
> He lay on the ground. The men
> had not eaten the watermelon for almost four days. There was
> no way to tell what happened. He began to walk.

**LOWER THIRD:**
```
RENDER 5/5 — 256 TOKENS — SOURCE NO LONGER RECOGNIZABLE AS SOURCE
```

*(This is the longest, most confident, least true render of the five. It has a jaw. It has legs.
It is going to hurt really good. Longer context did not mean better memory here — it meant more
runway to leave the memory behind. That's the actual finding, not just the bit: five real calls
to a real small model, ramped exactly the way it was asked to be ramped, and the more room it got,
the further it walked from "he just smiled and came in.")*

---

**[01:25–01:30] — TITLE HIT — same as broadcast cut**

SMASH CUT TO BLACK.

**TITLE:**
```
TYLER
A DOCUMENTARY ABOUT A MAN WHO WON'T STAY IN HIS OWN YEAR
```

**ON SCREEN, final card, new for this cut:**
```
FIVE RENDERS. ONE MEMORY. ZERO WATERMELONS IN THE ORIGINAL FOOTAGE.
```

**END LOG:**
```
BIRD CORRECTION PENDING
RENDER TRACK: ARCHIVED, NOT PROMOTED TO CANON
```

---

## Notes for whoever picks this up next

- **This is a variant, not a replacement.** `s01e01_pilot.md`'s cold open is still the broadcast
  cut. This file is the "DVD extra" / experimental alternate — a real place for it would be
  `compiled/s01e01/alternates/`, once/if this gets pushed through the MPT compilation pipeline
  (`engine/moneyprinter_pipeline.md`).
- **The five RENDER inserts are the real GPT-2 output, byte-for-byte**, from
  `gpt2-alpine-c`'s `emily-ft` checkpoint, `temperature=0.85`, five sequential `POST
  :8088/generate` calls at `max_tokens` 16/32/64/128/256, each fed the full growing transcript as
  its prompt. Nothing in the quoted blocks was rewritten, smoothed, or cherry-picked between
  takes — one run, kept in full, including the parts that don't work.
- **Real, unresolved question for whoever scopes this further**: does "Zidane" and the watermelon
  become an actual recurring in-universe glitch-motif (Emily OS has a stable hallucination it
  keeps returning to — genuinely spooky, worth a callback later), or was this just what one
  temperature setting on one small checkpoint happened to produce on one day, not worth chasing?
  Flagging the question, not answering it — that's a real creative call, not a technical one.
- **Latency, stated plainly**: each of the five calls took roughly 3–5 minutes on this box (single
  4-core VM, single-threaded inference server, load average ~10 at generation time). Founder is
  already aware and asked to work within the constraint for now rather than optimize it as part of
  this pass — noted here so the next person doesn't rediscover the same thing from scratch.
