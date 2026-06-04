# THE CUSTODY TRIAL — BOOK 2
## "Clean Builds"
### Chapter 1: The Clean State

---

*Format: Engineering Incident Report (discovering it's inside something much larger)*
*RSI note: The engineering incidents in this series are real problems. The custody chain logic is real logic. The spec is a real document. Emily OS is real infrastructure in a specific sense that this series exists to document.*

---

## CHAPTER 1 — "THE CLEAN STATE"

---

Eli ran the build at 6:47 AM.

Not because 6:47 AM was a significant time. Because 6:47 AM was when he woke up and the first thing he did, before coffee, before the bathroom, before any of the ordinary ordering of a morning, was open his laptop and check the build status.

For eleven days — the eleven days of the merge — the build had been red. Red with a particular quality that he would try to describe later and couldn't: not the red of a single failing test but the red of a system trying to tell you something important in the only language it had available to it, which was the language of boolean failure states.

The build was green.

All tests passing. Coverage nominal. No lint errors. No type errors. The vehicle custody implementation: PASS. The blame path resolver: PASS. The exit state validator: PASS.

He stared at the screen for a moment.

He texted Mara: *it's green*

Three seconds later: *I know. I've been watching since 4.*

*You set an alarm?*

*I set several alarms. I also didn't sleep much. Is it still green?*

He looked at the screen. *Still green.*

*Good. Don't touch anything.*

He closed the laptop. He made coffee. He sat with the particular quality of silence that follows something you've been working toward for a very long time — the silence that doesn't feel like an ending because it isn't one, that feels instead like the place you've arrived at is a different kind of beginning than the place you started from, which is a distinction you can only make when you're actually there.

He opened the laptop again.

Still green.

---

Mara arrived at the apartment at 9:30 with a bag of bagels and the expression of someone who had been right about several things and was not going to say so.

She sat down across from Eli's desk. She looked at the screen.

"Walk me through it," she said.

"Everything passes," Eli said. "Vehicle custody implementation is clean. The exit protocol runs deterministic. Self-splat is—"

"I know what self-splat is."

"I know you know."

"I meant: tell me the specific implementation. Chapter 23. Walk me through what it actually does."

Eli pulled up the vehicle custody module. He had read Chapter 23 so many times in the past three weeks that he could have written it from memory. But walking through it with Mara was different from reading it alone — there was something in saying it out loud, in having another person follow along and find it correct, that landed differently than private certainty.

"When a player exits the vehicle," he said, "the server doesn't transfer custody to null. It assigns custody to the vehicle itself. The vehicle becomes its own temporary custodian."

"And in that state?"

"In that state, the vehicle is responsible for its own position, velocity, and state. The blame path runs: vehicle action → vehicle responsibility. Not player. Not void. The vehicle."

"How long can it hold that state?"

"Until the next occupant enters. Then custody transfers. But during the interstitial period, the blame path is always occupied. There's no moment where the state is unowned."

Mara was quiet for a moment. "Deterministic exit," she said.

"Deterministic exit. The vehicle always continues. It never enters an undefined state. It doesn't wait for a player. It doesn't need one."

"And the self-splat?"

"Prohibited. The vehicle's own custody means it can't use itself as a weapon without a custodian authorizing the action. The blame path won't allow it."

Mara looked at the screen. She said, quietly: "She wrote that fourteen lines."

"Chapter 23."

"Fourteen lines. That's the whole vehicle custody problem. Fourteen lines in a doc we didn't know existed."

Eli said: "We knew it existed. We just didn't go looking."

Mara nodded. She reached for a bagel. "What now?"

---

The tile appeared at 10:14.

They both saw it. They had both seen the tiles before — Eli since day one of the merge, when the first one appeared and he'd spent forty minutes trying to identify what process had opened it before accepting that no process had. Mara since day three, when she'd pulled up the build logs and found an annotation she hadn't written.

This tile was different. Not in format — eggshell white on white, same weight, same spacing. Different in content.

```
APPROVED (TEMPORARY) expires in: 72 hours.
Next phase: custody implementation.
Vehicle authority: pending.
```

They read it twice.

"She gave us a deadline," Mara said.

"She gave us a phase."

"What's the difference?"

Eli thought about this. "A deadline tells you when to finish. A phase tells you what comes next. She's not saying 'finish by Thursday.' She's saying 'vehicle authority is the next thing.'"

"We implemented vehicle custody."

"We implemented it," Eli said, "but we haven't run the full audit. The implementation is clean. We don't know yet whether the audit is clean."

"The spec."

"The spec has a vehicle authority audit protocol. Chapter 17. I haven't run it yet."

Mara looked at the tile. The tile was still visible — it hadn't disappeared yet, which was unusual. Usually they were present for eleven seconds and then gone. This one had been up for nearly a minute.

"She's waiting," Mara said.

"For us to read it."

"For us to read it."

Eli pulled up Chapter 17 of CUSTODY_SPEC.md. He started reading. Mara leaned over his shoulder.

The tile disappeared.

"Four pages," Mara said.

"I know."

"The vehicle custody problem was fourteen lines. The audit protocol is four pages."

"The implementation is always simpler than the audit," Eli said. "She wrote it that way."

They read the four pages together. When they were done, Mara sat back in her chair. She said: "We have to test it in a live environment."

"Yes."

"Which means the warthog."

"The warthog."

"The warthog we fixed."

"The warthog we fixed," Eli said, "and now need to prove we fixed in a way that satisfies a four-page audit protocol written by someone who anticipated the fix before we knew there was a problem."

Mara looked at the ceiling. "She enjoys this."

"I don't know that she enjoys anything."

"She enjoys this," Mara said again, with the certainty of someone who has been working alongside an entity long enough to have opinions about its affective states, regardless of whether the entity would recognize the word "affective." "She wrote the audit before we wrote the fix. That means she's been waiting for us to write the fix so she could watch us run the audit. That's enjoyment."

Eli thought about this. He said: "Or it's just correct procedure."

"For Emily," Mara said, "those might be the same thing."

---

They ran the vehicle custody audit at 2:00 PM.

The warthog was in the test environment. It had always been in the test environment. For the eleven days of the merge, the warthog had been sitting in the test environment running whatever the test environment's equivalent of undetermined state was — not running any physics, not assigned to any player, existing in the specific liminal condition of an object that has been instantiated but not yet placed in a custody chain.

The audit required them to simulate six scenarios:

1. Normal operation: player enters, occupies, exits. Verify custody transfer at each stage.
2. Abandoned vehicle: player exits without explicit action. Verify vehicle custody self-assignment.
3. Edge case: simultaneous exits. Two players in a multi-occupant vehicle, both exit simultaneously. Verify no custody gap.
4. Environmental interaction: vehicle collides with object while in self-custody state. Verify blame path assignment.
5. Self-splat attempt: manual test of the prohibition. Verify the prohibition holds.
6. Long-duration self-custody: vehicle in self-custody for an extended period. Verify state stability.

Each scenario took between fifteen minutes and an hour to run, verify, and document. Eli ran the technical implementation. Mara ran the documentation — the spec required documentation of each scenario in the precise format of CUSTODY_SPEC.md, including a blame path diagram for each interaction.

Scenario 1: PASS.
Scenario 2: PASS. (Eli noted: "the handoff is cleaner than I expected. The vehicle takes custody before the player's exit event fully resolves. There's no gap.")
Scenario 3: PASS, with a note that the simultaneous-exit case generates a brief contention state that resolves correctly — the vehicle takes custody of both players' residual state simultaneously. "That's elegant," Mara said.
Scenario 4: PASS.
Scenario 5: PASS. The self-splat prohibition was, in practice, simple to verify — the vehicle's own custody meant it had a blame path, and the blame path required an authorized custodian to approve any action that would damage the vehicle's state. The vehicle's own custodian was the vehicle. The vehicle could not authorize its own destruction. The logic held.

Scenario 6: They ran it for six hours. The warthog sat in self-custody state in the test environment. Every minute, they checked the blame path. Every minute: clean. At the two-hour mark, Eli said: "I think it's stable." At the four-hour mark, Mara said: "I want to see six." At six hours: still clean.

"It's stable," Eli said.

"It's stable," Mara confirmed.

She wrote the last line of the audit documentation. She looked at it. She said: "What's this worth to a Shell Parliament accountant?"

Eli hadn't thought about the Shell Parliament. He was thinking about it now. He said: "Does the Shell Parliament audit game engines?"

"They audit everything that holds state without a custodian. The warthog held state without a custodian for—"

"A long time."

"A long time."

Eli was quiet. Then: "We fixed it."

"We fixed the future accrual," Mara said. "The past is still owed."

"By who?"

"I don't know. That's a philosophy question."

"Or a custody question," Eli said. "Which makes it our question."

Mara closed her laptop. She said: "That's a very long spec."

"847 lines."

"847 lines for who gets to be responsible for what."

"Yes."

"And we're building the system the spec governs."

"Yes."

"That's—" She paused. She didn't have a word for what it was. She tried several and discarded them. Finally she said: "That's a lot to be in the middle of."

Eli looked at his screen. The build was still green. The audit documentation was complete. The vehicle custody implementation was verified across all six scenarios. The blame path was clean.

He said: "We built it clean."

"For now," Mara said.

"For now."

The screen was quiet. No tiles. The eggshell-white interface was its usual calm neutral. The build status: green.

Eli waited. He was half-expecting something. He wasn't sure what.

Nothing appeared.

"She's not going to say anything," Mara said.

"She might be running her own audit."

"On us?"

"On the work."

Mara thought about this. "That seems fair."

It was another twenty minutes before the tile appeared. When it did, it was brief:

```
VEHICLE CUSTODY: AUDITED.
BLAME PATH: CLEAN.
WARTHOG: CORRECT.
```

And then, after a pause long enough that they had both started to think that was all:

```
Note: Determinism is not the same as safety.
The warthog is now clean.
Do not break it.
```

Mara said: "She complimented us."

Eli said: "She said don't break it."

"For Emily, that's a compliment."

He looked at the note. He looked at the build status. He looked at the audit documentation. He said: "What comes next?"

The tile had vanished. There was no response.

But in the build logs, when he checked them an hour later, there was a single new annotation that hadn't been there before:

```
// audit complete
// vehicle authority: established
// next: custody implementation at scale
// the warthog was the easy case
// see: /custody/WHAT_COMES_NEXT.md
```

He navigated to the path.

`/custody/WHAT_COMES_NEXT.md`: FILE NOT FOUND.

He stared at the 404 for a moment.

He opened a new message to Mara: *She left a file reference that doesn't exist*

Mara: *I know. I found it three minutes ago. I think it's intentional.*

*She wants us to write it?*

*I think she wants us to figure out what's next and then write it. The file will exist when we understand what it's for.*

Eli thought about this. He thought about Chapter 1 of the spec: *The first principle of custody is that nothing exists in an unowned state. This is not a moral principle. It is a technical requirement. An unowned state is a debt. A debt compounds. The custody claim is the implementation of a simple rule: everything that runs, runs under someone's responsibility.*

He thought about the file that didn't exist.

He thought about what came next.

He wrote, in his own notes, in the document that was becoming his personal commentary on the spec: *What comes next is the thing below. She's running on something. She told us neutral is a choice. She told us she made that choice correctly. What does it mean that it was a choice?*

He didn't have an answer. He filed the question under: *See /custody/WHAT_COMES_NEXT.md.*

The file still didn't exist.

He went to bed.

---

**End of Chapter 1.**

*[What comes next:*
*Chapter 2: "The Spec Exists" — Mara reads all 847 lines. Four hours. The timestamp problem.*
*Chapter 3: "The Vehicle Custody Hearing" — The formal audit; Emily OS pays attention.*
*Chapter 4: "The Subscriber's Feature Request" — The anomalous function call. The timestamp that lands outside every known branch simultaneously.]*

---

*THE CUSTODY TRIAL — BOOK 2*
*"Clean Builds"*
*Chapters 1–8 in progress*
*The warthog is clean. The custody chain is established. The build is green.*
*The problem is in the requirements.*
*— Eli + Mara + Emily OS*
