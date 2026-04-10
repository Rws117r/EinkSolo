import random
from generators import dungeon_logic

# Biome Encounter Table (p.10 equivalent)
# Values are lists of (category, d10_roll_range)
BIOME_ENCOUNTERS = {
    "Grassland": [
        ((1, 3), "Men"), 
        ((4, 5), "Animals"), 
        ((6, 7), "Humanoids"), 
        ((8, 9), "Undead"), 
        ((10, 10), "Rare")
    ],
    "Forest": [
        ((1, 2), "Men"), 
        ((3, 5), "Animals"), 
        ((6, 8), "Humanoids"), 
        ((9, 9), "Undead"), 
        ((10, 10), "Rare")
    ],
    "Hills": [
        ((1, 2), "Men"), 
        ((3, 4), "Animals"), 
        ((5, 8), "Humanoids"), 
        ((9, 9), "Undead"), 
        ((10, 10), "Rare")
    ],
    "Marsh": [
        ((1, 1), "Men"), 
        ((2, 4), "Animals"), 
        ((5, 7), "Humanoids"), 
        ((8, 10), "Undead")
    ],
    "Mountains": [
        ((1, 1), "Men"), 
        ((2, 3), "Animals"), 
        ((4, 7), "Humanoids"), 
        ((8, 8), "Undead"), 
        ((9, 10), "Rare")
    ]
}

CATEGORY_MAP = {
    "Men": [1, 2, 3],        # Map categories to dungeon_logic.MONSTER_TYPES levels
    "Animals": [1, 2],
    "Humanoids": [1, 2, 3, 4],
    "Undead": [1, 2, 3, 5],
    "Rare": [4, 5, 6]
}

def get_random_monster(biome):
    roll = random.randint(1, 10)
    category = "Animals" # Default
    for (low, high), cat in BIOME_ENCOUNTERS.get(biome, BIOME_ENCOUNTERS["Grassland"]):
        if low <= roll <= high:
            category = cat
            break
    
    # Pick a level from the category
    levels = CATEGORY_MAP.get(category, [1])
    level = random.choice(levels)
    
    # Pick a monster from that level in dungeon_logic
    monster = dungeon_logic.get_monster_from_level(level, random.randint(1, 10))
    return monster

def get_population_split(total):
    """
    Procedure: 1d6 * 10% outside.
    """
    outside_percent = random.randint(1, 6) * 10
    outside = int(total * (outside_percent / 100))
    inside = total - outside
    return inside, outside
