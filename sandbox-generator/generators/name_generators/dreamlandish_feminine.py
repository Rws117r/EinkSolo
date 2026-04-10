import random

FIRST_PART = {
    # Column 1 (1-100)
    1: "A", 2: "Ai", 3: "Ay", 4: "Ba", 5: "Bha", 6: "Bia", 7: "Cha", 8: "Che", 9: "Ci", 10: "Cia",
    11: "Cta", 12: "Cy", 13: "E", 14: "Ea", 15: "Ei", 16: "Ga", 17: "Gha", 18: "Ghe", 19: "Ghi", 20: "Gy",
    21: "Ha", 22: "I", 23: "Ia", 24: "Iai", 25: "Ihy", 26: "Io", 27: "Iou", 28: "Isa", 29: "Iu", 30: "Iza",
    31: "Ja", 32: "Jai", 33: "Je", 34: "Jha", 35: "Jho", 36: "Kha", 37: "Kho", 38: "Khu", 39: "Kia", 40: "Ko",
    41: "Ksha", 42: "Kya", 43: "La", 44: "Lea", 45: "Lia", 46: "Lo", 47: "Ma", 48: "Mha", 49: "Mho", 50: "Mi",
    51: "Mie", 52: "Mo", 53: "My", 54: "Ne", 55: "Nha", 56: "Nhe", 57: "Nhu", 58: "Nia", 59: "Nua", 60: "Nue",
    61: "Nya", 62: "O", 63: "Oa", 64: "Ra", 65: "Ri", 66: "Rhy", 67: "Rya", 68: "Sa", 69: "Se", 70: "Sha",
    71: "Shia", 72: "Sho", 73: "Shu", 74: "So", 75: "Su", 76: "Sua", 77: "Sui", 78: "Sya", 79: "Tia", 80: "Tsa",
    81: "Ua", 82: "Ui", 83: "Xa", 84: "Xe", 85: "Xi", 86: "Xo", 87: "Ya", 88: "Ye", 89: "Yha", 90: "Yhe",
    91: "Yhi", 92: "Yi", 93: "Yo", 94: "Yu", 95: "Yua", 96: "Zal", 97: "Zha", 98: "Zia", 99: "Zo", 100: "Zoa",
    # Column 2 (101-200)
    101: "Aya", 102: "Ali", 103: "Abis", 104: "As", 105: "Ais", 106: "Bali", 107: "Baly", 108: "Biel", 109: "Bial", 110: "Bry",
    111: "Bri", 112: "Cyr", 113: "En", 114: "Ama", 115: "Eila", 116: "Gala", 117: "Gwy", 118: "Cria", 119: "Gri", 120: "Grise",
    121: "Hala", 122: "Es", 123: "Aus", 124: "Ais", 125: "Ias", 126: "Ies", 127: "Isi", 128: "Ysa", 129: "Yso", 130: "Ispi",
    131: "Ios", 132: "Jia", 133: "Djas", 134: "Yc", 135: "Issa", 136: "Te", 137: "Tana", 138: "Tine", 139: "Jana", 140: "Sri",
    141: "Raa", 142: "Rha", 143: "Raki", 144: "Tri", 145: "Ksi", 146: "Ksa", 147: "Kse", 148: "Cas", 149: "Cis", 150: "Chra",
    151: "Bou", 152: "Baha", 153: "Laho", 154: "Lhi", 155: "Hla", 156: "Yra", 157: "Iri", 158: "Is", 159: "Mwe", 160: "Mui",
    161: "Nui", 162: "Tui", 163: "Twi", 164: "Sva", 165: "Sve", 166: "Rai", 167: "Ola", 168: "Oly", 169: "Ties", 170: "Da",
    171: "Dy", 172: "Des", 173: "As", 174: "Sai", 175: "Sei", 176: "Fa", 177: "Fe", 178: "Fae", 179: "Fey", 180: "Fia",
    181: "Pa", 182: "Pha", 183: "Psi", 184: "Psa", 185: "Ce", 186: "Seo", 187: "Cio", 188: "Yua", 189: "Hami", 190: "Zala",
    191: "Yoe", 192: "Yoca", 193: "Yil", 194: "Yal", 195: "Iul", 196: "Yul", 197: "Yil", 198: "Zil", 199: "Zi", 200: "Tal"
}

ENDING = {
    1: "ä", 2: "älys", 3: "ätha", 4: "äthine", 5: "ävin", 6: "balys", 7: "brilis", 8: "cambryl", 9: "camerel", 10: "camerin",
    11: "canda", 12: "canthe", 13: "casina", 14: "casta", 15: "castia", 16: "cate", 17: "chanda", 18: "chandra", 19: "chanil", 20: "charyl",
    21: "charys", 22: "chatha", 23: "cheen", 24: "chel", 25: "chenyl", 26: "chia", 27: "chys", 28: "ciande", 29: "cilta", 30: "citana",
    31: "csanda", 32: "csanne", 33: "cyne", 34: "deryn", 35: "dwen", 36: "gaeena", 37: "gharad", 38: "gharat", 39: "jaril", 40: "jawai",
    41: "jheril", 42: "khameril", 43: "kis", 44: "ladha", 45: "lanthe", 46: "lfara", 47: "lia", 48: "lianthe", 49: "lsamir", 50: "lune",
    51: "lunis", 52: "mhe", 53: "medha", 54: "mis", 55: "mix", 56: "muire", 57: "nala", 58: "ngharad", 59: "nivere", 60: "nuil",
    61: "nwin", 62: "ölanthis", 63: "pharis", 64: "phiela", 65: "radhana", 66: "ranis", 67: "rhianne", 68: "rhylde", 69: "riam", 70: "riian",
    71: "riawen", 72: "riljat", 73: "rwin", 74: "ryel", 75: "sairys", 76: "salime", 77: "salynde", 78: "sarinde", 79: "satma", 80: "scine",
    81: "seryl", 82: "shala", 83: "shana", 84: "shanda", 85: "sharys", 86: "shia", 87: "shlyn", 88: "siltia", 89: "stine", 90: "takia",
    91: "tasha", 92: "tashri", 93: "tashtana", 94: "tashtin", 95: "üne", 96: "wirin", 97: "xana", 98: "xanda", 99: "xantha", 100: "xiria"
}

def generate():
    start_roll = random.randint(1, 200)
    end_roll = random.randint(1, 100)
    return f"{FIRST_PART.get(start_roll, 'Unk')}{ENDING.get(end_roll, 'own')}"
