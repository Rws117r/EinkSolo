import random

# 2) Number of levels
ABOVEGROUND_LEVELS = {
    1: 1, 2: 2, 3: 2, 4: 3, 5: 3, 6: 3, 7: 4, 8: 4, 9: 4, 10: 5, 11: 5, 12: 6
}

UNDERGROUND_LEVEL_CHANCE = {
    1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 1, 9: 2, 10: 2, 11: 3, 12: 3
}

# 3) Levels connection
CONNECTION_TYPES = {
    1: "Staircase", 2: "Staircase", 3: "Staircase",
    4: "Spiral staircase", 5: "Spiral staircase", 6: "Spiral staircase",
    7: "Ladder", 8: "Ladder",
    9: "Elevator", 10: "Elevator",
    11: "Magic elevator",
    12: "Teleportation portals"
}

# 4) Outside appearance
MATERIALS = {
    1: "Cobblestone", 2: "Cobblestone", 3: "Cobblestone", 4: "Cobblestone", 5: "Cobblestone",
    6: "Wood", 7: "Wood", 8: "Wood", 9: "Wood", 10: "Wood",
    11: "Bricks", 12: "Bricks", 13: "Bricks",
    14: "Sandstone", 15: "Sandstone", 16: "Sandstone",
    17: "Limestone", 18: "Limestone",
    19: "Marble",
    20: "Metal"
}

SHAPES = {
    1: "Square", 2: "Square", 3: "Square", 4: "Square", 5: "Square",
    6: "Round", 7: "Round", 8: "Round", 9: "Round", 10: "Round",
    11: "Conical", 12: "Conical", 13: "Conical",
    14: "Tilted", 15: "Tilted", 16: "Tilted",
    17: "Asymmetrical",
    18: "S-shaped",
    19: "Stacked",
    20: "Twisted"
}

DETAILS = {
    1: "Nothing", 2: "Nothing", 3: "Nothing", 4: "Nothing", 5: "Nothing",
    6: "Nothing", 7: "Nothing", 8: "Nothing", 9: "Nothing", 10: "Nothing",
    11: "Balcony",
    12: "Banners",
    13: "Battlements",
    14: "Climbing plants",
    15: "Flags",
    16: "Moldings",
    17: "Porch",
    18: "Stained glass",
    19: "Statues/Gargoyles",
    20: "Turrets"
}

# 5) Inside appearance
INSIDE_APPEARANCE = {
    1: "Colorful", 2: "Cozy", 3: "Dark", 4: "Dusty", 5: "Extravagant",
    6: "Luxurious", 7: "Moldy", 8: "Old fashioned", 9: "Stark", 10: "Well decorated"
}

# 6) Special equipment
SPECIAL_EQUIPMENT = {
    1: "Nothing", 2: "Nothing", 3: "Nothing", 4: "Nothing", 5: "Nothing",
    6: "Nothing", 7: "Nothing", 8: "Nothing", 9: "Nothing", 10: "Nothing",
    11: "Acoustic tube",
    12: "Alarm system",
    13: "Dumbwaiter",
    14: "Emergency ladder/stairs",
    15: "Garbage chute",
    16: "Oversized pet doors",
    17: "Pneumatic tubes",
    18: "Secret passage",
    19: "Slide",
    20: "Ventilation system"
}

# 7) Levels usage
USAGE_GROUND = {
    1: "Empty and dusty", 2: "Fortified room", 3: "Hallway", 4: "Reception desk",
    5: "Ruined room", 6: "Shop/Tavern", 7: "Trapped room", 8: "Unloading room"
}

USAGE_ABOVEGROUND = {
    1: "Abandoned/Cursed level", 2: "Archives", 3: "Armory", 4: "Bedroom(s)",
    5: "Kitchen and dining room", 6: "Laboratory", 7: "Library", 8: "Meeting room",
    9: "Museum", 10: "Music room/Art room", 11: "Office/Study", 12: "Storage room"
}

