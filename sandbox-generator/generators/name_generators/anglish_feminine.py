import random

# Table 4-2: Anglish Feminine Personal Names
NAMES_1 = {
    1: "Abfreth", 2: "Abfreya", 3: "Abreen", 4: "Abrys", 5: "Absin", 6: "Abwen", 7: "Abwyn", 8: "Aileen", 9: "Ailys", 10: "Alacind",
    11: "Alacinda", 12: "Alacinde", 13: "Alacyn", 14: "Alafreya", 15: "Alafrin", 16: "Alascine", 17: "Alasine", 18: "Albys", 19: "Alecsine", 20: "Alecta",
    21: "Alleen", 22: "Alys", 23: "Anfrith", 24: "Anseline", 25: "Arabel", 26: "Aracinda", 27: "Aracynde", 28: "Aralandra", 29: "Araleathe", 30: "Aralis",
    31: "Arasind", 32: "Aravys", 33: "Arawen", 34: "Arawyn", 35: "Arivaine", 36: "Aryvis", 37: "Aulys", 38: "Ayleen", 39: "Balys", 40: "Banys",
    41: "Barsynde", 42: "Beafrith", 43: "Beasinda", 44: "Belfreya", 45: "Belfrith", 46: "Belwen", 47: "Belwyd", 48: "Belwyn", 49: "Belyn", 50: "Belynd",
    51: "Belynda", 52: "Belys", 53: "Belys", 54: "Beolin", 55: "Beracyn", 56: "Berawyn", 57: "Bodecinde", 58: "Bralcinde", 59: "Bralwen", 60: "Bralwyn",
    61: "Bralys", 62: "Brandcin", 63: "Braniss", 64: "Branwen", 65: "Brecyne", 66: "Breniss", 67: "Briovere", 68: "Brycaun", 69: "Brysel", 70: "Bywen",
    71: "Bywis", 72: "Caldeen", 73: "Calfrith", 74: "Callyn", 75: "Caulsel", 76: "Caulsin", 77: "Celacynde", 78: "Celandra", 79: "Celasine", 80: "Celevere",
    81: "Celewyn", 82: "Celys", 83: "Chalyn", 84: "Cialta", 85: "Cilcine", 86: "Cirilys", 87: "Cyleen", 88: "Cyniss", 89: "Cyralta", 90: "Cywen",
    91: "Dafreya", 92: "Dafrith", 93: "Daicinda", 94: "Daicyn", 95: "Daileen", 96: "Dailys", 97: "Daisel", 98: "Daiwen", 99: "Daleatha", 100: "Dalevere"
}

NAMES_2 = {
    1: "Dalwen", 2: "Dalys", 3: "Dealwen", 4: "Delfren", 5: "Dellys", 6: "Delweth", 7: "Deolandra", 8: "Descyn", 9: "Desinde", 10: "Dulcine",
    11: "Dulcyn", 12: "Dulcynde", 13: "Dulivere", 14: "Dyfren", 15: "Ealda", 16: "Ealfren", 17: "Ealta", 18: "Ealwen", 19: "Ealys", 20: "Ealys",
    21: "Elfrith", 22: "Elleen", 23: "Elys", 24: "Eolaine", 25: "Eolanthe", 26: "Eolcyth", 27: "Eolda", 28: "Eoldra", 29: "Eolfrith", 30: "Eolwen",
    31: "Eolwind", 32: "Eolwiss", 33: "Eolwyn", 34: "Eolys", 35: "Eoscinda", 36: "Esabel", 37: "Esalys", 38: "Gilfren", 39: "Gilta", 40: "Gilys",
    41: "Gwyncel", 42: "Gwynfren", 43: "Gwynwen", 44: "Hecsin", 45: "Hecynda", 46: "Hecyth", 47: "Ialdra", 48: "Ialyn", 49: "Iawen", 50: "Iswen",
    51: "Jorcinda", 52: "Jorcinde", 53: "Jorcinth", 54: "Jorleen", 55: "Maulwen", 56: "Mereen", 57: "Merewyn", 58: "Merisel", 59: "Merwen", 60: "Merys",
    61: "Ocasin", 62: "Ocfrith", 63: "Olbel", 64: "Olcyth", 65: "Olfrith", 66: "Rhauleen", 67: "Rhialsin", 68: "Rhiawen", 69: "Riawyn", 70: "Risvin",
    71: "Riswen", 72: "Selcinde", 73: "Selcyth", 74: "Seldra", 75: "Selys", 76: "Suldra", 77: "Taeleen", 78: "Talacynde", 79: "Taline", 80: "Tealys",
    81: "Telecynd", 82: "Ulcyn", 83: "Uleandra", 84: "Ulfen", 85: "Ulfreya", 86: "Ulwen", 87: "Ulys", 88: "Ylabel", 89: "Ylinda", 90: "Ylneth",
    91: "Ylniss", 92: "Ylspeth", 93: "Ylwis", 94: "Ylyn", 95: "Ylys", 96: "Ysbel", 97: "Ysevere", 98: "Ysinda", 99: "Ysta", 100: "Yswen"
}

def generate_anglish_feminine():
    col = random.randint(1, 2)
    roll = random.randint(1, 100)
    if col == 1:
        return NAMES_1[roll]
    else:
        return NAMES_2[roll]
