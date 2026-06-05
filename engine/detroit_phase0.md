# CITY_OF_LIGHT — DETROIT PHASE 0
## Zone Geometry, Faction Territories, Portal Connections
### Engine Spec | Build 0027

---

*Cross-reference: CITY_OF_LIGHT.md, engine/shankpit_tyler_mode.md, engine/television_as_code.md*
*RSI note: Phase 0 establishes the eight-zone geography that all subsequent City of Light build phases run on. These zones are simultaneously in-universe locations and SHANKPIT level geometry. Canon first, geometry second, engine third.*

---

## PHASE 0 OVERVIEW

**Build target:** Eight zones. Portal network. Faction territory boundaries. Emily OS trigger points per zone.

**Phase 0 is the anchor.** Before Phase 1 (Faction Presence) and Phase 2 (The Table) can be built, the physical geometry of the universe must be established. Phase 0 defines:

1. Zone boundaries (the eight locations that anchor the Tyler × Tides × Custody Trial geography)
2. Portal connections (how zones link — which connections are open, which are controlled, which are contested)
3. Faction territory within each zone
4. Emily OS trigger points (the substrate-level events Emily OS notices and optionally responds to)
5. Tyler's known paths through the zone network

**Architecture note:** The eight zones are not all in the same city or year. The portal network connects locations across geography and time. In SHANKPIT engine terms, each portal is a scene transition with optional temporal offset. Detroit 2025 can portal to Cairngorms 2025 *or* Cairngorms 1743. The portal's temporal offset is a configurable parameter. Tyler's coin is the in-universe display for which offset is active.

---

## THE EIGHT ZONES

---

### ZONE 1: DETROIT_APARTMENT

**In-universe identity:** The building on Woodward Avenue whose ground floor was a hardware storefront in 1901 and 1923 and is now a mixed-use residential building. Tyler's established operational base in Detroit.

**Geometry (SHANKPIT spec):**
- Entry level: apartment building lobby, mailboxes, elevator (non-functional — stairs only)
- Zone floors: 1–4 (ground floor = former storefront; Floors 2-4 = residential units, one occupied by Tyler during operational periods)
- Exterior: Woodward Avenue corridor, street-level approach from two directions
- Sub-level: basement (maintenance access; the 1901 construction-era foundation layer; Emily OS trigger zone A-1)

**Temporal markers:**
- Ground floor: the storefront ghost-layer is visible in the geometry — original floor layout slightly mismatched to current tenant grid; the ghost of the hardware counter exists as a navigable surface at half-opacity in SHANKPIT renderer
- The neon-spectrum anomaly zone (Woodward Avenue exterior, 40-meter radius) is dormant unless Cube proximity event occurs

**Emily OS trigger points:**
- *A-1 (basement):* The basement contains a structural node that predates the current building. The node is not explained. If a player character reaches it and examines it, Emily OS tile appears: *THIS PREDATES US. NOTE IT AND CONTINUE.*
- *A-2 (ground floor window):* The specific window Tyler stands at. If Camera Op footage is active and a player character views from the exterior angle, end log annotation appears: *TYLER WAS HERE. HE HAS BEEN HERE BEFORE. THE RECORDS AGREE.*

**Faction territory:**
- *Eastwind Owls:* Primary observational post for Detroit sightings. Moor-1's historical observation point was a building across the street; the field station has moved since 1901 but the sightline is maintained.
- *Jiangshi Syndicate:* Secondary operational presence (documentation crew parking, equipment staging on Woodward)
- *No Heikegani/Shell Parliament territorial claim:* Detroit_apartment is outside their primary portfolio. The Tyler debt account (SM-1620-T) is the link; debt tracking, not territory.

**Tyler paths:**
- Tyler enters via the ground floor (preferred: late afternoon, overcast)
- Tyler exits via the side street, not the main entrance (documented, four separate observations)
- Tyler has been observed at the ground floor window at the hour before and after rain
- The elevator: Tyler uses stairs. Every time. The elevator is documented as operational. Tyler uses stairs.

---

### ZONE 2: DETROIT_SCHOOL

