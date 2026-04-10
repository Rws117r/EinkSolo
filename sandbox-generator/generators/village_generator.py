import random
from ecs import Registry
from components import VillageComponent, IdentityComponent, NameComponent
from generators import village_logic, settlement_logic
from generators.name_generators import dreamlandish_places
from generators.tavern_generator import TavernGenerator
from generators.abbey_generator import AbbeyGenerator
from generators.guild_generator import GuildGenerator

class VillageGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_village(self):
        # 1) Size (1d6)
        roll_size = random.randint(1, 6)
        size_str, grade = village_logic.SIZES[roll_size]
        population = grade * 50

        # 2) Occupation(s)
        occupations = ["Farming", "Cattle breeding"]
        if random.randint(1, 6) == 1:
            occ_roll = random.randint(1, 6)
            occupations.append(village_logic.EXTRA_OCCUPATIONS[occ_roll])

        # notable entities
        notable_ids = []
        
        # 4) Points of Interest
        poi_ids = [] # legacy gen
        # General (Always at least one) - Let's generate a Tavern for most villages
        tavern_entity = self.context.tavern_gen.generate_tavern()
        notable_ids.append(tavern_entity.id)

        # Special (grade times)
        special_pois = []
        for _ in range(grade):
            poi_roll = random.randint(1, 20)
            poi_name = village_logic.SPECIAL_LOCATIONS[poi_roll]
            special_pois.append(poi_name)
            
            # If POI is a specific entity we have a generator for, use it
            if poi_name == "Church":
                abbey = self.context.abbey_gen.generate_abbey()
                notable_ids.append(abbey.id)
            elif poi_name == "Guildhouse":
                guild = self.context.guild_gen.generate_guild()
                notable_ids.append(guild.id)
            elif poi_name == "Wizard Tower":
                tw = self.context.tow_gen.generate_tower()
                notable_ids.append(tw.id)

        # 5) Defense (grade times)
        defenses = []
        for _ in range(grade):
            def_roll = random.randint(1, 8)
            def_name = village_logic.DEFENSES[def_roll]
            if def_name not in defenses:
                defenses.append(def_name)
        
        # Guards
        guards = (random.randint(1, 3) + 3) * grade

        # 6) Disposition (2d6)
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
                # Opposite
                opposites = {
                    "Attack on sight": "Enthusiastic",
                    "Hostile": "Welcoming",
                    "Welcoming": "Hostile",
                    "Enthusiastic": "Attack on sight"
                }
                ruler_disp = opposites.get(villager_disp, "Neutral")

        # 7) Notable NPCs (grade times)
        npcs = []
        for _ in range(grade):
            npc_roll = random.randint(1, 20)
            npcs.append(village_logic.NOTABLE_NPCS[npc_roll])

        # Ruler(s)
        ruler_roll = random.randint(1, 8)
        ruler = village_logic.RULERS[ruler_roll]

        # 8) Secret (1/6)
        secret = None
        if random.randint(1, 6) == 1:
            secret_roll = random.randint(1, 12)
            secret = village_logic.SECRETS[secret_roll]

        # 9) Event (1/6)
        event = None
        if random.randint(1, 6) == 1:
            timing_roll = random.randint(1, 6)
            timing = "Ended earlier" if timing_roll == 1 else "Is happening now" if timing_roll <= 4 else "Will take place in the future"
            nature_roll = random.randint(1, 12)
            event = {"timing": timing, "nature": village_logic.EVENTS[nature_roll]}

        if ruler == "Monarch":
            m = self.context.mon_gen.generate_monarch()
            notable_ids.append(m.id)

        # 10) Cultural Traits
        pride = self._roll_d100(settlement_logic.PRIDE_OF_TOWN)
        draft_animal = self._roll_d100(settlement_logic.DRAFT_ANIMALS)
        
        dress_who = self._roll_d100(settlement_logic.STRANGE_DRESS_WHO)
        dress_what = self._roll_d100(settlement_logic.STRANGE_DRESS_WHAT)
        strange_dress = f"{dress_who}: {dress_what}"
        
        odd_behavior = self._roll_d100(settlement_logic.ODD_BEHAVIOR)
        cultural_gravity = self._roll_d100(settlement_logic.CULTURAL_GRAVITY)

        # Create Entity
        entity = self.registry.create_entity()
        comp = VillageComponent(
            size_str, grade, population, occupations, poi_ids, special_pois,
            defenses, guards, villager_disp, ruler_disp, npcs, 
            ruler, pride, draft_animal, strange_dress, odd_behavior, cultural_gravity,
            notable_ids, secret, event
        )
        self.registry.add_component(entity, comp)

        # Name
        place_name = dreamlandish_places.generate_place_name()
        name = f"Village of {place_name}"
        self.registry.add_component(entity, NameComponent(name))
        self.registry.add_component(entity, IdentityComponent("Village"))

        return entity

    def _roll_d100(self, table):
        roll = random.randint(1, 100)
        keys = sorted(table.keys())
        for k in keys:
            if roll <= k:
                return table[k]
        return table[keys[-1]]

    def _get_disp(self, roll):
        keys = sorted(village_logic.DISPOSITIONS.keys())
        for k in keys:
            if roll <= k:
                return village_logic.DISPOSITIONS[k]
        return village_logic.DISPOSITIONS[keys[-1]]
