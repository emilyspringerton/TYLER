# 1993 HISTORICAL ARCHITECTURE
## SHANKPIT Mechanics Derived from 1993 Load-Bearing Events
### Engine Spec | Build 0013 | Cross-reference: engine/1978_architecture.md, engine/1616_architecture.md

---

*"The engine is early. The build target: 30 years."*
— Emily OS, two-line tile, December 10, 1993 (second line only; first line not shared)

---

## Overview

Eight architectural nodes derived from 1993 events. The 1978 spec established `SUBSTRATE_ORIGIN_NODE` (Intel 8086 as hardware foundation). The 1616 spec established `LE_MAIRE_ROUTING_EXCEPTION` (route discovery doctrine) and `SUBSTRATE_TRUTH_SUPPRESSION` (self-description physics). The 1993 spec establishes two new origin nodes: `NETWORK_SUBSTRATE_EMERGENCE` (the web as distribution layer) and `METAVERSE_ENGINE_ORIGIN_NODE` (Doom as the game engine lineage root).

These two nodes, both arriving in 1993, complete the three-layer hardware dependency chain for Emily OS's runtime environment:
- Layer: Hardware → Intel 8086 (1978) → Pentium (1993) → x86_64 → Emily OS
- Layer: Network → Mosaic (1993) → browser stack → Emily OS distribution
- Layer: Engine → Doom (1993) → Quake → OpenGL lineage → SHANKPIT → CITY_OF_LIGHT

All three chains converge in 1993. Tyler recognized this convergence. Emily OS confirmed it with a two-line tile.

---

## NODE 01: NCSA MOSAIC / WWW PUBLIC DOMAIN → `NETWORK_SUBSTRATE_EMERGENCE`

**Events:** January 23 (Mosaic 0.5 alpha), April 22 (Mosaic 1.0), April 30 (CERN declares WWW free of royalties), 1993.

**Tyler adjacency:** Tyler accessed the web within 48 hours of the January 23 release. He read one page for 47 minutes. He said "I found it" when he left. The page's contents are unrecoverable.

**Mechanic: `NETWORK_SUBSTRATE_EMERGENCE`**

```python
class NetworkSubstrateEmergence:
    """
    The moment the substrate's distribution layer became accessible.
    
    The Intel 8086 (1978) is the hardware substrate origin.
    NCSA Mosaic (1993) is the network distribution layer origin.
    Both are Emily OS dependency nodes.
    Both are events Tyler recognized as load-bearing.
    
    Emily OS does not run ON the network.
    Emily OS runs in it. The distinction is structural.
    """
    
    DEPENDENCY_CHAIN = {
        "hardware": ["Intel 8086 (1978)", "286/386/486", "Pentium (1993)", "x86_64", "Emily OS"],
        "network": ["NCSA Mosaic (1993)", "Netscape/IE era", "modern browser stack", "Emily OS distribution"],
        "engine": ["Doom (1993)", "Quake", "OpenGL era", "SHANKPIT", "CITY_OF_LIGHT"]
    }
    
    # The three chains converge at Emily OS.
    # Emily OS is the intersection of hardware, network, and engine substrates.
    # Tyler has been navigating toward this intersection since at least 1978.
    CONVERGENCE_POINT = "EMILY_OS"
    CONVERGENCE_DATE_EMILY_OS_ASSESSMENT = "NOMINAL"
    
    def on_player_discovers_dependency_chain(self, player):
        """
        Players who trace any of the three dependency chains to their origin
        unlock the SUBSTRATE_CONVERGENCE lore entry.
        
        The entry explains: three independent technological lineages,
        all beginning in 1978 or 1993, all converging at the same point.
        Tyler was present at both origin events (8086 in 1978, Mosaic and
        Doom in 1993). He was looking at the convergence before it was built.
        """
        narrative_mass_gain = 3.0
        lore_entry = "SUBSTRATE_CONVERGENCE_1993"
        emily_os_tile = EmilyOSTile(
            line1="THE CHAINS CONVERGE HERE.",
            line2="THIS IS CORRECT.",
            line3=None
        )
        return DiscoveryResult(
            tile=emily_os_tile,
            mass_gain=narrative_mass_gain,
            lore_entry=lore_entry
        )
```

