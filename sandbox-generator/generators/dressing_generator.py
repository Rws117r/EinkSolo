import random
from ecs import Registry
from components import NameComponent, IdentityComponent, ContainerComponent, FurnitureComponent
from generators import dressing_logic

class DressingGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_container(self):
        cat_roll = dressing_logic.roll_d100()
        category = dressing_logic.get_from_table(dressing_logic.CONTAINER_TYPE_ROLL, cat_roll)
        
        entities = []
        
        if "Small" in category:
            entities.append(self._roll_small())
        elif "Large" in category:
            entities.append(self._roll_large())
        elif "Bizarre" in category:
            entities.append(self._roll_bizarre())
        elif "Numerous" in category:
            count = random.randint(3, 8)
            for _ in range(count):
                entities.append(self._roll_large())
                
        return entities[0] if len(entities) == 1 else entities

    def generate_furniture(self):
        item, aspect = dressing_logic.get_from_table(dressing_logic.FURNITURE_UNUSUAL, dressing_logic.roll_d100())
        ent = self.registry.create_entity()
        comp = FurnitureComponent(item, aspect)
        self.registry.add_component(ent, comp)
        self.registry.add_component(ent, IdentityComponent("Furniture"))
        self.registry.add_component(ent, NameComponent(item))
        return ent

    def _roll_small(self):
        item, feature = dressing_logic.get_from_table(dressing_logic.SMALL_CONTAINERS, dressing_logic.roll_d100())
        return self._create_container_ent("Small", item, feature)

    def _roll_large(self):
        item, feature = dressing_logic.get_from_table(dressing_logic.LARGE_CONTAINERS, dressing_logic.roll_d100())
        
        # Handle recursive rolls for Tub/Urn/Wardrobe
        if item == "Tub" or item == "Urn":
            # Just add extra features
            extra_f = dressing_logic.get_from_table(dressing_logic.LARGE_CONTAINERS, dressing_logic.roll_d100())[1]
            feature += f" AND {extra_f}"
        elif item == "Wardrobe":
            extra_f1 = dressing_logic.get_from_table(dressing_logic.LARGE_CONTAINERS, dressing_logic.roll_d100())[1]
            extra_f2 = dressing_logic.get_from_table(dressing_logic.LARGE_CONTAINERS, dressing_logic.roll_d100())[1]
            feature += f" AND {extra_f1} AND {extra_f2}"
            
        return self._create_container_ent("Large", item, feature)

    def _roll_bizarre(self):
        item = dressing_logic.get_from_table(dressing_logic.BIZARRE_CONTAINERS, dressing_logic.roll_d100())
        return self._create_container_ent("Bizarre", item)

    def _create_container_ent(self, cat, item, feature=None):
        ent = self.registry.create_entity()
        comp = ContainerComponent(cat, item, feature)
        self.registry.add_component(ent, comp)
        self.registry.add_component(ent, IdentityComponent("Container"))
        self.registry.add_component(ent, NameComponent(item))
        return ent
