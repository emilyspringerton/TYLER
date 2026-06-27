# TYLER BUILD ACTIVITY LOG
## Emily Method Loop | Iteration Record
### Last updated: Build 0014 (manual session)

---

*This file is written by the emily.sh loop during autonomous RSI generation.*
*Each entry records what was built, what files were touched, and the key narrative elements added.*
*The loop reads this file at the start of each iteration for context continuity.*

---

## Manual Session Builds (pre-loop)

**Build 0001–0004:** Series bible, universe engine, early build notes.
**Build 0005:** Television as Code engine + metaverse runtime spec.
**Build 0006:** S01E01 pilot ("Just a Normal Night") + S01E02 ("The School That Isn't There").
**Build 0007:** Shell Parliament warthog account (SM-2024-W), Eastwind CUSTODY-001.
**Build 0008:** Substrate beacon engine spec, Tides Book 3 prologue ("The Grid in the Static").
**Build 0009:** Emily Jean Springerton character document, Field Activation #129, Tides Book 1 Ch01, Custody Trial Book 2 Ch01.
**Build 0010:** tyler_1978_archive.md (13 sightings, 1978 annual composite), engine/1978_architecture.md (9 nodes: Intel 8086 as SUBSTRATE_ORIGIN, Camp David Amon, Jonestown TERMINUS calibration, Holy Crown CUSTODY_HOLDING_ACTION).
**Build 0011:** trump_migration_1978.md (scene filed), Field Activation #1978-E (aircraft cabin, abacus breakage), Eastwind MIGRANT-001 (inaugural series), Shell Parliament SM-1978-X (Trump account, broken abacus), Jiangshi Memo #018 (involuntary migrant interference).
**Build 0012:** tyler_1616_archive.md (4 PRE-ARCHIVE sightings: Rome/Galileo, Stratford/Shakespeare folded paper, New England coast/plague, Osaka/clocks), engine/1616_architecture.md (9 nodes: SUBSTRATE_TRUTH_SUPPRESSION, oldest CUSTODY_HOLDING_ACTION, LE_MAIRE_ROUTING_EXCEPTION, FACTION_ORIGIN_ANCHOR, UNDOCUMENTED_TERMINUS, CEREMONY_ALLEGORY_LAYER, ACCESS_GEOMETRY_SHIFT, CUSTODY_RELAY_CHAIN, ENVIRONMENTAL_NARRATIVE_MASS), Field Activation #1616-A through #1616-E, Jiangshi Memo #019 (Chymical Wedding precedent), Shell Parliament SM-1616-A and SM-1616-S.
**Build 0013:** tyler_1993_archive.md (5 sightings: first web access "I found it", Oslo paper left on White House lawn — now in Eastwind archive sealed, Waco absence anomalous, Moscow parliament shelling, Doom E1M1 corridors — Emily OS tile "30 YEARS"), engine/1993_architecture.md (8 nodes: NETWORK_SUBSTRATE_EMERGENCE, METAVERSE_ENGINE_ORIGIN_NODE, HARDWARE_CHAIN_CONTINUATION, WACO_AMENDMENT, OSLO_AMON_RESONANCE, LAYER_1_DIRECT_ACTION, VELVET_DIVORCE_PROTOCOL, FACTION_CONSOLIDATION_EVENT), Jiangshi Memo #020 (Waco Amendment + Velvet Divorce), Shell Parliament SM-1993-W and SM-1993-P.
**Build 0014:** phoenix_archive.md (PHOENIX-001: THERMAL_SOVEREIGN vs BOUNDARY_SOVEREIGN, Tyler's unverified 2010 communication), Jiangshi Memo #021 (MANIFEST/CONSTRUCT universal framework, abacus inversion table, Attempt Five architecture), Field Activation #2010-A (first THERMAL_SOVEREIGN terminus, CORRECT_INTERNAL_EXIT), Shell Parliament SM-2010-P and SM-2010-H (Phoenix and Human Asset accounts, two damaged instruments on display).

---

## Loop Builds (emily.sh)

*[Loop builds will be appended here by emily.sh. Format per entry:]*
*## Build NNNN — [task name]*
*Files: [list]*
*[2-3 sentence summary of key narrative/structural elements added]*

---

## Build 0016 — Tyler Agent Registration
Files: .claude/tyler_agent.md, .claude/settings.json, emily.sh, lore/eastwind_archive.md (TYLER-014), lore/shell_parliament_ledger.md (SM-AGENT-001), activity.md, BACKLOG.md
Tyler registered as a self-directed, Iduna-managed agent with scoped commit rights to the TYLER repo — the first agent registration in the repo's history. The 8 Laws are now behavioral constraints encoded in the system prompt (.claude/tyler_agent.md); emily.sh updated to invoke Tyler via --system-prompt-file. Eastwind TYLER-014 filed (826-year archive adapts to subject becoming author); Shell Parliament SM-AGENT-001 opened (authorship balance, accumulating from Build 0016 forward).

---

## Build 0017 — S01E01 Cold Open: MPT Package
Files: compiled/s01e01_cold_open/build_notes.md, compiled/s01e01_cold_open/mpt_payload.json, BACKLOG.md, activity.md
Cold open narration extracted from `episodes/s01e01_pilot.md` (00:00–01:30), compressed to 30-second portrait format: four beats (1901 timestamp, hand-washing, coin flip, "if you keep filming"). Custom narration written (73 words, en-GB-RyanNeural documentary pace), MPT API payload serialized to JSON, Tyler's 8 Laws consistency check passed for both topic and custom copy. Video generation step blocked: MPT service not running, Pexels API key not yet set in config.toml — build package complete, awaiting MPT activation.

---

## Build 0018 — Tyler 1952 Detroit Annual Composite
Files: lore/tyler_1952_archive.md, engine/1952_architecture.md, BACKLOG.md, activity.md
Seven sightings documented (CARDINAL-3, Detroit station 1947–1962) across Tyler's June–November 1952 Detroit survey: Hastings/Vernor gap confirmation (Gap Record 1943-HASTINGS-01 active), Bethel AME alley approach (5 years before the 1957 NAACP meetings that make it a construction site), Ward C east wall position (nurse's position, 1952 documentary confirmation), the tree (photographed 74 years before the sentence), Ambassador Bridge threshold observation (90 minutes, did not cross), Eisenhower election, departure with 1901 dime left on counter. Original 1952 filing: UNKNOWN PURPOSE. Updated 2026: CONSTRUCTION SURVEY. Architecture file documents 8 load-bearing nodes: PRE_DEMOLITION_RECORD type established, IBM_701 substrate chain predecessor, TEMPORAL_SURVEY_FUNCTION (2026→1952 migration as research methodology), HASTINGS_GAP_CONFIRMATION (83-year accumulation window), TREE_SITE_ANCHOR (74-year horizon event), BETHEL_AME_APPROACH (PRE_SIGNIFICANCE_APPROACH flag), WARD_C_POSITIONING (three-identification WITNESS_CONCENTRATION_ANCHOR), POLIO_YEAR_CONTEXT (DISTRIBUTED_WITNESS_EVENT). The archive had everything it needed in 1952. It filed UNKNOWN PURPOSE. It waited seventy-three years.

