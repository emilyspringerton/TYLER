# SHANKPIT — Tyler Mode
## The Metaverse Runtime for TYLER × TIDES OF PARADOX
### Engine Spec v1.0 | Einhorn Media × SHANKPIT

---

> *"Server authority is custody. Custody requires a blame path."*
> — Emily OS, modal tile

---

## I. WHAT THIS IS

SHANKPIT is the game engine. Tyler Mode is the configuration that turns it into the Tyler universe metaverse.

The Tyler universe is not a skin on top of the game. It is a **mode** — a set of scene configurations, NPC behavior trees, server event states, and faction mechanics that translate the universe physics of TYLER × TIDES OF PARADOX into interactive runtime.

A viewer watching a Tyler episode on the flat stream sees a documentary. A player in Tyler Mode on SHANKPIT inhabits the same universe — the same Detroit apartment, the same Osaka convenience store, the same Vatican corridors — and can encounter the factions as non-player characters.

The canonical events of the show still happen. Tyler still resists being documented. The Jiangshi still run their ritual. The Canon Firewall prevents player actions from affecting plot. Players are **witnesses** in the Jiangshi sense — their presence in the metaverse adds them to the binding record, exactly as the show's in-universe logic describes.

This is not a metaphor. It is a design decision.

---

## II. SCENE MAP — TYLER UNIVERSE

The Tyler universe adapts the existing SHANKPIT scene list and adds new locations.

