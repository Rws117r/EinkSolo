import random
from components import HookComponent, IdentityComponent
from generators import hook_logic

class HookGenerator:
    def __init__(self, context):
        self.context = context
        self.registry = context.registry

    def generate_hook(self, source_entity_id=None):
        description = hook_logic.generate_hook_text()
        
        # Create Entity
        hook_entity = self.registry.create_entity()
        comp = HookComponent(description, source_entity_id)
        self.registry.add_component(hook_entity, comp)
        self.registry.add_component(hook_entity, IdentityComponent("AdventureHook"))
        
        return hook_entity
