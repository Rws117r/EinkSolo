import random

# --- 1) Cross Section ---

THEMES = {
    13: "Burnt",
    14: "Crystalline",
    15: "Demonic",
    16: "Flooded",
    17: "Fortified",
    18: "Fungal",
    19: "Haunted",
    20: "Vegetal"
}

THEME_DETAILS = {
    "Burnt": "Floor and walls are covered in ash; traces of explosion.",
    "Crystalline": "Crystals growing everywhere, translucent walls, high echo.",
    "Demonic": "Red glowing glyphs, cries of pain, chained prisoners.",
    "Flooded": "Deeper levels filled with water; others are damp.",
    "Fortified": "First levels used as a stronghold by humanoids.",
    "Fungal": "Overgrown with fungi.",
    "Haunted": "Sounds of chains, torches go out due to icy wind.",
    "Vegetal": "Floor and walls covered in plants; vegetation hangs from ceiling."
}

# --- 2) Factions and Monster Scaling ---

# Depth (I to VI) -> Dice Roll (1-12) -> Monster Level (1-6)
# Depth index 0 = I, 5 = VI
MONSTER_LEVEL_BY_DEPTH = [
    # I: 1-9 -> L1, 10-11 -> L2, 12 -> L3
    {range(1, 10): 1, range(10, 12): 2, range(12, 13): 3},
    # II: 1-3 -> L1, 4-9 -> L2, 10-11 -> L3, 12 -> L4
    {range(1, 4): 1, range(4, 10): 2, range(10, 12): 3, range(12, 13): 4},
    # III: 1 -> L1, 2-3 -> L2, 4-9 -> L3, 10-11 -> L4, 12 -> L5
    {range(1, 2): 1, range(2, 4): 2, range(4, 10): 3, range(10, 12): 4, range(12, 13): 5},
    # IV: 1 -> L2, 2-3 -> L3, 4-9 -> L4, 10-11 -> L5, 12 -> L6
    {range(1, 2): 2, range(2, 4): 3, range(4, 10): 4, range(10, 12): 5, range(12, 13): 6},
    # V: 1 -> L3, 2-3 -> L4, 4-9 -> L5, 10-12 -> L6
    {range(1, 2): 3, range(2, 4): 4, range(4, 10): 5, range(10, 13): 6},
    # VI: 1 -> L4, 2-3 -> L5, 4-12 -> L6
    {range(1, 2): 4, range(2, 4): 5, range(4, 13): 6}
]

MONSTER_TYPES = {
    1: ["Bandits", "Dwarves/Elves", "Giant centipedes", "Giant rats", "Goblins", "Kobolds", "Orcs", "Pixies", "Skeletons", "Stirges"],
    2: ["Berserkers", "Cultists", "Ghouls", "Giant spiders", "Gnolls", "Hobgoblins", "Lizard-men", "Troglodytes", "Wolves", "Zombies"],
    3: ["Bugbears", "Giant ants", "Giant frogs", "Giant lizards", "Harpies", "Moth-men", "Ochre jellies", "Ogres", "Wererats", "Wights"],
    4: ["Doppelgangers", "Gargoyles", "Ghasts", "Giant scorpions", "Giant snakes", "Giant wasps", "Mushroom-men", "Skinwalkers", "Werewolves", "Wraiths"],
    5: ["Cockatrices", "Manticores", "Medusae", "Minotaurs", "Mummies", "Rust monsters", "Satyrs", "Specters", "Trolls", "Wyverns"],
    6: ["Basilisks", "Black mages", "Chaotic lords", "Dragons", "Evil patriarchs", "Giants", "Gorgons", "Hydras", "Purple worms", "Vampires"]
}

FACTION_RELATIONSHIPS = {
    2: "Open war",
    (3, 5): "Hostility",
    (6, 8): "Indifference",
    (9, 11): "Peace/Trade",
    12: "Alliance"
}

# --- 3) Structure ---

ROOM_SIZES = {
    (1, 2): ("Small", (1, 3)), # dice range, offset+1
    (3, 5): ("Medium", (2, 4)),
    6: ("Large", (3, 6))
}

ROOM_SHAPES = {
    (1, 14): "Rectangle/Square",
    15: "Parallelogram",
    16: "Trapezium",
    17: "Pentagon",
    18: "Hexagon",
    19: "Octagon",
    20: "Oval/Circle"
}

