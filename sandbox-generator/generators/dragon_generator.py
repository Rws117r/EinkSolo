import random
from ecs import Registry
from components import DragonComponent, IdentityComponent, NameComponent
from generators import dragon_logic
from generators.name_generators.draconic_names import generate_draconic_name

class DragonGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_dragon(self, in_lair=False):
        # 1) Description
        name = generate_draconic_name()
        alignment = dragon_logic.ALIGNMENTS[random.randint(1, 6)]
        size = dragon_logic.SIZES[random.randint(1, 8)]
        age = dragon_logic.AGES[random.randint(1, 12)]

        # 2) Breath & Color
        breath_type, _ = dragon_logic.BREATH_TYPES[random.randint(1, 4)]
        color = dragon_logic.COLORS[breath_type][random.randint(1, 6)]
        ac = dragon_logic.COLOR_AC.get(color, 18)

        # 3) Strength (1/6)
        strength = None
        if random.randint(1, 6) == 1:
            strength = dragon_logic.STRENGTHS[random.randint(1, 10)]
            # Apply AC modifiers from strength
            if strength == "Armor (+2 AC)": ac += 2
            elif strength == "Boneplates (+1 AC)": ac += 1

        # 4) Weakness (1/6)
        weakness = None
        if random.randint(1, 6) == 1:
            weakness = dragon_logic.WEAKNESSES[random.randint(1, 10)]
            # Apply AC modifiers from weakness
            if weakness == "Hurtscale (-1 AC)": ac -= 1
            elif weakness == "Perforated wings (-2 AC)": ac -= 2

        # 5) Food
        food = dragon_logic.FAVORITE_FOOD[random.randint(1, 8)]

        # 6) Status
        if in_lair:
            status = dragon_logic.STATUS_LAIR[random.randint(1, 10)]
        else:
            status = dragon_logic.STATUS_WILDERNESS[random.randint(1, 10)]

        # 7) Stats
        hp = dragon_logic.HP_MATRIX[age][size]
        saving_throw = dragon_logic.SAVING_THROWS[random.randint(1, 6)]
        morale = dragon_logic.MORALE[random.randint(1, 6)]
        if size == "Huge":
            morale += 1

        # 9) Lair
        lair = dragon_logic.LAIRS[random.randint(1, 10)]
        
        # 10) Special Treasure
        treasure = None
        if random.randint(1, 6) == 1:
            treasure = dragon_logic.SPECIAL_TREASURE[random.randint(1, 10)]

        # Create Entity
        dragon = self.registry.create_entity()
        comp = DragonComponent(
            name, alignment, size, age, breath_type, color, hp, ac,
            strength, weakness, food, status, saving_throw, morale, lair, treasure
        )
        self.registry.add_component(dragon, comp)
        self.registry.add_component(dragon, NameComponent(name))
        self.registry.add_component(dragon, IdentityComponent("Dragon"))

        return dragon
