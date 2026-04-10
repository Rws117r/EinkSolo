import random
from ecs import Registry
from components import ItemComponent, IdentityComponent, NameComponent
from generators import general_logic

class ItemGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_item(self):
        item_name = random.choice(general_logic.GENERAL_ITEMS)
        
        # Create Entity
        item_entity = self.registry.create_entity()
        comp = ItemComponent(item_name)
        self.registry.add_component(item_entity, comp)
        self.registry.add_component(item_entity, NameComponent(item_name))
        self.registry.add_component(item_entity, IdentityComponent("Item"))
        
        return item_entity
