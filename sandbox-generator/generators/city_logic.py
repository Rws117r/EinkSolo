# City Logic Tables

SIZES = {
    1: ("Small", 2),
    2: ("Small", 2),
    3: ("Medium", 3),
    4: ("Medium", 3),
    5: ("Medium", 3),
    6: ("Big", 4)
}

OCCUPATIONS = {
    1: "Brewing (breweries) or Viticulture (vineyard)",
    2: "Cattle breeding (farms, meadows)",
    3: "Farming crops (farms, fields)",
    4: "Fishing (fishery)",
    5: "Hunting (tannery)",
    6: "Logging (sawmills)",
    7: "Metallurgy (forge, foundry)",
    8: "Mining (mine)",
    9: "Pottery (workshop)",
    10: "Trading (caravanserai/port)"
}

CHARACTERISTICS = {
    1: "Nothing", 2: "Nothing", 3: "Nothing", 4: "Nothing", 5: "Nothing",
    6: "Corrupt", 7: "Crowded", 8: "Destroyed", 9: "Dry", 10: "Filthy",
    11: "Holy city", 12: "Humid", 13: "Narrow", 14: "Noisy", 15: "Open",
    16: "Renowned", 17: "Silent", 18: "Tiered", 19: "Unsafe", 20: "Windy"
}

APPEARANCE = {
    1: "Cluttered", 2: "Cobblestone", 3: "Colorful", 4: "Covered with art", 5: "Dark",
    6: "Eerie", 7: "Flowers", 8: "Geometric", 9: "Huge windows", 10: "Light",
    11: "Lots of canals", 12: "Lots of stairs", 13: "Misaligned buildings", 14: "Red bricks", 15: "Stark",
    16: "Tall towers", 17: "White marble", 18: "Wondrous", 19: "Wooden", 20: "Specific color scheme"
}

COLOR_SCHEMES = {
    1: "Black and white",
    2: "Blue and white",
    3: "Grayscale",
    4: "Sand and terracotta"
}

SPECIAL_LOCATIONS = {
    1: "Abandoned building",
    2: "Aqueduct",
    3: "Archaeological site",
    4: "Bridge",
    5: "Burnt/Ruined building",
    6: "Calvary",
    7: "Carriage stop",
    8: "Construction site",
    9: "Famous street",
    10: "Fighting pit",
    11: "Fountain",
    12: "Gallows",
    13: "Junkyard",
    14: "Market hall",
    15: "Military cemetery",
    16: "Monument/Memorial",
    17: "Park",
    18: "Pilgrimage",
    19: "Plaza",
    20: "Slave pit"
}

BUILDING_TYPES = {
    1: "Housing", 2: "Housing", 3: "Housing",
    4: "Business", 5: "Business", 6: "Business", 7: "Business", 8: "Business", 9: "Business", 10: "Business",
    11: "Official", 12: "Official", 13: "Official",
    14: "Religious",
    15: "Public", 16: "Public", 17: "Public",
    18: "Military", 19: "Military", 20: "Military"
}

HOUSING_SUB = {
    1: "Studio", 2: "One bedroom apartment", 3: "Two bedrooms apartment", 4: "Bungalow", 5: "Maisonnette",
    6: "Penthouse", 7: "Mansion", 8: "Hotel room", 9: "Tower", 10: "Boarding house",
    11: "Tent", 12: "Houseboat", 13: "Under a bridge", 14: "Shanty", 15: "Squat",
    16: "Underground bunker", 17: "Wagon", 18: "Treehouse", 19: "Basement", 20: "Hut"
}

BUSINESS_SUB = {
    1: "Alchemist", 2: "Animal trainer: birds", 3: "Animal trainer: horses", 4: "Animal trainer: unusual animals", 5: "Apothecary",
    6: "Architect", 7: "Armorer", 8: "Artist", 9: "Assassin or poisoner", 10: "Astronomer",
    11: "Attorney: civil", 12: "Attorney: criminal", 13: "Baker", 14: "Barber and bloodletter", 15: "Bathhouse",
    16: "Blacksmith", 17: "Boatwright", 18: "Bowyer or fletcher", 19: "Brewery", 20: "Bronze worker",
    21: "Brothel", 22: "Butcher", 23: "Cabinetmaker/joiner", 24: "Candlemaker", 25: "Caravanserai",
    26: "Carpenter", 27: "Carpet merchant", 28: "Carpet weavers", 29: "Cartographer", 30: "Cartographer",
    31: "Casino", 32: "Chandler", 33: "Cheese merchant", 34: "Cobbler", 35: "Coffin maker",
    36: "Doctor or physician", 37: "Dyer of cloth", 38: "Engineer (building)", 39: "Engineer (siege)", 40: "Engravings",
    41: "Farm or orchard owner", 42: "Fishmonger", 43: "Fortune teller", 44: "Furrier", 45: "Gem merchant",
    46: "General merchandise", 47: "Glassblower", 48: "Goldsmith", 49: "Grain merchant", 50: "Guildhall",
    51: "Herbalist", 52: "Hostel", 53: "Illuminator", 54: "Inn", 55: "Interpreter",
    56: "Jeweler", 57: "Land broker", 58: "Landlord or slumlord", 59: "Laundry", 60: "Leatherworker",
    61: "Limner", 62: "Locksmith", 63: "Mathematician", 64: "Miller", 65: "Money lender",
    66: "Musical instrument maker", 67: "Navigator", 68: "Parchment maker", 69: "Pawnshop", 70: "Perfumer",
    71: "Pet store", 72: "Potter", 73: "Printer", 74: "Rope maker", 75: "Sage: botany",
    76: "Sage: general", 77: "Sage: history", 78: "Sage: theology", 79: "Sailmaker", 80: "Scribe",
    81: "Sculptor", 82: "Silversmith", 83: "Spice merchant", 84: "Stables", 85: "Stonemason",
    86: "Tailor", 87: "Tanner", 88: "Tavern", 89: "Tea merchant", 90: "Tea shop or restaurant",
    91: "Teamsters", 92: "Tinker", 93: "Undertaker", 94: "Veterinarian", 95: "Wagon maker",
    96: "Warehouse", 97: "Weaponsmith", 98: "Whitesmith", 99: "Wine merchant", 100: "Wood carver"
}

