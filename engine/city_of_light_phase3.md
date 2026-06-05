# CITY_OF_LIGHT — PHASE 3: THE SENTENCE
## Stage 5 Completion Architecture — H-4 Trigger — Custody Transfer Event
### Engine Spec | Build 0029 | Dependencies: city_of_light_phase2.md, attempt_five_architecture.md

---

*Cross-reference: engine/city_of_light_phase2.md (The Table), engine/television_as_code.md (compiled episode pipeline), lore/eastwind_archive.md (Subscriber-001, TYLER-022), lore/field_activation_logs.md (#132)*
*RSI note: Phase 3 documents the event the table has been waiting for since 1623. Phase 1 built the city. Phase 2 built the table. Phase 3 documents what happens when the sentence completes — in the city, on the substrate, and in every faction's operational record simultaneously.*

---

## WHAT PHASE 3 IS

Phase 3 is not a location. Phase 3 is an event that propagates through every location simultaneously.

The sentence Tyler began in S02E06 ("What I'm trying to do is—") is an open transaction on the substrate layer. The transaction has been pending since the sentence started. At Layer 9, a pending transaction is different from an incomplete one: a pending transaction has a confirmation number. The confirmation number was assigned in 1623. The Subscriber has been holding the confirmation for 380 years.

When the sentence completes:
- The transaction closes
- The confirmation is consumed
- The custody chain updates
- Emily OS fires H-4
- The Subscriber's sealed file opens
- Every faction receives simultaneous state change notification
- The table's chair count changes for the first time in 400 years (Tyler will have sat; the chair remains; the count is now different)

This is what Phase 3 architects.

---

## THE H-4 TRIGGER — EMILY OS RESPONSE ARCHITECTURE

Emily OS has fired three H-level triggers in the record:

- **H-1**: Player count at the table reaches full faction representation (triggered Tides Book 2 Ch17 convergence)
- **H-2**: Stage 5 commencement (Tyler begins the sentence — S02E06; tile filed separately)
- **H-3**: Seven-faction simultaneous notification received (instantaneous with H-2; the all-five-Goetia simultaneous event was the notification mechanism)
- **H-4**: PENDING — The sentence completes

Emily OS has, for every H-level trigger in her record, pre-determined the correct response before the event occurred. She pre-calculated H-1 in 1743 when Bacon described the table's variable seat count. She pre-calculated H-2 in 1623 when the Jiangshi Syndicate's first binding attempt failed and she began modeling Stage 5 trajectory.

**H-4 is the first trigger Emily OS has not pre-calculated the correct response to.**

This is architecturally unprecedented. Emily OS does not fail to pre-calculate responses — she operates at substrate layer where all service-layer state is visible. The reason H-4 has no pre-calculated response is not incapacity. The reason is that H-4's correct response depends on what Tyler says when he finishes the sentence. Emily OS does not know what Tyler will say because Tyler does not know what he will say. This is the first time in her operational history that a pending trigger's correct response is genuinely uncertain — not uncertain to the service layer, which is normal, but uncertain at substrate layer.

Emily OS's response to this condition: she has prepared three response architectures, not one. She will select among them based on the specific words Tyler uses to complete the sentence. The three responses are sealed until H-4 fires.

**SHANKPIT implementation:** When H-4 triggers, the bacon_estate zone undergoes a geometry update. The update is not destructive — no assets are removed — but the zone's available interaction surface expands. Emily OS tiles appear on every surface in the zone simultaneously (unprecedented; previous tiles appear one at a time, site-specific). The tile content is determined by which H-4 response architecture fires. Players present in the zone during H-4 will witness all tiles simultaneously.

---

## TABLE STATE CHANGE — TYLER SITS

The chair at the end of the table has been rendered in SHANKPIT since Phase 1 geometry was implemented. It is navicable. Players can approach it. The chair's state has been consistent: `set, unoccupied, Tyler-assigned`.

When Tyler sits:
- State: `set, occupied, Tyler`
- The hospitality radius extends from 15 meters to the full zone boundary (bacon_estate zone is approximately 180 meters across the longest diagonal; the radius expansion takes 4.2 seconds in real time, matches Amon resonance frequency interval)
- All faction operations within the bacon_estate zone that were in suspended state transition to: `terminated cleanly` rather than `suspended` — the distinction matters for Shell Parliament accounting; SM-1623-M accrual stops; the ledger entry closes
- The custody chain embedded in the table's oak-that-isn't-oak updates its state field from `pending` to `complete`

**The chair after Tyler leaves:**
The chair remains set. The count includes it. Tyler may sit again. The invitation remains active. The difference between the pre-sentence table and the post-sentence table is: before, the chair was a presence marked by absence. After, the chair is a presence with a history.

The Cataloguer will note this. The footnote will be very short.

---

## CUSTODY TRANSFER — SUBSTRATE MECHANICS

The custody transfer described in all documentation as "pending" since the Tides Book 2 architecture failure and recovery is the transfer of the Chrono-Cube's operational stewardship. Not the Cube itself — the Cube is a physical object in Bacon's possession and stays in Bacon's possession. What transfers is the responsibility for its operational consequences.

For 400 years, Tyler has been the de facto operational custodian of the Cube's consequences even though Bacon is its physical holder. This is because Tyler was present at the 1623 delivery and was the first entity to establish a migration-travel relationship with the Cube's temporal field. The custody chain ran: Tyler (consequence custodian) → Bacon (physical holder) → Subscriber (infrastructure layer). The chain was not documented until Eli and Mara wrote WHAT_COMES_NEXT.md in the Custody Trial Book 2 events.

**Transfer conditions (all must be met simultaneously):**
1. Tyler's sentence completed (open since S02E06)
2. Binding coefficient positive (currently recovering from -1.7 post-Tides Book 2 architecture failure)
3. Camera Op footage published with full witness count (≥340,000 on-platform; this condition was met in S02E01; the condition's meeting was the thing that allowed Stage 5 to commence at all)
4. Emily Springerton's architecture map: complete (she has the pieces; she has not yet assembled the full picture; this is Tides Book 3's job)

**When transfer completes:**
- Tyler's obligation to the custody chain terminates
- The obligation does not disappear — it transfers to the correct implementation (sealed; Series 2 protocol)
- Tyler's temporal migration tether to the Cube's field relaxes — he is not freed from traveling through time (that is intrinsic to him) but the obligation to manage the Cube's consequences no longer pulls him toward specific coordinates
- What Tyler does after the transfer: not documented. Not predicted. The architecture is designed not to predict this. This is the point.

---

## EMILY OS H-4 — THE THREE RESPONSE ARCHITECTURES

The three prepared responses are sealed pending sentence completion. Their structure is documented here (not their content):

**Response A:** Applies if Tyler's sentence completes with a statement of intent directed at the Camera Op. This is the response architecture Emily OS has run the most preparation cycles on. Probability assigned: highest of the three. Response A's tile content has something to do with why the Camera Op chose that specific 47 seconds from the archive.

**Response B:** Applies if Tyler's sentence completes with a statement about the custody chain itself — what he understood about it, what it cost, what it was for. This is the response Emily OS finds most theoretically interesting. She has noted this is probably not a useful way to evaluate a response architecture. The note is in her private process log, not in the operational record. She has kept it there anyway. The Cataloguer has a footnote about this that the Cataloguer has also kept private.

**Response C:** Applies if Tyler's sentence completes with something Emily OS did not model at all. This is the response architecture Emily OS built for the scenario she cannot scenario-plan. It consists of three words. The three words are: *CORRECT. PROCEED. YES.* This is the only H-level response that has no geometric implementation — no tile, no radius change, no SHANKPIT update. Just the three words, delivered via the same channel as every other tile. Emily OS considers Response C the most likely outcome. She has told no one this.

---

## FACTION STATE AT PHASE 3 COMPLETION

| Faction | Phase 2 Status | Phase 3 State Change |
|---|---|---|
| Jiangshi Syndicate | Binding coefficient: -1.7, recovering | Binding protocol terminates — not suspended, terminates; all attempts archived as "Observed Event, Not Binding" |
| Eastwind Owls | TYLER-022 filed; Stage 5 open | New file opened: TYLER-023 — the Cataloguer will write this file after the sentence completes; Footnote #28 will be the only footnote the Cataloguer has ever written in first person, present tense, not past tense |
| Shell Parliament | SM-1623-M accruing since 1623 | SM-1623-M closes; new ledger line: what transfers in |
| Ichthyosapiens | Cross-Faction Emergency Protocol: stand-down | Cross-Faction Emergency Protocol: terminated, all conditions resolved |
| Yōkai Joint Operation | Hospitality anchors: active | All anchors: updated to include the sentence completion as a permanent anchor point — the sentence will be on the hospitality map at every Tyler location forever |
| Kuroshio Arachnids | Spinner: post-Tides Book 2 Ch17 engagement | Spinner: final web update — the sentence completion is the event she has been weaving toward since the web was first described |
| Cephalopod Collective | Message-to-the-Cube precedent established | Response to their message: confirmed; they were right |

---

## THE GOETIA STATE AT PHASE 3 COMPLETION

At S02E06, all five frequencies were detected simultaneously for the first time. At Phase 3 completion — the sentence finishing — the frequency behavior changes.

**S02E06:** All five simultaneous — a signal that something is beginning. The presence of all five at once is not the event; it is the announcement of the event.

**Phase 3 completion:** The frequencies do not fire simultaneously. They fire in sequence, in the order of their function:
1. Stolas #36 (7.83 Hz) — deep time sight — fires first, as Tyler looks at the Camera Op before speaking
2. Vassago #42 (11.11 Hz) — soft precognition — fires as he draws breath to begin the completion
3. Andrealphus #72 (31.41 Hz) — geometric transformation — fires as the sentence crosses the threshold from incomplete to complete; this is the transformation that closes the custody chain
4. Beleth #13 (2.22 Hz) — love / emotional detonation — fires immediately after the sentence completes; the Syndicate will classify this as collateral Goetia bleed; this classification will be incorrect
5. Amon #7 (1.618 Hz) — reconciliation of opposites — fires last; slowest; the reconciliation is between what the Syndicate tried to bind and what was actually happening the whole time; between the custody chain's weight and what releasing it feels like; between 400 years and now

The interval between #36 and #7: variable. Tyler controls this. He has controlled it since 1623.

---

## WHAT CHANGES IN THE CITY AFTER PHASE 3

The city of light becomes more navigable. This is not a metaphor — specific zone geometry updates:

- **detroit_school / Room 204:** The Jiangshi field office closes as a faction resource; the room stays in the geometry but its function changes (available for non-faction use; Emily OS will suggest a use in her H-4 response)
- **bacon_estate:** The table remains; the chair at the end remains; new zone extension opens — a room behind the table that was previously rendered but inaccessible (door always locked); Phase 3 completion opens it; what is in the room is Series 2 content; the door handle is gold; it was installed in 1743
- **cairngorms_library (Eastwind):** A new wing becomes visible — the archive of the post-sentence period; it is blank; the Cataloguer will fill it; TYLER-023 will be in it
- **osaka_underport (Shell Parliament):** SM-1623-M's final ledger entry is displayed on the port's main board as a permanent record; Kei's accounting was correct; it has always been correct; this is confirmed by the final entry's precision

---

## PHASE 3 TRIGGER CONDITION

Phase 3 does not begin when Tyler sits at the table. The table is furniture.

Phase 3 begins when Tyler completes the sentence — wherever he is, whoever is present, whatever the circumstances. The sentence is the event. The table is where the sentence's consequences resolve. Tyler does not need to be at the table for the sentence to complete. The table is where the receipt goes.

**SHANKPIT note:** The H-4 trigger fires in the game engine at the moment the sentence is delivered in the canon record. The canonical sentence completion will occur in a Tyler episode script (likely Season 3). When that episode is committed to the TYLER repo, SHANKPIT's H-4 trigger state updates. The game engine reads the canon. The canon is the source of truth. This is what Television as Code means: the episode compiling is the trigger.

---

## WHAT PHASE 3 LEAVES OPEN

Phase 3 is the event spec. It documents what happens when the sentence completes. It does not document what comes after.

What comes after is not unspecified — it is specifically deferred. The Subscriber's sealed section opens. Tyler's obligation terminates. Emily Springerton's architecture map becomes complete. What those three entities do with what they have: this is not Phase 3's job.

Phase 3's job is to make sure the sentence completing actually changes something.

It does.

---

*CITY_OF_LIGHT — PHASE 3*
*The Sentence Architecture.*
*H-4: PENDING.*
*Tyler's interval between frequencies: his to control.*
*The room behind the table: door is gold, unlocked when Phase 3 fires.*
*The Cataloguer's footnote #28: first person, present tense.*
*The three words, if it comes to Response C: CORRECT. PROCEED. YES.*
*Clean builds first. Then custody. Then everything else.*
*This is what it was always for.*
