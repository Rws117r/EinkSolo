import random
from . import alchemy_logic

class AlchemyGenerator:
    def __init__(self, registry):
        self.registry = registry

    def generate_ingredient(self):
        """Rolls on the Master Table for Alchemical Ingredients."""
        roll = alchemy_logic.roll_d100()
        
        if roll <= 20:
            return self._animal_part()
        elif roll <= 40:
            return self._person_part()
        elif roll <= 60:
            return self._plant_part()
        elif roll <= 80:
            return self._small_thing()
        else:
            return self._substance()

    def generate_effect(self, force_beneficial=False, force_curse=False):
        """Generates a random magical effect or curse."""
        if force_beneficial or (not force_curse and random.random() < 0.6): # 60% beneficial by default
            return random.choice(alchemy_logic.BENEFICIAL_EFFECTS)
        else:
            return random.choice(alchemy_logic.CURSES)

    def generate_potion(self):
        """Generates a liquid or powdered potion with a random effect."""
        effect = self.generate_effect()
        if random.random() < 0.8: # 80% liquid usually in fantasy
            return {
                "type": "liquid",
                "description": f"{self._liquid_potion()} that causes: {effect}"
            }
        else:
            return {
                "type": "powder",
                "description": f"{self._powdered_potion()} that causes: {effect}"
            }

    def _liquid_potion(self):
        idx = random.randint(0, len(alchemy_logic.LIQUID_POTIONS)-1)
        data = alchemy_logic.LIQUID_POTIONS[idx]
        return f"a {data['color'].lower()}, {data['consistency'].lower()} liquid that smells like {data['smell'].lower()} ({data['other'].lower()})"

    def _powdered_potion(self):
        idx = random.randint(0, len(alchemy_logic.POWDERED_POTIONS)-1)
        data = alchemy_logic.POWDERED_POTIONS[idx]
        return f"a {data['color'].lower()} powder that smells like {data['smell'].lower()} ({data['other'].lower()})"

    def _animal_part(self):
        pres = random.choice(alchemy_logic.ANIMAL_PRESERVATION)
        part = random.choice(alchemy_logic.ANIMAL_BODY_PARTS)
        monster = random.choice(alchemy_logic.TYPE_A_MONSTERS if random.random() < 0.5 else alchemy_logic.TYPE_B_MONSTERS)
        detail = random.choice(alchemy_logic.ANIMAL_OTHER_DETAILS)
        return f"{pres} {part} {monster} ({detail})"

    def _person_part(self):
        pres = random.choice(alchemy_logic.ANIMAL_PRESERVATION) # Uses same preservation list usually
        part = random.choice(alchemy_logic.PERSON_BODY_PARTS)
        person = random.choice(alchemy_logic.TYPE_P1_PERSON if random.random() < 0.5 else alchemy_logic.TYPE_P2_PERSON)
        detail = random.choice(alchemy_logic.ANIMAL_OTHER_DETAILS) # Detailed other for person too
        return f"{pres} {part} {person} ({detail})"

    def _plant_part(self):
        pres = random.choice(alchemy_logic.ANIMAL_PRESERVATION)
        plant = random.choice(alchemy_logic.PLANT_TYPES)
        detail = random.choice(alchemy_logic.PLANT_OTHER_DETAILS)
        return f"{pres} {plant} ({detail})"

    def _small_thing(self):
        pres = random.choice(alchemy_logic.SMALL_THING_PRESERVATION)
        thing = random.choice(alchemy_logic.SMALL_THING_TYPES)
        return f"{pres} {thing}"

    def _substance(self):
        form = random.choice(alchemy_logic.SUBSTANCE_FORMS)
        stype = random.choice(alchemy_logic.SUBSTANCE_TYPES)
        detail = random.choice(alchemy_logic.SUBSTANCE_OTHER)
        return f"{form} of {stype} ({detail})"
