import random
from ecs import Registry
from components import CastleComponent, IdentityComponent, NameComponent
from generators import castle_logic
from generators.name_generators import anglish_places, anglish_masculine, anglish_feminine

class CastleGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_castle(self):
        # 1) Base Type & Unusual
        type_name = castle_logic._get_from_dict(castle_logic.CASTLE_TYPES, random.randint(1, 100))
        unusual = castle_logic._get_from_dict(castle_logic.UNUSUAL_CASTLES, random.randint(1, 100))
        
        # 2) Condition
        condition = random.choice(castle_logic.CASTLE_CONDITION)
        
        # 3) Keep
        keep = None
        if "no keep" not in type_name.lower():
            shape = castle_logic._get_from_dict(castle_logic.KEEP_SHAPES, random.randint(1, 6))
            levels = random.randint(1, 3) + 1
            def_feat = castle_logic._get_from_dict(castle_logic.DEFENSIVE_FEATURES, random.randint(1, 12))
            non_def_feat = castle_logic._get_from_dict(castle_logic.NON_DEFENSIVE_FEATURES, random.randint(1, 12))
            
            # Treasure & Supplies
            treasure = self._generate_treasure()
            supplies = f"{random.randint(1, 6) + random.randint(1, 6)} months"
            
            # Jails
            jails = f"{random.randint(1, 6) + random.randint(1, 6)} commoners, {random.randint(1, 3)} nobles"
            
            keep = {
                "shape": shape, "levels": levels, 
                "defensive": def_feat, "non_defensive": non_def_feat,
                "treasure": treasure, "supplies": supplies, "jails": jails
            }
            
        # 4) Defense
        def_count = random.randint(1, 4)
        defenses = []
        has_stone = False
        has_moat = False
        while len(defenses) < def_count:
            d = castle_logic._get_from_dict(castle_logic.EXTRA_DEFENSES, random.randint(1, 6))
            if d not in defenses:
                defenses.append(d)
                if "stone" in d.lower(): has_stone = True
                if "moat" in d.lower(): has_moat = True
        
        # Walls & Towers
        walls = None
        if has_stone:
            w_shape, t_count_str = castle_logic.ENCLOSURE_SHAPES[random.randint(1, 8)]
            if t_count_str == "1d3 + 3":
                t_count = random.randint(1, 3) + 3
            else:
                t_count = t_count_str
            t_shape = "Square" if random.randint(1, 5) <= 3 else ("Round" if random.randint(1, 5) <= 5 else "Polygonal")
            walls = {"shape": w_shape, "tower_count": t_count, "tower_shape": t_shape}
        
        # Gatehouse
        gatehouse = None
        if has_stone:
            gatehouse = castle_logic._get_from_dict(castle_logic.GATEHOUSE_CLOSURE, random.randint(1, 6))
            
        # Moat
        moat = None
        if has_moat:
            moat = castle_logic._get_from_dict(castle_logic.MOAT_ENCOUNTERS, random.randint(1, 8))
            
        # 5) Garrison
        total_fighters = sum(random.randint(1, 6) for _ in range(3)) * 10
        garrison = self._generate_garrison(total_fighters)
        
        # 6) Staff
        staff_count = random.randint(3, 8)
        people = []
        while len(people) < staff_count:
            p_tuple = castle_logic._get_from_dict(castle_logic.CASTLE_PEOPLE, random.randint(1, 100))
            # Generate a name for the person
            gender = random.choice(["M", "F"])
            if gender == "M":
                p_name = anglish_masculine.generate_anglish_masculine()
            else:
                p_name = anglish_feminine.generate_anglish_feminine()
            
            p_entry = (f"{p_name} ({p_tuple[0]})", p_tuple[1])
            if p_entry not in people:
                people.append(p_entry)
                
        # 7) Disposition
        disp_roll = random.randint(1, 6) + random.randint(1, 6)
        disposition = castle_logic._get_from_dict(castle_logic.DISPOSITION, disp_roll)
        
        # 8) Events (1 in 6)
        event = None
        if random.randint(1, 6) == 1:
            timing = random.choice(castle_logic.EVENT_TIMING)
            nature = random.choice(castle_logic.EVENT_NATURE)
            event = f"{nature} ({timing})"
            
        # Name
        base_name = anglish_places.generate_anglish_place()
        name = f"Castle {base_name}"
        
        # Create Entity
        castle_entity = self.registry.create_entity()
        comp = CastleComponent(
            name, type_name, unusual, condition, keep, 
            defenses, gatehouse, moat, garrison, people, 
            disposition, event
        )
        self.registry.add_component(castle_entity, comp)
        self.registry.add_component(castle_entity, NameComponent(name))
        self.registry.add_component(castle_entity, IdentityComponent("Castle"))
        
        return castle_entity

    def _generate_treasure(self):
        items = []
        if random.randint(1, 100) <= 50: items.append(f"{random.randint(1, 4)*10000} gp")
        if random.randint(1, 100) <= 50: items.append(f"{random.randint(1, 6)*5000} gp")
        if random.randint(1, 100) <= 25: items.append(f"{random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)} gems")
        if random.randint(1, 100) <= 25: items.append(f"{random.randint(1, 10)} jewelry pieces")
        if random.randint(1, 100) <= 15: items.append(f"4 magic items, {random.randint(1, 6)} scrolls")
        return items if items else ["Empty"]

    def _generate_garrison(self, total):
        # 10/10/10/40/10/10/10
        lord_level = 9 + (total // 60)
        return {
            "Total Fighters": total,
            "Lord": f"Level {lord_level} Fighter",
            "Lieutenant": f"Level {lord_level-2} Fighter",
            "Bodyguards": f"Six Level {lord_level-3} Fighters",
            "Distribution": {
                "Heavy Cavaliers": total // 10,
                "Medium Cavaliers (Spear)": total // 10,
                "Medium Cavaliers (Bow)": total // 10,
                "Footmen (Sword)": (total * 4) // 10,
                "Footmen (Polearm)": total // 10,
                "Footmen (Crossbow)": total // 10,
                "Footmen (Longbow)": total // 10
            }
        }
