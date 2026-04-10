import random

# Table 10-4: Cthonic Single-Word Place Names
PART_1 = {
    1: "Aultra", 2: "Bholo", 3: "Cru", 4: "Ctho", 5: "Djee", 6: "Dora", 7: "Gha", 8: "Ghara", 9: "Gho", 10: "Ghu",
    11: "Goa", 12: "Gola", 13: "Golo", 14: "Gormo", 15: "Gotra", 16: "Groa", 17: "Grua", 18: "Gule", 19: "Gulo", 20: "Hulta",
    21: "Hultra", 22: "Hulu", 23: "Ie", 24: "Isma", 25: "Iu", 26: "Isy", 27: "Jala", 28: "Jeha", 29: "Jho", 30: "Jika",
    31: "Jila", 32: "Joca", 33: "Joco", 34: "Kho", 35: "Khulu", 36: "Kuo", 37: "Lhoo", 38: "Loa", 39: "Lua", 40: "Mhe",
    41: "Mhe", 42: "Mho", 43: "Moa", 44: "Nia", 45: "Nya", 46: "Oa", 47: "Obo", 48: "Ogo", 49: "Oo", 50: "Oolo",
    51: "Orbo", 52: "Orbo", 53: "Oro", 54: "Oro", 55: "Oru", 56: "Sara", 57: "Solio", 58: "Sota", 59: "Sua", 60: "Sula",
    61: "Suo", 62: "Sura", 63: "Suro", 64: "Suto", 65: "Sutro", 66: "Tche", 67: "Tcho", 68: "Thoa", 69: "Thumo", 70: "Thuo",
    71: "Tsara", 72: "Tsua", 73: "Tsulio", 74: "Tsutre", 75: "Tua", 76: "U", 77: "Ua", 78: "Ue", 79: "Ulio", 80: "Ulmo",
    81: "Urso", 82: "Ulo", 83: "Ultra", 84: "Ulu", 85: "Uo", 86: "Ura", 87: "Urmo", 88: "Usa", 89: "Voa", 90: "Ye",
    91: "Yeba", 92: "Yeha", 93: "Yesa", 94: "Yie", 95: "Yua", 96: "Yue", 97: "Yuo", 98: "Zolo", 99: "Zoro", 100: "Zula"
}

PART_2_POOL = [
    "babor", "balon", "baloth", "banthor", "bantua", "baraba", "bebor", "bhoa", "bhos", "bibor",
    "bol", "boros", "bothra", "buin", "chaga", "chagga", "chagge", "chna", "chne", "ctoros",
    "daghu", "dalon", "dawan", "doar", "doin", "doros", "doth", "dragu", "dranga", "drod",
    "droth", "duon", "duos", "garoc", "gatra", "gga", "ggar", "ggo", "ggoc", "ggon",
    "ghar", "ghara", "gharoc", "ghatra", "ghoa", "ghor", "ghra", "ghro", "ghru", "gna",
    "gnagg", "gnagor", "gnaros", "gnod", "gnor", "gnor", "gnorac", "gnoros", "gnoroth", "goa",
    "gon", "gonath", "gonor", "gonos", "gonoth", "gor", "gora", "graag", "gragu", "groa",
    "groth", "guna", "gunos", "kha", "khe", "lagna", "lhoar", "loar", "lochan", "lochar",
    "logg", "logos", "loroc", "loros", "lthe", "ltho", "lthoa", "lthoar", "lthu", "lze",
    "lzis", "lzol", "lzul", "mammon", "mamnor", "mamnos", "mannu", "marmor", "mbor", "mbora",
    "mboro", "mborod", "mbra", "memnon", "memnor", "mimi", "mnath", "mnid", "mnis", "mnor",
    "mnoro", "mnorod", "mnorog", "mnoros", "mnoroth", "mnos", "mnoth", "momnon", "mor", "mora",
    "mordua", "moria", "mormu", "mornu", "morthu", "morthua", "ndor", "ndur", "ngala", "ngua",
    "ngul", "ngula", "ngulos", "nid", "niss", "noa", "noroc", "nos", "ntanga", "ntar",
    "ntor", "ntoroth", "ntotha", "ntur", "nua", "phor", "pna", "poros", "pta", "ptamal",
    "pthoros", "ptoi", "ptomos", "ptor", "ptra", "sar", "satra", "satru", "shaba", "shatra",
    "sor", "sorbu", "soris", "ssanid", "tagoa", "talon", "tchagol", "tcho", "thar", "thoon",
    "tlan", "tloon", "toar", "togoa", "tor", "tsetse", "tsocho", "tsoro", "tua", "tuan",
    "tuond", "tuor", "tuoth", "valos", "vhe", "vhos", "vish", "voltos", "vor", "vorga",
    "voros", "voru", "zala", "zar", "zla", "zoar", "zolos", "zor", "zord", "zul"
]

