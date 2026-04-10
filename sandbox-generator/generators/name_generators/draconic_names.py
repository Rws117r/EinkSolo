import random

DRACONIC_PART_1 = {
    1: "Abra", 2: "Acra", 3: "Adra", 4: "Adustra", 5: "Agru", 6: "Anca", 7: "Andra", 8: "Arag", 9: "Arco", 10: "Arra",
    11: "Arug", 12: "Atra", 13: "Augru", 14: "Aurul", 15: "Auzo", 16: "Bar", 17: "Bara", 18: "Baru", 19: "Beru", 20: "Bhakra",
    21: "Bia", 22: "Bra", 23: "Brado", 24: "Bragna", 25: "Bramna", 26: "Bramno", 27: "Cadra", 28: "Casco", 29: "Caxa", 30: "Chrala",
    31: "Chro", 32: "Crala", 33: "Glau", 34: "Gra", 35: "Grim", 36: "Grima", 37: "Haga", 38: "Har", 39: "Helio", 40: "Hra",
    41: "Huro", 42: "Iula", 43: "Iulca", 44: "Iura", 45: "Jalan", 46: "Jara", 47: "Jarzem", 48: "Jazra", 49: "Jurga", 50: "Kabra",
    51: "Karu", 52: "Kaxa", 53: "Keruxa", 54: "Krala", 55: "Kralka", 56: "Lazal", 57: "Lazu", 58: "Macra", 59: "Maja", 60: "Majuri",
    61: "Malacho", 62: "Malol", 63: "Maluca", 64: "Mar", 65: "Marmora", 66: "Maugra", 67: "Maul", 68: "Melkar", 69: "Moth", 70: "Moul",
    71: "Oba", 72: "Ouro", 73: "Phoro", 74: "Phoso", 75: "Phrixu", 76: "Pyra", 77: "Raghra", 78: "Ragi", 79: "Rau", 80: "Rhada",
    81: "Rhado", 82: "Rhagi", 83: "Rhodo", 84: "Salcru", 85: "Sar", 86: "Sarcu", 87: "Sarda", 88: "Sarga", 89: "Sarghu", 90: "Scarva",
    91: "Scorvo", 92: "Sulcru", 93: "Tzor", 94: "Zalar", 95: "Zalor", 96: "Zaxa", 97: "Zaxu", 98: "Zerul", 99: "Zor", 100: "Zorga"
}

DRACONIC_PART_2 = {
    1: "alax", 2: "alaz", 3: "az", 4: "aziol", 5: "azioth", 6: "barabax", 7: "barax", 8: "baraz", 9: "bazios", 10: "bazius",
    11: "borax", 12: "boraz", 13: "boros", 14: "bradax", 15: "bragul", 16: "calchax", 17: "cazius", 18: "cazrax", 19: "cordax", 20: "cordrax",
    21: "gormax", 22: "gormis", 23: "lagon", 24: "lagor", 25: "lagoros", 26: "lagul", 27: "lagulax", 28: "madz", 29: "magazar", 30: "magol",
    31: "magolg", 32: "malax", 33: "malgh", 34: "mandros", 35: "mangor", 36: "manthir", 37: "manthog", 38: "manthyr", 39: "matar", 40: "mataz",
    41: "matz", 42: "maug", 43: "maugh", 44: "mazar", 45: "molax", 46: "molmagar", 47: "molmagor", 48: "molmagoth", 49: "molmagrax", 50: "moltz",
    51: "nadral", 52: "nadranax", 53: "nadrax", 54: "nagoloth", 55: "nagul", 56: "nalath", 57: "nalux", 58: "neriax", 59: "nerigol", 60: "noloth",
    61: "phalax", 62: "phorax", 63: "phoros", 64: "phoroz", 65: "phylax", 66: "scar", 67: "scath", 68: "scolax", 69: "scos", 70: "varax",
    71: "varmaz", 72: "vorax", 73: "vorgul", 74: "vorm", 75: "vormis", 76: "vorung", 77: "xagol", 78: "xagor", 79: "xagul", 80: "xar",
    81: "xenor", 82: "xor", 83: "xoth", 84: "xus", 85: "zarax", 86: "zarazax", 87: "zaug", 88: "zaul", 89: "zax", 90: "zaz",
    91: "zebrax", 92: "zemal", 93: "zioth", 94: "zoaz", 95: "zorax", 96: "zracos", 97: "zragol", 98: "zrakar", 99: "zrakas", 100: "zrax"
}

def generate_draconic_name():
    part1 = DRACONIC_PART_1[random.randint(1, 100)]
    part2 = DRACONIC_PART_2[random.randint(1, 100)]
    
    # Handle the "or" options by picking one randomly
    if " or " in part1:
        part1 = random.choice(part1.split(" or "))
        
    return f"{part1}{part2}"
