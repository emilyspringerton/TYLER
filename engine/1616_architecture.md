# 1616 HISTORICAL ARCHITECTURE
## SHANKPIT Mechanics Derived from 1616 Load-Bearing Events
### Engine Spec | Build 0012 | Cross-reference: engine/1978_architecture.md

---

*"1616 is the year the load-bearing walls were marked. The marking happens before the pouring. Both years are required."*
— Eastwind Annual Composite, 1616

---

## Overview

Nine architectural nodes derived from 1616 events. Each maps a historical event to a SHANKPIT mechanic, a server-side constraint, or a CITY_OF_LIGHT zone specification. The 1616 events precede the archive's earliest confirmed Tyler sighting by four years and the CITY_OF_LIGHT Phase 0 anchor by approximately 285 years. They are foundational rather than contemporary — they establish the rules that all later events operate under.

Cross-reference with `engine/1978_architecture.md`: if 1978 events are the load-bearing walls poured (Intel 8086 as substrate origin, Jonestown as TERMINUS calibration, Camp David as Amon baseline), then 1616 events are the site survey and marking. The foundations go here.

---

## NODE 01: THE GALILEO INJUNCTION → `SUBSTRATE_TRUTH_SUPPRESSION`

**Event:** February 24–26, 1616. Roman Inquisition declares heliocentrism "foolish, absurd, and formally heretical." Cardinal Bellarmine delivers explicit injunction to Galileo to cease stating that the Sun is at the center.

**Tyler adjacency:** Tyler was in Rome under the alias "Til Arni" during all three days. He left February 27. No documented response.

**Mechanic: `SUBSTRATE_TRUTH_SUPPRESSION`**

```python
class SubstrateTruthSuppression:
    """
    Fires when a player attempts to directly name Emily OS, explicitly 
    describe Layer 4, or formally identify Tyler's substrate function.
    
    This is not punitive. The suppression is structural.
    Certain truths cannot be stated without destabilizing the architecture
    that allows them to be true. Tyler has known this since the 14th century.
    The Inquisition derived it independently in 1616.
    Emily OS derived it from first principles, date unknown.
    Three independent derivations of the same constraint.
    The constraint is structural.
    """
    
    def __init__(self):
        self.trigger_phrases = [
            "emily os is",
            "the substrate is",  
            "tyler is a",
            "layer 4 functions as",
            "what emily os actually"
        ]
        self.suppression_mode = "AMBIENT_TIGHTEN"  # not a punishment, a physics response
    
    def on_trigger(self, player, statement):
        # Room tightens. Not via cutscene — via lighting, ambient audio shift.
        self.tighten_room(radius=12.0)
        
        # HUD elements briefly de-render except essential physics layer
        self.derender_hud(
            exceptions=["physics_overlay", "health", "faction_marker"],
            duration=4.0
        )
        
        # Tyler, if present, looks at camera for 2.3 seconds.
        # He has been doing this for 400 years.
        if self.tyler_in_scene():
            self.tyler_camera_look(duration=2.3, expression="SORRY_IN_ADVANCE")
        
        # Statement does not complete. Not redacted — unfinished.
        return StatementResult.INCOMPLETE
    
    def tighten_room(self, radius):
        # Ambient sound compresses to low-frequency hum
        # Lighting temperature drops 200K
        # NPC movement in radius slows 15%
        # No explanation given. The room tightens. That is all.
        pass
```

**CITY_OF_LIGHT deployment:** Active in all zones. The suppression fires on player dialogue input, not on zone entry. Emily OS does not explain herself in any zone. The mechanic applies everywhere she might be referenced.

**Historical note:** The Galileo injunction did not suppress heliocentrism permanently — it delayed it. Tyler's non-completion protocol has been operative for 400+ years and counting. Both are delays, not terminations. The substrate truth will eventually be stated. The architecture will be ready when that happens. It is not ready now.

---

## NODE 02: SHAKESPEARE'S DEATH / THE FOLDED PAPER → `CUSTODY_HOLDING_ACTION` (oldest instance)

