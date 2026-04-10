import random

# Table 4-3: Anglish Terrain Names 1 (General)
GENERAL_FIRST = {
    1: "Appen", 2: "Aptal", 3: "Aul", 4: "Aulden", 5: "Bal", 6: "Bala", 7: "Barel", 8: "Bell", 9: "Borel", 10: "Brid",
    11: "Brindle", 12: "Broken", 13: "Bul", 14: "Cat", 15: "Caul", 16: "Clay", 17: "Clear", 18: "Cloa", 19: "Clod", 20: "Copper",
    21: "Cowl", 22: "Cran", 23: "Crow", 24: "Cul", 25: "Down", 26: "Drof", 27: "Dun", 28: "Dus", 29: "El", 30: "Elder",
    31: "Fain", 32: "Fandel", 33: "Far", 34: "Fas", 35: "Feather", 36: "Fir", 37: "Gala", 38: "Gran", 39: "Grey", 40: "Grim",
    41: "Gryn", 42: "Guin", 43: "Gyr", 44: "Hall", 45: "Hul", 46: "Isel", 47: "Little", 48: "Mer", 49: "Mood", 50: "Moon",
    51: "Mor", 52: "Morel", 53: "Mur", 54: "Nes", 55: "Op", 56: "Os", 57: "Otter", 58: "Peat", 59: "Pont", 60: "Randel",
    61: "Red", 62: "Rindel", 63: "Roon", 64: "Rot", 65: "Skal", 66: "Soul", 67: "Spel", 68: "Stal", 69: "Stel", 70: "Still",
    71: "Sul", 72: "Tal", 73: "Tar", 74: "Three", 75: "Tor", 76: "Tour", 77: "Trey", 78: "Tri", 79: "Trill", 80: "Troi",
    81: "Usp", 82: "Ussel", 83: "Wart", 84: "Water", 85: "Watten", 86: "Weal", 87: "Weaver", 88: "Well", 89: "Wen", 90: "Wheat",
    91: "Wheel", 92: "Whet", 93: "Whistle", 94: "Win", 95: "Wind", 96: "Wittel", 97: "Wol", 98: "Wor", 99: "Wort", 100: "Wyr"
}

GENERAL_ENDING = {
    1: "bow", 2: "fork", 3: "fern", 4: "mold", 5: "weald", 6: "wold", 7: "wall", 8: "fell", 9: "mead", 10: "stone",
    11: "stoke", 12: "wood", 13: "weir", 14: "ward", 15: "rock", 16: "winter", 17: "fall", 18: "fen", 19: "falcon", 20: "gate",
    21: "kin", 22: "ken", 23: "spel", 24: "spar", 25: "spur", 26: "spear", 27: "sheaf", 28: "shear", 29: "shard", 30: "more",
    31: "moot", 32: "soon", 33: "wyn", 34: "wen", 35: "vine", 36: "ven", 37: "lock", 38: "fallow", 39: "fale", 40: "val",
    41: "fel", 42: "tree", 43: "wyth", 44: "beard", 45: "hearth", 46: "kettle", 47: "ket", 48: "mer", 49: "wyth", 50: "glif",
    51: "grif", 52: "gyle", 53: "farthing", 54: "ly", 55: "lind", 56: "wy", 57: "hallow", 58: "shale", 59: "wead", 60: "wess",
    61: "wys", 62: "been", 63: "beed", 64: "berry", 65: "bark", 66: "carp", 67: "cap", 68: "gar", 69: "garth", 70: "gery",
    71: "gri", 72: "tri", 73: "ry", 74: "ri", 75: "rith", 76: "reath", 77: "verin", 78: "sooth", 79: "soon", 80: "sood",
    81: "moor", 82: "mary", 83: "mery", 84: "kilber", 85: "bray", 86: "bri", 87: "bry", 88: "bred", 89: "bran", 90: "ring",
    91: "ringar", 92: "rangarth", 93: "zel", 94: "ish", 95: "shell", 96: "shal", 97: "shar", 98: "corem", 99: "carg", 100: "cairn"
}

# Table 4-4: Anglish Terrain Names 2 (Sinister)
SINISTER_FIRST = {
    1: "Auld", 2: "Axe", 3: "Bale", 4: "Bane", 5: "Beetle", 6: "Beorn", 7: "Bile", 8: "Black", 9: "Blister", 10: "Blood",
    11: "Bodkin", 12: "Brittle", 13: "Cairn", 14: "Catch", 15: "Caur", 16: "Chill", 17: "Cloak", 18: "Clutch", 19: "Cold", 20: "Cowl",
    21: "Dagger", 22: "Dank", 23: "Darken", 24: "Daur", 25: "Deaden", 26: "Deepen", 27: "Dire", 28: "Dirge", 29: "Dour", 30: "Dread",
    31: "Dripping", 32: "Drul", 33: "Dusk", 34: "Eel", 35: "Foul", 36: "Frost", 37: "Gall", 38: "Gnat", 39: "Graum", 40: "Grave",
    41: "Grey", 42: "Grim", 43: "Grin", 44: "Grit", 45: "Grot", 46: "Gul", 47: "Hist", 48: "Iorm", 49: "Ix", 50: "Lichen",
    51: "Loath", 52: "Loathe", 53: "Loom", 54: "Lorc", 55: "Lurk", 56: "Marg", 57: "Maul", 58: "Mawl", 59: "Mist", 60: "Mold",
    61: "Moon", 62: "Morth", 63: "Moul", 64: "Mourn", 65: "Mul", 66: "Mur", 67: "Murg", 68: "Murken", 69: "Murn", 70: "Nail",
    71: "Oozing", 72: "Pinch", 73: "Rack", 74: "Reck", 75: "Ruin", 76: "Rune", 77: "Scar", 78: "Shear", 79: "Shorn", 80: "Sibil",
    81: "Slaughter", 82: "Sleet", 83: "Spurn", 84: "Sword", 85: "Tangle", 86: "Tear", 87: "Thoal", 88: "Thorn", 89: "Toad", 90: "Usc",
    91: "Usk", 92: "Ux", 93: "Warn", 94: "Waspen", 95: "Witch", 96: "Wolf", 97: "Worm", 98: "Wrath", 99: "Wroth", 100: "Wyrm"
}

