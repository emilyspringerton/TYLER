# TYLER — S01E02, COLD OPEN (x2 / EXPERIMENTAL)
## "The School That Isn't There" — Memory Render Variant
### Build 0007 | GPT-2-Assisted Draft | Not Canon Unless Promoted

---

**PRODUCTION NOTE, READ BEFORE THE SCRIPT:**

Founder, real-time (2026-08-09), after the S01E01 x2 experiment
(`s01e01_pilot_coldopen_x2_experimental.md`) landed: *"well done following the instructions for
using gpt2 in a tyler episode - go ahead and use the next script in the cannon and give it the
same treatment please using appropriate series and episode identifiers."*

Confirmed the actual next canonical script first rather than guess: `TYLER/episodes/` lists
`s01e01_pilot.md` → `s01e02_school.md` in sequence — the S00 files (`pontiac`, `neptune`,
`arrival`, `july4`, `the_determination`) are a separate prequel/interlude numbering, not next in
the S01 line. **This is S01E02, "The School That Isn't There," not S00 material** — the founder
asked for correct identifiers this time, and getting that right up front is the actual ask.

Same method as the first experiment: five sequential `POST :8088/generate` calls against
`gpt2-alpine-c`'s fine-tuned checkpoint, `max_tokens` ramping 16 → 32 → 64 → 128 → 256, each
output appended and fed back as the next call's growing context. Seed prompt was S01E02's own
cold-open hook — *"It wasn't there Thursday. Then Friday morning there's a school."*

**What came back this run is a genuinely different flavor of drift than S01E01's**, reproduced
verbatim in the RENDER inserts below. Where the pilot's render wandered into a wholly invented
watermelon, this one stayed closer to the seed's own rhythm — it picked up the "wasn't there
Thursday / there Friday" cadence and extended it on its own ("Monday morning, it's a cemetery.
Friday morning, it's a cemetery.") before drifting into unprompted screenplay formatting
(`INT.`/`SOUND OF` cues it was never told to produce) and, by the final 256-token pass, an
unprompted swerve into *"the first year of World War II... no airplanes, no planes to do
anything... the only planes that have survived are planes."* Nobody asked the model to associate
a temporal-displacement horror show with WWII. It did anyway. Whether that's worth a real
narrative thread later is a founder call, not a technical one — flagged, not decided, same as the
S01E01 render's "Zidane" question.

---

## COLD OPEN (x2) — [00:00–02:00 + RENDER INSERTS]

---

**[00:00–00:30] — THE LOT WAS EMPTY YESTERDAY — same as broadcast cut**

```
EXT. DETROIT STREET — MORNING
```

Establishing shot. A city block in Detroit. A chain-link fence around a vacant lot that has been
vacant for a generation.

Except.

The lot is not vacant. There is a school. Three stories. Brick that is wrong for the decade.

**NEIGHBOR (V.O., later interview):**
It wasn't there Thursday. I walked past the lot every morning for eleven years.

*(pause)*

Then Friday morning there's a school.

**ON SCREEN (tiny, like a system log, new for this cut):**
```
EMILY OS: RENDER ATTEMPT 1/5 — SOURCE: DEGRADED
CONTEXT WINDOW: 16 TOKENS
```

---