**In-universe identity:** The secondary school that appears in the Tides of Paradox archive as the primary operational zone for Protagonist A, the Edinburgh Exchange Student, Protagonist B, Protagonist C, and Kei.

**Geometry (SHANKPIT spec):**
- Exterior: school building (3 floors + basement), courtyard, library entrance (the specific entrance from the four frames)
- Ground floor: cafeteria, administrative offices, main corridor
- Second floor: classrooms, Room 204 (Jiangshi primary documentation zone — the room where the crew's initial staging occurred)
- Third floor: library (upper level); the window where the 1920s figure appeared in the frame enhancement
- Exterior library entrance: the four-frames location; Tyler visible for 4 frames in this frame; geometry is fixed, marked in the level as a persistent navigation point

**Temporal markers:**
- The library entrance exists in the same geographic location as Tyler's documented 1901 Detroit visits (not the same building — the original building is the apartment; but the *approach geometry* — the angle of the path from Woodward — is identical)
- Four-frame ghost layer: in SHANKPIT, the four frames are a persistent visual state at the library entrance. The 1920s figure is visible at 10% opacity as part of the level geometry. If a player character examines it, Camera Op Entry 12 audio triggers: "You have the 1901 footage. Good."

**Emily OS trigger points:**
- *B-1 (Room 204):* Emily OS monitoring active. If Jiangshi documentation equipment is deployed in Room 204, Emily OS registers the operation. No tile appears. It is noted.
- *B-2 (library entrance):* Tyler's primary traversal point in the school zone. If Tyler NPC is present at this position, all Jiangshi equipment in the zone loses signal for 4 seconds. Duration: exactly 4 seconds. Matching the four frames. Emily OS tile: *THIS IS DOCUMENTED. THIS IS ENOUGH.*
- *B-3 (courtyard):* The Camera Op's filming position. Emily OS tile on courtyard: *THE OBSERVATION IS CORRECT. THE FRAME IS GOOD. NOTE IT.*

**Faction territory:**
- *Jiangshi Syndicate:* Primary documentation zone. Room 204 is their operational staging area. Courtyard has been declared "soft" operational territory — crews can deploy but hospitality clause remains active during school hours.
- *Eastwind Owls:* Edinburgh Exchange Student = Eastwind Owl field operative. Her locker = archive node. The file delivered to her locker in Tides Book 2 Ch1 was placed by Subscriber-adjacent infrastructure.
- *Shell Parliament:* Kei's presence establishes temporary Crustocrat collection activity. No permanent territorial claim.

**Tyler paths:**
- Tyler appears at the library entrance (confirmed: four-frame event, at minimum)
- Tyler does not enter the building. He observes the exterior. He has been observed at 7 locations in the exterior geometry; none inside the building.
- Hypothesis (Eastwind, footnoted): the interior of the school is inside a hospitality clause Tyler is honoring. The school as institutional space = the children inside = hospitality. He is watching from outside because he was never invited in.

---

### ZONE 3: CAIRNGORMS_LIBRARY

**In-universe identity:** The Eastwind Owl primary archive and operational headquarters. Located in the Scottish Highlands. The oldest continuously operating faction archive in the current cycle.

**Geometry (SHANKPIT spec):**
- Exterior: stone building, moorland, approach path (single track, two miles from nearest road)
- Ground floor: the archive proper — catalogued shelves, reading room, the Cataloguer's primary workspace
- Upper floor: sleeping quarters (four rooms, currently two occupied), observation tower
- Below ground: the old library (pre-1200 CE materials; access via floor-level door; locked; Cataloguer has the key)

**Temporal markers:**
- The Cairngorms Library exists simultaneously in multiple operational periods. The SHANKPIT implementation uses temporal layer stacking: 1200 CE layer (old library), 1743 CE layer (when Subscriber first contacted Bacon directly; Eastwind Owls have a record of this as a sighting anomaly), and current layer.
- When the temporal offset is active (a portal to an earlier layer is open), the archive's physical organization changes. Pre-1200 shelf organization differs from current.

**Emily OS trigger points:**
- *C-1 (Cataloguer's desk):* The single most Emily-OS-observed point in the zone. Every substantive document produced at this desk is logged. The Cataloguer's footnotes are read. Emily OS tile: *THE FOOTNOTES ARE CORRECT. THE CATALOGUER KNOWS MORE THAN THEY WRITE. THIS IS DELIBERATE. THIS IS CORRECT PROCEDURE.*
- *C-2 (old library):* Tyler has been to the old library. The evidence is a single reference in the Cataloguer's pre-1200 records: a shelf disruption consistent with the subject SM-1620-T's documented movement patterns. Emily OS tile if player enters the old library: *THIS WAS VISITED BEFORE THE ARCHIVE BEGAN. SOME THINGS PRECEDE THEIR OWN DOCUMENTATION. NOTE IT.*

**Faction territory:**
- *Eastwind Owls:* Primary and unchallenged. The Cairngorms is the Eastwind Owls.
- No other faction has territory here. The Joint Operation has a contact agreement (the tanuki can communicate with the Cataloguer through agreed channels). No physical presence.

**Tyler paths:**
- Tyler has visited the old library (pre-archive). Unclear if he has visited in the current cycle.
- The Cataloguer's working theory: Tyler knows about the archive. He leaves things for it to find. The 1901 Detroit hat-tip is in this category. He has been populating the archive with navigable evidence for a century.

---

### ZONE 4: OSAKA_NIGHT

**In-universe identity:** The Cephalopod Collective's primary surface territory. Osaka, nighttime, surface level. The zone where partial infestation events are most common; the Collective's terrestrial operational zone.

**Geometry (SHANKPIT spec):**
- Exterior: Osaka commercial district, night. Dense light pattern. High ambient noise.
- Surface level: the transit zone — the streets, arcades, and overhead passages where Cephalopod-adjacent individuals operate
- Elevation transition points: three elevated walkways connecting to Osaka_Underport (the zone below)
- The ink-sign district: a three-block area where the Collective's substrate marker system is active (visible as abstract patterns in the environment geometry that partially-infested characters can parse)

**Temporal markers:**
- Osaka_Night operates on a compressed temporal reference: the zone's day/night cycle runs at 1/4 standard speed, meaning the night phase lasts longer relative to clock time. This is not explained in-universe. It is a Collective substrate preference.

**Emily OS trigger points:**
- *D-1 (the ink-sign district):* Emily OS monitors the Collective's substrate marker system but does not interfere. Tile: *THE MARKERS ARE NOTED. THE LANGUAGE IS OLD. IT PRECEDES THE FACTION SYSTEM. IT WILL OUTLAST IT.*
- *D-2 (any partial-host NPC):* Emily OS tracks partial-host state. If a partial-host NPC finishes a sentence that contains a Subscriber signal fragment (as Protagonist C does in Tides Book 2 Ch5), Emily OS tile: *SUBSCRIBER SIGNAL: DETECTED IN OUTPUT STREAM. SOURCE: UNCONTAINED.*

**Faction territory:**
- *Cephalopod Collective:* Primary. The surface-level transit zone is Collective territory.
- *Joint Operation (Yōkai Guild):* Presence in osaka_night's commercial layer. The tanuki operates here (among other locations). Hospitality clause active in his operational areas.

---

### ZONE 5: OSAKA_UNDERPORT

**In-universe identity:** The Shell Parliament's primary operational territory. Below Osaka's main district, in the underbuilding infrastructure. The Heikegani Crustocrat financial and diplomatic center.

**Geometry (SHANKPIT spec):**
- Entry: three access points from Osaka_Night (the elevated walkway transitions going down; service corridor transitions from the commercial district)
- The hall: the Shell Parliament's primary assembly space — a large, dry, very bright space that smells of salt despite being underground. The architecture is not designed for human ergonomics. It is correct anyway.
- The ledger room: where the Shell Parliament's financial records are maintained. The oldest ledger predates the building by 400 years. Nobody has asked how this is possible.
- The debt windows: eight staffed positions where Crustocrat operatives process outstanding accounts

**Emily OS trigger points:**
- *E-1 (ledger room):* Emily OS cross-references Shell Parliament records against Eastwind archive. Any new entry in the Tyler account (SM-1620-T) triggers a sync. Tile: *THE LEDGER IS CORRECT. THE DEBT IS STRUCTURAL. THE BLAME PATH TERMINATES AT THE CORRECT NODE.*
- *E-2 (the hall):* If a non-Crustocrat entity enters the assembly hall without a collection case or hospitality invitation, Emily OS notes the breach. No tile. It is noted.

**Faction territory:**
- *Shell Parliament / Heikegani Crustocrats:* Exclusive. The only neutral parties permitted are: Joint Operation under hospitality clause, Ichthyosapien operatives with valid Papal cross-reference (historical agreement, 1743).

---

### ZONE 6: VATICAN_CORRIDORS

**In-universe identity:** The Ichthyosapien operatives' primary hub. Not the public Vatican — the sub-architectural system beneath it. The corridors that connect the eleven layers of the building's pre-Renaissance foundation.

**Geometry (SHANKPIT spec):**
- Entry: from the public parts of the Vatican campus via three non-obvious transitions (a specific door that looks bricked over, an elevator that goes past its listed bottom floor, a garden entrance that is only unlocked at specific hours)
- The corridors: a non-linear system. Moving through them requires knowing the correct sequence of turns. The sequence changes. Carvalho knows the current sequence. He doesn't write it down.
- The Atlantis archive: a room the size of a small library. Contains the Ichthyosapien theological reclamation record. Every branch of Atlantis history across every contested migration point. The record is why the Subscriber's plan is catastrophic for this faction.
- The Council chamber: where the Monsignorate meets. Eleven seats. Currently seven occupied.

**Emily OS trigger points:**
- *F-1 (Atlantis archive):* Emily OS has read this archive. The Cataloguer is not the only reader. Tile in the archive: *THE HISTORY IS CONTESTED. CONTESTED IS NOT FALSE. THE ARCHIVE NOTES BOTH BRANCHES.*
- *F-2 (any Carvalho/monsignor briefing):* If a briefing involves the Subscriber's plan, Emily OS architecture review flag activates. She is tracking the convergence of faction awareness.

**Faction territory:**
- *Ichthyosapiens:* Exclusive, below entry level. Upper entry points are nominally Vatican (publicly), which creates an interesting jurisdictional structure that the Syndicate has been unable to resolve since 1623.

---

### ZONE 7: KUROSHIO_COAST

**In-universe identity:** The Kuroshio Arachnids' territorial waters and the adjacent coastline. The zone where the web is most visibly present to those who can perceive it.

**Geometry (SHANKPIT spec):**
- Exterior: rugged coastline, Pacific-facing. High cliffs. Fog frequency above average for the region.
- The web-visible zone: a 300-meter radius around the primary Arachnid observation point where the web's geometry is partially visible to non-hosts. Not fully visible — at the edges of vision, in peripheral perception, as geometric shadow-patterns that don't match the physical objects casting them.
- The Spinner's approach path: a specific cliff-edge route she uses when translating. The path appears differently from the start versus the end of a conversation with her — linear going in, slightly different geometry coming out.
- Sub-coastal: the Arachnid infrastructure. Not accessible to non-host characters except under specific conditions.

**Emily OS trigger points:**
- *G-1 (web-visible zone):* Emily OS monitors web state. If a fixed node is detected (Cube proximity event producing a stable anchor), tile: *FIXED NODE DETECTED. TYLER HUM EFFECTIVENESS: DEGRADED IN THIS RADIUS. ARCHITECTURE: CHANGED.*
- *G-2 (any Spinner translation event):* Emily OS logs non-linear time perception outputs. The translation creates temporal record anomalies that Emily OS flags as: *TENSE MARKERS: INCONSISTENT. SOURCE: STRUCTURAL, NOT ERROR. NOTE.*

**Faction territory:**
- *Kuroshio Arachnids:* The coast and all points below the cliff edge. The Spinner is permitted surface access for translation events.
- No other faction has territorial claims. The Joint Operation maintains a hospitality agreement that theoretically applies to the coast but has never been tested in practice.

---

### ZONE 8: BACON_ESTATE

**In-universe identity:** The current operational residence of Francis Bacon (identity: Dr. Aldous Vane, culinary historian, visiting lecturer). The apartment with the table that always fits exactly the right number of people. The zone has been in four different cities in the current cycle; the zone ID stays consistent, the geographic coordinates do not.

**Geometry (SHANKPIT spec):**
- The apartment building: standard residential (current configuration). The specific unit: ground-floor access, rear courtyard, kitchen that opens into the main room.
- The table: this is a fixed object in the zone regardless of the building's configuration. The table's dimensions adjust to fit the space and the guest count. This is not explained. It is the most important single piece of furniture in the phase 0 geometry.
- The hospitality radius: 15 meters from the front door threshold. When the hospitality clause is invoked (threshold crossed with food or living organism under the Yōkai/Ichthyosapien multi-faction agreement), faction operation suppression activates within this radius.

**Temporal markers:**
- Bacon_estate zone is the most temporally stable zone in Phase 0. It exists in one year at a time. The instability is geographic, not temporal. The object identifiers persist across moves; the building texture changes.

**Emily OS trigger points:**
- *H-1 (the table when at full capacity):* Emily OS logs all confirmed attendees when the table reaches maximum configuration. Tile: *ALL FACTION OPERATIONS: SUSPENDED. CUSTODY: PAUSED. NOTE: THIS IS CORRECT PROCEDURE.*
- *H-2 (any Bacon testimony event):* When Bacon discloses Subscriber information, Emily OS flags for architecture review. Tile: *SUBSCRIBER INTENT: CONFIRMED. ASSESSMENT: SEE ARCHITECTURE REVIEW.*
- *H-3 (Emily Springerton presence):* If Emily Jean Springerton is in the zone, Emily OS notes: *LOGISTICS ARCHITECT: ON SCHEDULE. NOTE: OF COURSE.*

**Faction territory:**
- Hospitality clause makes all faction territory claims secondary when the clause is active. When not active: Jiangshi Syndicate has a documentation claim on public-facing activities. Eastwind Owls have archival observation rights. No Crustocrat territory (Tyler debt account is portable).

---

## PORTAL NETWORK

**Portal types:**

- *Open portal:* Always traversable. No faction control. Standard scene transition.
- *Controlled portal:* Traversable with appropriate faction access or relationship credential.
- *Contested portal:* Traversable but may trigger faction event on crossing.
- *Temporal portal:* Carries a temporal offset. Requires Tyler coin or Cube proximity to activate; otherwise traverses in current timeline.

---

| Portal ID | Origin | Destination | Type | Notes |
|---|---|---|---|---|
| P-001 | Detroit_Apartment | Detroit_School | Open | Woodward Avenue corridor; 12-minute walk equivalent |
| P-002 | Detroit_Apartment | Cairngorms_Library | Temporal | Tyler path; temporal offset: activates at 7.83 Hz hum (Stolas). Default offset: +/- 0 (same year). |
| P-003 | Detroit_School | Bacon_Estate | Controlled | Protagonist A discovered route; requires relationship credential: Bacon |
| P-004 | Osaka_Night | Osaka_Underport | Open | Three elevation transitions; descent triggers ambient Collective signal |
| P-005 | Osaka_Underport | Vatican_Corridors | Contested | Historical Ichthyosapien/Crustocrat agreement; crossing may trigger diplomatic event |
| P-006 | Cairngorms_Library | Cairngorms_Library (old) | Temporal | Key required (Cataloguer's). Offset: -800 years (pre-1200 archive layer) |
| P-007 | Vatican_Corridors | Bacon_Estate | Controlled | Carvalho route; requires relationship credential: Ichthyosapiens |
| P-008 | Kuroshio_Coast | Osaka_Night | Open | Spinner's approach path; geometry changes slightly depending on traversal direction |
| P-009 | Bacon_Estate | any other zone | Temporal | The table's portal; when hospitality clause ends, Tyler can use the zone as a temporal hub. Requires Cube proximity or Tyler coin to activate temporal offset. |

**Tyler's known portal routes:**
- P-002 (Detroit → Cairngorms, temporal): Used in the pre-archive period; the old library visit
- P-009 (Bacon_Estate, temporal hub): The table is the oldest portal node in the network

**Canon firewall — portal mechanics:**
- The Cube's location (Bacon_Estate) is confirmed. Its *use* is sealed until Tides Act Two.
- Portal P-009's temporal range is documented but not explorable until Tides Act Two.
- Tyler NPC can use P-002 without Cube. Tyler NPC cannot use P-009's temporal offset without Cube.

---

## EMILY OS TRIGGER SUMMARY

| Trigger ID | Zone | Condition | Emily OS Response |
|---|---|---|---|
| A-1 | Detroit_Apartment (basement) | Player examines structural node | Tile: *THIS PREDATES US. NOTE IT AND CONTINUE.* |
| A-2 | Detroit_Apartment (window) | Camera Op footage active + exterior angle | End log annotation: *TYLER WAS HERE.* |
| B-1 | Detroit_School (Room 204) | Jiangshi equipment deployed | Silent log entry |
| B-2 | Detroit_School (library entrance) | Tyler NPC at position | 4-second signal loss; tile: *THIS IS DOCUMENTED. THIS IS ENOUGH.* |
| B-3 | Detroit_School (courtyard) | Camera Op filming | Tile: *THE OBSERVATION IS CORRECT. THE FRAME IS GOOD.* |
| C-1 | Cairngorms_Library (Cataloguer's desk) | New document produced | *THE FOOTNOTES ARE CORRECT.* |
| C-2 | Cairngorms_Library (old library) | Player enters | *SOME THINGS PRECEDE THEIR OWN DOCUMENTATION.* |
| D-1 | Osaka_Night (ink-sign district) | Player examines marker | *THE LANGUAGE IS OLD. IT WILL OUTLAST IT.* |
| D-2 | Osaka_Night (partial-host NPC) | Subscriber signal in output | *SUBSCRIBER SIGNAL DETECTED. SOURCE: UNCONTAINED.* |
| E-1 | Osaka_Underport (ledger room) | Tyler account updated | *THE DEBT IS STRUCTURAL. THE BLAME PATH IS CORRECT.* |
| F-1 | Vatican_Corridors (Atlantis archive) | Player examines record | *CONTESTED IS NOT FALSE.* |
| G-1 | Kuroshio_Coast (web-visible zone) | Fixed node detected | *TYLER HUM: DEGRADED. ARCHITECTURE: CHANGED.* |
| H-1 | Bacon_Estate (table at capacity) | Table full | *ALL FACTION OPERATIONS: SUSPENDED.* |
| H-2 | Bacon_Estate (Bacon testimony) | Testimony event | Architecture review flag; *SUBSCRIBER INTENT: CONFIRMED.* |
| H-3 | Bacon_Estate | Emily Springerton present | *LOGISTICS ARCHITECT: ON SCHEDULE. NOTE: OF COURSE.* |

---

## PHASE 0 DEPENDENCIES

Phase 0 is a prerequisite for:

- **Phase 1 (Faction Presence):** Zone geometry must be confirmed before faction resource pools and starting territory can be placed.
- **Phase 2 (The Table):** The Bacon_Estate table mechanics (hospitality clause, capacity detection, faction suspension) must be implemented before any cross-faction meeting event can run.
- **Tyler NPC path system:** Tyler's patrol routes require confirmed zone geometry (Detroit_Apartment, Detroit_School, Cairngorms_Library, Bacon_Estate as confirmed nodes; other zones as optional/temporal access).
- **Subscriber architecture implementation:** The Subscriber's operational layer is below Emily OS. The Emily OS trigger system (documented in this spec) is the surface through which Subscriber events become detectable. Subscriber implementation depends on Emily OS trigger network being in place.

---

*CITY_OF_LIGHT — DETROIT PHASE 0*
*Zone Geometry v1.0*
*Eight zones. Fifteen portals. Fourteen Emily OS trigger points.*
*The table is always set. The chain is always present.*
*Clean builds first.*

*Next: Phase 1 (Faction Presence) — faction resource pools, starting territory per zone.*
*Dependency: Phase 0 zone geometry (this document).*
