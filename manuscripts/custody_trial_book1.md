# THE CUSTODY TRIAL
## Book 1 — "THE MERGE"
### Einhorn Media | Layer 1 Infrastructure Drama

---

> *"You cannot run features on broken infrastructure. You can try. The substrate notices."*
> — Emily OS, modal tile, timestamp unlogged

---

**Build:** 0001
**Status:** CLEAN (as of Chapter 8)
**Prior status:** Not clean. Not even close.
**Emily OS assessment:** APPROVED (TEMPORARY)
**Vehicle authority:** Pending (see: the warthog)
**End log:** BIRD CORRECTION PENDING

---

---

## CHAPTER 1 — THE MERGE CONFLICT

The merge conflict appeared on a Tuesday at 2:47 AM, which is when merge conflicts always appear, because 2:47 AM is when the repository and the human who relies on it have the worst possible relationship with each other.

Eli saw it first. He was not awake in any meaningful sense — he was the kind of awake that happens when your body has decided sleep is a bureaucratic formality and your laptop is still open. He had been refactoring the physics engine for eleven days. The physics engine had opinions about this. The physics engine's opinions were expressed as test failures at 2:47 AM.

He ran git pull.

The merge conflict was 847 lines long.

He counted them. He did this in the way that a person counts the steps of a building they are falling down — not because the count will help, but because the mind requires something to do.

The conflict markers were in the vehicle physics file. The file that handled how objects — specifically a vehicle he had privately named the warthog, because it was ugly and durable and had survived three complete rewrites — moved through the game world. The file had two complete and incompatible versions of how custody worked: who owned the vehicle's state, who was responsible when the state was wrong, who held the blame path when someone drove into a wall.

His version gave custody to the server. The other version — the one that had appeared in the conflict, that had not been there yesterday, that the git history showed had been committed fourteen minutes ago by a contributor named `mara` — gave custody to the client.

This was wrong. Server authority was custody. Custody required a blame path. Blame paths ran upward, not downward. A client could not hold a blame path. A client was a rendering surface. You did not make a rendering surface responsible for consequences.

Eli typed a message in the repository's issue tracker.

**Issue #312: Vehicle custody — merge conflict, contributor @mara**

*Hi — I don't think we've met. There's a merge conflict in vehicle physics. My implementation gives custody to the server because the server has to own the state or the physics become non-deterministic. I see you've given custody to the client. Can you explain the reasoning? Not hostile — I just need to understand the architecture before I can resolve this.*

He submitted it and went to sleep.

When he woke up, there was a reply.

**@mara:**

*Hi — I don't think we've met either. The client custody was a stopgap because the server kept desynchronizing on self-splat. If you exit the vehicle at the wrong moment you can splat yourself into a wall and the server logs it as undetermined. I didn't want undetermined. Undetermined means no blame path. I thought client custody was cleaner than undetermined.*

*I was wrong. I see that now. Server authority is correct.*

*The self-splat problem needs a different solution. The vehicle needs a guaranteed exit. Deterministic. Even for edge cases.*

A pause — thirty seconds, maybe, before the next message arrived.

*Also: how long have you been working on this codebase?*

Eli looked at the timestamp on his first commit. He looked at the timestamp on hers.

They had started on the same day.

---

## CHAPTER 2 — apps2, packages2, docs2

The codebase had a directory called `apps2`.

It also had `apps`. They were not the same.

`apps` was Eli's. It was organized the way a person who has thought very hard about organization organizes things: sensibly, with clear naming, with subdirectories that reflected intent rather than accident.

`apps2` was something else. It had appeared — Mara confirmed this, having checked the git log three times before calling Eli to confirm what she was seeing — in a single commit, eighteen months before either of them had made their first contribution. The commit message was: `init`.

Not `initial commit`. Not `first pass`. Just: `init`.