USAGE_UNDERGROUND = {
    1: "Abandoned/Cursed level", 2: "Alchemylab", 3: "Cellar", 4: "Chapel",
    5: "Forge", 6: "Menagerie", 7: "Mushroom cave", 8: "Prison",
    9: "Rituals room", 10: "Storage", 11: "Torture room", 12: "Wine cellar"
}

USAGE_TOP = {
    1: "Aviary", 2: "Beacon", 3: "Duel platform", 4: "Foghorn", 5: "Golden apple tree",
    6: "Greenhouse", 7: "High security prison", 8: "Landing platform", 9: "Lightning rod",
    10: "Lookout post", 11: "Magic searchlight", 12: "Monster nest", 13: "Observatory",
    14: "Panic room", 15: "Ruined/Overgrown", 16: "Siege engine", 17: "Throne room",
    18: "Treasure room", 19: "Weather station", 20: "Windmill"
}

USAGE_BOTTOM = {
    1: "Abyss", 2: "Ancient ruins", 3: "Arena", 4: "Boudoir", 5: "Creature mouth",
    6: "Excavation site", 7: "Flesh pit", 8: "Flooded pit", 9: "Gambling den",
    10: "Magic portal", 11: "Magic well", 12: "Mine", 13: "Oubliette",
    14: "Secret society headquarters", 15: "Tomb", 16: "Tunnel to a lair",
    17: "Tunnel to the center of the planet", 18: "Tunnel to the surface",
    19: "Vault", 20: "Well"
}

# --- SENSORY & DETAIL TABLES (FOR MODULE-STYLE DESCRIPTIONS) ---

SENSORY_DETAILS = [
    "heavy atmosphere", "stale air", "refreshing breeze", "deathly silence",
    "scent of ozone", "smell of old parchment", "damp chill", "low humming sound",
    "smell of sulfur", "warm and cozy", "dusty and oppressive", "vibrant energy"
]

FLAVOR_OBJECTS = [
    "Candelabra", "Heirlooms", "Rotted furniture", "Wall carvings", "Strange vials",
    "Cracked mirror", "Iron chest", "Rug", "Tapesty", "Writing desk",
    "Pile of bones", "Incense burner", "Stone statue", "Alchemy jar", "Book shelf"
]

OBJECT_DETAILS = [
    "glimmering", "broken", "vibrant", "shifting", "bloody", "marked with runes",
    "ancient", "functioning", "damaged", "covered in cobwebs", "expertly carved",
    "glowing faintly", "ominous", "well-preserved"
]

INTERACTION_TRIGGERS = [
    "Upon entering", "Searching the corners", "Examining the equipment",
    "Disturbing the dust", "Touching the walls", "Listening closely"
]

INTERACTION_RESULTS = [
    "Find 1d6 gold pieces", "Trigger a minor alarm", "Discover a secret compartment",
    "Nothing unusual is found", "Scent of blood fills the air", "Shadows seem to move",
    "Find a rusted key", "A draft of cold air blows in"
]

# --- SPECIALTY FLAVOR TABLES (BY WIZARD SCHOOL) ---

SPECIALTY_THEMES = {
    "Necromancy": {
        "objs": ["Pile of bones", "Skeletal hand", "Black candles", "Canopic jars"],
        "dets": ["grave-chilled", "smelling of rot", "stained with dried blood", "imbued with necromancy"],
        "results": ["Find a human tooth", "Shadows lash out at you", "Whispers of the dead fill the room"]
    },
    "Illusion": {
        "objs": ["Prismatic mirror", "Invisibility cloak fragment", "Curtain of shifting light", "Fake door"],
        "dets": ["shimmering", "unstable to the touch", "multicolored", "distorted"],
        "results": ["You realize the object isn't there", "Your reflection starts mocking you", "Space seems to warp"]
    },
    "Druid": {
        "objs": ["Overgrown ivy", "Wooden carving", "Twisted roots", "Herbal drying rack"],
        "dets": ["vibrant", "humming with life", "covered in moss", "smelling of damp earth"],
        "results": ["Small insects swarm to your light", "Plants grasp at your ankles", "A soft animal call echoes"]
    },
    "Cleric": {
        "objs": ["Holy symbol", "Incense burner", "Kneeling pad", "Vial of holy water"],
        "dets": ["consecrated", "shining with light", "meticulously cleaned", "peaceful"],
        "results": ["You feel a sense of divine calm", "A faint choir is heard", "The shadows retreat slightly"]
    },
    "Elemental magic (Fire)": {
        "objs": ["Ever-burning coals", "Heat-warped iron", "Ashen remains"],
        "dets": ["scorched", "magically heated", "emitting orange light"],
        "results": ["The air burns your lungs", "Small sparks follow your movements"]
    }
}

