import random

PLACE_START = {
    1: "A", 2: "Aba", 3: "Ael", 4: "Aia", 5: "Ala", 6: "Alia", 7: "Alio", 8: "Altra", 9: "Alu", 10: "Ao",
    11: "Are", 12: "Areo", 13: "Atra", 14: "Aza", 15: "Azi", 16: "Baha", 17: "Batra", 18: "Boa", 19: "Cala", 20: "Cala",
    21: "Cele", 22: "Chada", 23: "Chala", 24: "Chara", 25: "Chuo", 26: "Cia", 27: "Dhara", 28: "Dura", 29: "Ere", 30: "Etra",
    31: "Ghantu", 32: "Ha", 33: "Hal", 34: "Hala", 35: "Halu", 36: "Haya", 37: "Ia", 38: "Ie", 39: "Io", 40: "Jaia",
    41: "Jala", 42: "Jalta", 43: "Julu", 44: "Lana", 45: "Landa", 46: "Lani", 47: "Lanta", 48: "Lantu", 49: "Latra", 50: "Leo",
    51: "Lio", 52: "My", 53: "Nia", 54: "Ny", 55: "Oa", 56: "Oba", 57: "Oco", 58: "Ol", 59: "Ore", 60: "Ospa",
    61: "Otra", 62: "Phaba", 63: "Shulu", 64: "Suala", 65: "Suana", 66: "Sula", 67: "Taba", 68: "Tala", 69: "Tala", 70: "Taraba",
    71: "Taru", 72: "Tela", 73: "Thua", 74: "Thula", 75: "Thule", 76: "Tila", 77: "Trini", 78: "Tsaia", 79: "Tsio", 80: "Tsuo",
    81: "Tuara", 82: "Tula", 83: "U", 84: "Ua", 85: "Ua", 86: "Ual", 87: "Uala", 88: "Ue", 89: "Uele", 90: "Ui",
    91: "Uia", 92: "Ul", 93: "Ula", 94: "Ula", 95: "Ule", 96: "Uleo", 97: "Ulio", 98: "Ultra", 99: "Ulu", 100: "Via"
}

PLACE_ENDING = {
    1: "bai", 2: "bantis", 3: "banto", 4: "bantu", 5: "bhis", 6: "bis", 7: "bne", 8: "buon", 9: "cantis", 10: "charkos",
    11: "charos", 12: "chas", 13: "chiros", 14: "csion", 15: "cta", 16: "ctaros", 17: "ctis", 18: "daan", 19: "dath", 20: "diaphis",
    21: "dis", 22: "dontor", 23: "dora", 24: "doth", 25: "duthe", 26: "fandas", 27: "fantis", 28: "for", 29: "ianthe", 30: "linos",
    31: "mantoa", 32: "mantu", 33: "matar", 34: "matra", 35: "mbatha", 36: "memnis", 37: "memnon", 38: "mna", 39: "mnai", 40: "mnais",
    41: "mnar", 42: "mnaros", 43: "mne", 44: "mneon", 45: "mneos", 46: "mnith", 47: "mpai", 48: "naa", 49: "nas", 50: "ndaar",
    51: "ndra", 52: "nha", 53: "noa", 54: "ntaar", 55: "nti", 56: "ntis", 57: "paal", 58: "paas", 59: "pang", 60: "panga",
    61: "pangu", 62: "pantha", 63: "pash", 64: "pashai", 65: "phaa", 66: "phai", 67: "phais", 68: "phan", 69: "phanda", 70: "phandis",
    71: "phne", 72: "phor", 73: "phoras", 74: "pne", 75: "pos", 76: "pteon", 77: "ptia", 78: "ptoa", 79: "ptos", 80: "qua",
    81: "quar", 82: "quaris", 83: "quo", 84: "shaa", 85: "shan", 86: "shanta", 87: "shantis", 88: "shotan", 89: "spara", 90: "tantalos",
    91: "taros", 92: "thandu", 93: "thantis", 94: "thantor", 95: "thar", 96: "thoris", 97: "tiabis", 98: "toa", 99: "vhoa", 100: "vhos"
}

def generate_place_name():
    start = PLACE_START[random.randint(1, 100)]
    ending = PLACE_ENDING[random.randint(1, 100)]
    return f"{start}{ending}"