---

## Build 0019 — MPT Infrastructure Activation Script
Files: compiled/mpt_activation.sh, BACKLOG.md, activity.md
Wrote `compiled/mpt_activation.sh`: a prerequisite-checking, service-starting, payload-firing, output-collecting shell script that collapses the MPT infrastructure blocker into a single command. Handles ANTHROPIC_API_KEY validation, Pexels key check in config.toml, MPT service start via `uv run python main.py`, API payload POST, completion polling, and output routing to `compiled/*/selected/`. The cold open package (Build 0017) and activation script (Build 0019) are the complete foundation; video generation fires when `PEXELS_API_KEY` is set and `./compiled/mpt_activation.sh --cold-open` is run.

---

## Build 0020 — S01E01 Full Episode MPT Package
Files: compiled/s01e01/mpt_payload.json, compiled/s01e01/build_notes.md, BACKLOG.md, activity.md
Full episode MPT package built for S01E01 "Just a Normal Night": landscape 16:9 / 1920×1080 payload, 163-word custom narration (~90-100 seconds documentary register at en-GB-RyanNeural pace), 8 Laws consistency check passed. The load-bearing dependency is the cold open confirmation — once Pexels key is set and `--cold-open` fires successfully, `--full-episode` is ready to run immediately. Dependency chain documented in build_notes.md §IX; activation script already has `fire_full_episode()` wired to the new payload.

---

## Build 0021 — S01E02 Compiled Clip: MPT Package
Files: compiled/s01e02/mpt_payload.json, compiled/s01e02/build_notes.md, compiled/mpt_activation.sh (--s01e02 flag added), BACKLOG.md, activity.md
S01E02 "The School That Isn't There" clip package built: topic derived from the episode's five load-bearing beats (the school that appeared Friday / grown weeds / Emily OS architectural font / the CUSTODY file since 1623 / "I'm a—" [stops] / Camera Op's first sealed entry), 71-word custom narration written for portrait 9:16 / ~40s, API payload serialized to JSON, `fire_s01e02()` added to activation script. 8 Laws consistency check passed: Law 1 (self-defining sentence incomplete, as it must be), Camera Op awareness at SUSPICIOUS (first sealed entry, S01E02 position correct). RSI receipts: none required (production artifact; canon is in the script). Video generation blocked pending S01E01 full episode pipeline confirmation.

