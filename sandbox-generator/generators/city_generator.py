import random
from ecs import Registry
from components import CityComponent, IdentityComponent, NameComponent
from generators import city_logic, settlement_logic
from generators.name_generators import dreamlandish_places
from generators.tavern_generator import TavernGenerator
from generators.abbey_generator import AbbeyGenerator
from generators.guild_generator import GuildGenerator

class CityGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_city(self):
        # 1) Size (1d6)
        roll_size = random.randint(1, 6)
        size_str, grade = city_logic.SIZES[roll_size]
        population = grade * 500

        # 2) Main occupations
        occupations = []
        for _ in range(grade):
            occ_roll = random.randint(1, 10)
            occ = city_logic.OCCUPATIONS[occ_roll]
            if occ not in occupations:
                occupations.append(occ)

        # 3) Characteristics
        characteristics = []
        for _ in range(2):
            char_roll = random.randint(1, 20)
            char = city_logic.CHARACTERISTICS[char_roll]
            if char != "Nothing" and char not in characteristics:
                characteristics.append(char)

        # 4) Appearance
        app_roll = random.randint(1, 20)
        appearance = city_logic.APPEARANCE[app_roll]
        if appearance == "Specific color scheme":
            color_roll = random.randint(1, 4)
            appearance = f"Color scheme: {city_logic.COLOR_SCHEMES[color_roll]}"

        # Notable Entities
        notable_ids = []
        
        # 5) Points of Interest (General)
        poi_counts = {}
        poi_types = ["blacksmiths", "cemeteries", "churches", "general stores", "markets", "stables", "taverns"]
        for pt in poi_types:
            count = random.randint(1, grade)
            poi_counts[pt] = count
            
            # For each Tavern or Church, generate a real entity
            if pt == "taverns":
                for _ in range(count):
                    t = self.context.tavern_gen.generate_tavern()
                    notable_ids.append(t.id)
            elif pt == "churches":
                for _ in range(count):
                    a = self.context.abbey_gen.generate_abbey()
                    notable_ids.append(a.id)

        # Special Locations
        special_pois = []
        for _ in range(grade):
            sp_roll = random.randint(1, 20)
            poi_name = city_logic.SPECIAL_LOCATIONS[sp_roll]
            special_pois.append(poi_name)
            
            # Map specific names to generators
            if poi_name == "Abbey":
                a = self.context.abbey_gen.generate_abbey()
                notable_ids.append(a.id)
            elif poi_name == "Guildhall":
                g = self.context.guild_gen.generate_guild()
                notable_ids.append(g.id)
            elif poi_name == "Wizard Tower":
                tw = self.context.tow_gen.generate_tower()
                notable_ids.append(tw.id)

        # 6) Buildings of Interest
        buildings = []
        for _ in range(grade * 3):
            b_type_roll = random.randint(1, 20)
            b_type = city_logic.BUILDING_TYPES[b_type_roll]
            
            sub_name = "Unknown"
            if b_type == "Housing":
                sub_roll = random.randint(1, 10)
                sub_name = city_logic.HOUSING_SUB[sub_roll]
                # Small chance to generate a House entity for detail
                if random.randint(1, 20) == 1:
                    h = self.context.house_gen.generate_house(sub_name if sub_name in ["Poor", "Common", "Rich", "Noble"] else None)
                    notable_ids.append(h.id)
            elif b_type == "Business":
                sub_roll = random.randint(1, 100)
                sub_name = city_logic.BUSINESS_SUB[sub_roll]
            elif b_type == "Official":
                sub_roll = random.randint(1, 100)
                sub_name = self._roll_d100(city_logic.OFFICIAL_SUB)
            elif b_type == "Religious":
                sub_roll = random.randint(1, 100)
                sub_name = self._roll_d100(city_logic.RELIGIOUS_SUB)
                if "Temple" in sub_name or "Shrine" in sub_name:
                    a = self.context.abbey_gen.generate_abbey()
                    notable_ids.append(a.id)
            elif b_type == "Public":
                sub_roll = random.randint(1, 100)
                sub_name = self._roll_d100(city_logic.PUBLIC_SUB)
            elif b_type == "Military":
                sub_roll = random.randint(1, 20)
                sub_name = city_logic.MILITARY_SUB[sub_roll]
            
            buildings.append({"type": b_type, "name": sub_name})

        # 7) Defense
        walled = random.randint(1, 2) == 1
        entrances = []
        entrance_defenses = "None"
        if walled:
            directions = ["North", "East", "South", "West"]
            random.shuffle(directions)
            for i in range(grade):
                entrances.append(directions[i])
            
            # Defense sub-roll for entrances
            def_roll = random.randint(1, 6)
            if def_roll <= 3: entrance_defenses = "Wooden doors"
            elif def_roll <= 5: entrance_defenses = "Portcullis"
            else: entrance_defenses = "Both (Wooden doors and Portcullis)"
        
        # Guards
        guards = (random.randint(1, 3) + 3) * 5 * grade
        
        # Supplies
        supplies = random.randint(1, 6) + random.randint(1, 6)

        # 8) People
        npcs = []
        for _ in range(grade):
            npc_roll = random.randint(1, 20)
            npcs.append(city_logic.NOTABLE_NPCS[npc_roll])
            
        ruler_roll = random.randint(1, 8)
        ruler = city_logic.RULERS[ruler_roll]

        # 9) Disposition
        villager_roll = random.randint(1, 6) + random.randint(1, 6)
        villager_disp = self._get_disp(villager_roll)
        
        # Ruler Disposition
        ruler_roll = random.randint(1, 6)
        if villager_disp == "Neutral":
            ruler_disp = "Hostile" if ruler_roll <= 3 else "Welcoming"
        else:
            if ruler_roll <= 4:
                ruler_disp = villager_disp
            else:
                opposites = {
                    "Attack on sight": "Enthusiastic",
                    "Hostile": "Welcoming",
                    "Welcoming": "Hostile",
                    "Enthusiastic": "Attack on sight"
                }
                ruler_disp = opposites.get(villager_disp, "Neutral")
        
        # Monarch Generator call? If the ruler is "Monarch"
        if ruler == "Monarch":
            m = self.context.mon_gen.generate_monarch()
            notable_ids.append(m.id)

        # 10) Events
        event = None
        if random.randint(1, 6) == 1:
            timing_roll = random.randint(1, 6)
            timing = "Ended earlier" if timing_roll == 1 else "Is happening now" if timing_roll <= 4 else "Will take place in the future"
            nature_roll = random.randint(1, 12)
            event = {"timing": timing, "nature": city_logic.EVENTS[nature_roll]}

        # 11) Cultural & Urban Expansion
        pride = self._roll_d100(settlement_logic.PRIDE_OF_TOWN)
        draft_animal = self._roll_d100(settlement_logic.DRAFT_ANIMALS)
        
        dress_who = self._roll_d100(settlement_logic.STRANGE_DRESS_WHO)
        dress_what = self._roll_d100(settlement_logic.STRANGE_DRESS_WHAT)
        strange_dress = f"{dress_who}: {dress_what}"
        
        odd_behavior = self._roll_d100(settlement_logic.ODD_BEHAVIOR)
        cultural_gravity = self._roll_d100(settlement_logic.CULTURAL_GRAVITY)
        
        interesting_street = self._roll_d100(city_logic.INTERESTING_STREETS)
        
        # Districts
        districts = []
        num_districts = random.randint(1, 4) + grade
        for _ in range(num_districts):
            d = self._roll_d100(city_logic.CITY_DISTRICTS)
            if d not in districts:
                districts.append(d)
        
        prison = self._roll_d100(city_logic.PRISONS)
        latest_news = self._roll_d100(city_logic.LATEST_NEWS)
        faction_war = self._roll_d100(city_logic.FACTION_WARS)
        cultural_change = self._roll_d100(city_logic.CULTURAL_CHANGES)

        # Create Entity
        entity = self.registry.create_entity()
        comp = CityComponent(
            size_str, grade, population, occupations, characteristics, 
            appearance, poi_counts, special_pois, buildings, 
            walled, entrances, entrance_defenses, guards, supplies, 
            villager_disp, ruler_disp, npcs, ruler,
            pride, draft_animal, strange_dress, odd_behavior,
            cultural_gravity, interesting_street, districts,
            prison, latest_news, faction_war, cultural_change,
            notable_ids, event
        )
        self.registry.add_component(entity, comp)

        # Name
        place_name = dreamlandish_places.generate_place_name()
        name = f"City of {place_name}"
        self.registry.add_component(entity, NameComponent(name))
        self.registry.add_component(entity, IdentityComponent("City"))

        return entity

    def _roll_d100(self, table):
        roll = random.randint(1, 100)
        keys = sorted(table.keys())
        for k in keys:
            if roll <= k:
                return table[k]
        return table[keys[-1]]

    def _get_disp(self, roll):
        from generators import village_logic
        keys = sorted(village_logic.DISPOSITIONS.keys())
        for k in keys:
            if roll <= k:
                return village_logic.DISPOSITIONS[k]
        return village_logic.DISPOSITIONS[keys[-1]]
