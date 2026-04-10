import random
from ecs import Registry
from components import (
    LevelComponent, NameComponent, IdentityComponent, 
    SpecialtyComponent, AppearanceComponent, GoalComponent, 
    StaffComponent, GenderComponent
)
from generators.name_generators import (
    dreamlandish_masculine, 
    dreamlandish_feminine,
    dreamlandish_long
)

from generators.wizard_logic import (
    roll_dice, roll_2d6, roll_1d12, roll_1d4,
    get_wizard_level, get_wizard_specialty, get_robe_color,
    get_wizard_appearance, get_wizard_goal, get_wizard_staff
)

class WizardGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_wizard(self, name=None, gender=None, min_level=None):
        if gender is None:
            gender = random.choice(["Masculine", "Feminine"])
        
        lvl_roll = roll_2d6()
        level = get_wizard_level(lvl_roll)
        
        while level < (min_level or 0):
            lvl_roll = roll_2d6()
            level = get_wizard_level(lvl_roll)
        
        spec_roll = roll_1d12()
        specialty = get_wizard_specialty(spec_roll)
        
        app_roll = roll_1d12()
        appearance = get_wizard_appearance(app_roll, specialty)
        
        goal_roll = roll_1d12()
        goal = get_wizard_goal(goal_roll)
        
        mat, top, bot, shape, det = get_wizard_staff()
        signature_spell = self.context.spell_gen.generate_spell()
        
        wizard = self.registry.create_entity()
        
        self.registry.add_component(wizard, IdentityComponent("Wizard"))
        self.registry.add_component(wizard, LevelComponent(level))
        self.registry.add_component(wizard, SpecialtyComponent(specialty))
        self.registry.add_component(wizard, AppearanceComponent(appearance))
        self.registry.add_component(wizard, GoalComponent(goal))
        self.registry.add_component(wizard, StaffComponent(mat, top, bot, shape, det, signature_spell=signature_spell))
        self.registry.add_component(wizard, GenderComponent(gender))
        
        if not name:
            # Chance for long names, especially for high level (10-11)
            is_powerful = level >= 10
            long_name_chance = 0.5 if is_powerful else 0.1
            
            if random.random() < long_name_chance:
                name = dreamlandish_long.generate()
            elif gender == "Masculine":
                name = dreamlandish_masculine.generate()
            else:
                name = dreamlandish_feminine.generate()
            
        self.registry.add_component(wizard, NameComponent(name))
        self.context.dial_gen.apply_dialogue(wizard, "Wizard")
            
        print(f"Generated Wizard: {name} (Level {level})")
        print(f"  Gender: {gender}, Specialty: {specialty}")
        print(f"  Appearance: {appearance}")
        print(f"  Goal: {goal}")
        print(f"  Staff: {str(self.registry.get_component(wizard, StaffComponent))}")
        return wizard
