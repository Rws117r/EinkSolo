import random
from ecs import Registry
from components import GemComponent, NameComponent, IdentityComponent
from generators import gem_logic

class GemGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_gem(self):
        """Generates a single gem entity with name and description."""
        # Roll on d100 table
        roll = random.randint(1, 100)
        gem_data = self._get_gem_data(roll)
        
        gem = self.registry.create_entity()
        self.registry.add_component(gem, GemComponent(gem_data["name"], gem_data["description"]))
        self.registry.add_component(gem, NameComponent(gem_data["name"]))
        self.registry.add_component(gem, IdentityComponent("Gem"))
        
        return gem

    def _get_gem_data(self, roll):
        for k, v in gem_logic.GEMS.items():
            if isinstance(k, tuple):
                if k[0] <= roll <= k[1]:
                    return v
            elif k == roll:
                return v
        return {"name": "Unidentified Stone", "description": "An unremarkable but possibly valuable stone."}
