import random
from ecs import Registry
from components import MonarchComponent, IdentityComponent, NameComponent
from generators import monarch_logic
from generators.name_generators import angelic_names # Reuse for grand names

class MonarchGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_monarch(self):
        # 1) Base Title
        base_title = random.choice(list(monarch_logic.NOBLE_TITLES.keys()))
        data = monarch_logic.NOBLE_TITLES[base_title]
        
        # 2) Official Term & Address
        official_term = random.choice(data["Terms"])
        base_address = data["Address"]
        
        # 3) Gender & Name
        gender = random.choice(["Masculine", "Feminine"])
        prefix = "His" if gender == "Masculine" else "Her"
        
        # 4) Type
        m_type = "Ordinary"
        roll = random.randint(1, 100)
        if roll >= 95: m_type = "Wicked"
        elif roll >= 80: m_type = "Tyrant"
        
        # Use angelic names for that "High Fantasy" feel
        name = angelic_names.generate_angelic_name()
        
        # 5) Fantasy Mode of Address
        fantasy_address = monarch_logic.generate_mode_of_address(prefix, m_type)
        
        # Create Entity
        monarch_entity = self.registry.create_entity()
        comp = MonarchComponent(
            name, base_title, official_term, base_address, fantasy_address, gender, m_type
        )
        self.registry.add_component(monarch_entity, comp)
        self.registry.add_component(monarch_entity, NameComponent(name))
        self.registry.add_component(monarch_entity, IdentityComponent("Monarch"))
        
        return monarch_entity