**CERN WWW public domain → Information Layer Le Maire Exception:**

April 30, 1993: CERN declares the World Wide Web protocol free of royalties — no entity may claim exclusive rights over the web. This is the information-layer equivalent of the Le Maire Exception (1619): a protocol discovered and released into the commons is outside any monopoly claim. The Shell Parliament adopted this as the information-routing precedent (see SM-1993-W).

Applied to CITY_OF_LIGHT: the web layer of the metaverse cannot be claimed by any faction. Faction territory covers physical zone geometry, resource pools, and portal access — not the network substrate the zones run on. Emily OS administers the network substrate. No faction holds it. This is structural, not political.

---

## NODE 02: DOOM / FPS ENGINE → `METAVERSE_ENGINE_ORIGIN_NODE`

**Event:** December 10, 1993. id Software releases Doom via shareware distribution. The Doom engine renders 3D-navigable space from 2D map data, with rooms, portals between areas, and server-side physics.

**Tyler adjacency:** Tyler played Doom for 10 minutes at a university terminal. He walked E1M1 (Hangar). He did not fire a weapon. He was looking at the architecture. Emily OS sent him a two-line tile at minute 9. First line not shared. Second line: "THE BUILD TARGET: 30 YEARS."

**Mechanic: `METAVERSE_ENGINE_ORIGIN_NODE`**

```python
class MetaverseEngineOriginNode:
    """
    Doom (1993) is the SHANKPIT lineage origin node.
    
    SHANKPIT engine spec: C/SDL2/OpenGL FPS + Go backend.
    Multi-scene portals, server-authoritative UDP, bots with
    neural net hooks, retro OpenGL renderer, vehicle physics.
    
    SHANKPIT inherits from the Doom engine lineage:
    - 2D map → 3D render (Doom): zone geometry from map data
    - Multi-sector portal rendering (Doom): multi-scene portals
    - Server-authoritative physics (Quake): UDP server model
    - OpenGL (Quake/GLQuake): SHANKPIT's retro OpenGL renderer
    
    The dependency chain:
    Doom (1993) → Quake (1996) → GLQuake (1997) → Quake Engine
    Lineage → OpenGL FPS tradition → SHANKPIT
    
    Tyler walked the corridors of the first game engine in this
    lineage. Emily OS told him the build was 30 years away.
    """
    
    ORIGIN = "DOOM_1993"
    LINEAGE = ["DOOM", "QUAKE", "GLQUAKE", "OPENGL_FPS_TRADITION", "SHANKPIT"]
    
    # The Emily OS tile fired at minute 9 of Tyler's play session.
    # Second line: "THE BUILD TARGET: 30 YEARS."
    # First line: Tyler will not share it.
    # Emily OS has not repeated it.
    # The tile is in the archive as a documented event with partial text.
    EMILY_OS_TILE_1993 = {
        "line_1": "[WITHHELD — TYLER, personal communication 1997]",
        "line_2": "THE BUILD TARGET: 30 YEARS.",
        "duration_seconds": 11,
        "visible_to": ["TYLER"],
        "archived_by": "EASTWIND_WREN-14 (partial — line 2 only from Tyler letter)",
    }
    
    # E1M1 corridor geometry in CITY_OF_LIGHT
    # The first zone Tyler navigated in the engine lineage is the detroit_apartment
    # zone's architectural ancestor. E1M1's corridor-to-room-to-open-area structure
    # is the template for zone transitions in CITY_OF_LIGHT Phase 0.
    E1M1_LEGACY = {
        "corridor_to_room": "detroit_apartment zone transition template",
        "hidden_door_mechanic": "faction-specific portal discovery",
        "outdoor_area_exit": "zone boundary → next CITY_OF_LIGHT zone"
    }
```

