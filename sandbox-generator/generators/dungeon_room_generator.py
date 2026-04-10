import random
from ecs import Registry
from components import DungeonRoomComponent, NameComponent, IdentityComponent, AlchemyComponent
from generators import dungeon_logic

class DungeonRoomGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_room(self, theme=None, is_lair=False):
        # 1) Size
        size_roll = random.randint(1, 6)
        size_name, dim_range = self._get_size(size_roll)
        width = random.randint(dim_range[0], dim_range[1])
        height = random.randint(dim_range[0], dim_range[1])
        
        # 2) Content Type
        content_roll = random.randint(1, 6)
        treasure_roll = random.randint(1, 100)
        
        r_type = "Monsters"
        treasure_chance = 50
        
        if content_roll == 1:
            r_type = "Trap"
            treasure_chance = 25
        elif content_roll in [2, 3]:
            r_type = "Empty"
            treasure_chance = 15
        elif content_roll == 4:
            r_type = "Special"
            treasure_chance = 0 # Variable usually
        
        # 3) Detail
        detail = ""
        if r_type == "Trap":
            detail = dungeon_logic.roll_on_table(dungeon_logic.TRAPS_100)
        elif r_type == "Empty":
            detail = dungeon_logic.roll_on_table(dungeon_logic.EMPTY_ROOMS_100)
        elif r_type == "Special":
            detail = dungeon_logic.roll_on_table(dungeon_logic.SPECIAL_ROOMS_100)
            # Some specials have treasure or monsters built in
        
        # 4) Treasure roll
        has_treasure = treasure_roll <= treasure_chance
        
        # Create Entity
        entity = self.registry.create_entity()
        comp = DungeonRoomComponent(
            size=f"{size_name} ({width}x{height})",
            r_type=r_type,
            detail=detail,
            treasure_chance=treasure_chance if has_treasure else 0,
            is_lair=is_lair
        )
        self.registry.add_component(entity, comp)
        self.registry.add_component(entity, NameComponent(f"{r_type} Room: {detail[:20]}"))
        self.registry.add_component(entity, IdentityComponent("DungeonRoom"))
        
        # 5) Alchemical and Book Integration
        notable_ids = []
        if detail in ["Alchemy table", "Mislabeled potions", "Mutation room", "Medical office"]:
            # Dungeon labs are often chaotic or unstable
            num_ing = random.randint(1, 3)
            ingredients = [self.context.alchemy_gen.generate_ingredient() for _ in range(num_ing)]
            num_pot = random.randint(1, 2)
            potions = [self.context.alchemy_gen.generate_potion() for _ in range(num_pot)]
            self.registry.add_component(entity, AlchemyComponent(ingredients, potions))
            
        if detail in ["Furnished library", "Rotting library", "Ancient memories sphere"]:
            num_books = random.randint(1, 2)
            for _ in range(num_books):
                book = self.context.book_gen.generate_book()
                notable_ids.append(book.id)

        if detail == "Dungeon tavern":
            tavern = self.context.tavern_gen.generate_tavern(is_dungeon=True)
            notable_ids.append(tavern.id)

        if has_treasure:
            # Chance to find a gem if treasure is present
            if random.random() < 1.0: # TEMPORARY 100% for testing
                gem = self.context.gem_gen.generate_gem()
                notable_ids.append(gem.id)
                
        comp.notable_ids = notable_ids

        return entity

    def _get_size(self, roll):
        for k, v in dungeon_logic.ROOM_SIZES.items():
            if isinstance(k, tuple):
                if k[0] <= roll <= k[1]: return v
            elif k == roll: return v
        return ("Medium", (3, 6))
