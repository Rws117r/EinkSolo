import random

# Table 11-1: Creator Deity Alignment
CREATOR_ALIGNMENTS = {
    1: "Law (all)",
    2: "Chaos (all)",
    3: "Neutral (all)",
    4: "Lawful Good",
    5: "Lawful Neutral",
    6: "Lawful Evil",
    7: "Neutral Good",
    8: "Neutral Evil",
    9: "Chaotic Good",
    10: "Chaotic Neutral",
    11: "Chaotic Evil",
    12: "True Neutral"
}

# Table 11-2: Failure Allegory
FAILURE_ALLEGORIES = {
    1: "Blind",
    2: "Insane",
    3: "Deaf",
    4: "Unpredictable",
    5: "Eldritch Horror",
    6: "So Very Alien and Different",
    7: "Doesn't Care",
    8: "Clumsy",
    9: "Deliberately not using omniscience/omnipotence",
    10: "Attention is focused elsewhere (cannot be everywhere at once)"
}

# Table 11-3: Current Status
CREATOR_STATUS = {
    3: "Still alive and in command of most of the gods",
    4: "Dead",
    5: "Insane",
    6: "Sleeping",
    7: "Still alive but in hiding, exile, or prison",
    8: "Damaged or wounded"
}

# Table 11-4: Traditional Description
CREATOR_DESCRIPTIONS = {
    1: "Human appearance",
    2: "Human with animal head",
    3: "Giant bug-like creature, wholly alien (Eldritch Horror)",
    4: "Giant mammal",
    5: "Giant fish-like creature",
    6: "Giant bird",
    7: "Dragon or giant reptilian creature",
    8: "Giant amphibian-type creature",
    9: "A formless ooze or cloud",
    10: "Part animal, part human",
    11: "Formless light or darkness",
    12: "Machine or constructed being"
}

# Table 11-5: Methods of Creation
CREATION_METHODS = {
    1: "Mines cosmic material and populates the resulting world.",
    2: "Looks around and 'activates' existing cosmic matter.",
    3: "Places things in position like a master builder/mosaic artist.",
    4: "Lays eggs that hatch into realities and civilizations.",
    5: "Forms things from cosmic clay or mud like a potter.",
    6: "Forms things from metal in a celestial forge.",
    7: "Spins and weaves cosmic threads into a final reality.",
    8: "Carves realities from cosmic wood.",
    9: "Paints or draws things which then become real.",
    10: "Singing brings the multiverse into creation."
}

# Table 11-6: Monotheism Types
MONOTHEISM_TYPES = {
    1: "True Monotheism: All other gods are expressions of the one.",
    2: "Ruler of other gods: Own god is the only one worth worshipping.",
    3: "Especially beloved: Lead god is 'native', all others are 'foreign'."
}

# Table 11-7: Mono Lead roles
MONOTHEISM_LEADS = {
    20: "Creator-Deity",
    40: "Law-Giver",
    60: "Complex Deity",
    80: "Randomly-Generated Deity",
    100: "Foreign Deity with new status"
}

# Table 11-31: Areas of Divine Power (300 Entries)
DIVINE_AREAS_1 = [
    "A Monster Type", "Accidents", "Air", "Alchemy", "Alleyways and Turnings", "Ancestry", "Animals", "Appointments and Honors", "Arcana", "Architecture",
    "Armaments", "Art", "Autumn", "Avarice", "Balance", "Bargains", "Battle", "Beauty", "Beer", "Beggars",
    "Belches", "Berserker Rage", "Betrayal", "Birds", "Blades and Points", "Blights", "Blood", "Books", "Bowls and Basins", "Bravery and Courage",
    "Bread", "Bugs", "Bureaucracy", "Buttons and Fastenings", "Cats", "Caverns", "Change", "Chaos", "Charity", "Charlatans",
    "Charms and Domination", "Cheese", "Circles", "Cities", "Civilization", "Clouds and Mist", "Coincidence and Conjunction", "Cold", "Community", "Confusion",
    "Cooking", "Corruption", "Counting and Tallies", "Craft and Creating", "Crossroads", "Cubs and Children", "Cunning plans", "Curses and Ill Will", "Cycles, Repetition and Tradition", "Dancing",
    "Darkness", "Dawn", "Dead bodies", "Death", "Desert", "Destruction", "Dexterity", "Digging, Burrowing, and Tunnels", "Discoveries", "Disease and Plague",
    "Disguise and Masks", "Dishonor", "Dogs", "Drama, Theater, and Poetry", "Dreams", "Drugs and Hallucinogens", "Drunkenness", "Dwarves", "Earth", "Eccentricity and Variation",
    "Elegance", "Elves", "Emptiness, Void, and Space", "Endurance", "Envy", "Escapes and Excuses", "Evil", "Explosions", "Eyes", "Fairs",
    "Falling and Rising", "Family", "Famine", "Fate", "Fertility", "Fey", "Filth", "Fire", "Fish", "Fishermen"
]