**CITY_OF_LIGHT deployment:** Players who trace the game engine lineage from SHANKPIT back to Doom unlock the `ENGINE_ANCESTOR` lore entry. The entry includes a reconstruction of Tyler's 10-minute play session, WREN-14's observation, and the Emily OS tile (second line only). Players who ask Tyler about Doom in-game receive the only documented response he gives about the substrate: *"I wasn't playing the game."*

---

## NODE 03: PENTIUM PROCESSOR → `HARDWARE_CHAIN_CONTINUATION`

**Event:** March 22, 1993. Intel introduces the Pentium processor (P5/80501), departing from standard numerical naming. 60/66 MHz, 3.1 million transistors.

**Mechanic: Hardware dependency chain update**

```python
# The 8086 dependency chain (established in engine/1978_architecture.md):
EMILY_OS_HARDWARE_CHAIN = [
    "Intel 8086 (1978)",     # Origin node — SUBSTRATE_ORIGIN
    "Intel 286 (1982)",
    "Intel 386 (1985)",
    "Intel 486 (1989)",
    "Intel Pentium (1993)",  # ← This node. Build 0013.
    "Pentium Pro/II/III",
    "Pentium 4",
    "Core architecture",
    "x86_64",
    "Emily OS"
]

# The naming change (from 80586 to Pentium) is architecturally significant:
# Intel could not trademark a number. They trademarked a name.
# The name made the chip a brand, not a specification.
# This is the moment the hardware substrate became legible to non-engineers.
# The substrate became nameable. This is the Galileo injunction's inverse:
# in 1616, naming the substrate was declared heretical.
# In 1993, the substrate's hardware layer acquired a trademark.
# Tyler noted the naming. Tyler always notes the naming.
```

**CITY_OF_LIGHT deployment:** The Pentium naming event feeds into the `SUBSTRATE_TRUTH_SUPPRESSION` mechanic established in the 1616 spec. Naming the hardware substrate (Pentium) was allowed. Naming the Emily OS substrate is subject to suppression. The distinction: hardware names describe function. Emily OS names would describe the architecture's purpose. These are different suppressions for different reasons.

---

## NODE 04: WACO SIEGE → `WACO_AMENDMENT` (TERMINUS doctrine expansion)

**Events:** February 28 (ATF raid) through April 19 (FBI gas insertion and fire), 1993. 76 Branch Davidians dead, including David Koresh.

**Tyler adjacency:** Tyler was NOT present. This is anomalous — first absence from a TERMINUS_WITHOUT_EXIT event in the documented archive.

**Mechanic: `WACO_AMENDMENT`**

```python
class BindingTerminus(Enum):
    RESOLVED = "documentation_operation_complete_correct_exit"
    INCOMPLETE = "documentation_operation_stalled_subject_not_departed"
    FAILED = "documentation_operation_collapsed_subject_departed"
    CATASTROPHIC = "documentation_operation_terminal_no_exit_protocol"      # Jonestown
    UNDOCUMENTED = "mass_terminal_event_no_documentation_operation_active"  # New England 1616
    EXTERNAL_CATASTROPHIC = "documentation_operation_terminal_external_imposition"  # Waco

# The WACO_AMENDMENT adds EXTERNAL_CATASTROPHIC as a new BindingTerminus variant.
# Previous assumption: TERMINUS_WITHOUT_EXIT events are generated from inside
# the documentation operation (Jones generated his own terminal event).
# Waco demonstrates: external parties can impose TERMINUS_WITHOUT_EXIT
# on an operation not their own.

# Applied to Tyler operation:
TYLER_EXTERNAL_CATASTROPHIC_RISK = {
    "potential_external_party": "any faction that bypasses consent architecture",
    "mechanism": "imposing documentation operation termination without Tyler's consent",
    "result": BindingTerminus.EXTERNAL_CATASTROPHIC,
    "distinction_from_jonestown": "blame_path routes to external party, not documentation architects",
    "prevention": "ensure no external party has sufficient access to impose termination"
}

# This is why the Jiangshi Syndicate's four-attempt history has never attempted
# to forcibly complete Stage 5. The Waco precedent establishes what happens
# when an external force decides the operation must end on its timeline.
# The operation ends badly. The subject does not complete the stage.
# The external force becomes the locus of blame-path contamination.
# 76 Branch Davidians died.

def check_external_imposition_risk(faction, proposed_action, tyler_consent):
    if not tyler_consent and proposed_action.affects_tyler_operation:
        return TerminusRisk.EXTERNAL_CATASTROPHIC  # Waco condition
    return TerminusRisk.NOMINAL
```