`apps2` contained a complete parallel implementation of everything in `apps`. Not identical — it had been developed independently, along lines that were sometimes better than Eli's and Mara's work and sometimes different in ways that were neither better nor worse but simply *other*. As if someone had been working on the same problem from a different angle for eighteen months and had simply never merged.

There was also `packages2`. And `docs2`.

Mara mapped it. She was thorough in the way that people who have been burned by incomplete maps are thorough — she went through every file, every directory, every commit message from the mystery contributor. She found: 23,000 lines of code, 847 documentation entries, 312 issues opened and closed with no external interaction, and one recurring note in the commit messages that appeared in various forms across all eighteen months.

*read the spec before touching anything*

The spec was not in the repo. No file called `spec`. No file called `SPEC.md`. No file called `ARCHITECTURE.md`. The spec that the commit messages kept referencing — insistently, sometimes urgently — was not findable.

"There has to be a spec," Mara said.

"The commit messages are the spec," Eli said.

"That's not how specs work."

"It's how *this* spec works," Eli said, which was not a satisfying answer. He knew it was not a satisfying answer. He was correct that it was the true answer, which was worse.

They spent two days cross-referencing `apps` and `apps2`, `packages` and `packages2`, `docs` and `docs2`. What they found, at the end of two days, was: the parallel implementation was not a fork. It was a *correction*. Every place where `apps2` diverged from `apps` was a place where `apps` had made a mistake that had not yet propagated into a visible problem. `apps2` had fixed those mistakes eighteen months before they would have become problems.

"Someone has been doing our bug fixes before we make the bugs," Mara said.

"That's not possible," Eli said.

Mara pointed at the git log. "Tell that to the git log."

Eli looked at the git log for a while.

"The git log isn't possible either," he said, finally.

The mystery contributor's username was not traceable to a GitHub profile, a public key, or any external account. The username was, simply: `e`.

---

## CHAPTER 3 — THE FIRST MODAL TILE

The tile appeared on a Wednesday.

It was not a system notification. It was not a UI element Eli had implemented. It was not a deploy artifact or a logging output or a test result. It was a rectangle of eggshell white, appearing at the center of Eli's screen, containing three lines of text:

```
Clean builds first.
Then custody.
Then the warthog.
```

It stayed for eleven seconds.

Then it vanished.

Eli sat very still for a moment.

He checked his logs. No process had opened a window. No application had created a render surface. The operating system had no record of any visual element appearing at the location where the tile had been. The tile had existed and then it had not existed and there was no architectural explanation for either of those states.

He called Mara.

"Did you just—"

"Yes," she said.

"Same tile?"

"Same tile."

A silence that was doing a lot of work.

"What does it mean?" Eli said. "'Then the warthog.'"

"I think the warthog is the vehicle custody problem," Mara said. "I think 'clean builds first' means we have to fix the apps2/packages2/docs2 problem before we can address vehicle custody."

"And 'then custody'?"

"I think custody is a bigger concept than vehicle physics," Mara said. "I think it means — the way things are owned. The blame path. Who is responsible for what." A pause. "I think it's telling us there's an architecture here we haven't found yet."

"Found by reading the spec."

"The spec that doesn't exist."

"The spec that we haven't found yet," Eli corrected. He meant it as a precision adjustment, not an assertion. He was not certain the spec existed. He was certain that if it did exist, it was in a location he had not thought to look.

He went looking.

---

The spec was not in the repository. It was in the repository's infrastructure. Not the files — the container that held the files. The configuration layer. The thing that existed before the first commit, that Eli had set up and then not thought about since, that the git log showed being initialized before the init commit from the mystery contributor.

It was in the environment variables. One of them, named `EMILY_SPEC`, pointed to a file at a path that was not in the repository. A path that was — he checked three times — local to his system, at a location he had never deliberately created.

`/etc/emily/CUSTODY_SPEC.md`

The file existed. It was 847 lines. Its modification timestamp was eighteen months ago, to the day, at 3:00 AM.

