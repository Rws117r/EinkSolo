import random

# Table 10-1: Colossoponderous Hyphenated Place Names
# Roll independently for Start and Ending. 
# Data is provided as pairs (Start, Ending) for each d100 range.
HYPHENATED_START = {
    1: "Ko", 3: "To", 5: "Azul", 7: "Azo", 9: "Zul", 11: "Tsa", 13: "Tso",
    15: "Enu", 17: "Anu", 19: "Uä", 21: "Tsul", 23: "Tsu", 25: "Ma", 27: "Tha",
    29: "Ta", 31: "Te", 33: "Ga", 35: "Ge", 37: "Che", 39: "Cho", 41: "Mo",
    43: "Am", 45: "An", 47: "Ohar", 49: "Ahar", 51: "Zaal", 53: "Utas", 55: "Ira",
    57: "Azi", 59: "Shara", 61: "Saru", 63: "Lazu", 65: "Pazu", 67: "Ka", 69: "Srija",
    71: "Vha", 73: "Kos", 75: "Khos", 77: "Jhos", 79: "Yhar", 81: "Yhal", 83: "Yal",
    85: "Nai", 87: "Bzai", 89: "Zai", 91: "Haz", 93: "Uos", 95: "Ktha", 97: "Lha", 99: "Mha"
}

HYPHENATED_ENDING = {
    1: "Atun", 3: "Aman", 5: "Kora", 7: "Bar", 9: "Amna", 11: "Mard", 13: "Maresh",
    15: "Tar", 17: "Taan", 19: "Tesh", 21: "Toa", 23: "Moäth", 25: "Atha", 27: "Atsa",
    29: "Ultan", 31: "Umna", 33: "Oom", 35: "Oon", 37: "Koa", 39: "Moa", 41: "Ghoza",
    43: "Gizek", 45: "Photua", 47: "Vanga", 49: "Moös", 51: "Mukhan", 53: "Vada", 55: "Pantu",
    57: "Otu", 59: "Otua", 61: "Jagna", 63: "Yaga", 65: "Yega", 67: "Yasht", 69: "Haga",
    71: "Montra", 73: "Tsoa", 75: "Tsaba", 77: "Uhru", 79: "Ahra", 81: "Yaza", 83: "Baza",
    85: "Kralo", 87: "Kranor", 89: "Thule", 91: "Mahal", 93: "Grama", 95: "Gzel", 97: "Gzal", 99: "Gantu"
}

# Table 10-2: Colossoponderous Two-Word Place Names
# Roll separately for Word 1 and Word 2.
TWO_WORD_FIRST = {
    1: "Ang", 3: "Az", 5: "Dal", 7: "Dath", 9: "Desh", 11: "Djal", 13: "Djang",
    15: "Djeng", 17: "Jal", 19: "Jang", 21: "Jath", 23: "Jeng", 25: "Kal", 27: "Kesh",
    29: "Kol", 31: "Kon", 33: "Koth", 35: "Quan", 37: "Quaz", 39: "Quen", 41: "Queng",
    43: "Ren", 45: "Reng", 47: "Resh", 49: "Sath", 51: "Saul", 53: "Seng", 55: "Seth",
    57: "Sool", 59: "Tash", 61: "Tsal", 63: "Tsat", 65: "Tsol", 67: "Yal", 69: "Yat",
    71: "Yath", 73: "Yeth", 75: "Yish", 77: "Yith", 79: "Yoth", 81: "Ysh", 83: "Yuth",
    85: "Yaz", 87: "Yesh", 89: "Om", 91: "Oor", 93: "Yil", 95: "Shal", 97: "Yoth", 99: "Zar"
}

TWO_WORD_SECOND = {
    1: "Brak", 3: "Bral", 5: "Bras", 7: "Brok", 9: "Dar", 11: "Dek", 13: "Dok",
    15: "Dorn", 17: "Dun", 19: "Gan", 21: "Gar", 23: "Gat", 25: "Gul", 27: "Harn",
    29: "Hes", 31: "Hin", 33: "Hoon", 35: "Hul", 37: "Kaj", 39: "Karg", 41: "Karj",
    43: "Karn", 45: "Kaul", 47: "Kes", 49: "Kharg", 51: "Kharn", 53: "Khaul", 55: "Kho",
    57: "Khoz", 59: "Kin", 61: "Kul", 63: "Tak", 65: "Talj", 67: "Tam", 69: "Tan",
    71: "Tang", 73: "Tarc", 75: "Targ", 77: "Teng", 79: "Toc", 81: "Tok", 83: "Tole",
    85: "Zet", 87: "Yar", 89: "Yem", 91: "Yod", 93: "Yok", 95: "Yom", 97: "Yor", 99: "Zat"
}

