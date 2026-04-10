import random

START = {
    1: "A", 2: "Bha", 3: "Bho", 4: "Bhu", 5: "Bna", 6: "Bua", 7: "Ca", 8: "Cha", 9: "Cha", 10: "Che",
    11: "Chi", 12: "Cho", 13: "E", 14: "Ghe", 15: "Ghi", 16: "Gho", 17: "Gna", 18: "Gni", 19: "Gno", 20: "Go",
    21: "Gu", 22: "Ha", 23: "Ho", 24: "Hu", 25: "I", 26: "Ia", 27: "Io", 28: "Iou", 29: "Iza", 30: "Isa",
    31: "Iai", 32: "Iu", 33: "Ja", 34: "Je", 35: "Jha", 36: "Jho", 37: "Jhu", 38: "Kha", 39: "Kho", 40: "Khu",
    41: "Ko", 42: "Ksho", 43: "Ku", 44: "La", 45: "Lo", 46: "Lua", 47: "Ma", 48: "Mha", 49: "Mho", 50: "Mo",
    51: "Mu", 52: "Na", 53: "Ne", 54: "Nha", 55: "Nhe", 56: "Nhu", 57: "Nua", 58: "Nuo", 59: "Nya", 60: "Oa",
    61: "Ob", 62: "Ou", 63: "Oo", 64: "O", 65: "Pna", 66: "Pru", 67: "Pnu", 68: "Sa", 69: "Sha", 70: "Shi",
    71: "Shia", 72: "Sho", 73: "Shu", 74: "So", 75: "Su", 76: "Sua", 77: "Suo", 78: "Tsa", 79: "Tso", 80: "Tsu",
    81: "U", 82: "Ua", 83: "Uo", 84: "Xa", 85: "Xe", 86: "Xi", 87: "Xo", 88: "Ya", 89: "Ye", 90: "Yha",
    91: "Yhe", 92: "Yi", 93: "Yo", 94: "Yho", 95: "Yu", 96: "Yua", 97: "Zha", 98: "Zo", 99: "Zoa", 100: "Zu"
}