DIVINE_AREAS_2 = [
    "Floods", "Flowers", "Fools", "Forests", "Forge", "Forgery", "Forgotten things", "Fortune", "Freedom", "Frogs and Toads",
    "Gaps and Omissions", "Gardens", "Garments", "Generosity", "Glory", "Gluttony", "Glyphs and Sigils", "Gnomes", "Good", "Good Rulership",
    "Graves", "Greed", "Guile, Cunning, and Wits", "Hair", "Halflings", "Harvest", "Hatred", "Hazards, Ventures, and Gambles", "Healing", "Hearth",
    "Heraldry", "Herd animals", "Hiding and Concealment", "Hills", "History, writings, and records", "Honey", "Hope", "Horror", "Humility", "Hunt",
    "Hunted, prey, fugitives", "Illusion", "Insults and Innuendo", "Invention", "Itches and Itching", "Jewelry and Gems", "Joy", "Judgement", "Justice", "Justified Irritation",
    "Knighthood and Paladins", "Knots", "Knowledge", "Law", "Lawyers", "Lies", "Life", "Light", "Lords", "Love",
    "Loyalty", "Luck", "Lust", "Machines", "Madness", "Magic", "Market squares", "Marshes and Swamps", "Measurement", "Medicines and Antidotes",
    "Memory", "Messengers", "Metal", "Metalwork", "Mind", "Minor Hindrances", "Mirrors", "Mirth", "Mishaps", "Moon",
    "Mountains", "Murder", "Mushrooms and Fungus", "Music", "Musicians", "Nature", "Navigation and Directions", "Night", "Nobility", "Oaths",
    "Oceans and Seas", "Old Age", "Opening and Unlocking (locks and fastenings)", "Orchards", "Order", "Outcasts", "Outlaws and Pirates", "Pain", "Patience", "Patterns"
]

DIVINE_AREAS_3 = [
    "Peace", "Peasants and the Downtrodden", "Perseverance", "Persuasion and Diplomacy", "Planning", "Plants", "Pleasure", "Plots, Plans, and Organization", "Poisons", "Portals",
    "Pottery", "Preservation", "Pride", "Prisoners and Captives", "Protection", "Raids", "Rain", "Rats", "Renewal", "Repose",
    "Reptiles", "Retribution", "Revelry", "Riddles", "Righteous Indignation", "Rivers", "Roads", "Roots", "Runes", "Sailors",
    "Schadenfreude", "Scrying", "Searches and Finding", "Seasons", "Secrets", "Seeds", "Shadows", "Shadows", "Ships and Boats", "Shorelines, Edges and Borders",
    "Sight and Prophecy", "Silence", "Skill", "Sleep", "Slimes and Oozes", "Sloth", "Smells", "Snares", "Spiders", "Spring",
    "Stars and Heavens", "Stone", "Storms", "Strength", "Strife", "Suffering", "Summer", "Sun", "Surprises", "Technology",
    "Temperance", "The Hearth", "Thieves", "Thorns", "Thresholds", "Throws and Tosses", "Thunder", "Tides and Forces", "Time", "Torment",
    "Trade", "Trails and Footprints", "Travel", "Treachery and Treason", "Trees", "Trickery", "Truces and parlay", "Twilight", "Twists", "Tyranny",
    "Undeath", "Unlikely outcomes", "Vengeance", "Villages", "War", "Water", "Weather", "Weaving", "Weeds", "Wells",
    "Wild escapades", "Wild magic", "Wilderness", "Wind", "Wine and Vines", "Winter", "Wisdom", "Worms", "Wrath", "Zeal"
]