DOOR_TYPES = {
    (1, 10): "Stuck door",
    (11, 15): "Locked wooden door",
    (16, 18): "Portcullis",
    19: "Locked metal door",
    20: "Magic door"
}

# --- 4) Detailed Content (100-item tables) ---

# We'll use a dictionary for the 100 items to allow easy lookup and sparse definitions if needed.
TRAPS_100 = {
    1: "Acid pool", 3: "Alarm", 5: "Banana peel", 7: "Blade", 9: "Cage",
    11: "Caltrops", 13: "Circular saw", 15: "Crossbow", 17: "Crushed glass", 19: "Crushing ceiling",
    21: "Crushing wall(s)", 23: "Dart throwers", 25: "Electric shock", 27: "Electrified ground", 29: "Elevator to another level",
    31: "Extreme temperature", 33: "Fills with sand", 35: "Fills with water", 37: "Flamethrowers", 39: "Flammable gas",
    41: "Flashing light", 43: "Gas (confusion, death, sleep)", 45: "Illusory floor", 47: "Landslide", 49: "Lasso",
    51: "Lava flow", 53: "Lava pool", 55: "Magic (casts a spell)", 57: "Mist dispenser", 59: "Piston",
    61: "Pit", 63: "Poisoned caltrops", 65: "Portcullis closing", 67: "Projectile wall (arrows, etc.)", 69: "Quicksands",
    71: "Ram", 73: "Rolling stone", 75: "Slippery floor", 77: "Spike pit", 79: "Spray (acid, smelly, sticky)",
    81: "Sticky ground", 83: "Stretched spiky branch", 85: "Taut rope", 87: "Trap door (pit)", 89: "Trap door (spike pit)",
    91: "Trap door (to a lower level)", 93: "Vacuum chamber", 95: "Violent airstream", 97: "Violent water stream", 99: "Wolf trap"
}
# Fill even numbers with same description for 1-100 logic (d100)
TRAPS_100.update({k+1: TRAPS_100[k] for k in range(1, 100, 2)})

EMPTY_ROOMS_100 = {
    1: "Abandoned guard post", 2: "Alchemy table", 3: "Alcoves", 4: "Aligned beds", 5: "Aligned benches",
    6: "Altar", 7: "Anatomical skeleton", 8: "Aquarium", 9: "Banquet table", 10: "Barrels",
    11: "Barricade", 12: "Bear skin", 13: "Bed", 14: "Bench", 15: "Bloody stains",
    16: "Broken trap", 17: "Carpet", 18: "Cells", 19: "Chained skeletons", 20: "Chains",
    21: "Charred remains", 22: "Corpse nailed to a wall", 23: "Crates", 24: "Cryogenic/Formaline tubes", 25: "Cushions",
    26: "Dance parquet", 27: "Dark area", 28: "Desk", 29: "Drums", 30: "Dummy door",
    31: "Empty chest", 32: "Excavation site", 33: "Extinguished campfire", 34: "Fireplace", 35: "Flooded zone",
    36: "Fog", 37: "Food reserve", 38: "Forge", 39: "Fountain", 40: "Frames on the walls",
    41: "Fresco", 42: "Furnished library", 43: "Garbage", 44: "Gargoyle", 45: "Gears in the walls",
    46: "Gong", 47: "Graffiti", 48: "Guano covered floor", 49: "Hammock", 50: "Hieroglyphics",
    51: "Idol", 52: "Iron maiden", 53: "Ivy", 54: "Latrines", 55: "Leaking water pipe",
    56: "Leftovers on a table", 57: "Mushroom culture", 58: "Oil covered floor", 59: "Organ", 60: "Oubliette",
    61: "Pedestal", 62: "Pentagram", 63: "Piano", 64: "Pile of ashes (smoking)", 65: "Pile of bones",
    66: "Pile of bricks", 67: "Pile of logs", 68: "Pile of skulls", 69: "Pillars", 70: "Pool",
    71: "Puddle of vomit", 72: "Puddles of blood", 73: "Religious symbols", 74: "Rotting corpse", 75: "Rotting library",
    76: "Rotting tapestries", 77: "Rubble", 78: "Sarcophagus", 79: "Shelf", 80: "Showcases",
    81: "Signs of combat", 82: "Sink", 83: "Slime", 84: "Smokehouse", 85: "Stained glass",
    86: "Statues", 87: "Summoning circle", 88: "Table and chairs", 89: "Throne", 90: "Tools",
    91: "Torture easel", 92: "Training dummies", 93: "Trophies", 94: "Urns", 95: "Wardrobe",
    96: "Waste", 97: "Weapons/Armor racks", 98: "Wine cellar", 99: "Wooden bathtub", 100: "Workbench"
}

