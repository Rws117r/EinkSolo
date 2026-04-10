import random
from ecs import Registry
from components import RelicComponent, IdentityComponent, NameComponent, DeityComponent
from generators import relic_logic

class RelicGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_relic(self, deity_id=None):
        nature, detail = relic_logic.generate_relic_description()
        spell_level, spell_name = relic_logic.generate_relic_spell()
        
        # Source description
        source_name = ""
        if deity_id is not None:
            # Resolve ID to Entity
            deity_entity = self.registry.get_entity_by_id(deity_id)
            if deity_entity:
                deity = self.registry.get_component(deity_entity, DeityComponent)
                if deity:
                    source_name = f" of {deity.name}"
        
        full_name = f"{nature}{source_name} ({detail})"
        
        # Create Entity
        relic_entity = self.registry.create_entity()
        powers = f"Spell: {spell_name} (Level {spell_level})"
        history = f"Nature: {nature}. Detail: {detail}."
        comp = RelicComponent(full_name, powers, history)
        self.registry.add_component(relic_entity, comp)
        self.registry.add_component(relic_entity, NameComponent(full_name))
        self.registry.add_component(relic_entity, IdentityComponent("Relic"))
        
        return relic_entity
