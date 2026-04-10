import random
from ecs import Registry
from components import DungeonLevelComponent, IdentityComponent, NameComponent
from generators import dungeon_logic
from generators.dungeon_room_generator import DungeonRoomGenerator
from generators.name_generators.cthonic import generate_cthonic
from generators.name_generators.colossoponderous import generate_colossoponderous

class DungeonLevelGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context
        self.room_gen = DungeonRoomGenerator(context)

    def generate_level(self, area_id, depth):
        # 1) Factions (1-3)
        num_factions_roll = random.randint(1, 6)
        num_factions = 1 if num_factions_roll == 1 else (2 if num_factions_roll <= 4 else 3)
        
        factions = []
        for _ in range(num_factions):
            # Roll monster level per depth
            m_level = dungeon_logic.get_monster_level(depth, random.randint(1, 12))
            m_type = dungeon_logic.get_monster_from_level(m_level, random.randint(1, 10))
            factions.append({"type": m_type, "level": m_level})

        # 2) Wandering Monsters table
        wandering_table = self._generate_wandering_table(factions, depth)

        # 3) Rooms (2d20 + 10)
        num_rooms = random.randint(1, 20) + random.randint(1, 20) + 10
        room_ids = []
        for _ in range(num_rooms):
            room_entity = self.room_gen.generate_room()
            room_ids.append(room_entity.id)

        # 4) Faction Relationships
        # (Simplified: just store the faction list, UI/Logic can roll relationships if needed)

        # Create Entity
        entity = self.registry.create_entity()
        comp = DungeonLevelComponent(
            area_id=area_id,
            depth=depth,
            room_ids=room_ids,
            factions=factions,
            wandering_monsters=wandering_table
        )
        
        # Generate evocative name for the level
        if random.random() < 0.7:
            lname = f"{generate_cthonic()} (Level {depth})"
        else:
            lname = f"{generate_colossoponderous()} (Level {depth})"

        self.registry.add_component(entity, comp)
        self.registry.add_component(entity, NameComponent(lname))
        self.registry.add_component(entity, IdentityComponent("DungeonLevel"))

        return entity

    def _generate_wandering_table(self, factions, depth):
        # 1 faction: 1d4-in-6 chance
        # 2 factions: 1d3-in-6 each
        # 3 factions: 1d2-in-6 each
        table = [] # indices 1-6
        slots = [None] * 6
        
        if len(factions) == 1:
            chance = random.randint(1, 4)
            for i in range(chance): slots[i] = factions[0]["type"]
        elif len(factions) == 2:
            c1 = random.randint(1, 3)
            c2 = random.randint(1, 3)
            for i in range(c1): slots[i] = factions[0]["type"]
            for i in range(c1, min(6, c1+c2)): slots[i] = factions[1]["type"]
        else: # 3 factions
            c1 = random.randint(1, 2)
            c2 = random.randint(1, 2)
            c3 = random.randint(1, 2)
            for i in range(c1): slots[i] = factions[0]["type"]
            for i in range(c1, min(6, c1+c2)): slots[i] = factions[1]["type"]
            for i in range(c1+c2, min(6, c1+c2+c3)): slots[i] = factions[2]["type"]

        # Fill remaining slots
        for i in range(6):
            if slots[i] is None:
                # Roll on depth table
                m_level = dungeon_logic.get_monster_level(depth, random.randint(1, 12))
                slots[i] = dungeon_logic.get_monster_from_level(m_level, random.randint(1, 10))
        
        return slots
