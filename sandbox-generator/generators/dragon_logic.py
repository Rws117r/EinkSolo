import random

# 1) Description
NAMES = ["Arkos", "Dalum", "Enoch", "Franil", "Irken", "Myriad", "Numin", "Ragor", "Sarhin", "Tychos", "Xerius", "Zéphyr"]
ALIGNMENTS = {1: "Chaotic", 2: "Chaotic", 3: "Chaotic", 4: "Neutral", 5: "Neutral", 6: "Lawful"}
SIZES = {1: "Small", 2: "Small", 3: "Average", 4: "Average", 5: "Average", 6: "Average", 7: "Average", 8: "Huge"}
AGES = {1: "Baby", 2: "Young", 3: "Young", 4: "Adult", 5: "Adult", 6: "Adult", 7: "Adult", 8: "Adult", 9: "Adult", 10: "Old", 11: "Old", 12: "Ancient"}

# 2) Breath & Color
BREATH_TYPES = {
    1: ("Acid", "line"),
    2: ("Fire", "cone"),
    3: ("Ice", "cone"),
    4: ("Lightning", "line")
}

# Color mapping: (1-3, 4-5, 6)
COLORS = {
    "Acid": {1: "Green", 2: "Green", 3: "Green", 4: "Black", 5: "Black", 6: "Bronze"},
    "Fire": {1: "Red", 2: "Red", 3: "Red", 4: "Blue", 5: "Blue", 6: "Copper"}, # Assuming Copper for 6
    "Ice": {1: "White", 2: "White", 3: "White", 4: "Silver", 5: "Silver", 6: "Silver"},
    "Lightning": {1: "Yellow", 2: "Yellow", 3: "Yellow", 4: "Gray", 5: "Gray", 6: "Gold"}
}

COLOR_AC = {
    "Green": 18, "Red": 18, "White": 18, "Yellow": 18,
    "Black": 20, "Blue": 20, "Brown": 20, "Gray": 20,
    "Bronze": 22, "Copper": 22, "Silver": 22, "Gold": 22
}

# 3) Strength (1/6 chance)
STRENGTHS = {
    1: "Armor (+2 AC)", 2: "Boneplates (+1 AC)", 3: "Goodnose", 4: "Liesdetection",
    5: "Persuasive voice", 6: "Poisonous claws", 7: "Poisonous spines", 8: "Tailclub (+1d6 tail dmg)",
    9: "Twohearts", 10: "Underwater breathing"
}

# 4) Weakness (1/6 chance)
WEAKNESSES = {
    1: "Competitive mind", 2: "Cupidity", 3: "Curiosity", 4: "Flattery",
    5: "Hurtscale (-1 AC)", 6: "Perforated wings (-2 AC)", 7: "Pride", 8: "Remorse",
    9: "Sunlight", 10: "Too much self-confidence"
}

# 5) Favorite food
FAVORITE_FOOD = {
    1: "None", 2: "Adventurers", 3: "Cattle", 4: "Children",
    5: "Humans", 6: "Nobles", 7: "Other monsters", 8: "Rare animals"
}

# 6) Status
STATUS_WILDERNESS = {
    1: "Attacking someone", 2: "Carrying treasure", 3: "Flying", 4: "Hunted down",
    5: "Hunting", 6: "Making a deal", 7: "Protecting its territory", 8: "Returning to its lair",
    9: "Taking revenge", 10: "Terrorizing people"
}

STATUS_LAIR = {
    1: "Aggressive", 2: "Chained", 3: "Defensive", 4: "Enraged",
    5: "Hiding", 6: "Hurt", 7: "Neutral", 8: "Protecting its egg/baby",
    9: "Retired", 10: "Sleeping"
}

# 7) Stats Matrix
HP_MATRIX = {
    "Baby": {"Small": 3, "Average": 6, "Huge": 12},
    "Young": {"Small": 9, "Average": 18, "Huge": 36},
    "Adult": {"Small": 15, "Average": 30, "Huge": 60},
    "Old": {"Small": 21, "Average": 42, "Huge": 84},
    "Ancient": {"Small": 27, "Average": 54, "Huge": 108}
}

SAVING_THROWS = {1: 10, 2: 10, 3: 10, 4: 11, 5: 11, 6: 12} # Fighter level
MORALE = {1: 9, 2: 9, 3: 9, 4: 10, 5: 10, 6: 11}

# 8) Attacks
ATTACK_CLAW = {
    1: "1d4", 6: "1d4+1", 11: "1d6", 15: "1d6+1", 18: "1d8", 20: "2d8"
}
ATTACK_BITE = {
    1: "2d8", 6: "2d10", 11: "3d8", 15: "3d10", 18: "4d8", 20: "6d6"
}
ATTACK_TAIL = {
    1: "1d8", 6: "1d10", 11: "1d12", 15: "1d20", 18: "2d8", 20: "3d6"
}

# 9) Lair
LAIRS = {
    1: "Cave", 2: "Desecrated church", 3: "Giant nest", 4: "Giant tree", 5: "Mine",
    6: "Overgrown tower", 7: "Razed village", 8: "Ruined castle", 9: "Tumulus", 10: "Volcano"
}

# 10) Special Treasure (1/6 chance)
SPECIAL_TREASURE = {
    1: "Access to a special location", 2: "Ancient realm crown", 3: "Giant gem",
    4: "Lost art piece", 5: "Prisoner", 6: "Rare book", 7: "Renowned magic item",
    8: "Secret/Knowledge", 9: "Treasure map", 10: "Unique weapon"
}
