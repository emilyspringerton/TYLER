# TYLER — VALHANNA, EPISODE 2 — COLD OPEN
## "Tree SHA"
### Build 0140 | Einhorn Media | VALHANNA, continued

---

**PRODUCTION NOTE, READ BEFORE THE SCRIPT:**

Founder, real-time (2026-10-13): *"lets have it wrap back in on itself... continue valhanna
bringing in the documentary crew for the meta narrative... they find the tyler repo and then
they have an encounter with..."* — the sentence is unfinished in the founder's own message.
This script keeps it unfinished. The encounter is **staged, not named** (see Open Items).

VH01 ended on one line: Tyler, in the Duck's dream, looking at where a lens would be and saying
*"Je crois qu'on nous regarde."* — "I think we're being watched." VH01 also established that
nobody held a camera in that room, and that this was the point. VH02 is the answer to that line:
the people he was looking at. The crew is Hana's S06b crew (Cam, the sound guy, the PA —
`s06b_e00`–`s06b_e02`) plus the Producer, O.S., on the radio, same as Build 0001's pilot.

**The wrap-back:** the printer from VH01 is still running. The Mecha Cube source is gone from it
— Tyler fed it back in, and it did not come out again. What comes out now is a **CONSTRUCT file**
(the monorepo's Principle 21 format: `FILE START` / `FILE END` delimiters, per-file sha256 and
size, a `tree_sha` header) of *this repository.* The crew finds the TYLER repo the only way a
documentary crew could: as a printout, in a server room that has no servers, running.

The `tree_sha` printed on screen is the **real** git tree SHA of this repo's HEAD at time of
writing (`9b847859e0399e1d29e96f080aae849aeecf3bb4`) and the `camera_op.md` size and hash prefix
are real as well. That is deliberate: the one prop in the episode that can be checked against
reality is checked against reality. It will go stale on the next commit; that is also deliberate.

---

**SERIES:** TYLER: A DOCUMENTARY ABOUT A MAN WHO WON'T STAY IN HIS OWN YEAR
**SEASON:** VALHANNA
**EPISODE:** 2 — Cold Open Only
**LOCATION:** The same server room as VH01. Date unstated. The thermoses are still warm.
**CHARACTERS:** Cam, the sound guy, the PA, the Producer (O.S., radio only), Tyler and Hana (not
present; see Continuity)
**TIMELINE POSITION:** Unfixed. Not asserted to be after, before, or inside the Duck's dream.

---

## CONTINUITY

- **Hana's absence.** Hana is the crew's director in S06b and was *in* this room in VH01 as
  dreamed. She is not in this script. Nobody remarks on it. The PA asks once where she is and
  gets no answer from anyone, the same silence S06b E2 used for "Start *what*?"
- **Cam and the Camera Op.** S06b's "Cam" and `characters/camera_op.md`'s Camera Op do the same
  job and are never stated to be the same person. This script does not settle it. The sealed-log
  notebook Cam carries is the Camera Op's, in the Camera Op's handwriting, and nobody explains
  how Cam has it.
