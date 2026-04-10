import random
from ecs import Entity
from components import NameComponent, IdentityComponent, LairComponent
from generators import lair_logic

class LairGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_lair(self, biome):
        """
        Generates a monster lair based on the biome.
        """
        # 1. Determine monster type
        monster = lair_logic.get_random_monster(biome)
        
        # 2. Determine population (Randomized for variety, typically 'a few')
        total_count = random.randint(3, 15)
        inside, outside = lair_logic.get_population_split(total_count)
        
        # 3. Determine location relative to hex center (1-8)
        location = random.randint(1, 8)
        
        # 4. Create rooms (1-3 small rooms)
        room_ids = []
        num_rooms = random.randint(1, 3)
        for _ in range(num_rooms):
            room = self.context.room_gen.generate_room(is_lair=True)
            room_ids.append(room.id)
            
        # 5. Create Entity
        lair_entity = self.registry.create_entity()
        self.registry.add_component(lair_entity, NameComponent(f"Lair of {monster}"))
        self.registry.add_component(lair_entity, IdentityComponent("Lair"))
        self.registry.add_component(lair_entity, LairComponent(
            monster_type=monster,
            total_count=total_count,
            inside_count=inside,
            outside_count=outside,
            location_relative=location,
            room_ids=room_ids
        ))
        
        return lair_entity