DIVINE_AREAS = DIVINE_AREAS_1 + DIVINE_AREAS_2 + DIVINE_AREAS_3

# Specific Deity Archetypes
# Table 11-13: Art Deity
ART_SECONDARIES = {
    1: "Music", 2: "Paintings or drawing", 3: "Song", 4: "Poetry", 5: "Sculpture", 6: "Plays and drama"
}

# Table 11-14: Battle Gods
BATTLE_SECONDARIES = {
    3: "Appointments and Honors", 6: "Archery and Missile Weapons", 9: "Armaments", 12: "Battle", 15: "Berserker Rage",
    18: "Blades and Points", 21: "Bravery and Courage", 24: "Endurance", 27: "Fate", 30: "Glory", 33: "Good",
    36: "Heraldry", 39: "Hope", 42: "Knighthood and Paladins", 45: "Lords", 48: "Loyalty", 51: "Luck", 54: "Nobility",
    57: "Oaths", 60: "Order", 63: "Outcasts", 66: "Peasants and the Downtrodden", 69: "Perseverance", 72: "Prisoners and Captives",
    75: "Raids", 78: "Skill", 81: "Storms", 84: "Strength", 87: "The Hunt", 91: "The Hunted, Prey, Fugitives",
    94: "Thunder", 97: "War", 100: "Wrath"
}

# Table 11-15: Battle Legend
BATTLE_LEGENDS = {
    1: "A deity of battle-rage and berserking.",
    2: "Known for skillful leadership of other gods in battle.",
    3: "Renowned for prowess in one-on-one combat.",
    4: "Possesses a Mythic Item (weapon/armor) that grants most of their skill.",
    5: "Rides a celestial steed or mount that grants them combat power.",
    6: "Unwavering bravery; known for turning the tide when all seems lost.",
    7: "Mainly known as a master archer.",
    8: "Focuses on scouting, wits, and tactical direct combat."
}

# Table 11-16: Craft Deity
CRAFT_SECONDARIES = {
    1: "Smith or Metalworker", 2: "Weaver", 3: "Potter", 4: "Leatherworker", 5: "Brewer", 6: "Builder"
}

# Table 11-17: Guardian Deity
GUARDIAN_MYTHS = {
    1: "Guards a bridge or gate to the territory of the gods.",
    2: "Patrols the outskirts of the territory of the gods.",
    3: "A divine Watchman, responding to trouble like a policeman.",
    4: "A Steward/Accountant, protecting the possessions of the gods."
}

# Table 11-17: Guardian Secondaries
GUARDIAN_SECONDARIES = {
    1: "Armor", 2: "Shields", 3: "Walls", 4: "Gates", 5: "Locks", 6: "Watchfulness"
}

