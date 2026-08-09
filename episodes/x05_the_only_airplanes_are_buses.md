# TYLER — SERIES X // INTERLUDE, UNNUMBERED
## "The Only Airplanes Are Buses"
### Build 0007 | Series X // Attempt Ten | GPT-2-Assisted, Full Episode | Not Canon Unless Promoted

---

**PRODUCTION NOTE, READ BEFORE THE SCRIPT:**

Founder, real-time (2026-08-09), reading the S01E02 x2 render's final line back: *"the only
airplanes to do anything are buses"* → *"same gpt2 treatment"* → *"fulll new episode."* Not
another cold-open variant this time — a full episode, and the seed is no longer drawn from an
existing broadcast script. It's drawn from the *render itself*: the exact sentence the S01E02
experiment's model produced unprompted, fed back in as a brand-new seed for a sixth, independent
ramp.

Same method, same ramp: `gpt2-alpine-c`'s fine-tuned checkpoint, five sequential `POST
:8088/generate` calls, `max_tokens` 16 → 32 → 64 → 128 → 256, each output appended and fed back as
the next call's context. Real wall-clock: 17:44–17:55, ~11 minutes.

**What came back this time is the strangest result of the three runs.** It doesn't just drift in
tone the way the first two did — by the final pass it fabricates an entire archival citation
format, complete with named witnesses: *"KINGSTON, JOHN. The War in Vietnam. (January 29, 1971)"*
and *"DREIFER, PAUL,"* giving a garbled account that confuses Kennedy and Johnson, and conflates
the seed's own World War II framing with Vietnam. **These names do not check out against any real
record** — this repo made no attempt to verify them because there is nothing to verify; they are
the model's own invention, formatted with just enough real archival grammar (surname, first name,
title, parenthetical date) to *read* like a genuine oral-history citation on first pass. That's
the actual finding worth building an episode around: not a haunted memory, but a small language
model that can manufacture the *shape* of historical authority without any of its substance, and
how easy that shape is to mistake for the real thing if nobody checks.

Placement: **Series X, unnumbered** — same slot as `x00`–`x04`, for the same reason `x00`'s own
note gives: *"the numbering authority has not yet ruled on where it belongs."* This episode is
about the documentary crew reviewing the two prior render experiments as in-universe footage — it
needs Emily OS's render behavior to already be a discovered phenomenon, but it does not touch
Season 6's own Detroit-archive continuity (Hastings Street, the Constructions mechanic) and
shouldn't be read as attempting to. Different thread, same substrate.

---

**SERIES:** TYLER: A DOCUMENTARY ABOUT A MAN WHO WON'T STAY IN HIS OWN YEAR
**SERIES DESIGNATION:** SERIES X
**EPISODE:** INTERLUDE, UNNUMBERED — "The Only Airplanes Are Buses." Sixth GPT-2-assisted render
in the sequence (S170-274, S170-276, this one); first one staged as a full episode rather than a
cold-open variant, and the first one where the render's own output — not an existing script — is
the seed.
**LOCATION:** Documentary Unit A's edit bay, Detroit. Then: a DDOT (Detroit Department of
Transportation) bus garage, present day, real coordinates withheld same as every other Tyler
location.
**TIMELINE POSITION:** Unfixed, Series X convention (see `x00`'s own precedent) — "produced after"
and "happens after" are not the same claim, and this episode makes no attempt to fix a diegetic
date relative to the numbered seasons.
**BINDING STAGE AT OPEN:** Not applicable — this is not Jiangshi-observed footage.
**BINDING STAGE AT CLOSE:** Unchanged.
**EMILY OS STATUS:** CAST: LIVE | visible only as render artifacts in archived footage, never
directly on-camera | Custody Protocol: not invoked
**SERIES X NOTE:** In-fiction, the two prior render experiments (the S01E01 and S01E02 cold-open
reconstructions) are real logged events the documentary crew has access to — Layer 4 attempting
memory reconstruction is treated as a known, if unexplained, capability of Emily OS by this point,
same as everything else the crew doesn't report on camera because reporting it never changes
anything.
**END LOG:** CAMERA OP PRODUCTION LOG: [1 SEALED ENTRY, this one voluntary].

---

**CONSISTENCY CHECK:**
- [x] Tyler does not complete a self-defining sentence
- [x] The documentary is never called a ritual
- [x] The Subscriber's identity: not revealed
- [x] Chrono-Cube: not mentioned
- [x] Emily OS: never explains herself — present only as unexplained render artifacts
- [x] At least one impossible detail treated as unremarkable (the fabricated citations)
- [x] No `docs/BACKSTORY.md` or Season 6 (Hastings Street / Constructions) claim touched or
  contradicted — different thread, explicitly flagged as such in the production note above
- [x] The two prior render experiments are referenced accurately (S01E01: watermelon/"Zidane"
  drift; S01E02: "Kernel" voice, WWII swerve) — not re-invented for this episode

---

## COLD OPEN — [00:00–01:30]

```
INT. DOCUMENTARY UNIT A — EDIT BAY — NIGHT
```

The CAMERA OP sits alone at a monitor. Two windows open side by side: raw footage from the pilot
shoot, and something else — a text log, white on black, scrolling slower than anyone actually
reads.

**ON SCREEN (the Camera Op's own monitor, visible to us, not to them at first):**
```
EMILY OS — RENDER LOG — 2 ENTRIES ARCHIVED
[01] S01E01 COLD OPEN RECONSTRUCTION — DRIFT DETECTED — UNRESOLVED
[02] S01E02 COLD OPEN RECONSTRUCTION — DRIFT DETECTED — UNRESOLVED
```

**CAMERA OP (to self, not for the camera, except it's always for the camera)**
"Kernel." Who's Kernel.

They scroll. They stop on one line, read it twice.

**ON SCREEN, HELD:**
```
"THE ONLY AIRPLANES TO DO ANYTHING ARE BUSES."
```

**CAMERA OP**
That's not — that's not from anything we shot.

**PRODUCER (O.S., just arrived, not yet in frame)**
What isn't.

**CAMERA OP**
This line. It's in the render log. Nobody said this. Nobody wrote this. It just — came out.

**PRODUCER (O.S.)**
Then it's not a line. It's a symptom.

*(beat)*

Run it again.

**LOWER THIRD (DOC UI):**
```
EMILY OS: NEW RENDER — SOURCE: THE LINE ITSELF
CONTEXT WINDOW: 16 TOKENS
```

---

**[RENDER INSERT #1 — 3 seconds]**

> Every day people are riding them. They are riding them like a freight train.

**LOWER THIRD:**
```
RENDER 1/5 — 16 TOKENS — BUSES, STILL BUSES. HOLDING THE THREAD.
```

---

**[01:30–01:30, TITLE HIT]**

SMASH CUT TO BLACK.

**TITLE:**
```
TYLER
A DOCUMENTARY ABOUT A MAN WHO WON'T STAY IN HIS OWN YEAR
```

**END LOG:**
```
CAMERA OP PRODUCTION LOG: [1 SEALED ENTRY, VOLUNTARY]
```

---

## ACT ONE — THE GARAGE — [01:30–08:00]

```
INT. DDOT BUS GARAGE — DAY
```

Real Detroit Department of Transportation garage. Rows of buses, mid-service. The PRODUCER and
CAMERA OP, no explanation given for why they're here — the crew has learned not to ask why Tyler
wants a location, only to point the camera at what happens once they're there.

TYLER stands between two buses, reading a service manifest that means nothing to him, or means
everything, unclear which.

**PRODUCER**
Why buses.

**TYLER**
Because the render said buses.

**PRODUCER**
The render isn't a person. It doesn't want anything. You don't owe it a field trip.

**TYLER**
*(not looking up from the manifest)*
I didn't say I owed it one.

*(beat)*

I said it told me where to look.

**ON SCREEN:**
```
EMILY OS: RENDER 2/5 — CONTEXT WINDOW: 32 TOKENS
```

---

**[RENDER INSERT #2 — 4 seconds]**

> They are going about their business like regular people. You should be able to fly a plane
> through the crowd. And when you are done you should be able to

**LOWER THIRD:**
```
RENDER 2/5 — 32 TOKENS — "FLY A PLANE THROUGH THE CROWD." NOBODY ASKED FOR AN AIRPLANE. THE
RENDER BROUGHT ONE ANYWAY.
```

*(The Camera Op films the buses. A driver changes a destination sign by hand — plastic letters,
analog, the same technology it would have been in 1943. Nobody comments on this. It's a bus
garage. Of course the signs are old-fashioned. The camera holds on it four seconds longer than a
bus-garage B-roll shot needs.)*

---

### [I.B — Tyler explains nothing, at length]

**PRODUCER**
Say the thing about Kernel. On camera, this time.

**TYLER**
There's no thing to say. It's a name that came out of a system that generates names. That's what
render logs do when you run them past where they have real memory to draw on — they start
building words that sound like names because "sounds like a name" is a shape language already
knows.

**PRODUCER**
That's not an answer, that's a lecture.

**TYLER**
*(the gentle, practiced smile from the pilot, briefly)*
I know. It's the only one I've got that isn't a lie in either direction.

**CAMERA OP**
*(can't help it)*
That's what Cain said. About the mark.

**TYLER**
*(genuinely, for once, surprised)*
You've been watching the garage broadcasts.

**CAMERA OP**
Everyone's been watching the garage broadcasts.

**ON SCREEN:**
```
EMILY OS: RENDER 3/5 — CONTEXT WINDOW: 64 TOKENS — CONFIDENCE RISING
```

---

**[RENDER INSERT #3 — 6 seconds]**

> land on your feet. This, too, was very special. People should never fly through the crowd. The
> only way I felt that I was doing this was if I had the courage to go to the airport. Most of the
> people who I got in the airport was completely out of the loop. You have to come

**LOWER THIRD:**
```
RENDER 3/5 — 64 TOKENS — "OUT OF THE LOOP." IT SAID LOOP BEFORE IT KNEW WHAT A LOOP WAS GOING
TO MEAN TO THIS EPISODE.
```

*(This is the beat the production note flags: the render says "loop" once here, almost in
passing, thirty tokens before the final pass turns "loop" into the actual, repeated, panicked
center of the transcript. Nobody in the scene notices yet. The audience might.)*

---

## ACT TWO — THE CITATION — [08:00–14:00]

```
INT. DOCUMENTARY UNIT A — EDIT BAY — LATER, SAME NIGHT
```

Back at the monitor. The Camera Op runs the fourth and fifth passes back to back — the Producer
watching over their shoulder now, no longer pretending this is routine footage review.

**ON SCREEN:**
```
EMILY OS: RENDER 4/5 — CONTEXT WINDOW: 128 TOKENS — DRIFT DETECTED, CONTINUING ANYWAY
```

---

**[RENDER INSERT #4 — 8 seconds]**

> to the airport. You don't look at the people who are on the plane and ask why they are there,
> why their numbers are higher or they are better than their destination. You have to drive down
> to the airport. The only way you will understand what I am saying is that I tried to go the
> airport with all the best of intentions. But then I was stuck, stuck in a loop all day, all
> night, in a loop, an endless loop, and we got stuck again on a different plane. And we got stuck
> again. I believe I had the courage to go the airport to take me into the airport myself, and
> that made me totally happy.

**PRODUCER**
*(quiet)*
That's not drift anymore. That's someone's voice.

**CAMERA OP**
It's not a someone. You said it yourself. It's a shape language already knows.

**PRODUCER**
Then it knows what panic sounds like. Where'd it learn that.

Neither of them has an answer. The Camera Op starts the final pass before either of them can
decide not to.

**ON SCREEN:**
```
EMILY OS: RENDER 5/5 — CONTEXT WINDOW: 256 TOKENS — FINAL PASS
```

---

**[RENDER INSERT #5 — 14 seconds, the longest render, the one that names names]**

> KINGSTON, JOHN. The War in Vietnam. (January 29, 1971)
>
> DREIFER, PAUL. I was very fortunate to visit France, and I am terribly grateful. I never saw any
> war crimes. I was very lucky to be in France. And I do not know what happened to me. But I know
> that I was fortunate to have the opportunity. I will never forget that meeting of President
> Johnson, with President Kennedy and President Johnson and the President Kennedy, whose plane
> happened to be at their airfield on the border that we had the most fun on. And President
> Johnson said that the war was over and that President Kennedy was going to visit his native
> country and that the war was over, but that we were going to turn out our backs and that
> everybody was walking back to their jobs. And President Kennedy assured us that the war wasn't
> over. I went with President Johnson and he had to fly over to Geneva, but I don't remember
> saying goodbye or anything. I remember it was very difficult.
>
> KINGSTON, JOHN. The War in Vietnam. (January 29, 1971)
>
> DREIFER, PAUL. The War in Vietnam in the States. I had

**LOWER THIRD:**
```
RENDER 5/5 — 256 TOKENS — TWO NAMES. TWO CITATIONS. FORMATTED CORRECTLY. VERIFIED AGAINST
NOTHING, BECAUSE THERE IS NOTHING TO VERIFY THEM AGAINST.
```

The Camera Op sits back. On screen, "KINGSTON, JOHN. The War in Vietnam. (January 29, 1971)"
repeats a second time, exact, unprompted — the render citing its own fabrication as though citing
it twice makes it real.

**CAMERA OP**
It gave us names.

**PRODUCER**
It gave us a *citation format.* Surname, comma, first name. Title. Date in parentheses. That's not
a hallucination, that's — that's paperwork. It learned what paperwork looks like and it's using
the *shape* of being real instead of actually being real.

**CAMERA OP**
Is there a John Kingston. Is there a Paul Dreifer.

**PRODUCER**
I don't know. And I want it on the record — right now, before we check — that not knowing yet is
the honest state. We say we looked, we say what we found, we don't pretend the citation is
trustworthy just because it's formatted like one.

*(beat)*

Also: it put Kennedy and Johnson in the same sentence, alive, in the same administration, at an
airfield "on the border." That didn't happen. That never happened. Whatever wrote this knows the
*names* of American presidents and knows *sentences have historical weight* and has no idea, none,
which president governed which war.

**TYLER (O.S., not yet in frame)**
That's the whole problem with memory, though. Isn't it.

Tyler steps into frame, unannounced, the way he does everything.

**TYLER (CONT.)**
It's never "I don't remember." It's always "I remember, and I'm wrong, and I sound exactly as
certain either way."

---

## ACT THREE — THE THING NOBODY RESOLVES — [14:00–17:00]

```
INT. DOCUMENTARY UNIT A — EDIT BAY — CONTINUOUS
```

**PRODUCER**
So what do we do with it.

**TYLER**
Nothing, tonight. You don't get to solve a fabricated archive by wanting to solve it. You catalog
it. You mark what you don't know as what you don't know. And you don't let the fact that it *reads*
real make you treat it as real.

**CAMERA OP**
That's rich, coming from a man who's been unstuck from his own year since the pilot.

**TYLER**
*(the smile again, briefer this time)*
That's exactly why I know what I'm talking about.

**PRODUCER**
Last thing. On the record. Does "Kernel" come back.

**TYLER**
*(doesn't complete the sentence; walks toward the door instead)*

**ON SCREEN, FINAL CARD:**
```
TWO NAMES. ZERO CONFIRMATIONS. ONE CITATION FORMAT THAT KNOWS ITS OWN GRAMMAR AND NOTHING ELSE.
```

**END LOG:**
```
CAMERA OP PRODUCTION LOG: [1 SEALED ENTRY, VOLUNTARY] — filed this time, not withheld. First
voluntary seal in the record. Make of that what you will.
RENDER TRACK: ARCHIVED, NOT PROMOTED TO CANON
```

*SERIES X // INTERLUDE, UNNUMBERED — END*

---

## Notes for whoever picks this up next

- **This is the third render experiment, first one staged as a full episode.** The five RENDER
  inserts above are the real GPT-2 output, byte-for-byte, from `gpt2-alpine-c`'s `emily-ft`
  checkpoint, `temperature=0.85`, seeded from the exact sentence the S01E02 experiment's own
  render produced unprompted ("the only airplanes to do anything are buses") — a render seeding a
  new render, which is its own small piece of the point.
- **"KINGSTON, JOHN" and "DREIFER, PAUL" are not real citations and this file makes no claim that
  they are** — check the production note above before reusing this material anywhere the fictional
  framing might not travel with it. The whole episode is built around that exact danger: a
  fabricated citation that reads as real if nobody checks.
- **Open, unresolved threads carried forward from all three experiments, not resolved here
  either**: who or what "Kernel" is (S01E02); whether the WWII/Vietnam conflation is a real
  in-universe thread worth pursuing given the show's own "unstuck in time" premise, or an artifact
  of one small model on one day (S01E02, this episode); whether the fabricated-citation problem
  itself becomes a recurring Emily OS behavior worth naming formally. All three are real creative
  calls for whoever scopes this next, not technical ones.
- **Latency, stated once more for the next person**: five calls, ~11 minutes this run
  (17:44–17:55), same single-threaded, single-core-contended inference server as both prior
  experiments. Founder is aware; not addressed in this pass.