# Table 10-5: Cthonic Two-Word or Hyphenated Place Names
TWO_WORD_FIRST = {
    1: "Amu", 2: "Anu", 3: "Az", 4: "Bhool", 5: "Bhu", 6: "Bna", 7: "Bual", 8: "Cho", 9: "Choon", 10: "Em",
    11: "Gheel", 12: "Ghola", 13: "Gholun", 14: "Ghul", 15: "Gomo", 16: "Gul", 17: "Hamu", 18: "Hoa", 19: "Hos", 20: "Hu",
    21: "Ia", 22: "Ioum", 23: "Ioun", 24: "Ish", 25: "Iss", 26: "Ith", 27: "Iul", 28: "Izu", 29: "Jaal", 30: "Jeel",
    31: "Jhara", 32: "Jhor", 33: "Jhul", 34: "Khar", 35: "Khoom", 36: "Khor", 37: "Khur", 38: "Kol", 39: "Ksho", 40: "Kur",
    41: "Lo", 42: "Lua", 43: "Mhat", 44: "Mho", 45: "Mhos", 46: "Mool", 47: "Moth", 48: "Mu", 49: "Mul", 50: "Na",
    51: "Nhul", 52: "Nool", 53: "Nua", 54: "Nul", 55: "Nuol", 56: "Nyam", 57: "Nyang", 58: "Nyangat", 59: "Oalm", 60: "Oba",
    61: "Ool", 62: "Oom", 63: "Oth", 64: "Pna", 65: "Pru", 66: "Prua", 67: "Sa", 68: "Shia", 69: "Shool", 70: "Shoon",
    71: "Shu", 72: "Shual", 73: "Sool", 74: "Sua", 75: "Sultu", 76: "Suol", 77: "Tsam", 78: "Tsool", 79: "Tsul", 80: "Ul",
    81: "Ulu", 82: "Usu", 83: "Yal", 84: "Yamun", 85: "Yas", 86: "Yash", 87: "Yat", 88: "Yeth", 89: "Yil", 90: "Yis",
    91: "Yol", 92: "Yool", 93: "Yoon", 94: "Yoth", 95: "Youm", 96: "Yual", 97: "Yus", 98: "Zo", 99: "Zoa", 100: "Zul"
}

TWO_WORD_SECOND = {
    1: "Anka", 2: "Athut", 3: "Atra", 4: "Atras", 5: "Atrua", 6: "Axun", 7: "Bat", 8: "Botar", 9: "Butar", 10: "Chalu",
    11: "Chargah", 12: "Chaxu", 13: "Chirai", 14: "Dakra", 15: "Garu", 16: "Gheel", 17: "Ghoa", 18: "Gohan", 19: "Gurah", 20: "Hataan",
    21: "Iltar", 22: "Jartha", 23: "Jatar", 24: "Kaja", 25: "Kajir", 26: "Kan", 27: "Kanang", 28: "Kantu", 29: "Karku", 30: "Karthai",
    31: "Keptis", 32: "Keptra", 33: "Khar", 34: "Khargai", 35: "Kharj", 36: "Khor", 37: "Kojo", 38: "Koptis", 39: "Koptra", 40: "Kual",
    41: "Kualga", 42: "Kuatha", 43: "Lesh", 44: "Lieng", 45: "Mahar", 46: "Mhar", 47: "Morai", 48: "Morath", 49: "Murai", 50: "Octa",
    51: "Otua", 52: "Pachoon", 53: "Pai", 54: "Pajan", 55: "Pang", 56: "Panool", 57: "Panu", 58: "Parai", 59: "Paraj", 60: "Patna",
    61: "Patra", 62: "Petra", 63: "Pira", 64: "Pirak", 65: "Pnai", 66: "Pyak", 67: "Shagu", 68: "Shai", 69: "Shala", 70: "Shantu",
    71: "Sutrapa", 72: "Talcha", 73: "Tang", 74: "Tarba", 75: "Targ", 76: "Targa", 77: "Tarka", 78: "Tarool", 79: "Tcha", 80: "Tcho",
    81: "Tchor", 82: "Thara", 83: "Thatra", 84: "Thoon", 85: "Tirah", 86: "Toag", 87: "Tothu", 88: "Tsa", 89: "Tsaaga", 90: "Tso",
    91: "Tulai", 92: "Ukatan", 93: "Ulcha", 94: "Ulkoi", 95: "Ultar", 96: "Yai", 97: "Yara", 98: "Yarai", 99: "Yarak", 100: "Yatan"
}

def generate_cthonic(structure=None):
    """
    Generate a Cthonic name.
    structure 1: Single-Word (e.g., Aultrabhos)
    structure 2: Two-Word or Hyphenated (e.g., Choon Chaxu)
    """
    if not structure:
        structure = random.choice([1, 2])
        
    if structure == 1:
        roll_1 = random.randint(1, 100)
        part_2 = random.choice(PART_2_POOL)
        return f"{PART_1[roll_1]}{part_2}"
    
    if structure == 2:
        roll_1 = random.randint(1, 100)
        roll_2 = random.randint(1, 100)
        word_1 = TWO_WORD_FIRST[roll_1]
        word_2 = TWO_WORD_SECOND[roll_2]
        
        # Randomly choose space or hyphen
        sep = " " if random.random() > 0.5 else "-"
        return f"{word_1}{sep}{word_2}"
    
    return "Unknown"