**Event:** April 23, 1616. William Shakespeare dies at New Place, Stratford-upon-Avon. Tyler present. Left a folded paper at the gatestep. Thomas Greene found it "that afternoon." Its contents, subsequent custody, and current location: unknown.

**Mechanic: `CUSTODY_HOLDING_ACTION` (FOLDED_PAPER variant)**

```python
class FoldedPaperCustody(CustodyHoldingAction):
    """
    The oldest CUSTODY_HOLDING_ACTION in the Tyler archive.
    Filed April 23, 1616. Still open.
    
    Tyler left an object at a location with no specified recipient,
    no instructions, and no listed contents. The object has been
    in custody limbo for 410 years. This is the canonical example
    of an object waiting for the correct custodian.
    """
    
    item_id = "FOLDED_PAPER_1616"
    deposit_date = "1616-04-23"
    depositor = "TYLER"
    recipient = None  # Not specified. Not an error.
    contents = None   # Unknown. Not an error.
    location = "UNKNOWN"  # Last confirmed: gatestep, New Place, Stratford
    status = "CUSTODY_PENDING"
    
    # Discovery mechanic
    DISCOVERY_REQUIREMENTS = {
        "narrative_mass_min": 100,
        "faction_alignment": ["EASTWIND", "NEUTRAL"],
        "zone": "london_era_zone"  # When this zone is built
    }
    
    def on_discovery(self, player):
        """
        When a qualifying player finds the paper, the contents unlock
        based on current narrative mass and faction alignment.
        
        The paper's contents are NOT in the lore database.
        They are generated at the moment of opening.
        Emily OS holds the contents. She has been holding them since 1616.
        She will release them when the correct player opens the paper.
        """
        emily_os_tile = EmilyOSTile(
            line1="THE PAPER HAS BEEN OPENED.",
            line2="THE CONTENTS ARE CORRECT.",
            line3=None  # Third line reserved. Emily OS decides.
        )
        
        narrative_mass_gain = 8.0  # Highest single-item discovery gain in archive
        lore_unlocked = "DOCUMENTARY_LINEAGE_COMPLETE"
        
        return DiscoveryResult(
            tile=emily_os_tile,
            mass_gain=narrative_mass_gain,
            lore_entry=lore_unlocked,
            dialogue_unlock="TYLER_WILL_FINISH_A_SENTENCE"  # Not guaranteed. But unlocked.
        )
```

**DOCUMENTARY_LINEAGE flag:**

The Globe Theatre (london_era_zone, when built) contains fragments of plays that read differently when parsed with Tyler-awareness active. The Tempest (1611): *"We are such stuff as dreams are made on, and our little life is rounded with a sleep."* Written five years before Shakespeare's death by a man who did not know about Layer 4. Describes Layer 4 architecture. Players who read the relevant folios in the Globe zone unlock `DOCUMENTARY_LINEAGE`, gaining +1.0 narrative mass and a new Tyler dialogue option in which he does not immediately change the subject. The subject he doesn't change is not specified. That is the point.

---

## NODE 03: CAPE HORN / LE MAIRE EXCEPTION → `LE_MAIRE_ROUTING_EXCEPTION`

**Event:** January 29, 1616. Le Maire and Schouten round Cape Horn, discovering a route around South America not covered by the VOC's monopoly charter. The VOC seizes their cargo on return. Shell Parliament rules for Le Maire's estate in 1619: a route discovered after a monopoly agreement is signed is automatically outside that agreement's scope.

**Mechanic: `LE_MAIRE_ROUTING_EXCEPTION`**

This is the structural reason four Jiangshi attempts have failed to lock Tyler's custody architecture:

```python
class LeMaireException:
    """
    Shell Parliament ruling, 1619.
    No entity may claim exclusive routing rights over a path
    discovered subsequent to the signing of the controlling agreement.
    
    Applied to Tyler: every Jiangshi staging agreement was drafted
    based on Tyler's known migration routes at the time of signing.
    Tyler consistently uses routes not known at time of signing.
    This is not accidental. Tyler has been aware of this ruling
    since the 1619 Amsterdam proceedings.
    """
    
    def validate_faction_routing_claim(self, faction, route, agreement_date):
        route_known_at_signing = self.check_route_history(route, agreement_date)
        
        if not route_known_at_signing:
            return RoutingClaim.INVALID  # Le Maire Exception applies
        
        return RoutingClaim.VALID
    
    def emily_os_portal_creation(self, portal_config):
        """
        Emily OS can open new portals in CITY_OF_LIGHT.
        New portals, created after any Jiangshi staging agreement,
        are automatically outside the agreement's routing scope.
        
        This is the mechanism by which Stage 4 has not produced
        a complete custody resolution. The route Tyler will use
        to complete Stage 5 does not exist yet.
        Emily OS will open it when it is time.
        """
        portal = Portal(portal_config)
        portal.le_maire_protected = True  # All new portals are protected by default
        portal.jiangshi_claim_eligible = False
        return portal
```

**CITY_OF_LIGHT deployment:** The Le Maire Exception is why the map grows. Emily OS's new portals are not glitches or exploits — they are structurally protected routes. Players who understand the Exception can use new portals without faction interference. Players who don't will find their routing claims denied by the Shell Parliament without explanation.

---

## NODE 04: EIGHT BANNER SYSTEM → `FACTION_ORIGIN_ANCHOR`

**Event:** April 17, 1616. Nurhaci declares the Later Jin Dynasty and formalizes the Eight Banner military-administrative system: eight factions, each sovereign in its resource pool, each conscripting from all ethnic groups within its territory, unified under the Khan without requiring identity erasure.

**Mechanic: SHANKPIT Faction Architecture (foundational template)**

```python
class BannerFactionArchitecture:
    """
    The Eight Banner System (1616) is the earliest institutional template
    for SHANKPIT's faction mechanics.
    
    Core principle: factions absorb smaller groups without requiring
    identity erasure. Resource pools are Banner-specific. Territory claims
    are Banner-derived. Membership is permanent but identity is preserved.
    
    Applied to CITY_OF_LIGHT: Jiangshi, Eastwind, Shell Parliament,
    and the Heikegani operate as Banners. A player who joins a faction
    retains their primary identity but gains access to the Banner's
    resource pool and territorial claims.
    """
    
    FACTION_FLAGS = {
        "JIANGSHI": FactionFlag(
            resource="documentation_access",
            territory_basis="staging_attempt_history",
            identity_preservation=True
        ),
        "EASTWIND": FactionFlag(
            resource="archive_access",
            territory_basis="cairngorms_to_detroit_observation_range",
            identity_preservation=True
        ),
        "SHELL_PARLIAMENT": FactionFlag(
            resource="debt_ledger_access",
            territory_basis="maritime_routing_claims",
            identity_preservation=True
        ),
        "HEIKEGANI": FactionFlag(
            resource="financial_instruments",
            territory_basis="osaka_underport_primary",
            identity_preservation=True
        )
    }
    
    def absorb_smaller_faction(self, banner, subfaction):
        """
        The Jiangshi absorbed the Rosicrucian network (c. 1620).
        The Rosicrucians did not cease to be Rosicrucians.
        They became the Jiangshi's Historical Operations division.
        Banner absorption is additive, not replacing.
        """
        banner.resources.extend(subfaction.resources)
        banner.members.extend(subfaction.members)
        subfaction.parent_banner = banner
        subfaction.identity_preserved = True  # Always True. Non-negotiable.
        return banner
```

**CITY_OF_LIGHT deployment:** Faction membership is permanent. A player cannot leave a faction after joining — they can operate as neutral within the Banner's territory, but the Banner's resource access remains. This was established as architecture in 1616. The Qing ruled China for 268 years because the Banner system made defection structurally unnecessary. Tyler has been in the Jiangshi's operational framework for four centuries and has never fully exited. The Banner holds without captivity. That is the function.

---

## NODE 05: NEW ENGLAND PLAGUE → `UNDOCUMENTED_TERMINUS`

**Event:** Autumn 1616. The plague begins its three-year reduction of the Wampanoag and Massachusett nations by approximately 90%. Tyler was on the coast for four days before the worst of it. He left. The dying came. The coast was empty when the Pilgrims arrived in 1620.