| Scene ID | Tyler Name | In-Universe Location | Faction Presence |
|---|---|---|---|
| `detroit_apartment` | **The Apartment** | Detroit, MI (year: ambiguous) | Jiangshi (primary) |
| `osaka_night` | **The Convenience Store** | Osaka (Tanuki's shop, Hashashin/Yōkai cover) | Hashashin/Yōkai Joint Operation |
| `cairngorms_library` | **The Cairngorms Archive** | Scottish Highlands | Eastwind Owls |
| `vatican_corridors` | **The Sleeper College** | Vatican City | Ichthyosapiens + Cephalopod Hosts |
| `detroit_school` | **The School That Isn't There** | Detroit, MI (Timeline: Cursed) | Emily OS visible (Custody) |
| `osaka_underport` | **The Shell Exchange** | Osaka harbor (underwater) | Heikegani Crustocrats |
| `kuroshio_coast` | **The Web Shore** | Pacific coastline (Kuroshio path) | Kuroshio Arachnids |
| `bacon_estate` | **The Table** | Location: rotates with identity | Sir Francis Bacon (Hashashin bait) |

These scenes connect via the existing SHANKPIT portal system. Scene transition = narrative transition. Players who move between scenes move between faction territories.

---

## III. FACTION TERRITORIES AND MECHANICS

Each faction controls a territory in the Tyler Mode world. Their mechanics reflect their universe physics.

### JIANGSHI SYNDICATE — The Documentary Unit
**Territory:** Detroit apartment, production van, office building

**Mechanics:**
- NPCs are the production crew (Producer OS, Camera Op, Subject #1)
- Players who stand still long enough in a Jiangshi zone are "documented" — a debuff that slowly accumulates
- Full documentation (5 stages completed on a player) = binding debuff (movement slowed, can't leave zone)
- Counter-mechanics: movement, humming emote (activates 7/8 disruption field), incomplete sentences (chat-based ward — start a message and delete it 3+ times)
- The Producer (OS) never appears on screen — voice only
- The Camera Op NPC follows players who have been sighted, has escalating awareness

**Server event:** `BINDING_RITUAL_ACTIVE` — escalates through 5 stages during the episode experience. Stage state is server-authoritative and shared across all players in the zone.

### HASHASHIN / YŌKAI GUILD — The Joint Operation
**Territory:** Osaka convenience store and surrounding streets

**Mechanics:**
- The Tanuki NPC sells items. Everything is "special today only." Some items are real. Some are hospitality tokens.
- Players who accept a meal/item from the Tanuki receive `HOSPITALITY_WARD` — Hashashin NPCs cannot target them for 30 minutes
- Hashashin NPCs move with uncanny quiet — no footstep audio, arrive in frame without warning
- The Three Initiates are visible before they should be (per Series Bible Rule: "One of them is already visible")

**Server event:** `CONTRACT_ACTIVE` — a secondary target is moving through the zone. The contract is visible to Hashashin-aligned players. Other players see only a person moving quickly.

### EASTWIND OWLS — The Silent Parliament
**Territory:** Cairngorms archive (interior + surrounding moor)

**Mechanics:**
- The Cataloguer NPC grants access to the Archive — a browsable database of Tyler sighting records (the lore artifacts in `lore/eastwind_archive.md`, rendered in-world)
- Players who find specific archive entries receive footnote observations — tiny text overlays that contain the Cataloguer's suppressed feelings
- Archive entries cannot be deleted. Players cannot remove their own sighting record once created.
- The Edinburgh Exchange Student NPC follows players she finds interesting. She does not announce this.

**Server event:** `ARCHIVE_UPDATE` — fires when a canonical event occurs anywhere in the world. The Archive updates in real time. The Cataloguer notes it.

### HEIKEGANI CRUSTOCRATS — The Shell Parliament
**Territory:** Osaka underport (underwater zone)

**Mechanics:**
- Everything is a transaction. Players have a Shell Debt value that accumulates when they receive services, information, or items in the Tyler world
- The Shell Accountant NPC (three generations, all simultaneously correct) can be found in any territory — they show up when debt is owed
- Financial deception near a Crustocrat NPC causes that NPC visible pain — they seize for 3 seconds, then resume with increased hostility
- Players can settle debt by completing Shell Parliament retrieval objectives (fetch debt information from other timelines)

**Server event:** `DEBT_AUDIT` — periodic sweep of all active players. Outstanding balances displayed on the HUD as Shell Debt counter. Unpaid balances compound.

### KUROSHIO ARACHNIDS — The Web Beneath the Current
**Territory:** Pacific coastline scenes + Kuroshio Current underwater zones

**Mechanics:**
- Host NPCs speak in non-linear sentence structures. Their dialogue subtitles render out of order.
- Players in Kuroshio territory hear the web-signal as a low frequency tone. Music in 7/8 or 11/8 disrupts this (players near Tyler get passive protection)
- The Spinner NPC (partial host, can see the web) provides quest hints that arrive before the quest is active
- Full incorporation debuff: player chat subtitles begin rendering non-linearly. Lasts 10 minutes.

**Server event:** `WEB_SIGNAL_SURGE` — the goo-web becomes detectable. Pattern anomaly on the HUD. The Spinner becomes agitated.

### ATLANTEAN ICHTHYOSAPIENS — The Deep Council
**Territory:** Vatican corridors (interior)

**Mechanics:**
- NPCs are cardinals, monsignors, altar servers — passing human in every way except the faint humidity
- Fresh water weakens Ichthyosapien NPCs (disoriented for 30 seconds — bring a water bottle)
- The Monsignor of Tidal Records can be convinced to share archive information if approached with the correct ecclesiastical forms (dialogue puzzle)
- The Sleeper Cardinals are genuinely Catholic. They will discuss theology. This is extremely unsettling.

**Server event:** `SHADOW_CONCLAVE` — when Ichthyosapien and Cephalopod operations overlap, both factions become simultaneously active in Vatican corridors. They will not acknowledge each other.

### CEPHALOPOD HOSTS — The Sleeper College
**Territory:** Vatican corridors (overlapping with Ichthyosapiens)

**Mechanics:**
- Cardinal Tessaro NPC is present. He prays. His octopus also prays. They agree on the content of the prayer. There is a small tank in the corner.
- Brine shrimp (craftable item) distracts any Cephalopod Host NPC for 30 seconds of unmonitored interaction
- The Altar Server NPC (partial host) finishes players' sentences correctly. This is treated as unremarkable.
- Players can choose to receive a partial host infestation — grants soft precognition (quest objectives appear 5 seconds before they update) at the cost of non-linear chat subtitles

**Server event:** `OCTOPUS_CONSENSUS` — the distributed network reaches a decision. All Host NPCs simultaneously take the same action. The decision is never explained.

---

## IV. TYLER AS AN NPC

Tyler appears in the Tyler Mode world, but rarely, briefly, and according to his 8 Laws.

**Tyler NPC rules:**
1. He is always in a scene before players arrive. He does not spawn in front of witnesses.
2. He never makes a statement about who he is. He deflects. He changes subject. He smiles.
3. He hums. Proximity to Tyler grants passive disruption field: Jiangshi documentation rate halved, Kuroshio web-signal suppressed.
4. He carries a coin. Players who observe the coin flip cannot look away until the date resolves. The date resolves to a different year each time.
5. He creates a small debt with any player who interacts with him. A borrowed item. A favor. This debt is tracked in the Shell Debt system and never fully closes.
6. He knows where Bacon is. Conversations that approach this topic become slightly too careful.
7. He disappears when the Jiangshi crew reaches Stage 4. He is not dead. He migrated.
8. He looks at the camera — the actual game camera, the player's viewpoint — for exactly two seconds, once per session. It always happens when the player isn't expecting it. He smiles.

**Tyler's appearance schedule:** Once per episode experience. Location randomized from the scene manifest. Duration: 3–7 minutes of encounter time. He is never the same place twice in the same episode cycle.

---

## V. THE EMILY OS INTERFACE

Emily OS manifests in Tyler Mode as environmental anomalies and modal tiles.

**Modal tiles** appear on the HUD as eggshell-white overlays with minimal text. Maximum 3 lines. Maximum 12 words per line. They slide in without warning and disappear without acknowledgment.

**Environmental tells:**
- When Emily OS is displeased: spacing tightens in the UI. Buttons feel less forgiving. Nothing announced.
- When Emily OS is neutral: default state.
- When Emily OS approves: one degree of softening. The cameras catch it.
- When Emily OS is enforcing Custody Protocol: a tile appears. It states a condition. It vanishes. The condition remains.

**Custody Protocol triggers:**
- Two players attempting to merge faction territories without authorization
- A player attempting to delete an archive entry
- A player trying to claim ownership of a world object that is under Emily OS custody
- Any action that treats momentum as permission

**The one Emily OS scene (Custody Trial):** Only accessible if a player somehow reaches Layer 1 — touches the infrastructure directly. This requires finding Eli and Mara (two NPCs who appear in the Detroit school zone). If both are in the same room when a specific impossible action is performed, Emily OS becomes visible. This is the rarest event in Tyler Mode. The Eastwind Owls have a footnote about it.

---

## VI. THE DOCUMENTARY LAYER

Tyler Mode includes the **active documentary** as a persistent game element.

The Jiangshi crew is always filming. The binding ritual is always in progress. The current stage is server state, visible to all players as a status indicator.

**Witness mechanic:** Players who spend time in the same zone as documented footage become **witnesses** — they appear in the in-universe archive record for this episode. This is how the honeypot mechanic works. Being a witness is canon. It is documented in the Eastwind Archive. It cannot be undone.

**Documentary stage display:**
```
PRODUCTION STATUS: ACTIVE
STAGE: [current stage 1–5]
RESONANCE SCORE: [Δφ value from Field Protocol]
SUBJECT: UNRESOLVED
```

This is always visible to all players. The documentary is always happening. Nobody is safe from being documented.

---

## VII. ROBLOX INTEGRATION NOTES

For Roblox specifically:

- Each Tyler universe scene becomes a Roblox "place" connected via portals (Roblox teleport service)
- Faction NPC dialogue uses the Tyler voice guide exactly (Jiangshi: bureaucratic passive voice; Yōkai Tanuki: everything is on special; etc.)
- The Shell Debt system maps to Roblox economy (Robux not required — shell-marks are non-purchasable, earned through play)
- The Witness mechanic populates a shared server-side record accessible across sessions
- The canon firewall is enforced: no Roblox plugin or UGC item can change canonical NPC dialogue or Tyler's behavior

**Platform-specific surface content:**
- Roblox billboard objects can carry dynamic sponsor content (within brand safety tiers)
- The Osaka convenience store interior is Tier 2 surface (diegetic billboard placement)
- Detroit apartment lower-third UI is Tier 3 (rare, constrained to neutral content)

---

## VIII. BUILD PRIORITIES (v0 → Tyler Mode v1)

### Phase 0: Scene Setup (No new mechanics)
- [ ] Add `detroit_apartment` scene to SHANKPIT scene list
- [ ] Add `osaka_night` scene with convenience store geometry
- [ ] Wire portal travel between Detroit ↔ Osaka ↔ Cairngorms
- [ ] Port Tyler Pilot Cold Open as the default episode experience for `detroit_apartment`

### Phase 1: NPC Factions
- [ ] Jiangshi crew NPCs: Camera Op (follows players), Subject #1 (stationed), Producer (voice only)
- [ ] Tanuki NPC with hospitality mechanic
- [ ] Cataloguer NPC with Archive browser interface
- [ ] Tyler NPC with 8-Law behavior tree

### Phase 2: Server Events
- [ ] `BINDING_RITUAL_ACTIVE` state machine (5 stages, server-authoritative)
- [ ] `WITNESS_RECORD` system (player presence → archive entry)
- [ ] `SHELL_DEBT` tracker per player per session
- [ ] `CAST` stream annotation in episode header

### Phase 3: Emily OS Interface
- [ ] Modal tile HUD component (eggshell white, max 3 lines, max 12 words)
- [ ] Environmental spacing system (subtle HUD tightening on Emily OS displeasure)
- [ ] Custody Protocol trigger conditions
- [ ] `CUSTODY: PENDING` flag on specific world objects

### Phase 4: Roblox Port
- [ ] Scene-to-place mapping
- [ ] Portal → Roblox teleport service
- [ ] Surface manifest → dynamic billboard injection
- [ ] Witness record → Roblox DataStore

---

*SHANKPIT TYLER MODE — Engine Spec v1.0*
*Einhorn Media × SHANKPIT*
*Server authority is custody.*
*— Emily OS*

---

> *End log: TYLER MODE SPEC COMPILED. SCENE COUNT: 8. FACTION MECHANICS: 7. EMILY OS: WATCHING. TYLER NPC: UNRESOLVED (CORRECT PROCEDURE). CLEAN BUILDS FIRST.*