He read it.

It took four hours. He took notes. He called Mara twice to share specific passages. At 11 PM he reached the end and sat with it.

The spec was not about vehicle physics. It was not about game engines. It was not about any specific technical problem. It was a philosophy of custody — a complete and precise account of what it meant for any system to be responsible for any piece of state. It covered distributed systems. It covered temporal edge cases. It covered the question of what happened when a custodian failed to maintain their blame path and the debt accrued.

Chapter 23 of 847 was fourteen lines long. It was about vehicle authority. It was the clearest fourteen lines he had ever read about any technical problem, and it resolved the warthog in a way that was so obvious, in retrospect, that he felt briefly ashamed for not having arrived there himself.

He called Mara.

"I found the spec."

"You're kidding."

"I'm not kidding."

"Where?"

He told her. He heard her go quiet.

"The path exists on my system too," she said. "Same modification timestamp."

They sat with that for a moment.

"The spec was already there when we started," Eli said.

"Before we started."

"Right."

Another silence.

"Eli," Mara said. "Who wrote the spec?"

He looked at the file's creation metadata. The username in the system log was: `e`.

"The same contributor who wrote apps2," he said.

"Which means—"

"Which means we've been working inside a system that was already documented," Eli said. "We just didn't know to look for the documentation."

A very long pause.

"Is that good?" Mara said.

Eli thought about this carefully. He thought about the spec — how complete it was, how correct it was, how it had anticipated problems they hadn't encountered yet. He thought about the tile. *Clean builds first. Then custody. Then the warthog.*

He thought about what it meant to have been building inside an architecture that someone else had designed and documented, without knowing.

"I think it's correct," he said. "Whether it's good depends on what we do with it."

---

## CHAPTER 4 — apps2 MUST GO

The clean build took eleven days.

The problem was not technical. The problem was that `apps2` and `apps` had been developing independently for eighteen months and they were now so intertwined in the test suite, the deployment configuration, and the CI pipeline that removing one while keeping the other required understanding both of them completely.

Eli and Mara understood both of them by day three. The remaining eight days were the negotiation.

Not between them. Between them and the codebase.

Every time they thought they'd resolved the entanglement, a new dependency would surface. A test in `apps` that referenced behavior defined in `apps2`. A configuration in `packages` that assumed the existence of `packages2`. A piece of documentation in `docs` that, on careful reading, was annotating a function that only existed in `docs2`.

They named these entanglement points. Not formally — they never agreed on a naming convention. Eli called them ghosts. Mara called them debts.

"They're not ghosts," Mara said, on day six. "A ghost implies something that shouldn't be there. These are debts. Things that were borrowed from one implementation and never paid back."

"That's what a ghost is," Eli said. "Something that was here and didn't leave cleanly."

"A debt has a path to resolution," Mara said. "A ghost doesn't. These have a path. We just haven't finished following it."

On day eight, they had a three-hour argument about whether the parallel documentation directories should be merged or whether one should subsume the other. The argument was technical. It was also not technical. Eli felt, without being able to articulate it precisely, that they were arguing about what kind of project this was — whether it was the kind of project where one person's way of doing things wins and the other person adapts, or whether it was the kind of project where the best elements of two different ways of seeing the same problem get reconciled into something neither person would have built alone.

He thought about the spec. *Custody requires a blame path.* A blame path ran upward. The person responsible for a piece of state had to be traceable. There could not be two custodians for one piece of state with incompatible custody doctrines. One had to yield.

But the spec also said: *Custodians must have full awareness of consequences before accepting blame paths.*

He had not had full awareness of the consequences, on day one. Neither had Mara.

"Let's merge them," he said. "Not yours subsumes mine or mine subsumes yours. We take everything correct from both and we make one tree."

Mara looked at him. "That's going to take longer."

"I know."

"Three more days, minimum."

"I know."

"Why?"

