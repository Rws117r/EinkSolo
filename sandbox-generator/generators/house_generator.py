import random
from ecs import Registry
from components import HouseComponent, IdentityComponent, NameComponent
from generators import house_logic

class HouseGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_house(self, house_type=None):
        if house_type is None:
            house_type = random.choice(list(house_logic.HOUSE_TYPES.keys()))
        
        data = house_logic.HOUSE_TYPES[house_type]
        
        # Roll for Loot (1d6)
        roll = random.randint(1, 6)
        loot = data["loot_table"].get(roll, "Nothing")
        
        # Create Entity
        house = self.registry.create_entity()
        comp = HouseComponent(
            house_type,
            data["description"],
            data["levels"],
            data["rooms"],
            loot
        )
        self.registry.add_component(house, comp)
        
        # Simple name like "Merchant's House" or "A Peasant House"
        name = f"A {house_type} House"
        self.registry.add_component(house, NameComponent(name))
        self.registry.add_component(house, IdentityComponent("House"))
        
        return house
