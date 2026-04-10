import random

# Table 4-15: Type of Castle
# 01-12 Concentric castle (two surrounding outer baileys)
# 13-25 Keep
# 26-38 Keep and Bailey with Gatehouse
# 39-51 Keep and Bailey with towers, and Gatehouse
# 52-64 Keep, inner bailey, outer bailey and Gatehouse
# 65-77 Motte and bailey, no keep
# 78-90 Shell Keep (stone bailey)
# 91-00 Single large tower (donjon)
CASTLE_TYPES = {
    12: "Concentric castle (two surrounding outer baileys)",
    25: "Keep",
    38: "Keep and Bailey with Gatehouse",
    51: "Keep and Bailey with towers, and Gatehouse",
    64: "Keep, inner bailey, outer bailey and Gatehouse",
    77: "Motte and bailey, no keep",
    90: "Shell Keep (stone bailey)",
    100: "Single large tower (donjon)"
}

# Table 4-16: Unusual Castles
UNUSUAL_CASTLES = {
    10: "Only entrance is underground (caverns/water channels)",
    20: "Built of bones",
    30: "Carvings/gargoyles can be animated to defend",
    40: "Cloud castle ruins",
    50: "Includes dimensional defenses",
    60: "Involves levitating towers, fire-platforms, or entrances",
    70: "Irregular, like coral formation",
    80: "Made of living plants (thorns, trees, etc.)",
    90: "Numerous trapped entrances; 'right' one changes magically",
    100: "Windowless, door-less; only access is underground"
}

# Table 4-17: People in a Castle
CASTLE_PEOPLE = {
    5: ("Almoner", "In charge of distributing alms to the poor"),
    10: ("Apothecary", "Physician and preparer of medicines"),
    15: ("Armorer", "Skilled blacksmith making weapons and armor"),
    20: ("Bailiff", "Administrative officer for the lord's land/village"),
    25: ("Barber", "Cuts hair and does bloodletting"),
    30: ("Blacksmith", "Handles regular tasks like shoeing horses"),
    35: ("Butler", "In charge of cellars and provision/storage of beer"),
    40: ("Candlemaker", "Responsible for castle lighting needs"),
    45: ("Carpenter", "Handles structural repair and furniture"),
    50: ("Castellan/Constable", "The boss; ultimately responsible for the castle"),
    55: ("Chancellor", "Personal secretary to a noble"),
    60: ("Chaplain", "The castle's religious counselor"),
    65: ("Clerk", "Responsible for accounts, math, and writing"),
    70: ("Cook/Kitchen staff", "Feeds everyone from servants to nobles"),
    75: ("Gardener", "Maintains vegetable/herb gardens and earthworks"),
    80: ("Jester", "Local comic relief"),
    85: ("Keeper of the Wardrobe", "Responsible for clothes, laundry, and tailoring"),
    90: ("Marshall", "In charge of transportation, wagons, and horses"),
    95: ("Lord", "The noble resident (vassal or direct owner)"),
    100: ("Porter", "Grant access at the gatehouse")
}

# Text 2: General Condition
CASTLE_CONDITION = ["Perfect", "Worn", "Worn", "Aged", "Aged", "Crumbling"]

# Text 3: Keep
KEEP_SHAPES = {3: "Square/Rectangle", 5: "Round", 6: "Shell (hollow cylinder)"}
DEFENSIVE_FEATURES = {
    6: "None", 
    7: "Ballista", 8: "Boiling oil", 9: "Catapult", 
    10: "Hoarding", 11: "Iron spikes", 12: "Piles of rocks"
}
NON_DEFENSIVE_FEATURES = {
    6: "None",
    7: "Banners/Flags", 8: "Gargoyles", 9: "Heads/Bodies", 
    10: "Overgrown", 11: "Religious symbols", 12: "Secret passage"
}

# Text 4: Defense
EXTRA_DEFENSES = {
    3: "Stone walls and towers",
    4: "Moat (trench)",
    5: "Motte (mound)",
    6: "Wooden palisade"
}

ENCLOSURE_SHAPES = {
    1: ("Square/Rectangle", 4),
    2: ("Trapezium", 4),
    3: ("Pentagon", 5),
    4: ("Hexagon", 6),
    5: ("Octagon", 8),
    6: ("Star", 10),
    7: ("Cross", 12),
    8: ("Circle", "1d3 + 3")
}

GATEHOUSE_CLOSURE = {3: "Portcullis and wooden door", 5: "Drawbridge", 6: "Both"}

MOAT_ENCOUNTERS = {4: "Nothing", 5: "Crocodiles", 6: "Electric eels", 7: "Leeches", 8: "Piranha"}

# Text 5: Disposition
DISPOSITION = {
    2: "Attack on sight",
    5: "Hostile",
    8: "Neutral",
    11: "Welcoming",
    12: "Enthusiastic"
}

# Text 6: Events
EVENT_TIMING = ["Ended earlier", "Is happening now", "Will take place in the future"]
EVENT_NATURE = [
    "Assassination", "Big monster attack", "Ceremony (wedding, etc.)", 
    "Festival/Fair", "Fire", "Plague", "Resources/Gold dwindling", 
    "Rivallord scouting", "Siege/Looting", 
    "Small monsters wanting to establish a lair nearby", 
    "Tournament", "Visit of a notable person"
]

def _get_from_dict(d, roll):
    keys = sorted(d.keys())
    for k in keys:
        if roll <= k:
            return d[k]
    return d[keys[-1]]