# Theme mapping: Usage -> [Objects, Details, Triggers]
USAGE_THEMES = {
    "Library": {
        "objs": ["Book shelf", "Reading desk", "Scroll rack", "Inkwell"],
        "dets": ["dusty", "smelling of old parchment", "crammed with leather spines", "expertly carved"],
        "triggers": ["Searching the scrolls", "Touching the oldest book", "Examining the inkwell"]
    },
    "Laboratory": {
        "objs": ["Strange vials", "Alchemy jar", "Incense burner", "Writing desk"],
        "dets": ["bubbling", "emitting a faint glow", "stained with various fluids", "functioning"],
        "triggers": ["Checking the experiments", "Disturbing the burner", "Testing a vial"]
    },
    "Dungeon/Prison": {
        "objs": ["Pile of bones", "Iron chest", "Rotted furniture", "Wall carvings"],
        "dets": ["bloody", "marked with runes", "damaged", "covered in cobwebs"],
        "triggers": ["Searching the bones", "Touching the walls", "Listening closely"]
    },
    "Bedroom(s)": {
        "objs": ["Canopy bed", "Wardrobe", "Rug", "Wash basin"],
        "dets": ["luxurious", "velvet-covered", "well-preserved", "ornate"],
        "triggers": ["Searching the bed", "Opening the wardrobe"]
    },
    "Archives/Library": {
        "objs": ["Scroll rack", "Inkwell", "Stacked ledgers", "Dusty bust"],
        "dets": ["crammed with parchment", "smelling of vinegar", "neatly organized", "partially burnt"],
        "triggers": ["Translating a passage", "Checking the index", "Disturbing a scroll"]
    },
    "Armory": {
        "objs": ["Weapon rack", "Shield display", "Armor stand", "Whetstone"],
        "dets": ["rusted", "brushed to a shine", "notched from battle", "of unusual design"],
        "triggers": ["Testing a blade", "Inspecting the armor", "Touching a shield"]
    },
    "Kitchen/Dining": {
        "objs": ["Long table", "Hearth", "Cast iron pot", "Spice cabinet"],
        "dets": ["greasy", "cold to the touch", "filled with strange herbs", "meticulously cleaned"],
        "triggers": ["Checking the pantry", "Stoking the embers", "Looking in the pot"]
    },
    "Chapel/Rituals": {
        "objs": ["Altar", "Stone icon", "Pew", "Incense burner"],
        "dets": ["consecrated", "desecrated", "stained with wax", "chilled by spirit presence"],
        "triggers": ["Kneeling to pray", "Touching the idol", "Chanting a phrase"]
    },
    "Forge/Laboratory": {
        "objs": ["Anvil", "Bellows", "Coal bin", "Vials"],
        "dets": ["soot-covered", "magically heated", "still glowing", "expertly crafted"],
        "triggers": ["Testing the heat", "Striking the anvil", "Checking the forge bellows"]
    }
}

def get_theme_data(usage):
    # Try to find a partial match (e.g. "Laboratory" in "Alchemylab")
    for key, data in USAGE_THEMES.items():
        if key.lower() in usage.lower():
            return data
    # Default fallback
    return {
        "objs": FLAVOR_OBJECTS,
        "dets": OBJECT_DETAILS,
        "triggers": INTERACTION_TRIGGERS
    }

def roll_d12(): return random.randint(1, 12)
def roll_d20(): return random.randint(1, 20)
def roll_d10(): return random.randint(1, 10)