# Table 11-18: Healer Deity
HEALER_SECONDARIES = {
    1: "A Monster Type", 2: "Accidents", 3: "Air", 4: "Alchemy", 5: "Arcana", 6: "Art", 7: "Balance", 8: "Birds",
    9: "Bravery and Courage", 10: "Cats", 11: "Civilization", 12: "Clouds and Mist", 13: "Craft and Creating",
    14: "Cycles, Repetition and Tradition", 15: "Darkness", 16: "Dawn", 17: "Desert", 18: "Disease and Plague",
    19: "Disguise and Masks", 20: "Dogs", 21: "Dreams", 22: "Earth", 23: "Elegance", 24: "Falling and Rising",
    25: "Family", 26: "Fertility", 27: "Fey", 28: "Flowers", 29: "Forests", 30: "Forgotten Things", 31: "Freedom",
    32: "Frogs and Toads", 33: "Gardens", 34: "Generosity", 35: "Glyphs and Sigils", 36: "Gnomes", 37: "Goodness",
    38: "Hearth", 39: "Herd Animals", 40: "Hills", 41: "History, Writings, and Records", 42: "Hope",
    43: "Hunted, Prey, Fugitives", 44: "Jewelry and Gems", 45: "Joy", 46: "Judgement", 47: "Night", 48: "Outcasts",
    49: "Pain", 50: "Peace", 51: "Peasants and the Downtrodden", 52: "Persuasion and Diplomacy", 53: "Planning",
    54: "Plants", 55: "Pleasure", 56: "Poisons", 57: "Portals", 58: "Pottery", 59: "Prisoners and Captives",
    60: "Protection", 61: "Rain", 62: "Renewal", 63: "Repose", 64: "Reptiles", 65: "Rivers", 66: "Sight and Prophecy",
    67: "Skill", 68: "Sleep", 69: "Slimes and Oozes", 70: "Spiders", 71: "Stars and Heavens", 72: "Stone",
    73: "Sun", 74: "Technology", 75: "Temperance", 76: "Travel", 77: "Trees", 78: "Twilight", 79: "Water",
    80: "Knowledge", 81: "Wind", 82: "Wine and Vines", 83: "Wisdom", 84: "Unlikely Outcomes", 85: "Smells",
    86: "Secrets", 87: "Preservation", 88: "Patterns", 89: "Old Age", 90: "Mushrooms and Fungus", 91: "Medicines and Antidotes",
    92: "Itches and Itching", 93: "Fortune", 94: "Drugs and Hallucinogens", 95: "Cubs and Children", 96: "Life",
    97: "Belches", 98: "Blood", 99: "Books", 100: "Bowls and Basins"
}

# Table 11-19: Healer Myth
HEALER_MYTHS = {
    1: "Possesses intrinsic powers of healing.",
    2: "Uses a device or Mythic Item that heals.",
    3: "Is basically a divine doctor, with vast medical knowledge.",
    4: "Is an alchemist who concocts magical medicines.",
    5: "Has an animal companion that performs the magical healing.",
    6: "Summons healing weather (mist, rain, etc.) to cure the sick."
}

# Table 11-20: Leader Authority
LEADER_AUTHORITY = {
    1: "Father or mother of the gods.",
    2: "Grandparent of the gods.",
    3: "Elected by the gods to the role.",
    4: "Chosen by lottery or game of chance.",
    5: "Given a symbol of leadership by a Mysterious Figure or Cosmic Law.",
    6: "Stole a symbol of leadership from a powerful place or creature.",
    7: "Bargained for/fought for a symbol of leadership from an antagonist.",
    8: "Appointed by an older, now-dead god.",
    9: "Divined leadership by watching patterns of the multiverse.",
    10: "An oracle or soothsayer pronounced them destined to lead."
}

# Table 11-20: Leader Secondaries
LEADER_SECONDARIES = {
    1: "Nobility", 2: "Oaths", 3: "Laws", 4: "Heraldry", 5: "Kings", 6: "Queens"
}

# Table 11-21: Provider Role
PROVIDER_ROLES = {
    1: "Farmer", 2: "Herder", 3: "Cook", 4: "Fisher", 5: "Gardener", 6: "Hunter"
}

# Table 11-21: Provider Secondaries
PROVIDER_SECONDARIES = {
    1: "Harvest", 2: "Livestock", 3: "Bread", 4: "Water", 5: "Fruit", 6: "Meat"
}

