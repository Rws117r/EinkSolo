import random

# 2) Decoration
DECORATIONS = {
    1: "Birdhouses", 2: "Bookshelves", 3: "Carved wood", 4: "Draperies",
    5: "Fishing trophies", 6: "Flags", 7: "Furs", 8: "Glowing crystals",
    9: "Hunting trophies", 10: "Naughty drawings", 11: "Naval themed items",
    12: "Old tools", 13: "Old weapons", 14: "Painted plates", 15: "Paintings",
    16: "Plants", 17: "Porcelain dolls", 18: "Quest/Wanted posters",
    19: "Shields", 20: "Skulls and bones", 21: "Stuffed animals",
    22: "Tapestries", 23: "Torture instruments", 24: "Trophies"
}

# 3) Bartender
BARTENDER_TRAIT_1 = [
    "Absent minded", "Always complaining", "Disturbed", "Flirty", "Funny",
    "Generous", "Good listener", "Grumpy", "Inquisitive", "Jumpy",
    "Loud", "Moody", "Nice", "Playful", "Rude",
    "Silent", "Talkative", "Unpleasant", "Welcoming", "Worrying"
]

BARTENDER_TRAIT_2 = [
    "Always busy", "Checks every coin", "Cocktail master", "Extravagant clothing",
    "Famous in the area", "Has a hidden weapon", "Has lots of piercings",
    "Knows a few magic tricks", "Looking for opportunities", "Needs help",
    "Never washes the glasses", "Not there at the moment", "Older than they seem",
    "Poisons at disposal", "Retired adventurer", "Stunning",
    "Tattooed from head to toes", "Terrible secret", "Thick accent", "Tipsy"
]

# 4) Servers
SERVER_COMMON_TRAITS = [
    "Also work as dancers", "Hate/Love each other", "Have a weapon",
    "Have the same hair color", "Hide their face", "Indistinguishable",
    "Orphans", "Outfit", "Scars", "Sisters/Brothers"
]

SERVER_INDIVIDUAL_TRAITS = [
    "Adventurer in downtime", "Artist", "Burnt face", "Child of the owner",
    "Debt to repay", "Demon waiting for a prey", "Gets lots of tips",
    "Has an identical twin", "Knows the gossip", "Not so young anymore",
    "Pickpockets clients", "Prince(ss) in disguise", "Sells their body",
    "Single parent", "Skilled assassin", "Soon to be parent", "Student",
    "Tattooed", "Unusual outfit", "Very cultured"
]

# 5) Patrons
PATRONS_MOST = {
    1: "Drunks", 2: "Drunks", 3: "Commoners", 4: "Commoners", 5: "Commoners", 6: "Commoners",
    7: "Adventurers", 8: "Bandits/Pirates", 9: "Guards/Soldiers", 10: "Merchants",
    11: "Nobles", 12: "Scholars"
}

PATRONS_SPECIFIC = [
    "Adventurer looking for a party", "Courier", "Drunk and loud dwarf", "Foreign prince(ss)",
    "Halfling dancing on a table", "Highwayman", "Lycanthrope/Vampire", "Man whose table is covered in food",
    "Peasant looking for a retainer job", "Pickpocket", "Priest(ess)", "Recruiter from a guild",
    "Slaver", "Someone celebrating their birthday", "Someone looking to hire adventurers for a quest",
    "Succubus/Incubus", "Tax collector", "Three goblins in disguise", "Traveler", "Vampire hunter"
]

# 6) Entertainment
ENTERTAINERS = {
    1: "None", 2: "None", 3: "None", 4: "None", 5: "None",
    6: "Bard", 7: "Bard", 8: "Bard", 9: "Bard", 10: "Bard", 11: "Bard", 12: "Bard", 13: "Bard",
    14: "Dancers", 15: "Fortune teller", 16: "Humorist", 17: "Jester", 18: "Magician",
    19: "Musicians", 20: "Poet"
}