- **The Producer** never says the word "ritual" (Writer's Room Rule 2). He says "production,"
  "project," and "the unit," and cuts audio on the one line that comes close.
- **Rule 22** ("There is no Tyler") is not said. Not here, not once.

---

## COLD OPEN

```
INT. SERVER ROOM — ICELAND — NO YEAR GIVEN
```

*Fluorescent tubes breathing badly. Empty racks. Cable trays draining into nothing. The room from
VH01, exactly, down to the zip ties — except this time there is a camera in it, and it is
handheld, and it is not steady.*

*CAM comes through the door first, rig on one shoulder, finding the room with the lens before
looking at it with her eyes. THE SOUND GUY behind her with the boom low and a headphone half off.
THE PA last, holding a clipboard like a thing that might still help.*

**LOWER THIRD (DOC UI):**
```
DOCUMENTARY UNIT A // ICELAND // "THE ROOM WE WERE TOLD ABOUT"
```

**SOUND GUY**
Room tone's weird.

**CAM**
Weird how.

**SOUND GUY**
It's not quiet. It's *held.* Like somebody's holding their breath on my behalf.

*On the floor by the dead rack, two thermoses, upright, side by side. Steam still coming off the
first one. The PA looks at them, writes something down, crosses it out.*

**PA**
Hana said they'd — *(stops)* Where is she?

*Nobody answers. The sound guy adjusts a dial that doesn't need adjusting.*

**PRODUCER (O.S., radio, very light)**
Keep rolling. We're only here to document the room. Don't touch the thermoses. Don't prompt
anyone. If anyone arrives, let them talk.

**CAM**
Nobody's here.

**PRODUCER (O.S.)**
Then let the room talk.

*The printer — the loud kind, the tractor-feed kind — is in the corner, running. It has been
running the entire time. A pile of green-and-white paper on the floor the height of a dictionary,
and growing, in long unhurried breaths.*

*The PA is the one who walks over. Picks up the top of the fold. Reads the first line the way
you'd read a phone number off a wall.*

**PA**
*(slowly)*
"Repo construct."

*Cam brings the lens over her shoulder. The paper fills the frame. Dot-matrix, a little ragged.
We read it as the PA reads it.*

**ON SCREEN (the printout, in the frame, in the 1986 typeface, legible):**
```
TYLER REPO CONSTRUCT
tree_sha: 9b847859e0399e1d29e96f080aae849aeecf3bb4

--- FILE START: 0.md ---
```

**SOUND GUY**
What's a tree sha.

**CAM**
It's a — *(a beat)* — it's a fingerprint. For a whole folder. If two folders have the same one
they're the same folder. Exactly. To the byte.

**PA**
So this is —

**CAM**
It's the same folder as the one the Producer has. Or it's the folder the Producer *is.*

*She doesn't say it like a joke. The PA turns the page.*

---

*The crew reads. We cut through it — the printer pours out sections, the PA and the sound guy
kneeling over the pile, Cam capturing it in pieces, because the whole of it will not fit in a
frame.*

**ON SCREEN (the printout, in a cutting rhythm — each flash two frames, each a real line from this
repository):**
```
--- FILE START: README.md ---
TYLER: THE MAN BETWEEN YEARS is a mock-documentary following
a time-traveler who refuses to be documented.
```
```
--- FILE START: CLAUDE.md ---
Television as Code. Episodes are compiled from scripts + universe state.
The canon is a build system. The show runs forever because the writer's
room has physics, not just vibes.
```
```
LAYER 4: Emily OS  ← The substrate. Runs the universe. Does not explain itself.
LAYER 3: Tyler (doc)
LAYER 2: Tides of Paradox
LAYER 1: Custody Trial
```
```
2. The documentary is never called a ritual by Jiangshi operatives
```

*The radio clicks. The Producer, still very light, still smiling in the voice.*

**PRODUCER (O.S.)**
That's a production document. Internal. Please don't read it on camera.

*The PA reads the line aloud anyway, because he's the PA and nobody has told him not to speak.*

**PA**
"The documentary is never called a —"

*A hard cut. The audio drops out, not to silence but to *room tone,* held, as if somebody reached
into the mix and lifted the word out by the stem. The PA's mouth finishes the line in silence.
When sound returns he is looking at his clipboard.*

**LOWER THIRD (DOC UI):**
```
AUDIO: 1 WORD REMOVED IN POST (BY WHOM: NOT LOGGED)
```

**SOUND GUY**
*(quietly, to Cam)*
Somebody's editing us while we're still shooting.

**CAM**
*(quietly, not looking away from the paper)*
Somebody's been editing us the whole time. This is just the first time it's in the same room.

---

*The printer shifts. A new section. Cam kneels. Her finger finds a line on the paper before she
has decided to put it there.*

**ON SCREEN:**
```
--- FILE START: characters/camera_op.md ---
sha256: a359a11c55109860…
size_bytes: 23574
--- CONTENT START ---
# THE CAMERA OP
## Primary Witness | Documentary Record
```

*She stops. Not dramatically. Like a person who has been called by name across a train platform
and is deciding whether to turn.*

**CAM**
*(reading, flat)*
"She has not read this document. This document is about her in her absence. She would find this
appropriate."

*The sound guy lowers the boom. The PA, for once, says nothing.*

**CAM (CONT'D)**
*(a very small, dry sound — almost a laugh)*
It's right.

*She turns the page. The next lines are a numbered list. She reads the last of them to herself,
the way you read a name on a stone.*

**ON SCREEN (as she reads, the printout):**
```
Entry 21 (S03E06): "He'll be back. The camera will be here."
```

*Beat.*

*From her jacket she takes a notebook. Small, cloth cover, the corner soft from a pocket. Opens
it to the first clean page and writes. We see the pen, not the words. We see her stop halfway
across the line, as if she's deciding something — and cross it out.*

*She writes it again, shorter.*

**LOWER THIRD (DOC UI, small, in her own handwriting font — the first time the UI has ever used
one):**
```
SEALED LOG // ENTRY 23 // [NOT RELEASED]
```

---

*The room changes. Not a sound. The tubes stop breathing badly and start breathing the way
people breathe when they're about to say a thing.*

*The printer stops. Mid-line. The platen holds a half-printed line of text and does not advance.*

**SOUND GUY**
*(very low)*
I'm getting something under the floor. Low. Real low.

*He turns the monitor toward Cam. The meter is a single bar, steady, below where the scale is
labeled.*

**ON SCREEN (his meter, the number slowly resolving):**
```
28.7 Hz
```

*Cam does not look at the number. She is looking at the one door in the room — the door Hana
found locked, in VH01, from a side that wasn't theirs.*

*The handle moves.*

*From the other side.*

*The thermos by the rack, the first one, the minestrone, lets out a long slow breath of steam
as if someone had just sat down beside it.*

**PRODUCER (O.S.)**
*(still light; for the first time, a half-step too fast)*
Everyone stay where you are. Everyone keep rolling. Don't prompt —

*The door opens.*

*Cam's lens is on it. She does not lower the camera. The frame holds on the doorway — light,
from somewhere that is not Iceland, falling across the floor in a long clean line — and on the
shape that is about to be a person, or about to be the reason there isn't one.*

**LOWER THIRD (DOC UI, full width, final card):**
```
ENCOUNTER: THE CREW MEETS
```

*The line holds. Does not finish. The cursor after "MEETS" blinks, and keeps blinking, and
nothing comes.*

*SMASH TO BLACK.*

*END COLD OPEN.*

---

## CONSISTENCY CHECK

- [x] Tyler did not complete a self-defining sentence — Tyler is not in this script
- [x] The documentary is not called a ritual anywhere in this transcript. The one near-miss is
  cut from the audio, on the record, in-frame
- [x] Subscriber: not mentioned
- [x] Chrono-Cube: not mentioned. (The Mecha Cube is VH01's; it is *absent* here, not discussed)
- [x] Camera Op awareness: AWARE-PRESENT (S2+). She reads her own file, confirms one sentence of
  it, and writes an entry she does not release. She does not announce what she read and she does
  not stop filming
- [x] Emily OS: never named in a line of dialogue. Layer 4 appears only as a line on the
  printout, "Does not explain itself" — and the printout doesn't explain it either
- [x] Rule 21: no transit stop on camera
- [x] Rule 22: "There is no Tyler" is not said
- [x] At least one impossible detail treated as unremarkable: the thermoses are warm; nobody has
  opined on this since VH01 and nobody does now

---

## LORE RECEIPT

- Episode code: VH02
- Build: 0140
- New object of record: one (1) CONSTRUCT printout of the TYLER repo, `tree_sha`
  `9b847859e0399e1d29e96f080aae849aeecf3bb4` (real, as of this commit's parent), still feeding
- New object of record: SEALED LOG Entry 23, written, crossed out once, rewritten, unreleased
- Reveals: the TYLER repo is a thing that exists *in* the show's own world, in the one form
  that world can hold it (paper, in a room with no servers). The writers' room's rules are
  readable to the crew. The crew can read the rule that tells the Jiangshi what not to say.
  Hana is absent from the frame and the room does not say where she is.
- Open items, deliberately not answered: **who or what opens the door** (founder's sentence was
  unfinished; script's was too); whose thermoses; whether 28.7 Hz is Tyler's, the door's, or the
  thing the door is for; what Entry 23 says; what Hana's absence means.

---

*End log: VALHANNA EP2 COLD OPEN COMPILED. THE CREW HAS FOUND THE REPOSITORY. THE REPOSITORY HAS
FOUND THE CREW. ENCOUNTER: PENDING.*