# Table 11-22: Complex Deity (1-100 Columns)
COMPLEX_COL1 = {
    1: "Ancestry", 2: "Appointments and Honors", 3: "Architecture", 4: "Art", 5: "Balance", 6: "Bargains", 7: "Beauty", 
    8: "Beggars", 9: "Books", 10: "Bowls and Basins", 11: "Bread", 12: "Bureaucracy", 13: "Charity", 14: "Cheese", 
    15: "Circles", 16: "Cities", 17: "Civilization", 18: "Clouds and Mist", 19: "Cold", 20: "Community", 21: "Cooking", 
    22: "Counting and Tallies", 23: "Craft and Creating", 24: "Cubs and Children", 25: "Dancing", 26: "Dawn", 
    27: "Drama, Theater, and Poetry", 28: "Dreams", 29: "Elegance", 30: "Fairs", 31: "Family", 32: "Fate", 33: "Fertility", 
    34: "Fortune", 35: "Freedom", 36: "Gardens", 37: "Generosity", 38: "Glory", 39: "Good", 40: "Good Rulership", 
    41: "Healing", 42: "History, Writings, and Records", 43: "Hope", 44: "Humility", 45: "Invention", 46: "Joy", 
    47: "Judgement", 48: "Justice", 49: "Knowledge", 50: "Law", 51: "Life", 52: "Light", 53: "Love", 54: "Luck", 
    55: "Machines", 56: "Magic", 57: "Market Squares", 58: "Measurement", 59: "Medicines and Antidotes", 60: "Memory", 
    61: "Messengers", 62: "Music", 63: "Musicians", 64: "Nature", 65: "Navigation and Directions", 66: "Nobility", 
    67: "Old Age", 68: "Order", 69: "Outcasts", 70: "Patience", 71: "Peace", 72: "Peasants and the Downtrodden", 
    73: "Plenty", 74: "Pottery", 75: "Preservation", 76: "Rain", 77: "Roads", 78: "Seasons", 79: "Seeds", 
    80: "Ships and Boats", 81: "Storms", 82: "Technology", 83: "Temperance", 84: "Forge", 85: "Harvest", 
    86: "Hearth", 87: "Mind", 88: "Sun", 89: "Wind", 90: "Thunder", 91: "Tides and Forces", 92: "Time", 
    93: "Trade", 94: "Travel", 95: "Villages", 96: "Weaving", 97: "Wells", 98: "Wine and Vines", 99: "Winter", 100: "Wisdom"
}

COMPLEX_COL2 = {
    1: "A Monster Type", 2: "Accidents", 3: "Arcana", 4: "Avarice", 5: "Battle", 6: "Beauty", 7: "Berserker Rage", 
    8: "Betrayal", 9: "Birds", 10: "Blights", 11: "Blood", 12: "Bugs", 13: "Caverns", 14: "Change", 15: "Chaos", 
    16: "Charlatans", 17: "Charms and Domination", 18: "Clouds and Mist", 19: "Coincidence and Conjunctions", 
    20: "Cold", 21: "Corruption", 22: "Curses and Ill-Will", 23: "Darkness", 24: "Death", 25: "Destruction", 
    26: "Disease and Plague", 27: "Disguise and Masks", 28: "Dreams", 29: "Drugs and Hallucinogens", 30: "Elegance", 
    31: "Envy", 32: "Evil", 33: "Explosions", 34: "Eyes", 35: "Falling and Rising", 36: "Famine", 37: "Fate", 
    38: "Filth", 39: "Fire", 40: "Floods", 41: "Fortune", 42: "Gaps and Omissions", 43: "Garments", 44: "Greed", 
    45: "Guile, Cunning, and Wits", 46: "Hatred", 47: "Hiding and Concealment", 48: "Hunt", 49: "Illusion", 
    50: "Jewelry and Gems", 51: "Knots", 52: "Lies", 53: "Luck", 54: "Machines", 55: "Madness", 56: "Magic", 
    57: "Marshes and Swamps", 58: "Minor Hindrances", 59: "Mishaps", 60: "Murder", 61: "Mushrooms and Fungus", 
    62: "Night", 63: "Old Age", 64: "Outlaws and Pirates", 65: "Pain", 66: "Poisons", 67: "Pride", 68: "Raids", 
    69: "Rats", 70: "Reptiles", 71: "Retribution", 72: "Runes", 73: "Shadows", 74: "Silence", 75: "Slimes and Oozes", 
    76: "Snares", 77: "Storms", 78: "Strife", 79: "Strife", 80: "Suffering", 81: "Thorns", 82: "Thunder", 
    83: "Tides and Forces", 84: "Time", 85: "Torment", 86: "Treachery and Treason", 87: "Trickery", 88: "Twilight", 
    89: "Twists", 90: "Tyranny", 91: "Undeath", 92: "Vengeance", 93: "War", 94: "Water", 95: "Wild Escapades", 
    96: "Wild Magic", 97: "Wind", 98: "Winter", 99: "Worms", 100: "Wrath"
}