OFFICIAL_SUB = {
    10: "Citadel", 20: "City Administration", 30: "Courts of law", 40: "Executions plaza", 50: "Hospital",
    60: "Jail", 70: "Orphanage", 80: "Public Baths", 90: "Town watch barracks", 100: "University"
}

RELIGIOUS_SUB = {
    10: "Hermitage", 20: "Holy ground", 30: "Hospital", 40: "Monastery", 50: "Ramshackle temple",
    60: "Rich temple", 70: "School", 80: "Scriptorium or archive", 90: "Shrine", 100: "University"
}

PUBLIC_SUB = {
    10: "Arena", 20: "Executions plaza and stocks", 30: "General market square", 40: "Graveyard", 50: "Holy ground",
    60: "Parade grounds", 70: "Political forum", 80: "Public park or gardens", 90: "Specific market type", 100: "Training grounds"
}

MILITARY_SUB = {
    1: "Armory", 2: "Barracks", 3: "Canteen", 4: "Citadel", 5: "Fort",
    6: "Guard post", 7: "Guard tower", 8: "Menagerie", 9: "Military archives", 10: "Military hospital",
    11: "Military school", 12: "Military surplus", 13: "Oubliette", 14: "Prison", 15: "Recruitment center",
    16: "Siege workshop", 17: "Spy academy", 18: "Training hall", 19: "Underground vault", 20: "Warehouse"
}

INTERESTING_STREETS = {
    10: "Buildings taller, shorter, wider, or narrower than normal",
    20: "Connected balconies and 'walkway streets' with bridges",
    30: "Flower gardens (window gardens or median)",
    40: "Hanging decorations (dead animals, streamers, real or fake heads)",
    50: "Limited access street: guards request credentials",
    60: "Predominant paint color",
    70: "Similar businesses clustered together",
    80: "Statues of a predominant type/theme",
    90: "Street is on a very steep slope",
    100: "Street on a bridge with houses and shops"
}

CITY_DISTRICTS = {
    10: "Segregated (Caste/Species/Foreigner concentrated)",
    20: "Guild Quarter (Craftsmen and hire watchmen)",
    30: "Merchants’ Quarter",
    40: "Poor Quarter/Slums",
    50: "Red Light District",
    60: "Slaughterhouse District (tanneries, stables)",
    70: "Temple District",
    80: "Thieves’ Quarter (Organized crime, theaters)",
    90: "Wealthy or Nobles’ District (Fortified houses, estates)",
    100: "Wharfs/Docks (Saillors, fishermen)"
}

LATEST_NEWS = {
    5: "A faction war has broken out",
    10: "A famous criminal is to be executed",
    15: "A major religious festival is being prepared",
    20: "A surge of conversions to some deity",
    25: "A war between nearby nobles outside the city",
    30: "Selection rigged, things turning ugly",
    35: "Arrival of important potentate or ambassador",
    40: "Buildings keep falling down or suffering structural damage",
    45: "Certain types of magic use are about to be forbidden",
    50: "Foreigners being rounded up and questioned",
    55: "Members of particular profession/ancestry rounded up",
    60: "Outbreak of Undeath nearby or within city",
    65: "Plague has broken out in some area",
    70: "Potential attack, large number of foes nearby",
    75: "Religious zealotry reaching point of violence",
    80: "Series of bizarre thefts",
    85: "Series of kidnappings",
    90: "Strangers lurking in disguise within city",
    95: "Guard investigating detail-less crime",
    100: "New tax with strange terms"
}