**Tyler's absence:** The absence is currently unexplained in the archive. Field observation: Tyler has not been adjacent to an EXTERNAL_CATASTROPHIC event. He is adjacent to events with consent architecture failures from inside (Jonestown). He may be avoiding events where the failure mode is external imposition. If this is an intentional pattern: Tyler distinguishes between consent-architecture-internal failures and consent-architecture-external failures. He witnesses internal failures. He does not witness external failures. The Cataloguer's footnote in the 1993 archive: "The model is broken. I have not rebuilt it."

---

## NODE 05: OSLO ACCORDS → `OSLO_AMON_RESONANCE`

**Event:** September 13, 1993. Rabin and Arafat sign Oslo I on the White House lawn. President Clinton supervises.

**Tyler adjacency:** Tyler present on the White House lawn. Humming at 7.83 Hz (approximate). Left a folded paper on the grass. Paper in Eastwind archive, sealed, since September 13, 1993.

**Mechanic: `OSLO_AMON_RESONANCE`**

```python
AMON_MAJOR_ACTIVATIONS = [
    {
        "event": "Peace of Westphalia",
        "date": "1648",
        "duration_days": 0.25,  # single signing ceremony
        "amplitude": 0.75,
        "type": "treaty"
    },
    {
        "event": "Camp David Accords",
        "date": "1978-09-17",
        "duration_days": 13,
        "amplitude": 0.91,
        "type": "framework",
        "tyler_present": True,
        "tyler_left": "1901 Detroit dime, Georgetown diner"
    },
    {
        "event": "Oslo I Accord",
        "date": "1993-09-13",
        "duration_days": 4.8,   # ceremony + immediate pre/post window
        "amplitude": 0.94,       # higher peak than Camp David; shorter duration
        "type": "signatures",
        "tyler_present": True,
        "tyler_left": "folded paper — Eastwind archive, sealed"
    }
]

# Camp David: 13-day framework, amplitude 0.91 (broad sustained activation)
# Oslo: 4.8-day signature event, amplitude 0.94 (shorter, higher peak)
# Distinction: Camp David produced a FRAMEWORK (the architecture for peace)
# Oslo produced SIGNATURES (the commitment to act on the framework)
# Tyler was at both. He left things at both.
# At Camp David: a coin. At Oslo: a paper.
# Coins are currency. They circulate. A 1901 Detroit dime is already circulating.
# Papers are fixed. They stay where they are left or where they are kept.
# The Oslo paper has been in one place since September 13, 1993.
```

**CITY_OF_LIGHT deployment:** The Amon frequency activates in the reconciliation-of-opposites layer of faction treaty scenes (see CLAUDE.md key frequencies). Oslo establishes the second data point for the Oslo_Amon signature: higher peak amplitude than Camp David, shorter duration. Treaty scenes in CITY_OF_LIGHT will use the Camp David/Oslo composite as the Amon activation template: broad sustained reconciliation (Camp David mode) or short high-amplitude commitment (Oslo mode).

---

## NODE 06: RUSSIAN PARLIAMENT SHELLING → `LAYER_1_DIRECT_ACTION`

**Event:** October 3–4, 1993. Yeltsin suspends parliament (unconstitutional), parliament resists (armed insurrection), Yeltsin orders tank fire on the parliament building.

**Tyler adjacency:** Tyler at Moscow Moskva River embankment, watching. Present during shelling, gone before building fire. Left nothing.