# Table 11-23: Travel Method
TRAVEL_METHODS = {
    1: "In a Mythic Vehicle.",
    2: "On a mythological steed.",
    3: "In a powerful boat.",
    4: "Using a magical garment that allows flight.",
    5: "As a passenger in weird vehicles.",
    6: "Overland on horseback, aided by a Mythic Item."
}

# Trade and Travel secondaries
TRADE_SECONDARIES = {
    1: "Mercantilism", 2: "Markets", 3: "Trade", 4: "Contracts", 5: "Wealth", 6: "Coins"
}

TRAVEL_SECONDARIES = {
    1: "Roads", 2: "Paths", 3: "Maps", 4: "Navigation", 5: "Merchants", 6: "Exploration"
}

# Table 11-24: Trickster Secondary
TRICKSTER_SECONDARIES = {
    3: "Alleyways and Turnings", 6: "Avarice", 9: "Cats or Rats", 12: "Charlatans", 15: "Coincidence and Conjunction",
    18: "Guile, Cunning, and Wits", 21: "Darkness", 24: "Dexterity", 27: "Discoveries", 30: "Disguise and Masks",
    33: "Drama, Theater, and Poetry", 36: "Escapes and Excuses", 39: "Freedom", 42: "Hazards, Ventures, and Gambles",
    45: "Hiding and Concealment", 48: "Luck or Fortune", 51: "Opening and Unlocking", 54: "Outlaws and Pirates",
    57: "Persuasion and Diplomacy", 60: "Planning", 63: "Plots, Plans, and Organization", 66: "Portals",
    69: "Revelry", 72: "Searches and Finding", 75: "Secrets", 78: "Skill", 81: "Surprises", 84: "Thieves",
    87: "Throws and Tosses", 91: "Travel", 94: "Twists", 97: "Unlikely Outcomes", 100: "Wild Escapades"
}

# Table 11-25: Trickster Myth
TRICKSTER_MYTHS = {
    1: "Spies on enemies of the gods through infiltration.",
    2: "Bargains for the gods, usually tricking the other side and keeping a cut.",
    3: "Cheats the gods occasionally, suffering periodic consequences.",
    4: "Explores new places, gets in trouble, and needs rescue.",
    5: "Rescues other gods from antagonists through deception.",
    6: "Causes major problems for no reason that the others must solve."
}

# Table 11-26: Nature Portrayal
NATURE_PORTRAYALS = {
    1: "As an actual tree or plant with a static location.",
    2: "As a large, talking animal.",
    3: "As a human or human-like figure.",
    4: "As a deity of pure wilderness and wild animals.",
    5: "As a deity of cultivation and domestication (farming).",
    6: "As a force of nature (cloud, waterfall)."
}

# Nature Sub-Areas (Inferred for variety)
NATURE_SUB_AREAS = [
    "Forests", "Mountains", "Oceans", "Deserts", "Rivers", "Plants", "Animals", "Seasons"
]

# Table 11-27: Judge Authority
JUDGE_AUTHORITY = {
    1: "Mother of the gods.",
    2: "Father of the gods.",
    3: "Grandparent of the gods.",
    4: "Elected by the gods.",
    5: "Chosen by lottery.",
    6: "Received interpretation from Cosmic Law.",
    7: "Stole interpretation from a mythic place.",
    8: "Bargained for interpretation from an antagonist.",
    9: "Appointed by a dead elder god.",
    10: "Created interpretation by watching multiverse patterns."
}