FACTION_WARS = {
    5: "Criminal group vs Criminal group",
    10: "Guild vs Guild",
    15: "Merchant vs Merchant",
    20: "Mob vs Municipal leaders",
    25: "Mob vs Wizard(s)",
    30: "Noble house vs Noble house",
    35: "Noble house vs Merchant",
    40: "Noble house vs Temple",
    45: "Noble house vs Wizard",
    50: "Nobles vs Criminal group",
    55: "Nobles vs Guilds",
    60: "Nobles vs Municipal leaders",
    65: "Nobles vs Religious leadership",
    70: "Nobles vs Workers (Revolution)",
    75: "Species vs Species",
    80: "Religious vs Criminal group",
    85: "Religious vs Municipal leaders",
    90: "Temple vs Merchant",
    95: "Usurper vs Nobles",
    100: "Workers vs Guild leadership"
}

PRISONS = {
    2: "Cell in high tower, with barred window",
    4: "Comfy room with tracing sigil",
    6: "Comfy room with promise not to leave",
    8: "Deep hole in public plaza (unguarded)",
    10: "Deep hole, locked grate (guarded)",
    12: "Deep hole in prison courtyard (guarded)",
    14: "Deep hole in prison courtyard (unguarded)",
    16: "Deep hole in public plaza (guarded)",
    18: "Fortress-prison built on a cloud",
    20: "Ground-floor gaol (Old West style)",
    22: "Entranced by voice of magical talking statue",
    24: "Underground complex with monsters",
    26: "Locked underground dungeon cell (alone)",
    28: "Locked underground dungeon room (shared)",
    30: "Magical 'shock collar' area tether",
    32: "Magnetic bracelets to metal wall",
    34: "Buried alive in stone chamber for duration",
    36: "Cage hanging over city plaza",
    38: "Glass bubble over chasm/volcano",
    40: "Iron cage in city street",
    42: "Magical suspended animation",
    44: "Polymorphed into inanimate object",
    46: "Shifted in time",
    48: "Turned into powder in a bottle",
    50: "Mind/Soul moved into container",
    52: "Unsupervised multi-room dungeon",
    54: "Enchanted to stay in area with check-ins",
    56: "Fed to huge bizarre cell-like creature",
    58: "Individual wooden shacks on high platforms",
    60: "Ring of fire/electricity (outdoors)",
    62: "Collar/Manacle chained to post",
    64: "Prison ship",
    66: "Small island (no constraints)",
    68: "Levitated in air (food on poles)",
    70: "Paralyzed in coffin-like boxes",
    72: "Paralyzed and stacked open-air",
    74: "Pocket dimension with strange laws",
    76: "Shrunken and kept in little cages",
    78: "Welded iron box in village square",
    80: "Windowless tower common rooms",
    82: "Windowless tower with underground entry",
    84: "Underwater air-filled dome",
    86: "Underwater glass bubble on chain",
    88: "Underwater air pockets",
    90: "Poisoned (needs temporary antidote)",
    92: "Walled enclosure (chained together, uncounted)",
    94: "Walled enclosure (chained to ground)",
    96: "Walled enclosure (guarded, unchained)",
    98: "Windowless cell in high tower (unguarded)",
    100: "Windowless cell in high tower (guarded)"
}

CULTURAL_CHANGES = {
    10: "Prevalent fashion in behavior/dress (e.g. pet jaguar)",
    20: "Religious sect rising rapidly in popularity",
    30: "Secular belief spreading causing strife",
    40: "New art forms considered dangerous/offensive",
    50: "Rediscovered literature from foreign country",
    60: "Political power vacuum leading to military rise",
    70: "Social change causing widespread unemployment",
    80: "Technological changes threatening unemployment",
    90: "Influx of foreigners (war/famine/trade)",
    100: "Crafts/Trade eclipsing farming (class struggle)"
}

NOTABLE_NPCS = {
    1: "Aggressive guard", 2: "Annoying minstrel", 3: "Bandit in disguise", 4: "Beggar who knows a lot",
    5: "Clever orphan", 6: "Corrupted official", 7: "Curious waitress", 8: "Distracted scholar",
    9: "Haughty nobleman", 10: "Lonely widow", 11: "Nervous tax collector", 12: "Penniless merchant",
    13: "Princess on the run", 14: "Retired mercenary", 15: "Seasoned adventurer", 16: "Shady diplomat",
    17: "Stubborn wizard", 18: "Talented craftsman", 19: "Traveler from a distant land", 20: "Vampire/Werewolf hunter"
}

RULERS = {
    1: "Noble", 2: "Noble", 3: "Clergy", 4: "Council", 5: "Mayor",
    6: "Merchants’ guild", 7: "Thieves’ guild", 8: "Vampire"
}

EVENTS = {
    1: "Announcement by a crier", 2: "Assassination", 3: "Ceremony (wedding, etc.)", 4: "Disappearances",
    5: "Festival/Fair", 6: "Fire", 7: "Market day", 8: "Plague", 9: "Siege/Looting",
    10: "Tournament", 11: "Vermin invasion", 12: "Visit of a religious person"
}