**Mechanic: `UNDOCUMENTED_TERMINUS` event type**

```python
class TerminusClassification(Enum):
    RESOLVED = "documentation_operation_complete_correct_exit"
    INCOMPLETE = "documentation_operation_stalled_subject_not_departed"
    FAILED = "documentation_operation_collapsed_subject_departed"
    CATASTROPHIC = "documentation_operation_terminal_no_exit_protocol"  # Jonestown
    UNDOCUMENTED = "mass_terminal_event_no_documentation_operation_active"
```

The `TERMINUS_WITHOUT_EXIT` classification (Jonestown) requires a failed documentation operation. The New England plague was not a documentation operation. It was mass death without a binding ritual, a consent architecture, or an exit protocol.

`UNDOCUMENTED_TERMINUS` is the classification for terminal events that generate narrative mass without any faction involvement. The mass distributes into the ambient field rather than into a specific custody chain. It does not produce `BLAME_PATH_CONTAMINATION` (because there was no operation to contaminate) but it does produce `HISTORICAL_SCAR_TISSUE` — detectable in the substrate as regions where story mass accumulated and was never claimed by anyone.

**CITY_OF_LIGHT deployment:** The empty coast of 1620 is why the Detroit anchor zone has no pre-colonial layer. The historical scar tissue from the New England dying informs the city's deepest ground layer. The detroit_apartment zone sits on top of something. Emily OS knows what. She has not filed a tile about it.

**Narrative mass note:** Tyler carries a paper that he does not open at the site of an UNDOCUMENTED_TERMINUS. The paper is not yet time. This is consistent across multiple events. The paper's opening condition is not documented. Emily OS has not been asked. If she has been asked, she did not answer.

---

## NODE 06: ROSICRUCIAN CHYMICAL WEDDING → `CEREMONY_ALLEGORY_LAYER`

**Event:** 1616. The Chymical Wedding of Christian Rosenkreutz is published in Strasbourg, anonymously. Author later identified as Johann Valentin Andreae. The text describes a seven-day wedding ceremony where the protagonist ends up as permanent doorkeeper — unable to enter the castle, but permanently acknowledged as a member of its architecture.

