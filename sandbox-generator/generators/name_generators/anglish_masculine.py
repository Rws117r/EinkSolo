import random

# Table 4-1: Anglish Masculine Personal Names
NAMES_1 = {
    1: "Ailan", 2: "Alain", 3: "Alan", 4: "Albert", 5: "Alec", 6: "Allan", 7: "Allen", 8: "Ansal", 9: "Ansel", 10: "Arnald",
    11: "Arnold", 12: "Aylan", 13: "Bantry", 14: "Barn", 15: "Bernard", 16: "Bodefrey", 17: "Bodo", 18: "Brance", 19: "Brand", 20: "Brant",
    21: "Brenart", 22: "Bret", 23: "Bretch", 24: "Brett", 25: "Brot", 26: "Brunce", 27: "Catch", 28: "Ciral", 29: "Ciril", 30: "Cratch",
    31: "Creech", 32: "Creed", 33: "Cyral", 34: "Cyril", 35: "Dale", 36: "Deal", 37: "Dule", 38: "Dyle", 39: "Elbert", 40: "Ernol",
    41: "George", 42: "Georph", 43: "Georv", 44: "Georve", 45: "Gerald", 46: "Giles", 47: "Gilhome", 48: "Godfrey", 49: "Goffrey", 50: "Gorald",
    51: "Goslin", 52: "Gosset", 53: "Guilford", 54: "Guilham", 55: "Hod", 56: "Hodwise", 57: "Hodwiss", 58: "Huff", 59: "Jarald", 60: "Jaromy",
    61: "Jeets", 62: "Jeremy", 63: "Jermyn", 64: "Jerold", 65: "Jerome", 66: "Jeromy", 67: "Jirold", 68: "Jiromy", 69: "Jorah", 70: "Joromy",
    71: "Juff", 72: "Kale", 73: "Kile", 74: "Kyle", 75: "Leek", 76: "Luke", 77: "Metchiss", 78: "Much", 79: "Muchiss", 80: "Mutchall",
    81: "Nodfrey", 82: "Nordel", 83: "Norel", 84: "Norwin", 85: "Odd", 86: "Oddwise", 87: "Odo", 88: "Odwiss", 89: "Olivar", 90: "Olivard",
    91: "Olivart", 92: "Oliver", 93: "Olizan", 94: "Ollec", 95: "Ollek", 96: "Orin", 97: "Orrin", 98: "Patch", 99: "Ralf", 100: "Ralph"
}

NAMES_2 = {
    1: "Randal", 2: "Ratch", 3: "Rendal", 4: "Rulpert", 5: "Rulph", 6: "Rundal", 7: "Rundel", 8: "Rupert", 9: "Rypert", 10: "Tamothy",
    11: "Temothy", 12: "Thorn", 13: "Thorne", 14: "Timothy", 15: "Torm", 16: "Torn", 17: "Torne", 18: "Ulbert", 19: "Ulec", 20: "Ullen",
    21: "Walter", 22: "Wilbert", 23: "Willem", 24: "William", 25: "Yadrick", 26: "Yedrick", 27: "Yeord", 28: "Yeorth", 29: "Yodrick", 30: "Yoric",
    31: "Yorick", 32: "Yorth", 33: "Yudrick", 34: "Yurth", 35: "Alun", 36: "Olbert", 37: "Ulbert", 38: "Olber", 39: "Ulber", 40: "Ulbro",
    41: "Otho", 42: "Otto", 43: "Otha", 44: "Utha", 45: "Othan", 46: "Uthan", 47: "Serl", 48: "Cearl", 49: "Bennart", 50: "Bannart",
    51: "Bronse", 52: "Dool", 53: "Gelford", 54: "Gullen", 55: "Gullem", 56: "Hode", 57: "Hoath", 58: "Hude", 59: "Hoad", 60: "Hoath",
    61: "Joam", 62: "Jermy", 63: "Jerlad", 64: "Jerlig", 65: "Gerlig", 66: "Garrol", 67: "Gorel", 68: "Gurel", 69: "Gurth", 70: "Gorth",
    71: "Gurm", 72: "Gort", 73: "Gorm", 74: "Huld", 75: "Hulch", 76: "Gaulch", 77: "Maulch", 78: "Maul", 79: "Motch", 80: "Mautch",
    81: "Nedwin", 82: "Nodwin", 83: "Nudwin", 84: "Nobwin", 85: "Nunce", 86: "Nott", 87: "Mott", 88: "Lott", 89: "Dormer", 90: "Doon",
    91: "Dole", 92: "Boon", 93: "Broon", 94: "Bross", 95: "Broz", 96: "Uilath", 97: "Waul", 98: "Wode", 99: "Woad", 100: "Worth"
}

def generate_anglish_masculine():
    col = random.randint(1, 2)
    roll = random.randint(1, 100)
    if col == 1:
        return NAMES_1[roll]
    else:
        return NAMES_2[roll]
