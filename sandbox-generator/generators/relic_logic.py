import random

# Table 11-75: Nature of Relics
RELIC_NATURE = {
    10: "Clothes of hero/saint",
    20: "Deity's body",
    30: "Holy fountain, font, or spring",
    40: "Holy stone or statue",
    50: "Item blessed by deity",
    60: "Item owned by hero/saint",
    70: "Part of deity's body",
    80: "Remnants of hero/saint's body",
    90: "Weapon or armor of hero/saint",
    100: "Writings"
}

# Table 11-76 & 11-77 (Details)
RELIC_DETAILS = {
    "Clothes of hero/saint": {10:"Robe", 20:"Shoes", 30:"Belt", 40:"Hat", 50:"Codpiece", 60:"Glove", 70:"Shirt", 80:"Chains", 90:"Cloak", 100:"Mask"},
    "Deity's body": {30:"Body is husk, deity lives on other plane", 60:"Dark secret; mummified or suspended animation", 70:"Deity resides here, still lives", 80:"Imprisoned", 90:"Insane", 100:"Not actual body; divine attention focused here"},
    "Holy fountain, font, or spring": {10:"Blessed", 20:"Falsely identified", 30:"Gives visions", 40:"Heals", 50:"Non-material source", 60:"Poisonous test", 70:"Raises dead", 80:"Removes curses", 90:"Removes diseases", 100:"Shows other places"},
    "Holy stone or statue": {10:"Animates", 20:"Blessed", 30:"Carved from meteorite/gem/sacred wood", 40:"Falsely identified", 50:"Forbidden to look upon", 60:"Heals at touch", 70:"Raises dead", 80:"Removes curses", 90:"Removes diseases", 100:"Speaks - oracle"},
    "Item blessed by deity": {10:"Amulet", 20:"Black velvet painting or tapestry", 30:"Chariot", 40:"Goblet", 50:"Helmet", 60:"Holy symbol", 70:"Lantern or lamp", 80:"Ring", 90:"Staff", 100:"Statuette"},
    "Item owned by hero/saint": {10:"Amulet", 20:"Crown or coronet", 30:"Goblet", 40:"Helmet", 50:"Holy symbol", 60:"Lantern or lamp", 70:"Plate", 80:"Ring", 90:"Staff", 100:"Statuette"},
    "Part of deity's body": {10:"Arm", 20:"Eye", 30:"Finger", 40:"Foot", 50:"Hair", 60:"Hand", 70:"Head", 80:"Heart", 90:"Leg", 100:"Tooth/Tusk"},
    "Remnants of hero/saint's body": {10:"Bones or teeth", 20:"Ashes", 30:"Brain", 40:"Hair", 50:"Mummified body", 60:"Mummified hand", 70:"Mummified mistress", 80:"Mummified steed", 90:"Skeleton", 100:"Skull"},
    "Weapon or armor of hero/saint": {10:"Bow", 20:"Chain mail", 30:"Gauntlets", 40:"Hammer or mace", 50:"Helmet", 60:"Leather armor", 70:"Plate mail", 80:"Shield", 90:"Spear", 100:"Sword"},
    "Writings": {10:"Clay tablets", 20:"Evil/Cursed/Taboo texts", 30:"Forbidden texts", 40:"Holy writ (cannot be copied)", 50:"Journal", 60:"Letters", 70:"Map to sacred location", 80:"Map to tombs", 90:"Secret scriptures", 100:"Stone tablets"}
}

def generate_relic_description():
    roll_nature = random.randint(1, 100)
    nature = _get_from_dict(RELIC_NATURE, roll_nature)
    
    roll_detail = random.randint(1, 100)
    detail = _get_from_dict(RELIC_DETAILS[nature], roll_detail)
    
    return nature, detail

# Priest spell levels (d20)
RELIC_SPELL_LEVELS = {
    8: 1,
    14: 2,
    17: 3,
    19: 4,
    20: 5
}

PRIEST_SPELLS = {
    1: ["Bless", "Cure Light Wounds", "Detect Evil", "Protection from Evil"],
    2: ["Blessing of Courage", "Find Traps", "Hold Person", "Silence 15' Radius"],
    3: ["Continual Light", "Cure Disease", "Lesser Restoration", "Remove Curse"],
    4: ["Cure Serious Wounds", "Neutralize Poison", "Protection from Evil 10' Radius", "Speak with Plants"],
    5: ["Commune", "Cure Critical Wounds", "Flame Strike", "Raise Dead"]
}

def generate_relic_spell():
    roll = random.randint(1, 20)
    level = _get_from_dict(RELIC_SPELL_LEVELS, roll)
    spell = random.choice(PRIEST_SPELLS[level])
    return level, spell

def _get_from_dict(d, roll):
    keys = sorted(d.keys())
    for k in keys:
        if roll <= k:
            return d[k]
    return d[keys[-1]]
