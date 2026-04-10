# Hex Map Logic Tables

BIOMES = {
    "Starting": {
        (1, 4): "Grassland",
        (5, 6): "Forest",
        (7, 8): "Hills",
        (9, 9): "Marsh",
        (10, 10): "Mountains"
    },
    "Next": {
        (1, 5): "Same", # Special handling for "Same as previous"
        (6, 6): "Grassland",
        (7, 7): "Forest",
        (8, 8): "Hills",
        (9, 9): "Marsh",
        (10, 10): "Mountains"
    }
}

FEATURES = {
    (1, 3): "Landmark",
    (4, 4): "Settlement",
    (5, 5): "Lair",
    (6, 6): "Dungeon"
}

SETTLEMENT_TYPES = {
    1: "Hamlet",
    2: "Village",
    3: "City",
    4: "Castle",
    5: "Tower",
    6: "Abbey"
}

RELATIONSHIPS = {
    (2, 2): "Open war",
    (3, 5): "Hostility",
    (6, 8): "Indifference",
    (9, 11): "Peace/Trade",
    (12, 12): "Alliance"
}

EVENT_TIMING = {
    (1, 1): "Ended earlier",
    (2, 4): "Is happening now",
    (5, 6): "Will take place in the future"
}

EVENT_NATURE = {
    1: "Assassination",
    2: "Celebration",
    3: "Curse",
    4: "Holy quest",
    5: "Hostage situation",
    6: "Mysterious ally",
    7: "Negotiations with another faction",
    8: "New headquarters",
    9: "New leader",
    10: "Plague",
    11: "Treaty signed with another faction",
    12: "War"
}

# Hex Symbols (Informational/Metadata)
BIOME_SYMBOLS = {
    "Grassland": "Plain",
    "Forest": "Trees",
    "Hills": "Small Bumps",
    "Marsh": "Reeds",
    "Mountains": "Peaks"
}
