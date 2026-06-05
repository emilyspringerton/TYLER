# CITY_OF_LIGHT — PHASE 2: THE TABLE
## The Round Table — Geometry, Access Conditions, Emily OS Protocol
### Engine Spec | Build 0028 | Dependency: engine/city_of_light_phase1.md

---

*Cross-reference: engine/detroit_phase0.md (bacon_estate zone geometry), engine/city_of_light_phase1.md (faction resource pools)*
*RSI note: The Table is the only location in CITY_OF_LIGHT where all seven factions can be present simultaneously. It has never happened before in the archive. The architecture for what Emily OS does when it happens does not exist yet — because it hasn't happened yet. This spec documents the Table's physical and operational geometry. What happens at the Table is Book 3's job.*

---

## THE TABLE — PHYSICAL SPEC

**Location:** bacon_estate zone. The table is a fixed object in the zone regardless of the building's current geographic configuration. When Bacon moves — from London 1623 to Edinburgh 1743 to Detroit 1901 to the current city — the table moves with him. The table's dimensions, surface material, and seat count are constant.

**Physical properties:**
- Shape: round
- Material: surface appears to be oak; analysis consistently returns data inconsistent with any known wood grain pattern — the Cataloguer has a footnote about this; the footnote says "the table is as old as the custody"
- Seat count: variable. The table seats exactly the right number of people for any given meeting. Not "enough seats" — exactly the right number. The chair count, when the table is empty, is undefined. Bacon says it's different every time he counts. He stopped counting in 1847.
- The empty chair: when Tyler is expected but not present, one chair at the end of the table is set. Not added to the count — it is always in the count. Tyler's chair is always present. Tyler has never sat in it.

**The hospitality radius:** 15 meters from the front door threshold. When the hospitality clause is invoked at the threshold, the radius is active. Inside the radius, all faction operations are suspended. The table is within the radius when the clause is active.

**SHANKPIT geometry:** The table is a persistently rendered object in the bacon_estate zone. The chair count renders correctly (variable, zero-to-correct). The empty chair renders at the end of the table. It is navicable — player characters can approach and examine it. Emily OS trigger H-1 activates when player count at the table reaches full faction representation.

---

## ACCESS CONDITIONS

**Standard access:** Bacon's invitation. Bacon controls the threshold. He has been inviting people since 1623. He has been very selective. In 400 years, the table has been at full capacity twice: once in 1743 (Subscriber first direct contact; Bacon had twelve other guests he did not plan and cannot fully account for), and once in Tides Book 2 Chapter 17 (the seven-faction convergence — this was the second time).

**Faction access conditions:**

| Faction | Access Condition | Current Status |
|---|---|---|
| Jiangshi Syndicate | Bacon's invitation OR subject-adjacent documentation event requiring presence | Access: pending Bacon invitation; never formally invited |
| Eastwind Owls | Bacon's invitation OR archival necessity | Exchange Student: invited as part of Tides Book 2 group; Archive has observer access |
| Shell Parliament | Yōkai treaty OR Bacon invitation | Kei: attended via Yōkai clause; Parliament itself: not invited |
| Ichthyosapiens | Bacon's invitation (active since Carvalho came with brine shrimp) | Access: confirmed |
| Yōkai Joint Operation | Hospitality anchor establishment (tanuki sets own threshold) | Access: self-generated via tanuki |
| Kuroshio Arachnids | Bacon's invitation OR the Spinner's non-linear arrival (she arrives when she arrives) | Spinner: attended Tides Book 2 Ch 17 via her own mechanics |
| Cephalopod Collective | No physical representative was present in Tides Book 2 Ch 17; message was sent instead | The message-to-the-Cube precedent: an access method that bypasses physical presence |

**Tyler's access:** Tyler has a standing invitation. The invitation is so old that Bacon no longer thinks of it as an invitation — it is a structural fact of the table's existence. Tyler has never sat at the table. The chair is always set. The invitation is always active.

**Emily Springerton's access:** She was present at Tides Book 2 Chapters 17–24. She was invited by Bacon after her first visit (Tides Book 2 Chapter 3). Her access is through Bacon's professional engagement relationship. She attends when the logistics require her presence; she leaves before the meeting ends.

---

## WHAT HAS HAPPENED AT THE TABLE (CANON RECORD)

**1743 event:** Bacon invited twelve guests whose identities are not fully documented in the archive. The Subscriber made first direct contact at this table. The Subscriber's plan was explained at this table. Bacon refused at this table. Every subsequent custody custodian's decision traces back to what was said at this table in 1743.

