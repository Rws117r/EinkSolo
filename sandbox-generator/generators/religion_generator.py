import random
from ecs import Registry
from components import DeityComponent, IdentityComponent, NameComponent, PantheonComponent
from generators import religion_logic
from generators.name_generators import angelic_names, draconic_names, dreamlandish_feminine, dreamlandish_masculine, dreamlandish_long

class ReligionGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_creator_deity(self, name=None):
        if name is None:
            name = religion_logic.generate_creator_name()
        
        stats = religion_logic.generate_creator_stats()
        desc = f"{stats['Description']} ({stats['Failure Myth']}). Method: {stats['Creation Method']}"
        
        entity = self.registry.create_entity()
        comp = DeityComponent(name, "Creator", ["All"], desc, stats["Status"])
        self.registry.add_component(entity, comp)
        self.registry.add_component(entity, NameComponent(name))
        self.registry.add_component(entity, IdentityComponent("Deity"))
        return entity

    def _apply_deity(self, name, role, areas, desc):
        entity = self.registry.create_entity()
        appearance = religion_logic.generate_appearance()
        full_desc = f"{desc} Appearance: {appearance}"
        
        comp = DeityComponent(name, role, areas, full_desc)
        self.registry.add_component(entity, comp)
        self.registry.add_component(entity, NameComponent(name))
        self.registry.add_component(entity, IdentityComponent("Deity"))
        return entity

    def generate_art_deity(self, name=None):
        if name is None: name = dreamlandish_long.generate()
        secondary = religion_logic._get_from_dict(religion_logic.ART_SECONDARIES, random.randint(1, 6))
        areas = ["Art", secondary] + [random.choice(religion_logic.DIVINE_AREAS) for _ in range(2)]
        return self._apply_deity(name, "Art", areas, f"Deity of Creativity. Focus: {secondary}")

    def generate_battle_deity(self, name=None):
        if name is None: name = draconic_names.generate_draconic_name()
        secondary = religion_logic._get_from_dict(religion_logic.BATTLE_SECONDARIES, random.randint(1, 100))
        areas = ["Battle", secondary] + [random.choice(religion_logic.DIVINE_AREAS) for _ in range(2)]
        return self._apply_deity(name, "Battle", areas, f"Deity of War. Focus: {secondary}")

    def generate_craft_deity(self, name=None):
        if name is None: name = dreamlandish_long.generate()
        secondary = religion_logic._get_from_dict(religion_logic.CRAFT_SECONDARIES, random.randint(1, 100))
        areas = ["Craft", secondary] + [random.choice(religion_logic.DIVINE_AREAS) for _ in range(2)]
        return self._apply_deity(name, "Craft", areas, f"Deity of Work. Focus: {secondary}")

    def generate_guardian_deity(self, name=None):
        if name is None: name = draconic_names.generate_draconic_name()
        secondary = religion_logic._get_from_dict(religion_logic.GUARDIAN_SECONDARIES, random.randint(1, 6))
        areas = ["Guardian", secondary] + [random.choice(religion_logic.DIVINE_AREAS) for _ in range(2)]
        return self._apply_deity(name, "Guardian", areas, f"Deity of Protection. Focus: {secondary}")

    def generate_healer_deity(self, name=None):
        if name is None: name = (dreamlandish_feminine.generate() if random.random() < 0.7 else angelic_names.generate_angelic_name())
        secondary = religion_logic._get_from_dict(religion_logic.HEALER_SECONDARIES, random.randint(1, 6))
        areas = ["Healing", secondary] + [random.choice(religion_logic.DIVINE_AREAS) for _ in range(2)]
        return self._apply_deity(name, "Healing", areas, f"Deity of Health. Focus: {secondary}")

    def generate_leader_deity(self, name=None):
        if name is None: name = angelic_names.generate_angelic_name()
        secondary = religion_logic._get_from_dict(religion_logic.LEADER_SECONDARIES, random.randint(1, 6))
        areas = ["Good Rulership", secondary] + [random.choice(religion_logic.DIVINE_AREAS) for _ in range(2)]
        return self._apply_deity(name, "Leadership", areas, f"Deity of Sovereignty. Focus: {secondary}")

    def generate_provider_deity(self, name=None):
        if name is None: name = (dreamlandish_masculine.generate() if random.random() < 0.5 else dreamlandish_feminine.generate())
        secondary = religion_logic._get_from_dict(religion_logic.PROVIDER_SECONDARIES, random.randint(1, 6))
        areas = ["Plenty", secondary] + [random.choice(religion_logic.DIVINE_AREAS) for _ in range(2)]
        return self._apply_deity(name, "Provider", areas, f"Deity of Sustenance. Focus: {secondary}")

    def generate_trickster_deity(self, name=None):
        if name is None: name = dreamlandish_long.generate()
        secondary = religion_logic._get_from_dict(religion_logic.TRICKSTER_SECONDARIES, religion_logic._roll_d20_odd())
        areas = ["Trickery", secondary] + [random.choice(religion_logic.DIVINE_AREAS) for _ in range(2)]
        return self._apply_deity(name, "Trickster", areas, f"Deity of Deception. Focus: {secondary}")

    def generate_complex_deity(self, name=None):
        if name is None: name = dreamlandish_long.generate()
        areas = random.sample(religion_logic.DIVINE_AREAS, 4)
        return self._apply_deity(name, "Complex", areas, "A deity of many varied and complex facets.")

    def generate_nature_deity(self, name=None):
        if name is None: name = (draconic_names.generate_draconic_name() if random.random() < 0.5 else dreamlandish_long.generate())
        areas = ["Nature"] + random.sample(religion_logic.NATURE_SUB_AREAS, 1) + random.sample(religion_logic.DIVINE_AREAS, 2)
        return self._apply_deity(name, "Nature", areas, "A deity of the wild and natural world.")

    def generate_judge_deity(self, name=None):
        if name is None: name = angelic_names.generate_angelic_name()
        stats = religion_logic.generate_judge_stats()
        authority = stats["Authority"]
        source = stats["Source"]
        areas = ["Law", random.choice(religion_logic.DIVINE_AREAS), random.choice(religion_logic.DIVINE_AREAS), random.choice(religion_logic.DIVINE_AREAS)]
        return self._apply_deity(name, "Judge", areas, f"Interpreter of Law. Authority: {authority}. Source: {source}")

    def generate_weather_deity(self, name=None):
        if name is None: name = draconic_names.generate_draconic_name()
        areas = [random.choice(religion_logic.WEATHER_AREAS)] + [random.choice(religion_logic.DIVINE_AREAS) for _ in range(3)]
        return self._apply_deity(name, "Weather", areas, "A deity of air, storm, and sky.")

    def generate_beneficence_deity(self, name=None):
        if name is None: name = angelic_names.generate_angelic_name()
        areas = ["Good", "Protection", "Community", "Healing"]
        random.shuffle(areas)
        return self._apply_deity(name, "Beneficence", areas[:4], "A deity of general goodness and protection.")

    def generate_trade_deity(self, name=None):
        if name is None: name = dreamlandish_masculine.generate()
        secondary = religion_logic._get_from_dict(religion_logic.TRADE_SECONDARIES, random.randint(1, 6))
        areas = ["Trade", secondary] + [random.choice(religion_logic.DIVINE_AREAS) for _ in range(2)]
        return self._apply_deity(name, "Trade", areas, f"Deity of Commerce. Focus: {secondary}")

    def generate_travel_deity(self, name=None):
        if name is None: name = dreamlandish_long.generate()
        secondary = religion_logic._get_from_dict(religion_logic.TRAVEL_SECONDARIES, random.randint(1, 6))
        myth = religion_logic._get_from_dict(religion_logic.TRAVEL_METHODS, random.randint(1, 6))
        areas = ["Travel", secondary] + [random.choice(religion_logic.DIVINE_AREAS) for _ in range(2)]
        return self._apply_deity(name, "Travel", areas, f"Deity of Journeys. {myth}")

    def generate_deity(self, name, role="Native", areas=None):
        if not areas:
            areas = random.sample(religion_logic.DIVINE_AREAS, 2)
        return self._apply_deity(name, role, areas, f"A {role} deity.")

    def generate_pantheon(self, culture_name, creator_entity_id=None):
        pattern_roll = random.randint(1, 4)
        deities = []
        lead_id = None
        pattern_name = f"Pattern {pattern_roll}"
        
        # Helper to generate native gods using various archetypes
        def get_native_archetype(i):
            archetype = random.choice([
                "Art", "Battle", "Craft", "Guardian", "Healer", "Leader", 
                "Provider", "Complex", "Trickster", "Nature", "Judge", 
                "Weather", "Beneficence", "Trade", "Travel"
            ])
            if archetype == "Art": return self.generate_art_deity()
            if archetype == "Battle": return self.generate_battle_deity()
            if archetype == "Craft": return self.generate_craft_deity()
            if archetype == "Guardian": return self.generate_guardian_deity()
            if archetype == "Healer": return self.generate_healer_deity()
            if archetype == "Leader": return self.generate_leader_deity()
            if archetype == "Provider": return self.generate_provider_deity()
            if archetype == "Trickster": return self.generate_trickster_deity()
            if archetype == "Nature": return self.generate_nature_deity()
            if archetype == "Judge": return self.generate_judge_deity()
            if archetype == "Weather": return self.generate_weather_deity()
            if archetype == "Beneficence": return self.generate_beneficence_deity()
            if archetype == "Trade": return self.generate_trade_deity()
            if archetype == "Travel": return self.generate_travel_deity()
            return self.generate_complex_deity()

        if pattern_roll == 1: # Single-Deity
            type_mono = religion_logic._get_from_dict(religion_logic.MONOTHEISM_TYPES, random.randint(1, 3))
            pattern_name += f" ({type_mono})"
            lead_roll = random.randint(1, 100)
            if lead_roll <= 20 and creator_entity_id:
                lead_id = creator_entity_id
            elif lead_roll <= 40:
                lead_id = self.generate_judge_deity(f"The Law-Giver of {culture_name}")
            elif lead_roll <= 60:
                lead_id = self.generate_complex_deity(f"The All-Face of {culture_name}")
            else:
                lead_id = get_native_archetype(0)
            deities.append(lead_id)
            
        elif pattern_roll == 2: # Creator + Law-Giver + Antagonist + 1d4+4 Native
            if creator_entity_id: deities.append(creator_entity_id)
            deities.append(self.generate_judge_deity("The Supreme Judge"))
            from generators.religion_generator import ReligionGenerator # Self reference check
            # generate_antagonist_deity? I need to implement it in this class
            def generate_antagonist(n):
                # Simple antagonist logic
                return self._apply_deity(n, "Antagonist", ["Evil", "Chaos"], "A dark force.")
            deities.append(generate_antagonist("The Adversary"))
            lead_id = deities[0]
            num_native = random.randint(1, 4) + 4
            for i in range(num_native):
                deities.append(get_native_archetype(i))
                
        elif pattern_roll == 3: # Creator + Leader + 2 Antagonists + 1d4+4 Native
            if creator_entity_id: deities.append(creator_entity_id)
            lead_id = self.generate_leader_deity("The High King of Gods")
            deities.append(lead_id)
            num_native = random.randint(1, 4) + 4
            for i in range(num_native):
                deities.append(get_native_archetype(i))

        else: # Pattern 4: Primordial
            lead_id = self._apply_deity("The Living Landmark", "Primordial", [random.choice(["Sun", "Moon", "Mountain", "Volcano"])], "A deity residing in the material plane.")
            deities.append(lead_id)
            num_native = random.randint(1, 4) + 4
            for i in range(num_native):
                deities.append(get_native_archetype(i))

        # Create Entity
        p_entity = self.registry.create_entity()
        comp = PantheonComponent(culture_name, pattern_name, lead_id, deities)
        self.registry.add_component(p_entity, comp)
        self.registry.add_component(p_entity, NameComponent(f"Pantheon of {culture_name}"))
        self.registry.add_component(p_entity, IdentityComponent("Pantheon"))
        return p_entity
