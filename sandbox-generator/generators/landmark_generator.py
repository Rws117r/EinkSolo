import random
from ecs import Entity
from components import LandmarkComponent, IdentityComponent, NameComponent
from generators import landmark_logic

class LandmarkGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_landmark(self):
        # 1. Type
        l_type = self._roll_on_table(landmark_logic.TYPES)
        
        # 2. Category
        if l_type == "Natural":
            cat_id = random.randint(1, 6)
            category = landmark_logic.NATURAL_CATEGORIES[cat_id]
            nature = landmark_logic.NATURAL[category][random.randint(1, 10)]
        elif l_type == "Artificial":
            cat_id = random.randint(1, 6)
            category = landmark_logic.ARTIFICIAL_CATEGORIES[cat_id]
            nature = landmark_logic.ARTIFICIAL[category][random.randint(1, 10)]
        else: # Magic
            cat_id = random.randint(1, 6)
            category = landmark_logic.MAGIC_CATEGORIES[cat_id]
            nature = landmark_logic.MAGIC[category][random.randint(1, 10)]
            
        # 3. Content & Treasure
        content_roll = random.randint(1, 6)
        content = self._roll_on_table(landmark_logic.CONTENT, roll=content_roll)
        
        detail = None
        treasure_chance = 0
        
        if content == "Hazard":
            treasure_chance = 25
            detail = landmark_logic.HAZARDS[random.randint(1, 20)]
        elif content == "Empty":
            treasure_chance = 15
            info = self._roll_on_table(landmark_logic.EMPTY_INFO, roll=random.randint(1, 20))
            method = landmark_logic.EMPTY_METHOD[random.randint(1, 6)]
            detail = f"{info} (Learned via: {method})"
        elif content == "Monsters":
            treasure_chance = 50
            detail = "Variable monsters present"
        elif content == "Special":
            treasure_chance = 0 # Variable/Manual in book
            spec_type = self._roll_on_table(landmark_logic.SPECIAL_GEN, roll=random.randint(1, 12))
            
            if spec_type == "Arbitrate a dispute":
                detail = f"Dispute: {landmark_logic.DISPUTES[random.randint(1, 6)]}"
            elif spec_type == "Prevent a threat":
                detail = f"Threat: {landmark_logic.THREATS[random.randint(1, 6)]}"
            elif spec_type == "Uncover a mystery":
                detail = f"Mystery: {landmark_logic.MYSTERIES[random.randint(1, 10)]}"
            elif spec_type == "NPC(s)/Monster(s) in need":
                detail = f"NPC Problem: {landmark_logic.NPC_PROBLEMS[random.randint(1, 10)]}"
            else:
                detail = spec_type

        notable_ids = []
        if treasure_chance > 0:
            if random.random() < 1.0: # TEMPORARY 100% for testing
                gem = self.context.gem_gen.generate_gem()
                notable_ids.append(gem.id)

        # Create Entity
        entity = self.registry.create_entity()
        comp = LandmarkComponent(l_type, category, nature, content, detail, treasure_chance)
        comp.notable_ids = notable_ids
        self.registry.add_component(entity, comp)
        self.registry.add_component(entity, NameComponent(nature))
        self.registry.add_component(entity, IdentityComponent("Landmark"))
        
        return entity

    def _roll_on_table(self, table, roll=None):
        if roll is None:
            roll = random.randint(1, max(k[1] if isinstance(k, tuple) else k for k in table.keys()))
        
        for k, v in table.items():
            if isinstance(k, tuple):
                if k[0] <= roll <= k[1]:
                    return v
            elif k == roll:
                return v
        return None