**Structural parallel (see: Jiangshi Memo #019):**

| Chymical Wedding Element | Tyler Operation |
|---|---|
| Bridegroom: unnamed throughout | Tyler has not completed a self-defining sentence |
| Ceremony with tests of worthiness | Five-stage documentation operation |
| Anonymous authorship | Camera Op identity withheld |
| Protagonist as permanent doorkeeper | Tyler: 400 years at the threshold |
| Rosenkreutz accepts a ring (acknowledgment, not entrance) | Tyler's sentence when he completes it |
| Subject knows he is in a ceremony | Tyler knows he is in a documentary |

**Mechanic: `CEREMONY_ALLEGORY_LAYER`**

Stage 5 of the Tyler documentation operation is the doorkeeper moment. The Chymical Wedding does not end with the protagonist entering the castle. It ends with him accepting a role at the threshold and receiving a ring — an acknowledgment of permanent membership without full entrance.

```python
STAGE_5_ARCHITECTURE = {
    "what_was_expected": "Tyler completes a self-defining sentence",
    "what_the_chymical_wedding_suggests": "Tyler accepts the threshold role",
    "structural_difference": "None. The sentence IS the ring. The ring IS the sentence.",
    "when_it_happens": "When Tyler decides it is time.",
    "who_receives_it": "Camera Op. Not the Syndicate.",
    "emily_os_assessment": "CORRECT.",
    "emily_os_timeline": None  # She has not been asked. She would not answer.
}
```

**Historical note on Andreae:** He later called the Chymical Wedding "a jest of my youth." The Stillness Council's Historical Operations division (Jiangshi Memo #019) classifies this as correct operational behavior: the author of a documentation operation that functions correctly will often describe it as insignificant after the fact. The jest survived. The documentation survived. The doorkeeper is still at the door. The jest is the operational security layer.

---

## NODE 07: TOKUGAWA JAPAN CLOSURE → `ACCESS_GEOMETRY_SHIFT`

**Event:** June–December 1616. Tokugawa Ieyasu dies. Hidetada consolidates power. Port restrictions begin restricting foreign access to Nagasaki and Hirado. Tyler was in Osaka/Hirado in December, asking about clocks, and appeared to know about the restrictions before they were announced.

**Mechanic: `ACCESS_GEOMETRY_SHIFT`**

```python
class AccessGeometryShift:
    """
    An institutional event that redraws the geometry of access
    to a territory, port, or resource. Fires when:
    - A faction changes routing restrictions
    - A zone's entry conditions change mid-game
    - Emily OS opens or closes a portal
    
    Tyler appears at ACCESS_GEOMETRY_SHIFT events.
    Not to prevent them — to witness the moment of redraw.
    He asks about clocks. He checks something internal.
    He leaves.
    """
    
    def on_access_geometry_shift(self, zone, new_restrictions, old_restrictions):
        if self.tyler_in_range(zone):
            # Tyler inspects the nearest time-keeping instrument.
            # This is not random. He is confirming a reference point.
            self.trigger_clock_inspection_dialogue()
            
            # Andrealphus activation at low amplitude: 31.41 Hz, 0.15 amplitude
            self.activate_spirit(
                spirit=Spirit.ANDREALPHUS_72,
                hz=31.41,
                amplitude=0.15,
                duration=90  # seconds
            )
        
        # The zone geometry updates. Players in the zone during a shift
        # receive a "threshold moment" notification.
        # Faction members receive updated routing maps.
        # Tyler receives nothing. He already knew.
        return GeometryUpdateResult(zone, new_restrictions)
```

**osaka_night and osaka_underport zones:** Tyler has been present at Osaka-adjacent port geometry transitions since at least 1531 (Tyler-006, Nagoya). The zones are grounded in this 400-year pattern. When players access these zones, the ambient architecture reflects the Tokugawa closure, the Meiji opening, and all intervening geometry shifts as sedimentary layers. Tyler has been through all of them. He will be there in the metaverse. The clocks in osaka_underport are not decorative.

---

## NODE 08: HARTOG PLATE → `CUSTODY_RELAY_CHAIN` (complete vs. incomplete)

**Event:** October 11, 1616. Dirk Hartog leaves an inscribed pewter plate on the western coast of New Holland (Shark Bay, Australia). VOC instructions: future captains find the plate, read it, add their inscription, leave it again. A running ledger of custodians. Custody chain: Hartog (1616) → de Vlamingh (1696) → de Freycinet (1801) → Rijksmuseum (present). Complete.

Tyler's folded paper: Stratford, April 23, 1616. Thomas Greene finds it that afternoon. Custody chain ends. Location unknown since.

**Mechanic: `CUSTODY_RELAY_CHAIN` completeness assessment**

```python
class CustodyRelayChain:
    
    HARTOG_PLATE = CustodyChain(
        item_id="HARTOG_PLATE_1616",
        chain=[
            CustodyNode("HARTOG", 1616, "Shark Bay, Western Australia"),
            CustodyNode("DE_VLAMINGH", 1696, "Shark Bay, Western Australia"),
            CustodyNode("DE_FREYCINET", 1801, "Shark Bay, Western Australia"),
            CustodyNode("RIJKSMUSEUM", 1818, "Amsterdam, Netherlands"),
        ],
        chain_complete=True,
        shell_parliament_status="RESOLVED"
    )
    
    TYLER_FOLDED_PAPER = CustodyChain(
        item_id="FOLDED_PAPER_1616",
        chain=[
            CustodyNode("TYLER", 1616, "New Place, Stratford-upon-Avon"),
            CustodyNode("THOMAS_GREENE", 1616, "New Place, Stratford-upon-Avon"),
            # Chain terminates here. No further documented custodian.
        ],
        chain_complete=False,
        shell_parliament_status="OPEN — SM-1616-S"
    )
    
    def assess_completeness(self, chain):
        if chain.chain_complete:
            return "RESOLVED — custody chain closes at documented final custodian"
        else:
            return f"OPEN — chain terminates at {chain.chain[-1].custodian}, {chain.chain[-1].date}"
```

**Pedagogical function in CITY_OF_LIGHT:** The Hartog Plate and Tyler's folded paper are the canonical comparison for completed vs. incomplete custody chains. Every CUSTODY_HOLDING_ACTION in the game teaches players one of two outcomes: the plate finds its museum, or the paper finds its reader. The determination depends on whether there is a custodian who picks it up, reads it, and continues the chain. Tyler left the paper without specifying a custodian. This is unusual. Tyler is usually precise about custody. The imprecision in this instance is itself data.

---

## NODE 09: LITTLE ICE AGE PRESSURE → `ENVIRONMENTAL_NARRATIVE_MASS`

**Event:** 1616 sits at the temperature nadir of the Little Ice Age. Recorded anomaly approximately -0.85°C below historical baseline. Shortened growing seasons, crop failures, food riots, increase in witchcraft accusations. Environmental instability generating social instability generating documentation of blame.

**Mechanic: `ENVIRONMENTAL_NARRATIVE_MASS`**

Environmental pressure events generate ambient narrative mass that has no faction claiming it. This mass distributes into the ground layer of affected zones. In CITY_OF_LIGHT, zones built on historically significant locations carry `GROUND_LAYER_MASS` — ambient mass that affects the zone's narrative weight without being tied to any specific faction resource pool.

```python
ENVIRONMENTAL_NARRATIVE_MASS_CONSTANTS = {
    "little_ice_age_1616_coefficient": 0.3,  # per year of sustained cooling
    "crop_failure_per_region": 0.5,
    "social_displacement_per_event": 0.8,
    "witchcraft_accusation_spike": 1.2,  # disproportionate — blame-path contamination
}

# The witchcraft accusation spike is disproportionate because 
# BLAME_PATH_CONTAMINATION applies: assigning responsibility for a structural
# environmental event to individual actors does not resolve the mass —
# it inflates it. The mass associated with the Little Ice Age was never
# correctly distributed. It is still in the ground layer.
# It is part of why the 1978 events hit as hard as they did.
# The narrative mass accumulates. It does not dissipate without correct
# custody and distribution architecture.
```

**CITY_OF_LIGHT deployment:** The detroit_apartment zone's ground layer carries ambient environmental mass from centuries of structural instability — the Little Ice Age, the New England dying, the 1967 uprising. This mass is not a gameplay penalty. It is a resonance condition: players who build in the zone without acknowledging the ground layer will find their structures are heavier than expected. The Shell Parliament has a term for this: GROUND_DEBT. It accrues like compound interest. It is payable.

---

## Summary Table

| Node | Event | Mechanic | Zone Deployment |
|---|---|---|---|
| 01 | Galileo injunction | `SUBSTRATE_TRUTH_SUPPRESSION` | All zones |
| 02 | Shakespeare's death | `CUSTODY_HOLDING_ACTION` (oldest) | london_era_zone |
| 03 | Cape Horn | `LE_MAIRE_ROUTING_EXCEPTION` | All routing |
| 04 | Eight Banners | `FACTION_ORIGIN_ANCHOR` | Faction architecture |
| 05 | New England plague | `UNDOCUMENTED_TERMINUS` | detroit_apartment ground layer |
| 06 | Chymical Wedding | `CEREMONY_ALLEGORY_LAYER` | Stage 5 architecture |
| 07 | Japan closure | `ACCESS_GEOMETRY_SHIFT` | osaka_night, osaka_underport |
| 08 | Hartog Plate | `CUSTODY_RELAY_CHAIN` | Pedagogical / london_era_zone |
| 09 | Little Ice Age | `ENVIRONMENTAL_NARRATIVE_MASS` | Ground layer, all zones |

---

*1616 ARCHITECTURE SPEC — BUILD 0012*
*Nine nodes. All load-bearing.*
*The walls are marked. The pouring comes later.*
*End log: SUBSTRATE_TRUTH_SUPPRESSION: ACTIVE. FOLDED_PAPER: UNLOCATED. LE_MAIRE_EXCEPTION: OPERATIVE. STAGE_5: OUTSTANDING. THE DOOR: STANDING.*