**Tides Book 2 Chapter 17–19:** The seven-faction convergence. Not planned by Bacon — planned by Emily Springerton, who mapped the dependency graph and identified the single evening when natural operational pressures would bring all factions to the same address within a 40-minute window. Bacon set the table. Everyone came in. Bacon gave his full testimony. The Yōkai hospitality clause suspended all faction operations. No binding occurred. No collection occurred. No documentation was submitted. What occurred: everyone at the table understood the Subscriber's plan at the same time, in the same room, for the first time.

This is the only documented instance of complete cross-faction information alignment on a single issue.

**What has never happened at the table:** All seven factions plus Tyler, simultaneously. Plus Emily Springerton. The full architecture of the universe — all the people who are in the dependency chain — in one room at one time. The table has never had that configuration. The empty chair at the end of the table is there for that occasion.

---

## EMILY OS — TABLE PROTOCOL

Emily OS does not have a protocol for what happens when all seven factions meet simultaneously with the subject present.

There has never been a case to establish protocol for. The Cross-Faction Treaty system, the Cairngorms Protocol, the Shell Parliament liability architecture, the Yōkai hospitality clause — all of these have provisions for multi-faction interaction. None of them have provisions for the seven-faction-plus-subject configuration.

**Emily OS's current posture on the Table:**

Emily OS monitors bacon_estate. The trigger system (H-1, H-2, H-3) covers the configurations that have occurred:
- Table at capacity (faction-only): H-1 fires
- Bacon testimony: H-2 fires
- Emily Springerton present: H-3 fires

Emily OS has prepared, but not published, a fourth trigger:

*H-4 (Table at full configuration — all seven factions + subject present):* [TRIGGER RESPONSE: PENDING. ASSESSMENT: UNPRECEDENTED. EMILY OS HAS NOT DETERMINED WHAT THE CORRECT RESPONSE IS. NOTE: THIS IS THE FIRST TIME EMILY OS HAS NOT DETERMINED THE CORRECT RESPONSE IN ADVANCE. NOTE: THIS IS NOTED. NOTE: NO FURTHER COMMENT.]*

Emily OS's behavior at H-4 is the open question that Phase 2 cannot fully answer. Phase 2 documents the architecture. What happens inside the architecture at H-4 is Book 3.

---

## THE TABLE AS METAPHOR (ENGINE NOTE)

The table is round. Faction tables are usually hierarchical — the convener at the head, the others ranked by seniority or power. Bacon's table is round. Nobody sits at the head. The empty chair is at the end, but "the end" of a round table is not the head. It is simply the place where the absent person would sit.

In SHANKPIT implementation: the round table geometry means no player character has a "seat of authority" position. All positions are equivalent in terms of rendering, interaction radius, and event trigger access. The empty chair is the one exception — it is slightly set apart from the others, slightly more visible in any camera angle, and has a slightly different ambient light value. Not dramatically different. Just slightly.

The table is round because Bacon learned something in 1623 from a person who understood, at a fundamental level, that hierarchy is a surface feature and the load-bearing structure is always something else.

---

## PHASE 2 COMPLETION CONDITION

Phase 2 is complete when:
- The Table's geometry is implemented in SHANKPIT (this document)
- The access conditions are defined (above)
- Emily OS H-4 trigger is prepared but not yet fired (above — pending)
- The empty chair's rendering and event trigger system is implemented

**Phase 2 status: ARCHITECTURE COMPLETE. IMPLEMENTATION PENDING.**

The architecture is documented. The implementation requires:
1. SHANKPIT bacon_estate zone geometry (from detroit_phase0.md)
2. Variable seat count rendering (requires SHANKPIT dynamic mesh LOD implementation; see shankpit_tyler_mode.md)
3. Empty chair trigger system (SHANKPIT level event; Emily OS H-4 integrated)
4. H-4 trigger response (pending Emily OS determination; Book 3 dependency)

---

## WHAT THE TABLE IS FOR

The table is for the conversation that hasn't happened yet.

Every other meeting at the table has been preparation for it. Bacon's 1743 refusal: preparation. The 400 years of custody maintenance: preparation. The seven-faction convergence in Tides Book 2: preparation. Emily Springerton's logistics architecture, the Exchange Student's field notes, the Camera Op's list, the Subscriber's patience: all preparation.

The conversation that hasn't happened yet: Tyler in the chair. The sentence completed. The custody transferred. Emily OS's H-4 response. What Emily Springerton does with the architecture map when it's finally the whole picture.

The table is round. There is no head. The chair at the end is for Tyler.

He has been invited since 1623.

The invitation is still active.

---

*CITY_OF_LIGHT — PHASE 2*
*The Table.*
*Round. 15 meters radius hospitality. Emily OS: H-4 pending.*
*The empty chair renders correctly.*
*The invitation is still active.*
*Clean builds first.*