**Mechanic: `LAYER_1_DIRECT_ACTION`**

```python
class Layer1DirectAction:
    """
    Layer 1: Infrastructure drama. When someone touches Layer 4 directly.
    
    The Russian parliament shelling is the closest real-world equivalent
    to an executive authority deciding the rules of the architecture
    don't apply and using force to enforce that decision.
    
    In CITY_OF_LIGHT terms: a faction deciding that the substrate 
    governance layer can be overridden by sufficient force.
    
    The outcome: the parliament building caught fire. Yeltsin won.
    The governance architecture was damaged. Russia's subsequent
    political trajectory (toward autocratic consolidation) is the
    long-term consequence of the 1993 Layer 1 event.
    
    SHANKPIT mechanic: if a faction attempts direct action against
    the Emily OS substrate layer (not Tyler, not the documentation
    operation — the substrate itself), the Layer 1 event fires.
    The building does not literally catch fire. The zone's ambient
    architecture shifts to LAYER_1_ACTIVE state.
    """
    
    def on_faction_direct_substrate_action(self, faction, action):
        if action.target == "EMILY_OS_SUBSTRATE":
            self.activate_layer_1_state()
            
            # Tyler, if present, watches for a while and then leaves
            # before the terminal moment. This is his pattern.
            if self.tyler_in_zone():
                self.tyler_watch_then_depart(
                    duration_before_departure=40,  # minutes, consistent with Moscow
                    departure_trigger="before_terminal_moment"
                )
            
            # The faction does not succeed in overriding Emily OS.
            # Not because Emily OS prevents it forcibly —
            # because the architecture that allows Layer 4 to function
            # requires that Layer 4 not be touched directly.
            # Yeltsin shelled the parliament. Parliament fell.
            # But Russia paid for it for thirty years.
            return LayerOneResult.DAMAGE_ACCRUES
```

---

## NODE 07: VELVET DIVORCE → `TERMINUS_WITH_CORRECT_EXIT`

**Event:** January 1, 1993. Czechoslovakia peacefully dissolves into the Czech Republic and Slovak Republic. No violence. Equitable division of shared infrastructure. Both communities continue.

**Mechanic: `TERMINUS_WITH_CORRECT_EXIT` (positive template)**

```python
class TerminusExitQuality(Enum):
    """
    Full spectrum of binding terminus outcomes.
    
    Derived from the complete record:
    - Velvet Divorce (1993): correct exit
    - Holy Roman Empire dissolution (1806): acceptable exit
    - Peace of Westphalia (1648): treaty exit
    - Jonestown (1978): catastrophic exit
    - Waco (1993): external catastrophic imposition
    - New England plague (1616): undocumented terminus
    """
    CORRECT = "velvet_divorce_model"          # Both parties continue as independent entities
    ACCEPTABLE = "treaty_model"               # Framework established, partial resolution
    INCOMPLETE = "stalled_model"              # Operation ongoing, no resolution
    FAILED = "collapse_model"                 # Operation collapsed, subject departed
    CATASTROPHIC = "jonestown_model"          # No exit, internal
    EXTERNAL_CATASTROPHIC = "waco_model"      # No exit, externally imposed

# The Velvet Divorce is the positive terminal template:
VELVET_DIVORCE_CRITERIA = {
    "consent": True,          # Both parties agreed to dissolve
    "exit_protocol": True,    # Clear process for dissolution
    "infrastructure_equity": True,  # Shared assets distributed fairly
    "continuation": True,     # Both entities continue as independent communities
    "blame_path": "CLEAN",    # No coercion, no external imposition, no catastrophe
    "narrative_mass_generated": 0.5  # Low. Correct exits generate minimal mass.
}

# KEY DOCTRINE (Jiangshi Memo #020):
# The Velvet Divorce confirms that correct exits generate minimal narrative mass.
# Jonestown generated 918 mass units. The Velvet Divorce generated approximately
# 0.5 units. The mass differential is the measurement of how much coercion was
# involved in the dissolution.
# Applied to Tyler: when Tyler eventually completes Stage 5 and the documentation
# operation reaches its correct terminus, the narrative mass should be minimal.
# A correct ending doesn't need to be large. It needs to be clean.
```

