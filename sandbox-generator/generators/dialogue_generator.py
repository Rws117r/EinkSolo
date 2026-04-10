import random
from components import DialogueComponent, IdentityComponent
from generators import dialogue_logic

class DialogueGenerator:
    def __init__(self, context):
        self.context = context
        self.registry = context.registry

    def generate_dialogue(self, specialty=None):
        bark = dialogue_logic.get_dialogue(specialty)
        
        # We don't necessarily create a new entity for every dialogue string, 
        # but we can return the component to be added to an NPC.
        return DialogueComponent(bark)

    def apply_dialogue(self, entity, specialty=None):
        comp = self.generate_dialogue(specialty)
        self.registry.add_component(entity, comp)
        return comp