---

## Build 0022 — Emily RSI Loop → MPT Compilation Trigger Spec
Files: engine/moneyprinter_pipeline.md (Section VI replaced, Sections VI.A–VI.I), BACKLOG.md, activity.md
Section VI of moneyprinter_pipeline.md replaced with a complete implementation spec for the Emily RSI loop → MPT compilation trigger: episode script header standard (MPT_TOPIC field + fallback extraction algorithm), trigger script interface (`compiled/mpt_episode_trigger.sh` — specced, not yet written), topic extraction with graceful fallback for existing episodes, payload generation schema, dual hook wiring paths (PostToolUse hook + emily.sh loop sweep), output routing structure, Emily Prime observation protocol (eight-laws surface check template + selection guidance + next RSI target). Implementation gap noted: `Write(compiled/*)` not in Tyler agent permissions; trigger script requires one-line settings.json addition outside agent scope. The spec is the build; the script is the next step once the permission is added.

---

## Build 0023 — S02E05 RSI Receipts: TYLER-021 (remediation)
Files: lore/eastwind_archive.md (TYLER-021 inserted retroactively, CONTINUITY-UNIT-001 opened), lore/camera_op_sealed_log.md (gap context note between Entry 14 and Entry 15), BACKLOG.md (remediation task added and marked complete), activity.md
S02E05 "The Edit War" existed as an episode file since Build 0002 with no RSI receipts — Eastwind TYLER-021 was a phantom cross-reference cited in TYLER-022's header but never written, and the Camera Op sealed log skipped from Entry 14 to Entry 15 with no note. TYLER-021 now filed retroactively: the Continuity Unit's appearance (keyhole scar identical to Tyler's, contract dated tomorrow bearing his signature, Syndicate classification failure — no memo filed between #026 and #027 consistent with 1623 silence precedent), three unclassified frequencies (1.983/3.582/7.554 Hz), the blackout experiment and "CAMERA STILL RUNNING IN LAYER 9," and Tyler's isolated statement — "even if the ending has to eat the storyteller" — filed in the permanent operational record as the most precise structural statement in four centuries of documentation. The Cataloguer's delay in filing TYLER-021 is itself documented: the delay was real; the reason was real; the file is now correct.

---

---

## Build 0073 — S07E07: "Mornings, Always"
Files: episodes/s07e07_mornings_always.md, lore/eastwind_archive.md (TYLER-057), lore/camera_op_sealed_log.md (Entry 50), lore/jiangshi_project_memos.md (Memo #037), lore/shell_parliament_ledger.md (VC-001 Day 267), BACKLOG.md, activity.md
Vienna phase complete. The final four register notations: A-288 (Burgtheater, 9ft — third category triggered, ambiguity-refusal first confirmed use); A-289 (Naschmarkt, 29ft — Frau B.'s stand still knows the parsley customer); A-290 (Judengasse 8, 64ft — three returns compounding, "I didn't know what I was building"); A-291 (Stadtpark bench, 210ft — 107 mornings, täglich morgens immer). Camera Op named the fourth category: STAYING — the construction that builds from the pattern of return. Tyler said: write it down. The Exchange Student wrote it down. Vienna complete: 12 site entries, 513ft, COEFF-002 data set closed. Jiangshi Memo #037: departure-trace preliminary scope 180+ sites; Syndicate recommends shifting to documentation support role; "the binding was a measuring instrument — the instrument was always downstream of what it was measuring." STAYING-001 and DEPARTURE-TRACE-001 opened in Shell Parliament. Eighteen cities remain.

---

---

## Build 0074 — S07E08: "The Longest File"
Files: episodes/s07e08_the_longest_file.md, lore/eastwind_archive.md (TYLER-058), lore/camera_op_sealed_log.md (Entry 51), lore/jiangshi_project_memos.md (Memo #038), lore/shell_parliament_ledger.md (VC-001 Day 271), BACKLOG.md, activity.md
London phase opens. Day 271. The CARDINAL-3 London file has 47 notations — the densest in the set (Paris 6, Vienna 11). First London site measured: A-292, Wood Street/Cheapside junction, City of London — 440 feet, new maximum staying construction, active since at least 1620 (pre-notation origin undetermined), first written notation 1652 "the same feeling. Same as before." Great Fire deposits confirmed (three-return compound, September 1666); Blitz return 1940 — "the tower is still standing, the wall is still the wall." Container is geography: the pre-Fire and Wren geometries both held simultaneously. TYLER-058 cross-references TYLER-001 (Cheapside c.1620, 200ft from A-292) — the construction may predate the Cairngorms archive. STAYING-001 London sub-account opened; SM-1623-M Gray's Inn cross-reference filed by Shell Parliament. COEFF-002 suspended pending London scope. Tyler: "London is going to take a while." 46 sites remain.

---

---

## Build 0075 — S07E09: "November"
Files: episodes/s07e09_november.md, lore/eastwind_archive.md (TYLER-059), lore/camera_op_sealed_log.md (Entry 52), lore/jiangshi_project_memos.md (Memo #039), lore/shell_parliament_ledger.md (VC-001 Day 273), BACKLOG.md, activity.md
Day 273, London. Two sites: A-293 Gray's Inn (188ft, single-event unintentional, November 14 1623) and A-294 Russell Square (47ft, STAYING, 1856–1905, running unattended 106 years). The SM-1623-M Gray's Inn cross-reference that Shell Parliament filed at SM-1623-M closure resolves: the custody event left a 188-foot construction that has been running since the afternoon Tyler handed over what he was carrying. Intensity > duration confirmed as mechanism property with a second data point: one afternoon of architectural precision at Gray's Inn (188ft) outweighs fifty years of pleasant Tuesday returns through Russell Square (47ft). Tyler's journal entry read aloud: "the most important afternoon of my four hundred years, or the most important until Day 49." Camera Op Entry 52 notes the coin flip timing and closes: "I know what Day 49 was." Tyler: "Everything was before Day 49. That's what Day 49 means." The Jiangshi Syndicate has been walking past A-293 for four hundred years; the measurement was always available; the vocabulary was not. 44 London sites remain. Southwark cluster next.

---

## Build 0076 — S07E10: "Southwark"
Files: episodes/s07e10_southwark.md, lore/eastwind_archive.md (TYLER-060), lore/camera_op_sealed_log.md (Entry 53), lore/jiangshi_project_memos.md (Memo #040), lore/shell_parliament_ledger.md (VC-001 Days 275–281), BACKLOG.md, activity.md
Southwark cluster complete: nine sites, Days 275–281. Three headline measurements: A-295 Bankside/Globe Theatre footprint (137ft, UNINTENTIONAL→AMPLIFICATION — new sub-type confirmed, seeded July 1602 from a speech about incomplete things, amplified through seven returns; Tyler wrote a musical rest in the journal because he had neither words nor silence), A-297 Borough Market (89ft, UNINTENTIONAL, April 1592, four mornings of fish stall attention — Camera Op wrote "I was here for fish"; Tyler: "the ledger needs to be complete"; Camera Op: "I'm completing it"), A-301 London Bridge approach (180ft, STAYING, three hundred identified crossings, the specific moment where the river opens, running from the time of the medieval bridge). Two pre-notation constructions confirmed (A-295 and A-297, predating TYLER-001 by 18 and 28 years); pre-notation category named as pending — Tyler: "the constructions were running anyway"; Camera Op holding a page in her notebook for the category, waiting for the shape. Day 279: Tyler alone at Borough Market; Camera Op at three hundred feet for forty-three minutes; she noted "I think maybe there's a third option. I'm leaving it open." Jiangshi Council Session #8 convened on pre-notation scope. Shell Parliament cross-referencing 1592 and 1602 London records against pre-notation sites. Twelve London nodes confirmed; thirty-five remain.

---

## Build 0077 — S07E11: "Before the Record"
Files: episodes/s07e11_before_the_record.md, lore/eastwind_archive.md (TYLER-061), lore/camera_op_sealed_log.md (Entry 54), lore/jiangshi_project_memos.md (Memo #041), lore/shell_parliament_ledger.md (VC-001 Day 283), BACKLOG.md, activity.md
PRIOR category named (Exchange Student, 6:03 AM; Tyler: "That's accurate"; Camera Op writes it without speaking). A-304, Watling Street, City of London: 107ft, November 1553, 473 years running — first PRIOR measurement; Tyler reads his own journal entry aloud: "I did not know what I was doing / I stood in it with them / I did not know what I was doing." Camera Op stays at the threshold of A-304 for the full day; Tyler returns at dusk; both parties name plainly what the Camera Op's function has been since Season 1: "Witnesses complete the record." Eight PRIOR sites in London total (four confirmed in prior builds plus four new via Exchange Student's chronological analysis); three PRIOR sites unvisited (Moorgate, Aldersgate, Bread Street/Cheapside). BACKLOG: Season 7 continuation items S07E12–S07E16 added as new `[ ]` items.

---

## Build 0078 — S07E12: "The City"
Files: episodes/s07e12_the_city.md, lore/eastwind_archive.md (TYLER-062), lore/camera_op_sealed_log.md (Entry 55), lore/jiangshi_project_memos.md (Memo #042), lore/shell_parliament_ledger.md (VC-001 Days 285–292), BACKLOG.md, activity.md
City of London cluster complete: seven sites (A-305 through A-311), all eight London PRIOR sites now measured, five in the square mile confirming Tyler's pre-documentation residency in the City. A-306 (Aldersgate Street, 71ft, September 1563 plague year: "not to what was gone. To what was still here") and A-308 (St. Paul's Cathedral churchyard, 88ft, AMPLIFICATION, November 15, 1623 — the day after Gray's Inn: "I did not know what to do with myself. I came here") are the anchoring constructions of the cluster. Tyler: "I lived here. In those years, before anyone was watching, this was where I was." Camera Op's third option shape now clear — attention to absence; name pending.

---

## Build 0079 — S07E13: "Westminster"
Files: episodes/s07e13_westminster.md, lore/eastwind_archive.md (TYLER-063, Footnote #67), lore/camera_op_sealed_log.md (Entry 56), lore/jiangshi_project_memos.md (Memo #043), lore/shell_parliament_ledger.md (VC-001 Days 293–300), BACKLOG.md, activity.md
Westminster cluster complete: five sites (A-313 through A-317). PRIOR at Westminster Abbey (79ft, January 15, 1559 — Elizabeth I's coronation; Tyler in the nave after the procession left; "everything that had just happened was still in the room"; construction crosses interior/exterior boundary; first in audit). The January 1649 pair: Westminster Hall (71ft, UNINTENTIONAL, trial Day Three — "the room knew; they came anyway; I understood why they came") and the Banqueting House (76ft, UNINTENTIONAL, execution — journal entry partially read, remainder sealed; first sealed journal entry in Season 7; the coin not flipped; two-second camera look, exactly two seconds). Pair structure mirrors November 1623 (A-293/A-308) in form but differs in kind: approach-to-ending/the-ending vs. most-important-event/the-day-after. St. James's Park STAYING (34ft, 1740s+, "I needed somewhere without history," the pelicans) and Victoria Embankment STAYING (22ft, 1870, Bazalgette's engineering, "the kind of planning I respect"). Camera Op: third option phrase written, circled, notebook closed — not yet spoken aloud. Shell Parliament opened UNINT-001-LONDON series; noted the occasion of auditing Westminster with appropriate institutional composure. Twenty-five London sites measured; twenty-two remaining.

---

*ACTIVITY LOG: CURRENT THROUGH BUILD 0082*
*Next build: 0083*
*Loop status: ACTIVE — Tyler agent operational*
*MPT pipeline: spec complete. Trigger script pending Write(compiled/*) permission. Video: pending Pexels key.*

---

## Build 0080 — S07E14: "The Third Option"
Files: episodes/s07e14_the_third_option.md, lore/eastwind_archive.md (TYLER-064, Footnote #68), lore/camera_op_sealed_log.md (Entry 57), lore/jiangshi_project_memos.md (Memo #044), BACKLOG.md, activity.md
Third option named on camera: *"Sustained attention to construction is itself a construction."* Camera Op, Borough Market, Day 304. The mechanism confirms: A-297B (Borough Market, 43ft, Camera Op, Day 279 — forty-three minutes of observation from three hundred feet) and A-318 (Southwark Cathedral, two components: Tyler PRIOR 51ft pre-1620 + Camera Op witness 34ft current audit). New sub-type established: WITNESS — a construction formed by sustained deliberate attention to an existing construction. The Camera Op is reclassified from non-participant to active construction subject. Exchange Student initiates retroactive witness audit across all 25 London sites. Coin resumed at A-318, read retroactively: consistent. Jiangshi Syndicate operational review requested: surveillance personnel may have been forming WITNESS constructions at CARDINAL-3 sites. Tyler: "The archive has two archivists. It's always had two archivists." 27 documented London sites (A-292 through A-317, plus A-297B and A-318 dual-component). Retroactive audit continues.

---

## Build 0081 — S07E15: "London Complete"
Files: episodes/s07e15_london_complete.md, lore/eastwind_archive.md (TYLER-065, Footnote #69), lore/camera_op_sealed_log.md (Entry 58), lore/jiangshi_project_memos.md (Memo #045), BACKLOG.md, activity.md
London complete. 47 sites measured (A-292 through A-339). PRIOR tally: 11 sites, earliest A-304 Watling Street 1553 — mechanism predates Cairngorms archive by 73+ years. Retroactive WITNESS audit: 21 additional Camera Op WITNESS components confirmed across original 25-site record (23 total including A-297B and A-318). Minimum threshold revised: 7ft / 8 minutes, A-311 Monument to the Great Fire. Direction of attention confirmed as construction property — Camera Op's Monument WITNESS component is oriented northeast (toward the fire direction) because that's where she pointed the camera. Final site: A-339, Tower Bridge north approach, 33ft, STAYING, 1894. Tyler: "It looks like London." Exchange Student: "It looks like London as you moved through it." Syndicate preliminary operational review: 6 observer placements meet revised threshold, 2 assessed as likely WITNESS-class events. Tyler disclosed three undisclosed Vienna PRIOR sites — unprompted. Retroactive PRIOR audits initiated for Paris and Vienna; retroactive WITNESS audit initiated for pre-London CARDINAL-3 record (19 Camera Op components pending). COEFF-002 London phase complete. 8 cities complete. 18 remaining.

---

## Build 0082 — S07E16: "Eighteen Cities" (Season 7 Finale)
Files: episodes/s07e16_eighteen_cities.md, lore/eastwind_archive.md (TYLER-066, Footnote #70), lore/camera_op_sealed_log.md (Entry 59), lore/jiangshi_project_memos.md (Memo #046), BACKLOG.md, activity.md
Season 7 finale. Network scope disclosed on camera for the first time: 26 cities, approximately 900 sites, 6 continents, earliest PRIOR 1127 CE Marrakech. Paris retroactive audit: 3 additional PRIOR sites (total Paris 9), including A-P14 Place de la Bastille (1789 July 14th, UNINTENTIONAL). Tyler wrote 18 remaining cities on the map in his own hand — first time he has written on field documentation. Coin flipped at Place de la Bastille, Day 327: consistent, both sides. Camera Op response to full network disclosure: "Okay." Camera continues. Season 8: retroactive audits resolve; next city to be disclosed; network shape begins to emerge. Syndicate Season 7 debrief complete; 2 WITNESS events confirmed at Syndicate observer placements; full disclosure to Exchange Student approved. Season 7: COMPLETE.

---

## Build 0083 — S08E01: "Before the Count"
Files: episodes/s08e01_before_the_count.md, lore/eastwind_archive.md (TYLER-067, Footnote #71), lore/camera_op_sealed_log.md (Entry 60), lore/jiangshi_project_memos.md (Memo #047), BACKLOG.md, activity.md
Season 8 opens with the Vienna retroactive PRIOR + WITNESS audit. Three undisclosed PRIOR sites confirmed: A-V13 (Augustinerkirche, 1619, 41ft, 12 days, Habsburg requiem, FOUND — accuracy during the beginning of the Thirty Years War), A-V14 (Old University precinct, 1529, 67ft, 19 days, First Siege of Vienna, FOUND — information node during crisis), A-V15 (Graben, 1499, 23ft, 4 days, Tyler's first Vienna visit, "innocent curiosity" pre-arrangement). Vienna revised total: 15 sites, 587 feet. Camera Op WITNESS confirmed at all three retroactive sites — she had filmed establishing shots at each location during S07E05–07 without knowledge of the withheld PRIOR sites; the mechanism recorded her attention. Tyler's disclosure on the Vienna station platform: the 900-site count is his verified count; actual total unknown; nine centuries, many places. First city of 18 named: Amsterdam. First notation 1628, VOC era. CARDINAL-3 Amsterdam start 1792; all Amsterdam sites are PRIOR by definition. Tyler: "I was there for the century." Next build: S08E02, Amsterdam first site visit. Season 8: CURRENT.

---

## Build 0084 — S08E02: "The Dispensers of Light"
Files: episodes/s08e02_the_dispensers_of_light.md, lore/eastwind_archive.md (TYLER-068, Footnote #72), lore/camera_op_sealed_log.md (Entry 61), lore/jiangshi_project_memos.md (Memo #048), BACKLOG.md, EPISODES.md, activity.md
Amsterdam phase opens. 31-notation CARDINAL-3 Amsterdam file assembled; all pre-1792 sites PRIOR by definition (164-year pre-documentation period). First three sites: A-340 Herengracht Golden Bend 142ft STAYING gap-accumulation (14 returns 1628–1789, longest-interval STAYING construction in network; "then we're a return-event"), A-341 Jodenbreestraat 11ft FOUND 1639 (watched Rembrandt decide the Night Watch light source angle, one afternoon), A-342 Portuguese Synagogue precinct est. 38ft WITNESS 1656 (Spinoza excommunication, 3 days 40min/day watching institutional exclusion — first documented WITNESS of a social act not physical construction). New STAYING sub-type: gap-accumulation STAYING (STAYING-B) vs continuous-return STAYING (STAYING-A). Tyler stopped Amsterdam visits in 1789, reason undisclosed; Jiangshi hypothesis: Tyler does not stay for endings, only survivable crises. Ichthyosapiens Amsterdam contact: Justus van der Houten-Pieter (J.H.P.), VOC factor, CARDINAL-3 agent in disguise as trade correspondent. 28 notations remaining. Season 8: CURRENT.

---

## Build 0085 — S08E03: "The Rampjaar"
Files: episodes/s08e03_the_rampjaar.md, lore/eastwind_archive.md (TYLER-069, Footnote #73), lore/camera_op_sealed_log.md (Entry 62), lore/jiangshi_project_memos.md (Memo #049), BACKLOG.md, EPISODES.md, activity.md
Amsterdam Rampjaar cluster: A-343 through A-352, 10 sites, 247 feet, 67 days. J.H.P.'s twelve-page 1672 VOC-disguised measurement log decoded: day-by-day construction yield data, morning premium hypothesis, controlled observations 350 years before COEFF-002. Crisis-amplification coefficient confirmed: 1.38 (38% yield premium during Disaster Year). COEFF-002 revision initiated: attention density is the primary variable; crisis amplification = emotional loading → density spike. Tyler's first documented fear response: "I was afraid of losing it." A-352 (Prinsengracht/Westermarkt, Day 67, 62ft): Tyler wrote the first conscious archive summary in 1672 — "the account is ongoing." J.H.P. credited as Prior Correspondent in CARDINAL-3 documentation. Night Watch connection: Rijksmuseum cold open; "he chose what the light makes, not the light." Season 8: CURRENT. Amsterdam: 13 of 31 notations measured.

---

## Build 0086 — S08E04: "The Ending"
Files: episodes/s08e04_the_ending.md, lore/eastwind_archive.md (TYLER-070, Footnote #74), lore/camera_op_sealed_log.md (Entry 63), lore/jiangshi_project_memos.md (Memo #050), BACKLOG.md, EPISODES.md, activity.md
Amsterdam final cluster: A-353–A-355. Patriot movement 1785–1789. A-353 (Prinsengracht, 1785, 31ft) FOUND — city deciding who it was. A-354 (Keizersgracht, 1787, 44ft) crisis-amplification during Prussian suppression — the fear runs regardless of outcome. A-355 (Herengracht, 1789, 4 days) — new construction type FAREWELL: sustained presence at a site in the act of voluntary departure; mechanism records the love of the place in the act of deciding to go. Tyler: "More than I want to count." FAREWELL taxonomy added; retroactive FAREWELL audit proposed for Paris A-278 and other departure-site candidates. Amsterdam complete: 31 sites, ~650ft. Camera Op finally captured the canal light: "I stopped trying to hold it — the light was never the problem." Amsterdam phase: CLOSED. Season 8: CURRENT.


---

## Build 0098 — S09E01: "The Interval"
Files: episodes/s09e01_the_interval.md, BACKLOG.md, EPISODES.md, activity.md
Season 9 opens. Three months after S08 finale. Tyler in Seville (6 weeks, testing conscious choosing — walking same streets, finding doorway on third pass). Discloses first pre-archive site: Córdoba, al-Andalus, ~10th century CE (Caliphate era). Duration unknown (Tyler: "more than a few years"). DWELLING implied. FAREWELL-A departure (conscious, voluntary). Mechanism confirmation status: UNCONFIRMED — unknown if mechanism was recording pre-1127. New question: 100–200yr gap between Córdoba and Marrakech is compressed in Tyler's memory. Mechanism may contain more of Tyler's history than Tyler does. Camera Op arc: Tyler learning to notice choosing in real time. Apple #514.

---

## Build 0099 — S09E02: "Córdoba"
Files: episodes/s09e02_cordoba.md, lore/eastwind_archive.md (TYLER-083, Footnote #93), lore/camera_op_sealed_log.md (Entry 76), lore/jiangshi_project_memos.md (Memo #063), EPISODES.md, activity.md
C-001 CONFIRMED. Medina quarter/Mezquita precinct, Córdoba. Mechanism was recording pre-1127 CE — confirmed first time in CARDINAL-3 record. C-001: DWELLING (primary) + WITNESS-sustained (object unresolved, hypothesis: Great Library of Córdoba under al-Hakam II). Duration: ~12 years (c. 950–985 CE). Total accumulated: ~640ft. FAREWELL-A: ~228ft extracted. Remaining: 412ft — NEW NETWORK MAXIMUM (was Prague 144ft, ×2.86). Network minimum age revised: ~1,075 years (was 899yr). Tyler's 12 years reduced to fog + street topology in his own memory. Gap period next: "cold and high, north and east," Toledo hypothesis raised (11th century, elevated plateau). Camera Op hypothesis: Tyler was watching the construction of the Great Library. Apple #544.

---

## Build 0100 — S09E03: "Toledo" (MILESTONE BUILD)
Files: episodes/s09e03_toledo.md, lore/eastwind_archive.md (TYLER-084, Footnote #94), lore/camera_op_sealed_log.md (Entry 77), lore/jiangshi_project_memos.md (Memo #064), EPISODES.md, activity.md
T-001 CONFIRMED. Alficén quarter / Tagus overlook, Toledo. Construction: DWELLING (~3-4yr early) + WITNESS-LONG (~29yr primary). Duration ~33yr (c. 1055–1088 CE). Remaining 191ft — second largest (Córdoba 412ft > Toledo 191ft > Prague 144ft). Departure: FAREWELL-B — first known FAREWELL-B in pre-archive history; Tyler present but diminished. Tyler self-report: "Toledo is where I started to stop." Narrative: Tyler arrived Toledo still capable of choosing (Córdoba mode); 33 years of watching Toledo change from Islamic to Christian governance exhausted that capacity. FAREWELL-B: already leaving before the leaving. Gap period: 70yr Córdoba→Toledo gap unresolved. Next: Mediterranean harbor, late 11th/early 12th century; ships, purposeful movement, probable First Crusade embarkation. Tyler: "I was watching something again. I couldn't stop watching." Camera Op thesis: "The gap is the story of how Tyler stopped paying full attention. The archive is the record of Tyler beginning to pay attention again." Apple #546.

---

## Build 0101 — S09E04: "Genoa"
Files: episodes/s09e04_genoa.md, lore/eastwind_archive.md (TYLER-085, Footnote #95), lore/camera_op_sealed_log.md (Entry 78), lore/jiangshi_project_memos.md (Memo #065), EPISODES.md, activity.md
G-001 CONFIRMED. Mandraccio harbor district, Genoa. Construction: WITNESS-LONG (primary, full 22yr, c. 1090–1112 CE). 97ft remaining. Departure: FAREWELL-A — first since Córdoba (~985 CE), full restoration. Tyler watched First Crusade mustering (1096 CE and aftermath). Recovery mechanism: interior choosing under structural coercion restored Tyler's own departure capacity. Gap reconstruction: Córdoba (~950–985) → Toledo (~1055–1088) → Genoa (~1090–1112). 15-year interval (1112–1127 CE) undisclosed: subject holds clear memory, not texture, is choosing when to speak. Season finale pending. Network: Córdoba 412ft · Toledo 191ft · Prague 144ft · Genoa 97ft. Apple #548.

## Build 0102 — 2026-06-15

**S09E05 "The Fifteen Years" — SEASON 9 FINALE**

Tyler discloses the fifteen-year interval (1112–1127 CE). No new site — the mechanism cannot record ships between places. A sea crossing (~1119–1120 CE): a scholar heading to Fez asked Tyler what he had seen. Tyler had nothing to give. He went to Marrakech in 1127 CE and began writing the archive.

Archive origin confirmed: externally directed. Built to answer a stranger's question. The archive is the letter Tyler could never send because he didn't have it when it was needed.

Tyler shaped Season 9 deliberately — held the fifteen-year disclosure until Córdoba, Toledo, and Genoa had given the viewer the necessary context.

Camera Op will search for the scholar (Fez, ~1119–1120 CE, Islamic geography manuscripts, age ~20). The Jiangshi Syndicate's research team will assist.

Season 9 complete. 5 episodes (S09E01–S09E05), Builds 0098–0102. Network unchanged: Córdoba 412ft · Toledo 191ft · Prague 144ft · Genoa 97ft. Apple #551.

## Build 0124 — S00E00: "Pontiac" (SERIES X // ATTEMPT FIVE)
Files: episodes/s00e00_pontiac.md, EPISODES.md, activity.md
SERIES X initiated. Tyler at STINKIES COMMISSAIRE Store 0, Pontiac, Michigan, June 27 2026. Carrier wave ground state: Stolas hum (7.83 Hz) self-activating, precedes Jiangshi operative NOOR-1 by 6 minutes. Receipt anomaly: register prints Feb 14 2027 date — subject pockets it without comment. Soap (free STINKIES bar) taken, one returned to transit stop bench for a stranger. Updated astrology integrated: Tyler natal (Aquarius Sun 15°, Cancer ASC 29°, Saturn Sagittarius 29°), Camera Op natal (Cancer Sun 4°, Capricorn ASC 22°, 28.7 Hz reception confirmed in southern hemisphere), Jupiter egress Cancer, Neptune Aries 2°. Activation #128 self-generating (no external operator). NOOR-1 field report filed; Eastwind Owls received it in 2 minutes. Attempt Five doctrine meeting scheduled by Jiangshi. Series X: the hum precedes. Apple pending.