ACTIVITIES = [
    "Arm wrestling", "Betting", "Billiards", "Bingo", "Books",
    "Brawls", "Cards", "Chess", "Dancing", "Darts throwing",
    "Dice", "Dominoes", "Drinking games", "Eating contest", "Fighting ring",
    "Hot bath", "Knife throwing", "Marbles", "Obstacle course", "Wheel of fortune"
]

# 7) Rooms
ROOMS_BEST = {
    1: "Suite", 2: "Richly decorated and comfortable", 3: "Cozy, with a view",
    4: "Bed, dresser and desk", 5: "Creaking bed and table", 6: "Mattress and chamber pot"
}

ROOMS_SPECIAL = [
    "Badly decorated", "Freezing cold", "Haunted", "Leaking roof",
    "Location of a sinister event", "Rat infested"
]

# 8) Outside
OUTSIDE_AMENITIES = [
    "Beehives", "Carriage stop", "Chicken house", "Dovecote", "Event grounds",
    "Garden", "Mailbox", "Orchard", "Outhouse toilets", "Patio",
    "Pigpen", "Playground", "Pond", "Porch", "Rainwater barrel",
    "Stables", "Tavern products stall", "Tent sites", "Vegetable patch", "Well"
]

# 9) Menu
DRINKS = ["Beer", "Cocktail", "Coconut milk", "Coffee", "Fruit juice", "Hot chocolate", "Lemonade", "Liquor", "Milk", "Wine"]
WINE_TYPES = ["Red", "Rosé", "Sparkling", "White"]

SNACKS = [
    "Cheese & meat platter", "Cheese platter (Small)", "Cheese platter (Large)", "Crisps",
    "Dry sausage", "Fried potatoes", "Fresh vegetables platter", "Hard-boiled eggs and bread",
    "Salad (Plain)", "Salad (With dressing)", "Salted peanuts", "Smoked sausage",
    "Toast with Butter", "Toast with Cheese", "Toast with Fish", "Toast with Ham",
    "Toast with Pâté", "Toast with Salted butter", "Toast with Truffle cream", "Toast with Vegetables",
    "Vinegar pickles"
]

SOUPS = [
    "Artichoke soup", "Asparagus cream", "Boar and chestnut", "Calamari soup", "Carrot soup",
    "Chef’s soup", "Chicken broth", "Chicken cream", "Fish soup", "Granny’s soup",
    "Lobster bisque", "Minestrone", "Mushroom cream", "Oyster soup", "Parsnip soup",
    "Peas and smoked sausage", "Pumpkin cream", "Secret soup", "Tomato cream", "Vegetable broth"
]

APPETIZERS = [
    "Bacon-wrapped sausage", "Beans casserole", "Cheese croquette", "Seafood plate",
    "Terrine (Boar & mushrooms)", "Terrine (Chicken)", "Terrine (Hare)", "Terrine (Pork)", "Terrine (Vegetables)", "Terrine (Zucchini)",
    "Verrine (Foie gras)", "Verrine (Salmon)", "Verrine (Vegetables)"
]

MAIN_DISHES = [
    "Boiled crab", "Carbonnade à la bière", "Leg of lamb", "Lentil meatloaf",
    "Meatballs with brown sauce", "Meatloaf", "Omelet (Bacon)", "Omelet (Cheese)", "Omelet (Fried vegetables)",
    "Quiche", "Rabbit pâté", "Roast (Beef)", "Roast (Chicken)", "Roast (Fish)", "Roast (Pork)",
    "Royal sausage & choucroute", "Sandwich (Cheese)", "Sandwich (Ham)", "Sandwich (Tuna)",
    "Sauteed mushrooms", "Scrambled eggs", "Steak", "Stew (Beef)", "Stew (Pork)", "Stew (Rabbit)", "Stew (Veal)",
    "Stuffed pâtisson", "Stuffed turkey", "Venison", "Vol-au-vent"
]