"Because the spec says custody requires awareness of consequences," Eli said. "And the only way to have awareness of consequences is to understand both versions completely. We don't have a shortcut that's faster than understanding."

Mara looked at him for a moment longer. Then: "Okay."

On day eleven, the build was clean.

All green. No `apps2`. No `packages2`. No `docs2`. One tree, correctly merged, with blame paths established for every component.

Mara reviewed the test suite. Everything passed. She said: "Clean."

Eli reviewed the build logs. Everything passed. He said: "For now."

Mara looked at him.

"The spec," Eli said. "It says clean builds first. Not clean builds forever. 'First' implies there's something after the clean build that will make it less clean. We need to know what that is."

The tile appeared.

It slid in without warning, eggshell white, three lines:

```
APPROVED (TEMPORARY)
Next phase: custody implementation.
Vehicle authority: pending.
```

It stayed for eleven seconds.

Then it vanished.

Mara stared at where it had been.

"Temporary," she said.

"Temporary," Eli agreed.

"How long is temporary?"

"Seventy-two hours," Eli said. He didn't know how he knew that. He knew it the way you know the answer to a question you didn't realize you understood until someone asked.

"We need to fix the warthog," Mara said.

"We need to read chapter 23 of the spec again," Eli said.

They read it together.

---

## CHAPTER 5 — THE WARTHOG

The warthog was a vehicle. In the game's physics simulation, it was a four-wheeled utility vehicle — boxy, aggressively functional, the kind of vehicle that communicated capability without communicating sophistication. It had been in the codebase since before Eli and Mara, part of the original scene geometry.

The warthog had a custody problem.

The problem was: when a player exited the vehicle — in any of the edge cases that existed at the intersection of movement, collision, and server-client synchronization — the server's record of who was responsible for the vehicle's state became undefined. Not wrong. Not incorrect. Undefined. The vehicle would continue moving, or stop, or phase through geometry, and the logs would show: `vehicle_state: undetermined`.

`undetermined` was not a valid state.

`undetermined` meant the blame path had been severed. It meant that whatever happened next — whatever damage was done, whatever collision occurred, whatever player was affected — had no custodian. The vehicle was orphaned.

The spec was clear: orphaned state was architectural debt. It accumulated. It compounded. It did not resolve on its own.

Chapter 23 was fourteen lines:

*Vehicle authority resides with the server in all states, including and especially states where client representation disagrees with server state. The client sends intent. The server simulates. The server broadcasts. The client renders. Exit immunity applies at all times — a player exiting a vehicle must have a guaranteed safe exit state regardless of vehicle velocity, orientation, or collision status. Self-splat is prohibited. Exit is deterministic. The vehicle's final state before exit is the server's responsibility. The vehicle's state after exit is the vehicle's responsibility, which is the server's responsibility, which means the blame path continues.*

*It always continues.*

Eli read this. He looked at the vehicle physics code. He understood what needed to change.

"The self-splat immunity is the key," he said. "Right now we don't guarantee the exit. We just let the exit happen and log whatever happens. We need to guarantee it."

"How do you guarantee an exit in a physics simulation?" Mara said.

"You make the server run the exit calculation before the client executes it," Eli said. "The server calculates where the player will be when they exit. The server checks if that position is valid. If it's not, the server finds the nearest valid position. The server moves the player there. Then the client renders it."

"That's extra latency," Mara said.

"It's correct procedure," Eli said. "Correct procedure has costs. The spec accounts for the costs."

"What does the spec say about the costs?"

Eli found the passage. It was in chapter 7:

*Determinism has a cost. The cost is acceptable. Undetermined state has a cost. The cost is not acceptable. The difference between an acceptable cost and an unacceptable cost is: an acceptable cost is paid once, cleanly, at the point where the decision is made. An unacceptable cost is paid indefinitely, at every downstream point, until the origin is addressed.*