SINISTER_ENDING = {
    1: "brac", 2: "fork", 3: "fern", 4: "mold", 5: "weald", 6: "wold", 7: "wall", 8: "fell", 9: "mord", 10: "stone",
    11: "stoke", 12: "wood", 13: "weir", 14: "wode", 15: "rock", 16: "winter", 17: "fall", 18: "fen", 19: "grip", 20: "gate",
    21: "kane", 22: "ken", 23: "spel", 24: "pool", 25: "spur", 26: "spear", 27: "sheaf", 28: "shear", 29: "shard", 30: "more",
    31: "moot", 32: "soon", 33: "wyn", 34: "wen", 35: "vine", 36: "ven", 37: "lock", 38: "fallow", 39: "fale", 40: "val",
    41: "fel", 42: "tree", 43: "wyth", 44: "beard", 45: "heed", 46: "beetle", 47: "ket", 48: "keat", 49: "wyth", 50: "rune",
    51: "grif", 52: "gyle", 53: "foal", 54: "ly", 55: "lind", 56: "wy", 57: "hallow", 58: "shale", 59: "wead", 60: "wess",
    61: "wys", 62: "geld", 63: "bors", 64: "ber", 65: "bark", 66: "carp", 67: "cap", 68: "gar", 69: "garth", 70: "gery",
    71: "grat", 72: "tri", 73: "ry", 74: "ri", 75: "rith", 76: "reath", 77: "vorin", 78: "sooth", 79: "soon", 80: "sood",
    81: "moor", 82: "mary", 83: "mery", 84: "kilber", 85: "bray", 86: "bri", 87: "bry", 88: "bred", 89: "bran", 90: "ring",
    91: "ringar", 92: "garn", 93: "zel", 94: "gorm", 95: "shell", 96: "shal", 97: "shar", 98: "corm", 99: "carg", 100: "cairn"
}

# Table 4-5: Optional Endings
OPTIONAL_ENDINGS = {
    "Forest": ["coed", "coil", "combe", "copse", "dare", "firth", "forest", "goed", "graf", "grave", "greave", "grove", "holt", "thicket", "uold", "wald", "weald", "woad", "wold", "wood"],
    "Grassland": ["mead", "field", "wold", "weald", "lea", "plain", "pasture", "grass", "ley", "land", "fallow", "green"],
    "Hills": ["hill", "howe", "knoll", "tor", "fell", "downs", "barrow", "mount", "high", "rise", "crest", "ridge"],
    "Marsh": ["fell", "fen", "guaun", "gwaun", "mar", "marsh", "mear", "merg", "mersh", "mire", "mirsh", "morsh", "muir", "murc", "murg", "murk", "myre", "quag", "reed", "water"],
    "Mountains": ["cairn", "cliff", "crag", "fell", "graig", "hill", "howe", "knoll", "lyth", "mond", "mont", "peak", "pike", "ridge", "scar", "scarp", "scaur", "stone", "top", "tor"],
    "River": ["bourne", "brook", "creek", "dour", "flow", "lyn", "rith", "stream", "waith", "water"]
}

def generate_anglish_place(sinister=False, terrain_type=None, formula=1):
    """
    Generate an Anglish place name using provided formulas.
    formula 1: [First Part] + [Ending] (standard Table 4-3/4-4)
    formula 2: [First Part] + [Optional Ending from Table 4-5]
    formula 3: [Formula 1 Result] + [Optional Ending as separate word]
    """
    first_pool = SINISTER_FIRST if sinister else GENERAL_FIRST
    ending_pool = SINISTER_ENDING if sinister else GENERAL_ENDING
    
    roll_first = random.randint(1, 100)
    roll_ending = random.randint(1, 100)
    
    base_first = first_pool[roll_first]
    base_ending = ending_pool[roll_ending]
    
    if formula == 1:
        return f"{base_first}{base_ending}"
    
    if formula == 2:
        if not terrain_type or terrain_type not in OPTIONAL_ENDINGS:
            # Fallback to general if type missing
            terrain_type = random.choice(list(OPTIONAL_ENDINGS.keys()))
        opt_ending = random.choice(OPTIONAL_ENDINGS[terrain_type])
        return f"{base_first}{opt_ending}"
    
    if formula == 3:
        res = f"{base_first}{base_ending}"
        if not terrain_type or terrain_type not in OPTIONAL_ENDINGS:
            terrain_type = random.choice(list(OPTIONAL_ENDINGS.keys()))
        opt_word = random.choice(OPTIONAL_ENDINGS[terrain_type])
        return f"{res} {opt_word.capitalize()}"
    
    return f"{base_first}{base_ending}"