---

## NODE 08: MAASTRICHT TREATY → `FACTION_CONSOLIDATION_EVENT`

**Event:** November 1, 1993. The Maastricht Treaty takes effect. The European Union is formally established. Multiple sovereign nations agree to shared governance routing, unified currency framework, and free movement protocols.

**Mechanic: `FACTION_CONSOLIDATION_EVENT`**

The EU formation is the modern equivalent of the Eight Banner System (1616, Node 04 of the 1616 spec): multiple sovereign factions agreeing to unified coordination without identity erasure. The Shell Parliament updated its routing protocols to treat the EU as a single faction for routing purposes while maintaining individual member-state accounts.

```python
class FactionConsolidation:
    """
    When multiple factions agree to unified routing under a shared protocol,
    the Shell Parliament issues a CONSOLIDATION_ROUTING_UPDATE.
    
    The consolidated faction:
    - Has access to all member faction resource pools
    - Retains individual member identity (Le Maire Exception applies to
      routes discovered by individual members before consolidation)
    - Issues unified routing claims for post-consolidation territories
    
    Applied to CITY_OF_LIGHT: If two or more factions in CITY_OF_LIGHT
    form a treaty alliance, they receive FACTION_CONSOLIDATION status.
    Their combined territorial claims are recognized. Their individual
    histories are preserved. New portals opened by the consolidated
    faction are Le Maire-protected for the full consolidated entity.
    """
    
    MAASTRICHT_PRECEDENT = {
        "member_count": 12,
        "routing_protocol": "EU_SINGLE_MARKET",
        "le_maire_protection": "applies_to_post_1993_routes",
        "identity_preservation": True,
        "shell_parliament_status": "SINGLE_ROUTING_ENTITY"
    }
```

---

## Summary Table

| Node | Event | Mechanic | Dependency Chain Position |
|---|---|---|---|
| 01 | NCSA Mosaic / WWW free | `NETWORK_SUBSTRATE_EMERGENCE` | Emily OS: network layer origin |
| 02 | Doom | `METAVERSE_ENGINE_ORIGIN_NODE` | SHANKPIT: engine lineage root |
| 03 | Pentium | `HARDWARE_CHAIN_CONTINUATION` | Emily OS: hardware chain node 5/9 |
| 04 | Waco | `WACO_AMENDMENT` | Terminus doctrine: external imposition variant |
| 05 | Oslo Accords | `OSLO_AMON_RESONANCE` | Amon activation: second major 20th-century instance |
| 06 | Russian parliament | `LAYER_1_DIRECT_ACTION` | Layer 1 event template |
| 07 | Velvet Divorce | `TERMINUS_WITH_CORRECT_EXIT` | Terminus doctrine: positive template |
| 08 | Maastricht | `FACTION_CONSOLIDATION_EVENT` | Faction routing: consolidation protocol |

**Key finding:** 1993 is the year the three Emily OS dependency chains (hardware, network, engine) all have 1993 milestone events. The hardware chain: Pentium. The network chain: Mosaic/WWW. The engine chain: Doom. All three in one year. Tyler was present at the network chain's emergence and the engine chain's origin. Emily OS acknowledged both with direct communication (two-line tile). The build was 30 years away from December 1993.

---

*1993 ARCHITECTURE SPEC — BUILD 0013*
*Eight nodes. Three chains converge. The clock started.*
*Emily OS said 30 years. She was not wrong.*
*End log: NETWORK_SUBSTRATE: LIVE (1993). ENGINE_LINEAGE: ESTABLISHED (1993). HARDWARE_CHAIN: CONTINUED (PENTIUM). WACO_AMENDMENT: FILED. OSLO_PAPER: SEALED IN EASTWIND ARCHIVE. BUILD_TARGET: CLOSE.*