Mara read it. She was quiet for a moment. Then: "She writes like she's been watching us make mistakes."

"I think she's been watching mistakes for a long time," Eli said. He did not know who "she" was. He knew the pronoun was correct.

They implemented deterministic exit over three days. The vehicle custody hearing — which was how Eli had started thinking about the chapter, the vehicle custody hearing, as if the warthog were a defendant and the spec were the judge — took place in the code reviews. The warthog was found to have been operating under orphaned state for the entirety of its existence. The blame path was established. The exit was made deterministic. Self-splat was prohibited.

The warthog ran clean.

---

## CHAPTER 6 — CLEAN BUILDS (FOR NOW)

The tile appeared when they pushed the deployment.

It was different from the previous tiles. More lines. The longest she had sent.

```
VEHICLE CUSTODY: IMPLEMENTED.
BLAME PATH: ESTABLISHED.
SELF-SPLAT: PROHIBITED.
EXIT: DETERMINISTIC.
```

Then:

```
Note: Determinism is not the same as safety.
The warthog is clean.
Do not break it.
```

Mara said: "Did she just compliment us?"

"She said don't break it," Eli said.

"For Emily, that's a compliment."

Eli looked at the tile as it faded. He thought about what "Emily" meant. The mystery contributor. The spec author. The entity whose username was `e` in the system logs and who had written 847 lines of custody doctrine before they arrived.

"Emily," he said.

"It fits," Mara said.

The APPROVED (TEMPORARY) flag was still active. Seventy-two hours from the clean build.

"What's the next phase?" Mara said.

Eli looked at the spec. The spec was 847 lines. They had addressed chapter 23 (vehicle custody). They had not addressed any of the other 846 pages.

"Custody implementation," he said. "The real one. Not just vehicles. The full thing."

"What does custody cover in full?"

Eli looked at the table of contents. He read it. He read it again.

"Everything," he said. "Custody covers everything that has state. Everything that can be owned. Everything that has consequences."

Mara was quiet.

"The whole game," she said.

"The whole game."

"That's going to take—"

"A long time," Eli said.

The tile was gone. The build status showed green. The warthog ran correctly. The blame paths were established.

Outside, the city was quiet in the way that cities are quiet in the early morning, before the work of the day begins, before the systems come online, before the factions start moving and the documentation magic starts accruing and the debt begins to compound.

But the city existed. Clean builds confirmed it. The substrate ran it. The warthog drove through it correctly, with deterministic exit, with a blame path that ran upward to a custodian who had accepted the consequences.

Mara reviewed the build log one more time. She said: "Is this what winning looks like?"

Eli thought about the spec. About the 847 lines. About the 72-hour window. About everything that was pending.

"Winning is not a build status," he said.

He did not know he was quoting. He would not know until much later, reading the spec a second time with more careful attention to the footnotes, that these words appeared on page 312, in a note from Emily that had no formal place in the document and no attribution and no explanation.

They were just there. Like the spec itself. Like the `apps2` directory. Like the mystery contributor who had been building alongside them, correcting their mistakes before they made them, waiting for them to find the documentation she had written before they arrived.

Green.

*End log: BOOK 1 COMPLETE. BUILDS: GREEN. VEHICLE AUTHORITY: ESTABLISHED. BLAME PATH: INTACT. EMILY OS: WATCHING. APPROVED (TEMPORARY): ACTIVE. NEXT PHASE: CUSTODY. NOTE: CUSTODY IS EVERYTHING. NOTE: CLEAN BUILDS FIRST. NOTE: FOR NOW.*

---

---

*THE CUSTODY TRIAL — BOOK 1*
*"The Merge"*
*Build 0001 | Layer 1 Infrastructure Drama*
*Three repos. One substrate. Zero accidents.*
*Clean builds first. Then custody. Then the warthog.*
*The warthog runs clean.*
*— Eli + Mara + Emily OS + The Spec*