# Table 11-28: Judge Source
JUDGE_SOURCES = {
    1: "An oracle device (Tarot, I-Ching).",
    2: "Personal wisdom and logic.",
    3: "A legendary book only the judge can read.",
    4: "A legendary book only the judge can interpret.",
    5: "Counselors (a duo or trio of animals).",
    6: "A measuring device (scales) to compare claims."
}

# Table 11-29: General Beneficence (5 Columns)
GENERAL_COLS = [
    ["Art", "Beauty", "Charity", "Civilization", "Community", "Craft and Creating", "Dawn", "Endurance", "Family", "Fertility"],
    ["Fortune", "Freedom", "Generosity", "Good", "Harvest", "Healing", "Hearth", "Herd Animals", "Hope", "Hunt"],
    ["Joy", "Judgement", "Justice", "Knowledge", "Law", "Life", "Light", "Luck", "Magic", "Memory"],
    ["Metalwork", "Moon", "Nature", "Navigation and Directions", "Oceans and Seas", "Order", "Peace", "Plants", "Pottery", "Preservation"],
    ["Protection", "Rain", "Renewal", "Seasons", "Stars and Heavens", "Sun", "The Hearth", "Tides and Forces", "Time", "Wisdom"]
]

# Table 11-30: Weather
WEATHER_AREAS = {
    1: "Clouds and Mist", 2: "Cold", 3: "Rain", 4: "Storms", 5: "Wind", 6: "Thunder",
    7: "Tides and Forces", 8: "Nature", 9: "Winter", 10: "Harvest", 11: "Seasons", 12: "Weather"
}

# Creator Deity Name Generation
# Table 2-1: Short Names
SHORT_NAME_COL1 = ["A", "O", "U", "A", "O", "U", "Tsa", "Jha", "Ola", "Ulu"]
SHORT_NAME_COL2 = ["ka", "lm", "mur", "os", "phos", "shu", "ta", "tha", "to", "tuan"]

# Table 2-2: Hyphenated Names
HYPHEN_PART1 = [
    "Ko-", "To-", "Azul-", "Azo-", "Zul-", "Tsa-", "Tso-", "Enu-", "Anu-", "Una-",
    "Tsul-", "Tsu-", "Ma-", "Tha-", "Ta-", "Te-", "Ga-", "Ge-", "Che-", "Cho-"
]
HYPHEN_PART2 = [
    "Atun", "Aman", "Kora", "Bar", "Amna", "Mard", "Maresh", "Tar", "Taan", "Tesh",
    "Toa", "Moath", "Atha", "Atsa", "Ultan", "Umna", "Oom", "Oon", "Koa", "Moa"
]

# Table 2-3: Epithets
CREATOR_EPITHETS = [
    "The Shaper", "The Beginning", "The Builder", "The Crafter", "The Creator",
    "The Dawn", "The Emerger", "The Fashioner", "The Genesis", "The Ignitor",
    "The Inceptor", "The Initiator", "The Locus", "The Maker", "The Origin",
    "The Originator", "The Prism", "The Seed", "The Weaver", "The World-Smith"
]

def generate_creator_name():
    # 50/50 Short vs Hyphenated
    if random.randint(1, 2) == 1:
        base = random.choice(SHORT_NAME_COL1) + random.choice(SHORT_NAME_COL2)
    else:
        base = random.choice(HYPHEN_PART1) + random.choice(HYPHEN_PART2)
    
    # Add epithet
    epithet = random.choice(CREATOR_EPITHETS)
    return f"{base}, {epithet}"

# Physical Appearance
# Table 11-32: Hybrid Forms
HYBRID_FORMS = {
    1: "Human with an animal head.",
    2: "Human with fur, chitin shell, or feathers.",
    3: "Human with animal legs (or tail/lower body).",
    4: "Human torso with animal head and legs.",
    5: "Human with animal head and wings.",
    6: "Human with animal legs and wings.",
    7: "Human with extra arms and an animal head.",
    8: "Human with multiple eyes and animal legs."
}