DESSERTS = [
    "Biscuits", "Cake", "Cheesecake", "Creme (Chocolate)", "Creme (Brûlée)", "Creme (Rice)", "Creme (Pudding)",
    "Fruit jelly", "Marzipan", "Mousse (Chocolate)", "Mousse (Strawberry)", "Mousse (Vanilla)",
    "Pancakes", "Pie/Cobbler (Apple)", "Pie/Cobbler (Cherry)", "Pie/Cobbler (Plum)", "Pie/Cobbler (Strawberry)", "Waffle"
]

# 11) Sign
SIGN_SHAPES = {
    1: "Oval", 5: "Round", 9: "Square", 13: "Rectangle", 17: "Banner", 19: "Shield", 20: "Tankard"
}
SIGN_MATERIALS = ["Wood", "Wrought iron", "Drift wood", "Stained glass", "Glass", "Stone"]
SIGN_POSITIONS = {
    1: "On the facade", 6: "Perpendicular to the facade", 11: "Above the door", 15: "On a pole",
    18: "On a fence", 19: "On a low wall", 20: "On the roof"
}
SIGN_MOUNTING = ["Iron studs", "Wrought iron structure", "Wooden structure"]

SIGN_ILLUSTRATIONS = [
    "Anchor", "Angel", "Boar/Pig", "Bottle", "Brand logo", "Cheese", "Chicken", "Coat of arms",
    "Crow", "Crown", "Cutlery", "Dog/Wolf", "Dragon", "Drunk person", "Eagle", "Face", "Fire",
    "Fish", "Fishing hook", "Flowers", "Fountain", "Fox", "Frog", "Gallows", "Goose", "Grape",
    "Griffin", "Hare", "Heart", "Hearth", "Honeybee", "Horse/Pony/Unicorn", "Horseshoe", "Jester",
    "Knight", "Kraken", "Lion", "Manticore", "Mascot", "Monster head", "Mouse/Rat", "Pinup",
    "Pirate", "Potion", "Sailor", "Ship", "Skull", "Stag", "Tree", "Wizard"
]

SIGN_SPECIAL = {
    1: "Nothing special", 13: "Bug trap", 14: "Clock", 15: "Decorative hanging tankard",
    16: "Decorative moldings", 17: "Glows in the dark", 18: "Lamp", 19: "Magically animated", 20: "Windmill"
}

SIGN_SUBPANELS = {
    1: "No sub-panel", 4: "Catchphrase", 7: "Owner(s) name(s)", 9: "Menu", 11: "Joke", 12: "Motto"
}

CATCHPHRASES = [
    "Bed and breakfast", "Best in town", "Come in", "Family Business", "Pets welcome", "Welcome"
]

# Table 29-13: Adjectives of Awesomeness
ADJECTIVES_AWESOMENESS = [
    "Admirable", "Baroque", "Beautiful", "Bright", "Brilliant", "Celebrated", "Dazzling", "Elegant", "Eminent", "Exceptional",
    "Exquisite", "Fantastic", "Glorious", "Grand", "Impeccable", "Imposing", "Impressive", "Lavish", "Lustrous", "Magnificent",
    "Marvelous", "Matchless", "Outstanding", "Peerless", "Remarkable", "Renowned", "Resplendent", "Rich", "Splendid", "Splendiferous",
    "Splendorous", "Sublime", "Sumptuous", "Superb", "Superlative", "Supreme", "Transcendent", "Unparalleled", "Unsurpassed", "Wondrous"
]

# Table 29-14: Adjectives of Luminosity
ADJECTIVES_LUMINOSITY = [
    "Amber", "Blue", "Bright", "Brilliant", "Dazzling", "Far-reaching", "Flashing", "Flickering", "Flickering", "Green",
    "Holy", "Illuminating", "Inextinguishable", "Lambent", "Luminous", "Lustrous", "Radiant", "Shadowy", "Shining", "Vivid"
]