ENDING = {
    # Ending 1 (1-100)
    1: "lthazar", 2: "ltazar", 3: "lthasar", 4: "besh", 5: "biade", 6: "briul", 7: "balus", 8: "carcho", 9: "kaganis", 10: "ccloas",
    11: "ceris", 12: "chirmus", 13: "charsis", 14: "chien", 15: "cildes", 16: "cilius", 17: "cleides", 18: "cli", 19: "ctanto", 20: "scramar",
    21: "kratides", 22: "ctemon", 23: "ctas", 24: "curus", 25: "scurus", 26: "damidas", 27: "damos", 28: "demos", 29: "dacus", 30: "dmus",
    31: "donios", 32: "dorus", 33: "dutha", 34: "doxus", 35: "dymarchos", 36: "dymos", 37: "gammon", 38: "genes", 39: "janandos", 40: "gorob",
    41: "garas", 42: "gos", 43: "hemeros", 44: "hippos", 45: "hippa", 46: "kris", 47: "ladas", 48: "laeus", 49: "laidas", 50: "laus",
    51: "lcidas", 52: "lesagoras", 53: "lios", 54: "lys", 55: "lleos", 56: "llicon", 57: "llomrades", 58: "llodorus", 59: "llus", 60: "lluthus",
    61: "lochus", 62: "lodotus", 63: "lon", 64: "lophanes", 65: "lotes", 66: "lsus", 67: "lycus", 68: "machus", 69: "mades", 70: "maeleon",
    71: "luziar", 72: "luthiar", 73: "mantos", 74: "maratos", 75: "masias", 76: "mastes", 77: "mbrotar", 78: "methe", 79: "melos", 80: "menos",
    81: "mnil", 82: "metrios", 83: "midor", 84: "mis", 85: "mios", 86: "moxedes", 87: "mocritus", 88: "molpidae", 89: "mon", 90: "monax",
    91: "monides", 92: "mophanes", 93: "mophilus", 94: "mophon", 95: "mosthenes", 96: "xanos", 97: "mpedocles", 98: "mos", 99: "nethos", 100: "nander",
    
    # Ending 2 (101-200)
    101: "nexiras", 102: "dniar", 103: "dnios", 104: "nios", 105: "nocles", 106: "nocrates", 107: "nomis", 108: "bnor", 109: "ntarios", 110: "ntor",
    111: "nthas", 112: "nthios", 113: "nychus", 114: "nymus", 115: "nysios", 116: "nysidar", 117: "minondas", 118: "phrodas", 119: "ptar", 120: "phanes",
    121: "phaniios", 122: "phantos", 123: "phemos", 124: "phialta", 125: "philos", 126: "phorion", 127: "phoros", 128: "phranor", 129: "phron", 130: "phos",
    131: "phantus", 132: "phemus", 133: "phialtes", 134: "philus", 135: "phontes", 136: "phorion", 137: "phranor", 138: "phron", 139: "phus", 140: "piades",
    141: "pios", 142: "pselos", 143: "psias", 144: "pos", 145: "racritos", 146: "ramyes", 147: "rax", 148: "rchides", 149: "rcol", 150: "rcyllidos",
    151: "tremon", 152: "rhas", 153: "ridemos", 154: "ripides", 155: "rissou", 156: "ritar", 157: "rmidar", 158: "rmor", 159: "roth", 160: "rondar",
    161: "ros", 162: "rotheus", 163: "rrhios", 164: "rybatos", 165: "rybiador", 166: "rycratar", 167: "rylochis", 168: "rymedon", 169: "rypon", 170: "rysthedar",
    171: "lazar", 172: "sandir", 173: "santhir", 174: "schinar", 175: "schylos", 176: "scorides", 177: "scor", 178: "sebios", 179: "secilus", 180: "siadar",
    181: "damir", 182: "demar", 183: "dacar", 184: "dmi", 185: "donior", 186: "dru", 187: "duthir", 188: "doxical", 189: "rchir", 190: "dymar",
    191: "gammar", 192: "genar", 193: "janandar", 194: "grobar", 195: "ghar", 196: "goltha", 197: "hemar", 198: "hippor", 199: "lcidar", 200: "lehar",
    
    # Ending 3 (201-300)
    201: "bangatha", 202: "barang", 203: "dambo", 204: "dampo", 205: "danga", 206: "diogu", 207: "diugu", 208: "dombo", 209: "fangua", 210: "farang",
    211: "faranga", 212: "farongo", 213: "fengi", 214: "ferinang", 215: "gadang", 216: "grai", 217: "hamaro", 218: "hango", 219: "hangu", 220: "homodo",
    221: "jaga", 222: "jatanga", 223: "jatse", 224: "java", 225: "kambua", 226: "komodo", 227: "maranga", 228: "maro", 229: "marongo", 230: "moro",
    231: "ngamodo", 232: "ngamoko", 233: "ngamoro", 234: "ngashi", 235: "ngatara", 236: "taga", 237: "tagara", 238: "tagra", 239: "tambu", 240: "tanthu",
    241: "tathua", 242: "thambu", 243: "thando", 244: "thanto", 245: "tiaga", 246: "tompo", 247: "tuara", 248: "chandra", 249: "charan", 250: "dha",
    251: "dwar", 252: "dayal", 253: "dayesh", 254: "dev", 255: "dhan", 256: "dhatri", 257: "daya", 258: "dayar", 259: "ganath", 260: "gesh",
    261: "girath", 262: "vhesh", 263: "vashtar", 264: "ghesh", 265: "lthe", 266: "thalar", 267: "thule", 268: "tontu", 269: "tontar", 270: "tchar",
    271: "rtchas", 272: "quarza", 273: "quiron", 274: "quara", 275: "zultir", 276: "zaltar", 277: "thatar", 278: "ängir", 279: "ätra", 280: "äzir",
    281: "shantu", 282: "shanti", 283: "jasha", 284: "jara", 285: "djira", 286: "hralto", 287: "keem", 288: "kheem", 289: "kheer", 290: "khara",
    291: "gwar", 292: "gatar", 293: "githri", 294: "phior", 295: "fazar", 296: "buor", 297: "zabul", 298: "rioch", 299: "rior", 300: "ltroch"
}

def generate():
    start_roll = random.randint(1, 100)
    end_roll = random.randint(1, 300)
    return f"{START.get(start_roll, 'Unk')}{ENDING.get(end_roll, 'own')}"
