import random

# Table 2-2: Legendary Book
LEGENDARY_BOOK_PARTS = {
    2: ("Y", "ldrashic", "Fragments"),
    4: ("O", "ldranic", "Libram"),
    6: ("Iu", "ldrunic", "Tome"),
    8: ("Io", "xamic", "Grimoire"),
    10: ("Yo", "zelic", "Scrolls"),
    12: ("U", "mnic", "Remnants"),
    14: ("Rhe", "ltic", "Inscriptions"),
    16: ("Ra", "rothic", "Carvings"),
    18: ("Gno", "ptic", "Pictograms"),
    20: ("Ghe", "drashic", "Manuscript"),
    22: ("Su", "lmamite", "Texts"),
    24: ("Sa", "shumite", "Mysteries"),
    26: ("Tso", "shemic", "Plays"),
    28: ("Sua", "lshemic", "Sagas"),
    30: ("Tu", "dharthic", "Epics"),
    32: ("Ia", "mbothic", "Cyphers"),
    34: ("Bu", "lothic", "Codex"),
    36: ("Boa", "xitan", "Epitaphs"),
    38: ("Pa", "ssari", "Records"),
    40: ("Vo", "racid", "Engravings"),
    42: ("Qe", "hric", "Tome"),
    44: ("Xa", "jundha", "Grimoire"),
    46: ("Xe", "jjoan", "Scrolls"),
    48: ("Gho", "sgholtic", "Tablets"),
    50: ("Ku", "gholtic", "Inscriptions"),
    52: ("Tsa", "ngaelic", "Carvings"),
    54: ("Tse", "ndarthic", "Pictograms"),
    56: ("Ye", "rhennian", "Manuscript"),
    58: ("Yhe", "boltic", "Texts"),
    60: ("Aba", "bhaltic", "Mysteries"),
    62: ("Dia", "parune", "Plays"),
    64: ("Luo", "pharsic", "Incantations"),
    66: ("Lue", "noptic", "Epics"),
    68: ("Yue", "rmadite", "Cyphers"),
    70: ("Mne", "lbhite", "Codex"),
    72: ("Pno", "habitic", "Epitaphs"),
    74: ("Pna", "hmish", "Records"),
    76: ("Kwa", "hmite", "Engravings"),
    78: ("Kwe", "hultanic", "Grimoire"),
    80: ("Ue", "holtanic", "Scrolls"),
    81: ("Uo", "chastic", "Codex"),
    82: ("Uo", "chastic", "Codex"), # Fixing potential d100 vs d20 mapping issues
    84: ("Ui", "clastic", "Inscriptions"),
    86: ("Kho", "hric", "Carvings"),
    88: ("Kha", "mornic", "Pictograms"),
    90: ("Ge", "chitan", "Manuscript"),
    92: ("Mebo", "hamanic", "Texts"),
    94: ("Sy", "sooltic", "Compilations"),
    96: ("Pra", "ldrannic", "Tablets"),
    98: ("Palu", "ldrunic", "Adnumbrations"),
    100: ("Che", "drashic", "Chronicles")
}

# Table 3-153: Book Types
BOOK_TYPES = [
    (20, "Bound book, normal"),
    (40, "Bound book, unusual binding"),
    (60, "Scrolls"),
    (80, "Tablets, clay"),
    (100, "Tablets, stone")
]

# Table 3-154: Unusual Book Bindings
UNUSUAL_BINDINGS = [
    (5, "Leather – human skin"),
    (10, "Leather – dragon skin"),
    (15, "Leather – snake or crocodile skin"),
    (20, "Leather – orc or goblin skin"),
    (25, "Leather – gnoll skin"),
    (30, "Leather – troll skin"),
    (35, "Metal covers"),
    (40, "Wood covers"),
    (45, "Stone covers (obsidian, etc.)"),
    (50, "No binding – loose pages"),
    (55, "Leather – painted"),
    (60, "Leather – scarred or scratched"),
    (65, "Cloth covers"),
    (70, "Transparent or invisible covers"),
    (75, "Ceramic covers"),
    (80, "Shifting pattern/picture on cover"),
    (85, "Skin with pulsing veins as cover"),
    (90, "Slime-like cover"),
    (95, "No cover or scroll"),
    (100, "In box")
]

UNUSUAL_FEATURES = [
    (5, "Lock"),
    (10, "Trap (mechanical)"),
    (15, "Lock and Trap"),
    (20, "Chained to shelves"),
    (25, "Pages glued together"),
    (30, "Incorporeal pages – how do you turn them?"),
    (35, "Hypnotic pattern on cover"),
    (40, "Poison on pages or cover"),
    (45, "Gem-encrusted"),
    (50, "Unusual writing"),
    (55, "Metal pages (thin)"),
    (60, "Pages out of order (possibly deliberate)"),
    (65, "Unusual illustrations"),
    (70, "Invisible pages"),
    (75, "Strange color ink"),
    (80, "Content of pages changes randomly or cyclically"),
    (85, "Virtually weightless or inexplicably heavy"),
    (90, "Written in code"),
    (95, "Trap (magical)"),
    (100, "Metal inlay on cover (filigree)")
]

def _get_from_list(lst, roll):
    for limit, val in lst:
        if roll <= limit:
            return val
    return lst[-1][1]

def _get_from_dict(d, roll):
    keys = sorted(d.keys())
    for k in keys:
        if roll <= k:
            return d[k]
    return d[keys[-1]]

def generate_book_title():
    # Roll independently on each column as per instructions
    p1 = _get_from_dict(LEGENDARY_BOOK_PARTS, random.randint(1, 100))[0]
    p2 = _get_from_dict(LEGENDARY_BOOK_PARTS, random.randint(1, 100))[1]
    p3 = _get_from_dict(LEGENDARY_BOOK_PARTS, random.randint(1, 100))[2]
    
    first_word = f"{p1}{p2}".capitalize()
    return f"{first_word} {p3}"

def generate_book_physical_details():
    roll_type = random.randint(1, 100)
    btype = _get_from_list(BOOK_TYPES, roll_type)
    
    binding = None
    feature = None
    
    if roll_type > 20 and roll_type <= 40: # Unusual binding
        binding = _get_from_list(UNUSUAL_BINDINGS, random.randint(1, 100))
        feature = _get_from_list(UNUSUAL_FEATURES, random.randint(1, 100))
        return f"{btype}: {binding} with {feature}"
    
    return btype