**[RENDER INSERT #1 — 3 seconds]**

> Monday morning, it's more like a cemetery. It's vacant. Monday morning

**LOWER THIRD:**
```
RENDER 1/5 — 16 TOKENS — IT HAS FOUND A RHYTHM. IT IS NOT THE RIGHT RHYTHM YET.
```

*(The render latches onto the seed's own cadence — day names, a state, a repeat — before it has
anything real to say with it. Sixteen tokens isn't long enough to be wrong yet. It's barely long
enough to be a shape.)*

---

**[00:30–01:15] — DOCUMENTARY CREW ARRIVES — same as broadcast cut**

```
EXT. DETROIT PREPARATORY INSTITUTE — CONTINUOUS
```

Documentary Unit A van parks half a block down. The Camera Op brings the camera up. Frames the
school. The frame feels wrong in a way the Camera Op won't be able to describe that night.

**PRODUCER (O.S.)**
Full exterior coverage. Wide first, then look for him in the student flow.

**CAMERA OP**
*(not quite under their breath)*
How would he be in the student flow?

**PRODUCER (O.S.)**
He is always in the flow. That's what the flow is for.

**ON SCREEN:**
```
LOWER-THIRD: STUDENT SUBJECTS — UNIDENTIFIED
EMILY OS: RENDER ATTEMPT 2/5 — CONTEXT WINDOW: 32 TOKENS
```

---

**[RENDER INSERT #2 — 4 seconds]**

> , it's a cemetery. Friday morning, it's a cemetery. And then Monday morning, it's an old house.
> It's just the same old house

**LOWER THIRD:**
```
RENDER 2/5 — 32 TOKENS — THE SCHOOL IS BECOMING A HOUSE. NOBODY ASKED IT TO.
```

*(This is the render's own idea, not a prompt leak — nothing in the seed mentions a house. Whether
that's the render reaching for "Detroit Preparatory Institute" and landing somewhere adjacent, or
reaching for something else entirely, is exactly the kind of question Layer 4 would never answer
directly.)*

---

**[01:15–02:00] — THE BUILDING READS — same as broadcast cut**

```
INT. DETROIT PREPARATORY INSTITUTE — LOBBY — CONTINUOUS
```

The crew enters. The lobby is correct. Institutional. The Camera Op's lens finds a fire exit map
on the lobby wall. The font is not standard — eggshell white on white, the specific weight seen
once before, in the pilot, on a modal tile that appeared on no device and vanished after eleven
seconds.

**ON SCREEN:**
```
LOWER-THIRD: EMILY OS — ARCHITECTURAL PRESENCE
CUSTODY PROTOCOL: ACTIVE
EMILY OS: RENDER ATTEMPT 3/5 — CONTEXT WINDOW: 64 TOKENS — CONFIDENCE RISING
```

---

**[RENDER INSERT #3 — 6 seconds]**

> . The driveway is old. It's just the same old driveway. It's really, really old. It's pretty
> much the same in any city. Everything's been vacant for the last 100 years now. INT. ROOFTOP —
> HOUSE OF EZ HOUSE — NIGHT. A young woman in her evening hood

**LOWER THIRD:**
```
RENDER 3/5 — 64 TOKENS — THE RENDER HAS STARTED WRITING SLUGLINES. NOBODY TAUGHT IT THAT.
```

*(Nobody fed this model screenplay format as an instruction — only as the shape of the seed text
itself. By 64 tokens it's started producing its own `INT.` cues unprompted. That's the render
believing it understands the medium, not just the memory.)*

---

## ACT I, RESTAGED — THE RENDER KEEPS GOING PAST WHERE THE BROADCAST CUT WOULD STOP

*(The real Act I — the library, the hallway, room 204 marked CUSTODY — is untouched, still
`s01e02_school.md`'s own. This variant doesn't restage all of Act I; it lets the render run two
more passes past the cold open's natural end, because that's where the ramp specification said to
go, and stopping early would have been editing the finding.)*

**ON SCREEN:**
```
EMILY OS: RENDER ATTEMPT 4/5 — CONTEXT WINDOW: 128 TOKENS — DRIFT DETECTED, CONTINUING ANYWAY
```

---

**[RENDER INSERT #4 — 8 seconds]**

> ie is about to open doors to her room. SOUND. SOUND OF KERNEL'S VOICE. She stands up and walks
> to the door. INT. ROOFTOP — HOME OF KERNEL'S VOICE. It is dark in the house. A lone woman
> sitting on the porch, eyes closed, walking quietly. She is not her mother, but her sister. SOUND
> OF CLEVELAND EYE. KERNEL'S VOICE. The door to an hour-long conversation. The only thing missing
> is silence. INT. THE PROPOSED EZ HOUSE. INT. MCC

**LOWER THIRD:**
```
RENDER 4/5 — 128 TOKENS — WHO IS KERNEL. WHO IS THE SISTER. THE RENDER WON'T SAY.
```

*(This is the point where S01E01's render invented "Zidane" from nothing. This render invents
"Kernel" instead — a voice, never a face, referenced only as a sound. In a show whose whole
substrate is an operating system that never explains itself, a render hallucinating a *voice
called Kernel* is close enough to on-the-nose that it's worth flagging rather than laughing off.)*

---

**[RENDER INSERT #5 — 11 seconds, the longest render, the one that leaves Detroit entirely]**

```
ON SCREEN:
```
```
EMILY OS: RENDER ATTEMPT 5/5 — CONTEXT WINDOW: 256 TOKENS — FINAL PASS
```

> LEAN ROUTE — BRIDGE OF CUTZ. CUTZ LIGHTLY OPENS, making the corner of the living room open. A
> small, old, old house. It's clean, white and built. It's finished and is in good condition.
> SOUND OF A BOX OF POTCHES. A POTCHES SHOOTER SHOOTING. SOUND OF A LITTLE LITTLE LITTLE AERIAL
> CLOTHING. SOUND OF A SINGLE GLASSING. INT. MILLING ROOM. A single, tiny table has been painted.
> A BOX OF POTCHES. A POTCHES SHOOTER. SOUND OF A LITTLE LITTLE LITTLE AERIAL CLOTHING. SOUND OF A
> SINGLE GLASSING. The only thing missing is silence. INT. STAGE #1 — NIGHT. A FEW YEARS PASSES.
> It is the first year of World War II. There are no airplanes, no planes to do anything. No
> trucks. No airmen. The only airplanes to do anything are buses. The only planes that have
> survived are planes, or, if there are planes,

**LOWER THIRD:**
```
RENDER 5/5 — 256 TOKENS — SOURCE NO LONGER RECOGNIZABLE AS SOURCE
```

*(Same finding as S01E01: more context did not mean better memory. It meant more runway to leave
Detroit entirely. By the end of the longest pass, the render isn't reconstructing a school
anymore — it's landed in "the first year of World War II" with no bridge from the seed to get
there. In a show about a man who won't stay in his own year, a render that also can't stay in its
own year is either a coincidence worth ignoring or the most honest thing Layer 4 has produced by
accident all season. Not resolved here.)*

---

**[02:00] — TITLE CARD, NEW FOR THIS CUT**

SMASH CUT TO BLACK.

**ON SCREEN, final card:**
```
FIVE RENDERS. ONE SCHOOL. ONE UNEXPLAINED WAR.
```

**END LOG:**
```
CAMERA OP PRODUCTION LOG: [1 SEALED ENTRY]. SEALED LOG ENTRY IS MINE BEFORE IT IS THEIRS.
RENDER TRACK: ARCHIVED, NOT PROMOTED TO CANON
```

---

## Notes for whoever picks this up next

- **This is a variant, not a replacement**, same convention as the S01E01 x2 file. The real Act I
  (library, hallway, room 204) is `s01e02_school.md`'s own and untouched here.
- **The five RENDER inserts are the real GPT-2 output, byte-for-byte**, from `gpt2-alpine-c`'s
  `emily-ft` checkpoint, `temperature=0.85`, five sequential `POST :8088/generate` calls at
  `max_tokens` 16/32/64/128/256, seeded from this episode's own cold open. Nothing quoted was
  rewritten or cherry-picked, including the mid-word tokenizer splits ("hood" / "ie" across two
  calls, "MCC" / "LEAN ROUTE" across two calls) — left exactly as the API returned them.
- **Two open, unresolved questions for whoever scopes this further**, same spirit as S01E01's
  "who is Zidane": who or what is "Kernel," whose voice the render invents and never explains —
  and does the unprompted WWII swerve deserve a real thread (a show about someone unstuck in time,
  rendered by a system that also can't hold a timeline) or was it one temperature setting on one
  small checkpoint on one day. Flagging, not answering — a creative call, not a technical one.
- **Latency, stated plainly, same as last time**: five calls, ~12 minutes total this run
  (17:07–17:19), single 4-core box, single-threaded inference server. Founder already knows and
  asked to work within the constraint — noted here so nobody rediscovers it from scratch.
