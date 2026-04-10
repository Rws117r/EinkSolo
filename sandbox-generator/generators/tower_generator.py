import random
from ecs import Registry
from components import (
    TowerComponent, IdentityComponent, ApprenticeComponent, 
    NameComponent, TowerLevelComponent, AlchemyComponent,
    SpecialtyComponent, BookComponent, ItemComponent, RelicComponent,
    TrapComponent, ContainerComponent, FurnitureComponent
)
from generators.wizard_generator import WizardGenerator
from generators import tower_logic
from generators.name_generators.dreamlandish_places import generate_place_name

class TowerGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_tower(self, name=None):
        if name is None:
            name = f"Tower of {generate_place_name()}"

        # 2) Number of levels
        above_count = tower_logic.ABOVEGROUND_LEVELS[tower_logic.roll_d12()]
        under_count = tower_logic.UNDERGROUND_LEVEL_CHANCE[tower_logic.roll_d12()]
        
        # 3) Connection
        connection = tower_logic.CONNECTION_TYPES[tower_logic.roll_d12()]

        # 4) Outside appearance
        material = tower_logic.MATERIALS[tower_logic.roll_d20()]
        shape = tower_logic.SHAPES[tower_logic.roll_d20()]
        
        details = []
        detail_rolls = random.randint(1, 3)
        for _ in range(detail_rolls):
            detail = tower_logic.DETAILS[tower_logic.roll_d20()]
            if detail != "Nothing" and detail not in details:
                details.append(detail)

        # Create Tower Entity
        # Resident Wizard (Level 9+)
        wizard_entity = self.context.wiz_gen.generate_wizard()
        wiz_spec = self.registry.get_component(wizard_entity, SpecialtyComponent).specialty
        
        # Alchemical Details (3 ingredients, 1 potion project)
        ingredients = [self.context.alchemy_gen.generate_ingredient() for _ in range(3)]
        potions = [self.context.alchemy_gen.generate_potion()]
        self.registry.add_component(wizard_entity, AlchemyComponent(ingredients, potions))

        # 3) Create Tower Entity
        tower = self.registry.create_entity()
        comp = TowerComponent(name, material, shape, connection, details, resident_id=wizard_entity.id)
        self.registry.add_component(tower, comp)
        self.registry.add_component(tower, NameComponent(name))
        self.registry.add_component(tower, IdentityComponent("Tower"))
        
        level_ids = []
        apprentice_ids = []

        # 7) Levels usage and appearances
        # Bottom level (if any)
        if under_count > 0:
            usage = tower_logic.USAGE_BOTTOM[tower_logic.roll_d20()]
            level_ids.append(self._add_level(tower.id, "Bottom", 0, usage, wiz_spec).id)
            
            # Underground levels
            for i in range(1, under_count + 1):
                usage = tower_logic.USAGE_UNDERGROUND[tower_logic.roll_d12()]
                level_ids.append(self._add_level(tower.id, "Underground", i, usage, wiz_spec).id)

        # Ground level
        usage = tower_logic.USAGE_GROUND[random.randint(1, 8)]
        level_ids.append(self._add_level(tower.id, "Ground", 0, usage, wiz_spec).id)

        # Aboveground levels
        for i in range(1, above_count + 1):
            usage = tower_logic.USAGE_ABOVEGROUND[tower_logic.roll_d12()]
            level_ids.append(self._add_level(tower.id, "Aboveground", i, usage, wiz_spec).id)

        # Top level
        usage = tower_logic.USAGE_TOP[tower_logic.roll_d20()]
        level_ids.append(self._add_level(tower.id, "Top", 0, usage, wiz_spec).id)

        # Update component with level IDs
        comp.level_ids = level_ids

        # Apprentice (25% chance, 1d6 level)
        if random.random() < 0.25:
            apprentice_level = random.randint(1, 6)
            apprentice = self.registry.create_entity()
            master_name = self.registry.get_component(wizard_entity, NameComponent).name
            app_name = f"Apprentice to {master_name}"
            self.registry.add_component(apprentice, NameComponent(app_name))
            self.registry.add_component(apprentice, IdentityComponent("Apprentice"))
            self.registry.add_component(apprentice, ApprenticeComponent(wizard_entity.id, apprentice_level))
            apprentice_ids.append(apprentice.id)

        # Update component with final linked IDs
        notable_ids = [wizard_entity.id] + apprentice_ids + level_ids
        
        # Legendary Books (75% chance)
        if random.random() < 0.75:
            num_books = random.randint(1, 2)
            for _ in range(num_books):
                book = self.context.book_gen.generate_book()
                notable_ids.append(book.id)

        comp.notable_ids = notable_ids

        return tower

    def _add_level(self, tower_id, level_type, index, usage, wiz_spec):
        # Use thematic data for better descriptions
        theme = tower_logic.get_theme_data(usage)
        spec_theme = tower_logic.SPECIALTY_THEMES.get(wiz_spec, {})
        
        # 1. Sensory Description
        sensory = random.choice(tower_logic.SENSORY_DETAILS)
        features = [f"**{usage}** ({sensory})."]
        
        # Merge theme objects with specialty bias (2 from theme, 1 from specialty)
        objs = random.sample(theme['objs'], k=min(2, len(theme['objs'])))
        if spec_theme and random.random() < 0.7:
            objs.append(random.choice(spec_theme['objs']))
            
        for obj in objs:
            # Prefer specialty details if available
            det_pool = spec_theme.get('dets', theme['dets'])
            det = random.choice(det_pool)
            features.append(f"**{obj}** ({det}).")
            
        # --- Specialized Content Integration ---
        usage_lower = usage.lower()
        if "library" in usage_lower or "archives" in usage_lower:
            book = self.context.book_gen.generate_book()
            book_comp = self.registry.get_component(book, BookComponent)
            features.append(f"Notable: **{book_comp.title}** ({book_comp.physical_detail}).")
        elif "laboratory" in usage_lower or "alchemylab" in usage_lower:
            ingred = self.context.alchemy_gen.generate_ingredient()
            features.append(f"Notable: **{ingred}** (sitting on a workbench).")
        elif "chapel" in usage_lower or "ritual" in usage_lower:
            relic = self.context.relic_gen.generate_relic()
            from components import RelicComponent
            relic_comp = self.registry.get_component(relic, RelicComponent)
            features.append(f"Notable: **{relic_comp.full_name}**.")
            
        # 4. Hazards & Dressing
        # Trap Chance (30% underground, 10% otherwise)
        trap_chance = 0.3 if level_type == "Underground" else 0.1
        if random.random() < trap_chance:
            trap_cat = "mechanical"
            if "magical" in " ".join(features).lower() or random.random() < 0.2:
                trap_cat = "magical"
            trap = self.context.trap_gen.generate_trap(trap_cat)
            from generators.trap_generator import TrapComponent
            trap_comp = self.registry.get_component(trap, TrapComponent)
            features.append(f"Hazard: **{trap_comp.trap_type} Trap** hidden in {trap_comp.concealment}.")

        # Containers (70% chance)
        if random.random() < 0.7:
            container_ent = self.context.dressing_gen.generate_container()
            # If multiple containers were returned (Numerous), just pick one for the text or summarize
            if isinstance(container_ent, list):
                c_comp = self.registry.get_component(container_ent[0], ContainerComponent)
                features.append(f"Storage: A collection of **{c_comp.description}s**.")
            else:
                c_comp = self.registry.get_component(container_ent, ContainerComponent)
                features.append(f"Storage: **{c_comp.description}** ({c_comp.special}).")
                
        # Unusual Furniture (20% chance)
        if random.random() < 0.2:
            furn = self.context.dressing_gen.generate_furniture()
            f_comp = self.registry.get_component(furn, FurnitureComponent)
            features.append(f"Oddity: An unusual **{f_comp.furniture_type}** ({f_comp.aspect}).")
            
        appearance = " ".join(features)
        
        # 2. Interactions
        interactions = []
        triggers = random.sample(theme['triggers'], k=min(2, len(theme['triggers'])))
        for trig in triggers:
            # Specialty biased results
            res_pool = spec_theme.get('results', tower_logic.INTERACTION_RESULTS)
            res = random.choice(res_pool)
            interactions.append(f"▶ **{trig}**: {res}.")
            
        equipment = "\n".join(interactions)
        
        level_comp = TowerLevelComponent(tower_id, level_type, index, usage, appearance, equipment)
        
        level_entity = self.registry.create_entity()
        self.registry.add_component(level_entity, level_comp)
        self.registry.add_component(level_entity, IdentityComponent("TowerLevel"))
        self.registry.add_component(level_entity, NameComponent(f"{level_type} Level ({usage})"))
        
        return level_entity
