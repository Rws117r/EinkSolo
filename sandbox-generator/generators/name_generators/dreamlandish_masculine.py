import random

START = {
    1: "A", 2: "Bha", 3: "Bho", 4: "Bhu", 5: "Bna", 6: "Bua", 7: "Ca", 8: "Cha", 9: "Chu", 10: "Che",
    11: "Chi", 12: "Cho", 13: "E", 14: "Ghe", 15: "Ghi", 16: "Gho", 17: "Gna", 18: "Gni", 19: "Gno", 20: "Go",
    21: "Gu", 22: "Ha", 23: "Ho", 24: "Hu", 25: "I", 26: "Ia", 27: "Io", 28: "Iou", 29: "Iza", 30: "Isa",
    31: "Iai", 32: "Iu", 33: "Ja", 34: "Je", 35: "Jha", 36: "Jho", 37: "Jhu", 38: "Kha", 39: "Kho", 40: "Khu",
    41: "Ko", 42: "Ksho", 43: "Ku", 44: "La", 45: "Lo", 46: "Lua", 47: "Ma", 48: "Mha", 49: "Mho", 50: "Mo",
    51: "Mu", 52: "Na", 53: "Ne", 54: "Nha", 55: "Nhe", 56: "Nhu", 57: "Nua", 58: "Nuo", 59: "Nya", 60: "Oa",
    61: "Ob", 62: "Ool", 63: "Oom", 64: "Oth", 65: "Pna", 66: "Pru", 67: "Prua", 68: "Sa", 69: "Sha", 70: "Shi",
    71: "Shia", 72: "Sho", 73: "Shu", 74: "So", 75: "Su", 76: "Sua", 77: "Suo", 78: "Tsa", 79: "Tso", 80: "Tsu",
    81: "U", 82: "Ua", 83: "Uo", 84: "Xa", 85: "Xe", 86: "Xi", 87: "Xo", 88: "Ya", 89: "Ye", 90: "Yha",
    91: "Yhe", 92: "Yi", 93: "Yo", 94: "Yho", 95: "Yu", 96: "Yua", 97: "Zha", 98: "Zo", 99: "Zoa", 100: "Zul"
}

ENDING = {
    1: "ralto", 2: "as", 3: "yis", 4: "yas", 5: "jir", 6: "jha", 7: "jal", 8: "djal", 9: "djas", 10: "huo",
    11: "hua", 12: "cobo", 13: "ghobo", 14: "jopo", 15: "loño", 16: "lorso", 17: "spero", 18: "quaro", 19: "biano", 20: "drigo",
    21: "fael", 22: "mondo", 23: "nieri", 24: "niero", 25: "oul", 26: "noldo", 27: "cco", 28: "ddo", 29: "bbo", 30: "drico",
    31: "drigo", 32: "rolfo", 33: "mero", 34: "ssano", 35: "santhu", 36: "thu", 37: "llus", 38: "los", 39: "ng", 40: "njar",
    41: "mbor", 42: "bha", 43: "bhar", 44: "bul", 45: "bhu", 46: "dhar", 47: "dhan", 48: "dra", 49: "du", 50: "gho",
    51: "gul", 52: "ghur", 53: "hesh", 54: "hur", 55: "jandu", 56: "jantu", 57: "jat", 58: "jatha", 59: "jesh", 60: "kaj",
    61: "kash", 62: "kesh", 63: "khe", 64: "kha", 65: "khaj", 66: "khu", 67: "kho", 68: "lal", 69: "lai", 70: "lam",
    71: "lan", 72: "lu", 73: "lua", 74: "majat", 75: "majir", 76: "mys", 77: "myr", 78: "mood", 79: "boda", 80: "namb",
    81: "pantu", 82: "noosh", 83: "noom", 84: "rash", 85: "risi", 86: "tama", 87: "thune", 88: "tyar", 89: "tuar", 90: "tuor",
    91: "hiyat", 92: "hian", 93: "mian", 94: "zool", 95: "tzan", 96: "thazar", 97: "ltimar", 98: "ltan", 99: "modo", 100: "phor"
}

def generate():
    start_roll = random.randint(1, 100)
    end_roll = random.randint(1, 100)
    return f"{START.get(start_roll, 'Unk')}{ENDING.get(end_roll, 'own')}"
