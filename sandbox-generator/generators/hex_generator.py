import random
from ecs import Entity
from components import (
    HexComponent, FactionComponent, NameComponent, IdentityComponent,
    VillageComponent, CityComponent, HamletComponent, CastleComponent, TowerComponent, AbbeyComponent
)
from generators import hex_logic
from generators.village_generator import VillageGenerator
from generators.city_generator import CityGenerator
from generators.hamlet_generator import HamletGenerator
from generators.castle_generator import CastleGenerator
from generators.tower_generator import TowerGenerator
from generators.abbey_generator import AbbeyGenerator

from generators.generator_context import GeneratorContext
from generators.name_generators.anglish_places import generate_anglish_place

class HexGenerator:
    def __init__(self, registry):
        self.registry = registry
        self.hexes = {} # (q, r, s) -> entity_id
        
        # Initialize context (which holds all sub-generators)
        self.context = GeneratorContext(registry)
        
        # Pull generators from the shared context
        self.wiz_gen = self.context.wiz_gen
        self.vil_gen = self.context.vil_gen
        self.cit_gen = self.context.cit_gen
        self.ham_gen = self.context.ham_gen
        self.cas_gen = self.context.cas_gen
        self.tow_gen = self.context.tow_gen
        self.abbey_gen = self.context.abbey_gen
        self.land_gen = self.context.land_gen
        self.dun_gen = self.context.dun_gen
        self.lair_gen = self.context.lair_gen

    def generate_map(self, layers=2):
        """
        Generates a snowflake hex map. 
        Layer 0: Center
        Layer 1: 6 neighbors
        Layer 2: 12 outer hexes to complete the 19-hex snowflake.
        """
        # 1. Starting Hex (0,0,0)
        center_qrs = (0, 0, 0)
        center_biome = self._roll_biome(is_starting=True)
        center_id = self._create_hex(0, 0, 0, center_biome)
        self.hexes[center_qrs] = center_id

        # 2. First Layer (6 neighbors)
        neighbors = self._get_neighbors(0, 0, 0)
        for q, r, s in neighbors:
            biome = self._roll_biome(previous_biome=center_biome)
            hex_id = self._create_hex(q, r, s, biome)
            self.hexes[(q, r, s)] = hex_id

        # 3. Second Layer (Completing 19 hexes)
        layer1_qrs = list(self.hexes.keys())[1:7]
        for l1_qrs in layer1_qrs:
            l1_ent = self.registry.get_entity_by_id(self.hexes[l1_qrs])
            l1_biome = self.registry.get_component(l1_ent, HexComponent).biome
            l1_neighbors = self._get_neighbors(*l1_qrs)
            for q, r, s in l1_neighbors:
                if (q, r, s) not in self.hexes:
                    if max(abs(q), abs(r), abs(s)) <= layers:
                        biome = self._roll_biome(previous_biome=l1_biome)
                        hex_id = self._create_hex(q, r, s, biome)
                        self.hexes[(q, r, s)] = hex_id

        # 4. Assign Features
        self._assign_features()

        # 5. Process Factions and Domains
        self._process_factions()

    def _create_hex(self, q, r, s, biome):
        entity = self.registry.create_entity()
        self.registry.add_component(entity, HexComponent(q, r, s, biome))
        self.registry.add_component(entity, IdentityComponent("Hex"))
        
        # Terrain-based Anglish naming
        # Formula 2/3 uses terrain_type, Formula 1 is general
        formula = random.choice([1, 2, 2, 3]) 
        name = generate_anglish_place(terrain_type=biome, formula=formula)
        
        self.registry.add_component(entity, NameComponent(name))
        return entity.id

    def _get_neighbors(self, q, r, s):
        offsets = [
            (+1, -1, 0), (+1, 0, -1), (0, +1, -1),
            (-1, +1, 0), (-1, 0, +1), (0, -1, +1)
        ]
        return [(q + dq, r + dr, s + ds) for dq, dr, ds in offsets]

    def _roll_biome(self, is_starting=False, previous_biome=None):
        roll = random.randint(1, 10)
        table = hex_logic.BIOMES["Starting" if is_starting else "Next"]
        
        biome = "Grassland" # Default
        for (low, high), b in table.items():
            if low <= roll <= high:
                biome = b
                break
        
        if biome == "Same" and previous_biome:
            return previous_biome
        elif biome == "Same":
            return "Grassland"
        return biome

    def _assign_features(self):
        """Assign Landmarks, Settlements, Lairs, Dungeons."""
        for qrs, hex_id in self.hexes.items():
            entity = self.registry.get_entity_by_id(hex_id)
            comp = self.registry.get_component(entity, HexComponent)
            
            # center hex (0,0,0) is always a settlement (Village)
            if qrs == (0, 0, 0):
                vil = self.vil_gen.generate_village()
                comp.feature_id = vil.id
                continue
            
            # Second hex (the first neighbor rolled) is always a dungeon (by rule)
            if qrs == (1, -1, 0): 
                comp.feature_id = self.dun_gen.generate_new_area().id
                continue
            
            roll = random.randint(1, 6)
            feature_type = "Landmark"
            for (low, high), f in hex_logic.FEATURES.items():
                if low <= roll <= high:
                    feature_type = f
                    break
            
            if feature_type == "Settlement":
                sub_roll = random.randint(1, 6)
                if sub_roll <= 2: s_type = "Hamlet"
                elif sub_roll <= 4: s_type = "Village"
                elif sub_roll == 5: s_type = "City"
                else: # Other
                    other_roll = random.randint(1, 6)
                    if other_roll <= 3: s_type = "Castle"
                    elif other_roll <= 5: s_type = "Tower"
                    else: s_type = "Abbey"
                
                # Generate actual settlement entity and store its ID
                if s_type == "Hamlet": comp.feature_id = self.ham_gen.generate_hamlet().id
                elif s_type == "Village": comp.feature_id = self.vil_gen.generate_village().id
                elif s_type == "City": comp.feature_id = self.cit_gen.generate_city().id
                elif s_type == "Castle": comp.feature_id = self.cas_gen.generate_castle().id
                elif s_type == "Tower": comp.feature_id = self.tow_gen.generate_tower().id
                elif s_type == "Abbey": comp.feature_id = self.abbey_gen.generate_abbey().id
            elif feature_type == "Landmark":
                comp.feature_id = self.land_gen.generate_landmark().id
            elif feature_type == "Lair":
                comp.feature_id = self.lair_gen.generate_lair(comp.biome).id
            elif feature_type == "Dungeon":
                comp.feature_id = self.dun_gen.generate_new_area().id
            else:
                comp.feature_id = feature_type

    def _process_factions(self):
        """Assign territories and initialize diplomatic relations."""
        factions = [] # List of faction entity IDs
        
        # 1. Identify Hex-based Factions
        for qrs, hex_id in self.hexes.items():
            hex_ent = self.registry.get_entity_by_id(hex_id)
            h_comp = self.registry.get_component(hex_ent, HexComponent)
            f_id = h_comp.feature_id
            
            if not f_id or isinstance(f_id, str): continue
            
            # Check if this feature creates a faction
            feat_ent = self.registry.get_entity_by_id(f_id)
            if not feat_ent: continue
            
            creates_faction = False
            is_big = False
            base_name = "Faction"
            
            if self.registry.get_component(feat_ent, CityComponent):
                creates_faction = True
                is_big = True
                city_name = self.registry.get_component(feat_ent, NameComponent).name
                base_name = f"City State of {city_name}"
            elif self.registry.get_component(feat_ent, CastleComponent):
                creates_faction = True
                is_big = True
                castle_name = self.registry.get_component(feat_ent, NameComponent).name
                base_name = f"Barony of {castle_name}"
            elif self.registry.get_component(feat_ent, TowerComponent):
                creates_faction = True
                tower_name = self.registry.get_component(feat_ent, TowerComponent).name
                base_name = f"Sorcerous Enclave of {tower_name}"
            elif self.registry.get_component(feat_ent, AbbeyComponent):
                creates_faction = True
                abb_comp = self.registry.get_component(feat_ent, AbbeyComponent)
                base_name = f"Order of {abb_comp.name}"
            
            if creates_faction:
                # Create Faction Entity
                f_ent = self.registry.create_entity()
                self.registry.add_component(f_ent, FactionComponent(name=base_name, leader_id=f_id))
                self.registry.add_component(f_ent, IdentityComponent("Faction"))
                self.registry.add_component(f_ent, NameComponent(base_name))
                fac_id = f_ent.id
                factions.append(fac_id)
                
                # Assign initial hex
                h_comp.faction_id = fac_id
                fac_comp = self.registry.get_component(f_ent, FactionComponent)
                fac_comp.hex_ids.append(hex_id)
                
                # Expand domain
                if is_big:
                    neighbors = self._get_neighbors(*qrs)
                    for n_qrs in neighbors:
                        if n_qrs in self.hexes:
                            n_id = self.hexes[n_qrs]
                            n_hex = self.registry.get_entity_by_id(n_id)
                            nh_comp = self.registry.get_component(n_hex, HexComponent)
                            
                            if not nh_comp.faction_id:
                                nh_comp.faction_id = fac_id
                                fac_comp.hex_ids.append(n_id)
                
                # Wizard Enslavement (Tower)
                if self.registry.get_component(feat_ent, TowerComponent):
                    neighbors = self._get_neighbors(*qrs)
                    for n_qrs in neighbors:
                        if n_qrs in self.hexes:
                            if random.randint(1, 6) == 1: # 1-in-6 chance
                                n_id = self.hexes[n_qrs]
                                n_hex = self.registry.get_entity_by_id(n_id)
                                nh_comp = self.registry.get_component(n_hex, HexComponent)
                                if not nh_comp.faction_id:
                                    nh_comp.faction_id = fac_id
                                    fac_comp.hex_ids.append(n_id)

        # 2. Roll Relationships between neighboring factions
        for f1_id in factions:
            f1_ent = self.registry.get_entity_by_id(f1_id)
            f1_comp = self.registry.get_component(f1_ent, FactionComponent)
            
            for f2_id in factions:
                if f1_id == f2_id or f2_id in f1_comp.relationships: continue
                
                neighboring = False
                for h1_id in f1_comp.hex_ids:
                    h1_ent = self.registry.get_entity_by_id(h1_id)
                    h1_comp = self.registry.get_component(h1_ent, HexComponent)
                    h1_neighbors = self._get_neighbors(h1_comp.q, h1_comp.r, h1_comp.s)
                    for n_qrs in h1_neighbors:
                        if n_qrs in self.hexes:
                            n_hex = self.registry.get_entity_by_id(self.hexes[n_qrs])
                            nh_comp = self.registry.get_component(n_hex, HexComponent)
                            if nh_comp.faction_id == f2_id:
                                neighboring = True
                                break
                    if neighboring: break
                
                if neighboring:
                    roll = random.randint(1, 6) + random.randint(1, 6) # 2d6
                    rel = "Indifference"
                    for (low, high), r in hex_logic.RELATIONSHIPS.items():
                        if low <= roll <= high:
                            rel = r
                            break
                    f1_comp.relationships[f2_id] = rel
                    f2_ent = self.registry.get_entity_by_id(f2_id)
                    f2_comp = self.registry.get_component(f2_ent, FactionComponent)
                    f2_comp.relationships[f1_id] = rel

        # 3. Roll Events for each faction
        for f_id in factions:
            f_ent = self.registry.get_entity_by_id(f_id)
            f_comp = self.registry.get_component(f_ent, FactionComponent)
            if random.randint(1, 6) == 1:
                t_roll = random.randint(1, 6)
                n_roll = random.randint(1, 12)
                timing = next((t for (low, high), t in hex_logic.EVENT_TIMING.items() if low <= t_roll <= high), "Is happening now")
                nature = hex_logic.EVENT_NATURE[n_roll]
                f_comp.active_event = {"timing": timing, "nature": nature}

    def get_hex_at(self, q, r, s):
        return self.hexes.get((q, r, s))
