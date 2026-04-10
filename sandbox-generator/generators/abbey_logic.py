import random
from generators.name_generators import angelic_names

# 1) Name
ABBEY_NAMES = {
    1: "Blessed-Land",
    2: "Clear-Water",
    3: "Fruitful-Garden",
    4: ("Good-", ["Help", "Hope", "Relief"]), # prefix, options
    5: ("Our-Lady-of-", ["Chastity", "Mercy", "the Poor"]),
    6: "Peaceful-Soul",
    7: "Sacred-Heart",
    8: "Saint-"
}

def generate_name():
    roll = random.randint(1, 10)
    if roll in [1, 2, 3, 6, 7]:
        return ABBEY_NAMES[roll]
    elif roll == 4:
        prefix, options = ABBEY_NAMES[4]
        return prefix + random.choice(options)
    elif roll == 5:
        prefix, options = ABBEY_NAMES[5]
        return prefix + random.choice(options)
    else:
        # 8-10: Saint-...
        return "Saint-" + angelic_names.generate_angelic_name()

CORE_LOCATIONS = [
    "Abbot's room", "Cellars", "Cemetery", "Church", "Cloisters and garden", 
    "Infirmary", "Kitchen and refectory", "Monkscells", "Necessarium (latrines)", 
    "Servants, laborers and tradesmen quarters", "Storehouses"
]

ADDITIONAL_LOCATIONS = {
    "Garden": ["Flowergarden", "Fountain", "Kitchen garden", "Physic garden (medicine)"],
    "Infirmary": ["Bloodletting & purging room", "Drugstore", "Physician's residence", "Room for critical patients"],
    "Religious buildings": ["Chapter house (for meetings)", "Parlour", "School", "Scriptorium and library"],
    "Other": ["Abbot's gateway", "Barns and stables", "Guestrooms", "Vestarium (clothing storage)", "Washhouse", "Watchtower"]
}

ACTIVITIES = {
    "Farming": [
        "Barley (beer)", "Chickens (meat, eggs)", "Cotton", "Cows (meat, milk and cheese)", 
        "Goats (meat, milk and cheese)", "Grapes (wine)", "Hops (beer)", "Orchard (fruits and preserves)", 
        "Pigs (meat)", "Sheep (meat and wool)", "Vegetables", "Wheat (flour and bread)"
    ],
    "Workshop": ["Candlemakers", "Cutlers", "Potters", "Shoemakers", "Smiths", "Tanners"],
    "Other": ["Beekeeping", "Bookshop", "Catering", "Copy & translation", "Exorcism", "Guided tour"]
}

FAME_REASONS = [
    "Age", "Architecture", "Cattle baptism", "Curative (hot) springs", 
    "Domain and landscapes", "Grave of well known bishop", "Key religious celebration", 
    "Meals served to travelers", "Pilgrimage", "Power", "Quality of products"
] # 12-20 is Relic

EVENT_TIMING = ["Ended earlier", "Is happening now", "Will take place in the future"]
EVENT_NATURE = [
    "Broken device", "Cowls shrunken/dyed in red", "Demonic corruption", 
    "Disappearance of the abbot", "Drought/Flood", "Festival/Fair", "Fire", 
    "Looting", "Moles/Rats infestation", "Plague", "Scandal", "Visit of a notable person"
]

HISTORY_EVENTS = [
    "Abandoned then used again", "Changed confession", "Claimed its autonomy", 
    "Destroyed then rebuilt", "Founded {years} years ago", "Has seen better days", 
    "Only one original building remains", "Sponsored by a rich patron", 
    "Started as a knight hermitage", "Used to be a boarding school", 
    "Was relocated", "Was under a spell"
]

def generate_history():
    event = random.choice(HISTORY_EVENTS)
    if "{years}" in event:
        years = random.randint(2, 20) * 10
        event = event.format(years=years)
    return event