SPECIAL_ROOMS_100 = {
    1: "Advanced technology", 2: "Amplified magic room", 3: "Ancient memories sphere", 4: "Animated furniture", 5: "Anti-magic room",
    6: "Armor disintegrating ray", 7: "Aviary", 8: "Body exchange", 9: "Boss monster", 10: "Bottomless pit",
    11: "Ceaseless wailing", 12: "Cleaning receptacle", 13: "Crying statues", 14: "Cursed room", 15: "Cursed treasure",
    16: "Demon trap", 17: "Demonic portal", 18: "Devouring coin", 19: "Divination basin", 20: "Divine altar",
    21: "Dungeon tavern", 22: "Duplicating machine", 23: "Emergency exit", 24: "Ethereal voices", 25: "Evil altar",
    26: "Fake treasure", 27: "Fear room", 28: "Flesh room", 29: "Flood lever", 30: "Floor is lava",
    31: "Food rot room", 32: "Freshly walled corridor", 33: "Gold statue", 34: "Golden apple tree", 35: "Greed room",
    36: "Hallucinogenic spores", 37: "Healing lava pool", 38: "Heart of the dungeon", 39: "High up item", 40: "Human outpost",
    41: "Hungry mouth", 42: "Illusory treasure", 43: "Interplanar portal", 44: "Invisible bridge", 45: "Key storage room",
    46: "Lava pit", 47: "Maddening mural", 48: "Magic berry bush", 49: "Magic forge", 50: "Magic fountain",
    51: "Magic pool", 52: "Magic stairs", 53: "Medical office", 54: "Merchant in a wall", 55: "Minecart",
    56: "Mirror of opposites", 57: "Mirror room", 58: "Mislabeled potions", 59: "Monster market", 60: "Moving statues",
    61: "Musical slabs", 62: "Mutation room", 63: "Neutral altar", 64: "No way back", 65: "Orb of transformation",
    66: "Parasitized monster", 67: "Party room", 68: "Peace room", 69: "Petrified adventurers", 70: "Powerful electromagnet",
    71: "Rabbit switch", 72: "Reverse gravity", 73: "Room out of time", 74: "Rotating cylinders", 75: "Rotating room",
    76: "Safe", 77: "Shrinking pedestal", 78: "Shrinking ray", 79: "Sleep inducing room", 80: "Slot machine",
    81: "Sphinx", 82: "Strange eggs", 83: "Structural treasure", 84: "Switch in a hole", 85: "Talking basin",
    86: "Talking skull", 87: "Talking statue", 88: "Tentacles room", 89: "Trampoline room", 90: "Translating device",
    91: "True intentions room", 92: "Truth room", 93: "Valuable monster (alive)", 94: "Valuable monster (part)", 95: "Vending machine",
    96: "Voices of the ancestors", 97: "Vortex", 98: "Water to wine machine", 99: "Wheel of fortune", 100: "Wish fountain"
}

# --- Helper Functions ---

def get_monster_level(depth_int, d12_roll):
    """
    depth_int: 1 to 6 (mapped to I-VI)
    d12_roll: 1 to 12
    """
    depth_map = MONSTER_LEVEL_BY_DEPTH[depth_int - 1]
    for r, level in depth_map.items():
        if d12_roll in r:
            return level
    return 1 # Fallback

def get_monster_from_level(level, d10_roll):
    """
    level: 1 to 6
    d10_roll: 1 to 10
    """
    return MONSTER_TYPES[level][d10_roll - 1]

def roll_on_table(table, dice_size=None):
    """
    Helper to roll on tables with range keys or single int keys.
    """
    if dice_size is None:
        # Determine max key
        max_k = 1
        for k in table.keys():
            if isinstance(k, tuple): max_k = max(max_k, k[1])
            elif isinstance(k, int): max_k = max(max_k, k)
        dice_size = max_k
        if dice_size < 1: dice_size = 20 # Fallback
    
    roll = random.randint(1, dice_size)
    for k, v in table.items():
        if isinstance(k, tuple):
            if k[0] <= roll <= k[1]: return v
        elif k == roll:
            return v
    return None