# Table 10-3: Colossoponderous Single-Word Place or Deity Names
SINGLE_WORD_START = {
    1: "Anhu", 2: "Ana", 3: "Beha", 4: "Tuo", 5: "Tuha", 6: "Koa", 7: "Anga", 8: "Azu", 9: "Dalja", 10: "Daga",
    11: "Deshi", 12: "Djalga", 13: "Djanga", 14: "Djentu", 15: "Joba", 16: "Jangi", 17: "Jathu", 18: "Jenga", 19: "Kalu", 20: "Keshta",
    21: "Konto", 22: "Konu", 23: "Kotha", 24: "Quana", 25: "Quaza", 26: "Quena", 27: "Quenga", 28: "Reho", 29: "Rengu", 30: "Reshu",
    31: "Sathu", 32: "Sauri", 33: "Senga", 34: "Sethi", 35: "Soolti", 36: "Tasha", 37: "Tsalga", 38: "Tsatra", 39: "Tsoltra", 40: "Yala",
    41: "Yatna", 42: "Yathri", 43: "Yethri", 44: "Yishta", 45: "Yithma", 46: "Yothma", 47: "Yshta", 48: "Yuthu", 49: "Yaza", 50: "Yesha",
    51: "Omba", 52: "Oorda", 53: "Yilka", 54: "Shalai", 55: "Yothu", 56: "Zormu", 57: "Anua", 58: "Ama", 59: "Bahi", 60: "Tuala",
    61: "Sua", 62: "Goa", 63: "Gubu", 64: "Azra", 65: "Doa", 66: "Moa", 67: "Ulha", 68: "Ulga", 69: "Olra", 70: "Ulra",
    71: "Mhanga", 72: "Vanga", 73: "Phanto", 74: "Vanja", 75: "Kanja", 76: "Jilza", 77: "Jalza", 78: "Jalja", 79: "Loa", 80: "Mura",
    81: "Lona", 82: "Jolba", 83: "Jota", 84: "Iol", 85: "Iul", 86: "Ueng", 87: "Ongu", 88: "Dobra", 89: "Ysta", 90: "Yema",
    91: "Yana", 92: "Yiza", 93: "Oshma", 94: "Goru", 95: "Phazu", 96: "Xana", 97: "Zana", 98: "Shabo", 99: "Yhota", 100: "Yhatu"
}

SINGLE_WORD_ENDING = {
    1: "biri", 2: "boko", 3: "bora", 4: "borgo", 5: "bota", 6: "brala", 7: "bralu", 8: "brangi", 9: "brazu", 10: "cantha",
    11: "dekah", 12: "doknu", 13: "gamar", 14: "gara", 15: "gartha", 16: "gatang", 17: "gatu", 18: "ghara", 19: "gontua", 20: "gubor",
    21: "gulga", 22: "gulma", 23: "gultra", 24: "harin", 25: "hloon", 26: "hoonda", 27: "janth", 28: "jantha", 29: "kaja", 30: "kakri",
    31: "kantha", 32: "kanthu", 33: "karga", 34: "karja", 35: "karna", 36: "kesar", 37: "khara", 38: "kharga", 39: "khari", 40: "kharna",
    41: "khaulj", 42: "khora", 43: "khoza", 44: "kindu", 45: "koaaz", 46: "kul", 47: "londu", 48: "magol", 49: "maja", 50: "majo",
    51: "manthu", 52: "matra", 53: "mboro", 54: "mera", 55: "mimor", 56: "modo", 57: "modra", 58: "mojo", 59: "mola", 60: "mondu",
    61: "moro", 62: "morthu", 63: "mortoc", 64: "mulu", 65: "ngara", 66: "ngaroth", 67: "nulmar", 68: "ulga", 69: "parthu", 70: "pura",
    71: "quara", 72: "quarma", 73: "quaru", 74: "rada", 75: "roa", 76: "rodo", 77: "sagua", 78: "sua", 79: "taja", 80: "taka",
    81: "taltaj", 82: "tama", 83: "tana", 84: "tanga", 85: "tengu", 86: "tharta", 87: "toko", 88: "tolgoth", 89: "tuab", 90: "tueen",
    91: "tulu", 92: "varma", 93: "yargu", 94: "yembu", 95: "yodo", 96: "yokta", 97: "yomba", 98: "yoora", 99: "zantu", 100: "zolta"
}

def generate_colossoponderous(structure=None):
    """
    Generate a Colossoponderous name.
    structure 1: Hyphenated (e.g., Ko-Atun)
    structure 2: Two-Word (e.g., Ang Brak)
    structure 3: Single-Word (e.g., Anhubiri)
    """
    if not structure:
        structure = random.choice([1, 2, 3])
        
    if structure == 1:
        roll_start = random.choice(list(HYPHENATED_START.keys()))
        roll_end = random.choice(list(HYPHENATED_ENDING.keys()))
        return f"{HYPHENATED_START[roll_start]}-{HYPHENATED_ENDING[roll_end]}"
    
    if structure == 2:
        roll_first = random.choice(list(TWO_WORD_FIRST.keys()))
        roll_second = random.choice(list(TWO_WORD_SECOND.keys()))
        return f"{TWO_WORD_FIRST[roll_first]} {TWO_WORD_SECOND[roll_second]}"
    
    if structure == 3:
        # Start and Ending 1-100
        roll_start = random.randint(1, 100)
        roll_end = random.randint(1, 100)
        return f"{SINGLE_WORD_START[roll_start]}{SINGLE_WORD_ENDING[roll_end]}"
    
    return "Unknown"