# Table 11-33: Quick Animal Types
QUICK_ANIMALS = {
    1: "Simian (Ape/Monkey)", 2: "Rodent (Rat/Beaver)", 3: "Reptilian (Snake/Lizard)",
    4: "Arachnid/Insect (Spider/Bug)", 5: "Avian (Hawk/Heron)", 6: "Feline (Cat/Lion)"
}

# Table 11-34/35: Massive Animal List (Inferred combined)
DETAILED_ANIMALS = [
    "Aardvark", "Alligator", "Alpaca", "Ant", "Antelope", "Baboon", "Badger", "Bat", "Bear", "Beaver",
    "Boar", "Buffalo", "Camel", "Cat", "Cheetah", "Cobra", "Cougar", "Coyote", "Crocodile", "Deer",
    "Dolphin", "Donkey", "Dragon", "Eagle", "Elephant", "Falcon", "Fox", "Frog", "Giraffe", "Goat",
    "Gorilla", "Hawk", "Hippopotamus", "Horse", "Hyena", "Iguana", "Jackal", "Jaguar", "Kangaroo", "Koala",
    "Leopard", "Lion", "Llama", "Lynx", "Mammoth", "Monkey", "Moose", "Octopus", "Owl", "Panther",
    "Peacock", "Penguin", "Pig", "Python", "Rabbit", "Raccoon", "Rat", "Raven", "Rhino", "Shark",
    "Snake", "Spider", "Squirrel", "Tiger", "Toad", "Turtle", "Vulture", "Wolf", "Wolverine", "Zebra"
]

# Table 11-36: Formless Perception
FORMLESS_PERCEPTION = {
    1: "Behavior of animals in the vicinity.",
    2: "Behavior of people in the vicinity.",
    3: "Behavior of materials (stone/wood) in the vicinity.",
    4: "Behavior of forces (magic/fire) in the vicinity.",
    5: "Behavior of weather in the vicinity.",
    6: "Behavior of signs (glyphs/writing) in the vicinity.",
    7: "Behavior of doors and portals in the vicinity.",
    8: "Behavior of insects in the vicinity."
}

def _get_from_dict(d, roll):
    keys = sorted(d.keys())
    for k in keys:
        if roll <= k:
            return d[k]
    return d[keys[-1]]

def _roll_d20_odd():
    res = random.randint(1, 100)
    # The trickster table has entries at 3, 6, 9... (multiples of 3)
    # Actually, the logic in generate_trickster_deity was:
    # secondary = religion_logic._get_from_dict(religion_logic.TRICKSTER_SECONDARIES, religion_logic._roll_d20_odd())
    # I should probably just return a roll that aligns with the dictionary keys or use _get_from_dict with a 1-100 roll.
    return random.randint(1, 100)

def generate_judge_stats():
    return {
        "Authority": _get_from_dict(JUDGE_AUTHORITY, random.randint(1, 10)),
        "Source": _get_from_dict(JUDGE_SOURCES, random.randint(1, 6))
    }

def generate_creator_stats():
    align = _get_from_dict(CREATOR_ALIGNMENTS, random.randint(1, 12))
    fail = _get_from_dict(FAILURE_ALLEGORIES, random.randint(1, 10))
    status = _get_from_dict(CREATOR_STATUS, random.randint(1, 8))
    desc = _get_from_dict(CREATOR_DESCRIPTIONS, random.randint(1, 12))
    method = _get_from_dict(CREATION_METHODS, random.randint(1, 10))
    return {
        "Alignment": align,
        "Failure Myth": fail,
        "Status": status,
        "Description": desc,
        "Creation Method": method
    }

def generate_appearance():
    roll = random.randint(1, 3)
    if roll == 1: # Human
        return "Human-like appearance."
    elif roll == 2: # Hybrid
        form = _get_from_dict(HYBRID_FORMS, random.randint(1, 8))
        animal = random.choice(DETAILED_ANIMALS)
        return f"{form} (Animal trait: {animal})"
    else: # Formless
        perception = _get_from_dict(FORMLESS_PERCEPTION, random.randint(1, 8))
        return f"Formless; perceived by {perception}"
