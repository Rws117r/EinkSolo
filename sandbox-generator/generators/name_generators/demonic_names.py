import random

# Table 2-11: Demonic Name Part 1
PART_1 = [
    "Aa", "Acha", "Alu", "Ara", "Aza", "Azu", "Bua", "Bulu", "Cha", "Cho", "Dro", "Dru", "Ee", "Gha", "Gho", "Ghu", "Gla", "Gu", "Gua", "Guga",
    "Hue", "Huo", "Ibu", "Icta", "Icto", "Ictu", "Ixe", "Ixi", "Ixu", "Kya", "Shuhu", "Soa", "Sza", "Tca", "Tika", "Tso", "Tsu", "Tzu", "Ua", "Uaga",
    "Ucto", "Ulu", "Uo", "Uzo", "Vau", "Vil", "Vu", "Vua", "Vyl", "Xa", "Xu", "Yaa", "Yaga", "Yee", "Yoa", "Yu", "Yua", "Yuthu", "Zo", "Zu"
]

# Table 2-12: Demonic Name Part 2
PART_2 = [
    "ach", "baal", "bazaz", "bech", "belth", "bex", "bor", "boraz", "brog", "butu", "chaag", "chal", "eg", "eth", "gai", "gg", "ghu", "gnalth", "gobah", "gobb",
    "gog", "grax", "groam", "gyaa", "gyee", "haag", "jhool", "jool", "jub", "kaaz", "karg", "kaz", "khark", "krau", "kriv", "kuaz", "kudu", "lchor", "lmaal", "luri",
    "malk", "marag", "melth", "moaz", "molth", "morb", "moru", "mulk", "muz", "nau", "nid", "ninj", "nul", "nym", "olb", "phaal", "raag", "ranag", "rilthu", "rioch",
    "riog", "rioth", "rogog", "ruk", "ruz", "shai", "shu", "trolg", "trulg", "tzu", "urb", "vol", "vrath", "vulu", "wig", "xaag", "xaga", "xool", "xua", "zmoaz"
]

# Table 2-13: Arch-Demonic or Evil God Epithets
EPITHET_PART_1 = [
    "Binder", "Biter", "Breaker", "Burier", "Capturer", "Cauterizer", "Changer", "Claw", "Constrainer", "Constrictor", "Decayer", "Despoiler", "Destroyer", "Displacer", "Drinker", "Eater", "Enchanter", "Enkindler", "Enslaver", "Entangler",
    "Forager", "Harrier", "Haunter", "Hunter", "Igniter", "Invader", "Kindler", "Looter", "Madness", "Marauder", "Melter", "Piercer", "Pillager", "Plunderer", "Poisoner", "Questioner", "Raider", "Ransacker", "Remaker", "Scorcher",
    "Scourge", "Seizer", "Shatterer", "Shifter", "Shriveler", "Slayer", "Stalker", "Taker", "Talon", "Tangler", "Thief", "Tormenter", "Trapper", "Twister", "Unmaker", "Unraveler", "Warper", "Waster", "Winnower", "Witherer"
]

EPITHET_PART_2 = [
    "of Cities", "of Dimensions", "of Dreams", "of Empires", "of Forests", "of Kingdoms", "of Kings", "of Lakes", "of Magics", "of Moons", "of Oracles", "of Planes", "of Portals", "of Seas", "of Souls", "of Stars", "of Temples", "of the Spheres", "of Wizards", "of Worlds"
]

def generate_demonic_name():
    """
    Generate a two-part demonic name (e.g., Aagrax).
    """
    prefix = random.choice(PART_1)
    suffix = random.choice(PART_2)
    return f"{prefix}{suffix}"

def generate_demonic_epithet(include_part_1=True, include_part_2=True):
    """
    Generate a demonic epithet (e.g., "The Breaker of Empires").
    """
    if not include_part_1 and not include_part_2:
        return ""
        
    res = "The"
    if include_part_1:
        res += f" {random.choice(EPITHET_PART_1)}"
    
    if include_part_2:
        res += f" {random.choice(EPITHET_PART_2)}"
        
    return res

def generate_full_demonic_name():
    """
    Generate a full demonic name with an epithet (e.g., "Aagrax, The Breaker of Empires").
    """
    name = generate_demonic_name()
    epithet = generate_demonic_epithet()
    return f"{name}, {epithet}"
