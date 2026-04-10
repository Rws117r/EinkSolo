import random

# Table 29-3: Short Tavern Items 1
SHORT_TAVERN_ITEMS_1 = [
    "Acorn", "Anchor", "Anvil", "Arch", "Awl", "Axe", "Banner", "Barrel", "Beak", "Bell",
    "Boat", "Book", "Bottle", "Box", "Branch", "Broom", "Brush", "Buckle", "Button", "Cap",
    "Cask", "Cauldron", "Chains", "Chime", "Chisel", "Clamp", "Claw", "Cloak", "Coat", "Cork",
    "Cowl", "Crowbar", "Crown", "Dagger", "Door", "Doublet", "Eye", "Finger", "Flail", "Flask",
    "Forge", "Glove", "Glyph", "Hammer", "Hand", "Hat", "Heart", "Helm", "Helmet", "Hood",
    "Hook", "Horn", "Hourglass", "Idol", "Keg", "Kettle", "Key", "Knife"
]

# Table 29-4: Short Tavern Items 2
SHORT_TAVERN_ITEMS_2 = [
    "Knot", "Lantern", "Leaf", "Lens", "Lever", "Lock", "Log", "Lute", "Mace", "Mallet",
    "Mantle", "Map", "Mask", "Nail", "Needle", "Net", "Oven", "Pearl", "Pickaxe", "Pincers",
    "Pitcher", "Plow", "Plume", "Pulley", "Rail", "Rake", "Relic", "Ribbon", "Ring", "Rock",
    "Rose", "Sandal", "Scroll", "Scythe", "Secret", "Seed", "Shears", "Shield", "Shoe", "Shovel",
    "Sickle", "Skull", "Spear", "Spell", "Staff", "Statue", "Stone", "Sword", "Tankard", "Thread",
    "Throne", "Tome", "Tongs", "Tongue", "Tooth", "Tree", "Veil", "Vial", "Walnut", "Web"
]

# Table 29-5: Long Tavern Items
LONG_TAVERN_ITEMS = [
    "Acorn", "Alembic", "Amphora", "Athanor", "Battle-Axe", "Billhook", "Bodkin", "Bracelet", "Brigandine", "Bucket",
    "Buckler", "Cabinet", "Candle", "Candlestick", "Coronet", "Decanter", "Elephant", "Falchion", "Figurine", "Galleon",
    "Gauntlet", "Gonfalon", "Grimalkin", "Grimoire", "Halberd", "Hauberk", "Hogshead", "Manacle", "Mandolin", "Mangonel",
    "Medallion", "Pikestaff", "Pillars", "Sarcophagus", "Scimitar", "Scissors", "Tambourine", "Tapestry", "Tinderbox", "Torch"
]
# Table 29-6: All Tavern Adjectives (200 entries)
ALL_TAVERN_ADJECTIVES = [
    "Amber", "Amorous", "Ancestral", "Ancient", "Angry", "Azure", "Bald", "Bashful", "Battered", "Bearded",
    "Black", "Blasted", "Blue", "Blushing", "Branching", "Brass", "Brazen", "Brilliant", "Broken", "Bronze",
    "Brotherly", "Burrowing", "Caroling", "Chattering", "Chiming", "Chirping", "Chivalrous", "Climbing", "Cloaked", "Cloven",
    "Clutching", "Copper", "Cowardly", "Cowled", "Crescent", "Crimson", "Crowned", "Crumbling", "Dancing", "Decadent",
    "Dim", "Dour", "Dreaming", "Drumming", "Drunken", "Dun", "Dusky", "Eerie", "Emerald", "Enchanted",
    "Fair", "Fallen", "Fat", "Fearsome", "Feathered", "Fiery", "Floating", "Flowering", "Fluttering", "Forbidden",
    "Fragmented", "Fragrant", "Freed", "Garlanded", "Ghostly", "Golden", "Gray", "Green", "Grim", "Growling",
    "Hidden", "High", "Hooded", "Howling", "Imperial", "Ivory", "Jesting", "Jeweled", "Kingly", "Knightly",
    "Knotted", "Laughing", "Looming", "Lost", "Lunar", "Lurking", "Mad", "Magical", "Magnificent", "Majestic",
    "Mantled", "Marbled", "Marvelous", "Moaning", "Moody", "Murky", "Muttering", "Mysterious", "Mystic", "Noble",
    "Odd", "Odorous", "Old", "Painted", "Pale", "Peculiar", "Perfumed", "Piping", "Placid", "Proud",
    "Quaking", "Quarrelsome", "Quick", "Quivering", "Scowling", "Red", "Resplendent", "Restless", "Ringing", "Rippling",
    "Rising", "Riven", "Robed", "Rootless", "Rotting", "Royal", "Ruined", "Runic", "Sapphire", "Scarlet",
    "Scholarly", "Scowling", "Screaming", "Scrying", "Shadowed", "Smiling", "Shimmering", "Shivering", "Shrieking", "Shrouded",
    "Silent", "Silver", "Silver", "Sinful", "Singing", "Singing", "Sleeping", "Slumbering", "Sly", "Speckled",
    "Spitting", "Spoiled", "Spotted", "Squalling", "Steaming", "Stolen", "Stone", "Stony", "Stormy", "Stout",
    "Strange", "Striped", "Sullen", "Sundered", "Talented", "Talking", "Tall", "Tangled", "Tempestuous", "Thin",
    "Trembling", "Trilling", "Turbulent", "Twining", "Twisted", "Twittering", "Umber", "Vanishing", "Hulking", "Grinning",
    "Veiled", "Walking", "Wandering", "Waning", "Wanton", "Warbling", "Watchful", "Waxen", "Waxing", "Weeping",
    "Whispering", "Whistling", "White", "Wicked", "Wild", "Wisping", "Wooden", "Wounded", "Wrathful", "Yellow"
]

# Table 29-7: Short Tavern Living Adjective (1-89 extracted)
SHORT_TAVERN_LIVING_ADJECTIVE = [
    "Amber", "Ancient", "Angry", "Azure", "Bad", "Bald", "Bashful", "Battered", "Bearded", "Black",
    "Blasted", "Blind", "Blue", "Blushing", "Branching", "Brass", "Brave", "Brazen", "Brilliant", "Broken",
    "Bronze", "Cheerful", "Chiming", "Chirping", "Clean", "Climbing", "Cloaked", "Cloven", "Clutching", "Copper",
    "Cowled", "Crescent", "Crimson", "Crowned", "Dancing", "Dim", "Dirty", "Dour", "Dreaming", "Drinking",
    "Druid's", "Drumming", "Drunken", "Dun", "Dusky", "Eerie", "Fair", "Fallen", "Fat", "Fattened",
    "Fearsome", "Feathered", "Fiery", "Flaming", "Floating", "Fragrant", "Freed", "Ghostly", "Glass", "Golden",
    "Good", "Gray", "Green", "Grim", "Grinning", "Growling", "Handsome", "Happy", "Haunted", "Hidden",
    "High", "Hissing", "Hooded", "Horned", "Howling", "Hulking", "Hungry", "Hunted", "Jealous", "Jesting",
    "Jeweled", "Jolly", "Jovial", "Joyful", "King's", "Kingly", "Knightly", "Knotted", "Laughing",
    "Moody", "Mottled", "Muddy", "Murky", "Mystic", "Noble", "Odd", "Old", "One-Eyed", "Painted",
    "Pale", "Patient", "Piping", "Placid", "Prize", "Proud", "Queen's", "Quick", "Quiet", "Red",
    "Restful", "Restless", "Ringing", "Rising", "Riven", "Robed", "Rootless", "Royal", "Ruined", "Runic",
    "Running", "Sapphire", "Scarlet", "Scowling", "Scowling", "Screaming", "Second", "Shrieking", "Shrouded", "Silent",
    "Silver", "Sinful", "Singing", "Singing", "Sleeping", "Slumbering", "Slow", "Sly", "Smiling", "Smoking", "Speckled", "Spitting",
    "Spoiled", "Spotted", "Squalling", "Steaming", "Stolen", "Stone", "Stony", "Stormy", "Stout", "Stout",
    "Strange", "Striped", "Sullen", "Sundered", "Swimming", "Talking", "Tall", "Tangled", "Thin", "Third",
    "Thirsty", "Tiny", "Tipsy", "Trembling", "Trilling", "Twin", "Twining", "Twisted", "Umber", "Veiled",
    "Waiting", "Walking", "Wandering", "Wanton", "Watchful", "Watching", "Waxen", "Waxing", "Wayward",
    "Lazy", "Little", "Looming", "Lost", "Lunar", "Lurking", "Mad", "Mantled", "Marbled", "Merry", "Moaning",
    "Weeping", "White", "Wicked", "Wild", "Wise", "Witch's", "Wizard's", "Wooden", "Wounded", "Wrathful", "Yellow"
]
# Table 29-8: Short Tavern Item Adjective (100 entries)
SHORT_TAVERN_ITEM_ADJECTIVE = [
    "Amber", "Ancient", "Archer's", "Azure", "Bard's", "Baron's", "Battered", "Beggar's", "Black", "Blacksmith's",
    "Bloody", "Blue", "Brass", "Brazen", "Broken", "Bronze", "Cleric's", "Copper", "Crimson", "Dancing",
    "Dragon's", "Dreaming", "Drunken", "Fallen", "Farmer's", "Feathered", "Fiery", "Fragrant", "Ghostly", "Giant's",
    "Golden", "Gray", "Green", "Holy", "Iron", "Jester's", "Jeweled", "King's", "Knight's", "Laughing",
    "Lordly", "Lost", "Mad", "Magic", "Marbled", "Merchant's", "Miller's", "Monk's", "Mystic", "Noble",
    "Notched", "Odd", "Old", "Painted", "Pale", "Peasant's", "Pikeman's", "Plowman's", "Priest's", "Prince's",
    "Proud", "Queen's", "Red", "Restless", "Rhyming", "Royal", "Ruined", "Runic", "Sacred", "Sailor's",
    "Sapphire", "Scarlet", "Shepherd's", "Silver", "Singing", "Sleeping", "Speckled", "Split", "Spotted", "Squire's",
    "Steaming", "Stolen", "Stone", "Stony", "Striped", "Talking", "Tall", "Thin", "Twisted", "Walking",
    "Watchful", "Wax", "Wayward", "Weaver's", "Whistling", "White", "Witch's", "Wooden", "Wyvern's", "Yellow"
]
# Table 29-9: Short Tavern Animal (100 entries)
SHORT_TAVERN_ANIMAL = [
    "Ape", "Badger", "Bear", "Beaver", "Bison", "Bluejay", "Boar", "Bull", "Camel", "Cat",
    "Cattle", "Cow", "Crow", "Cub", "Doe", "Dog", "Dogs", "Dove", "Duck", "Eagle",
    "Fox", "Gazelle", "Giraffe", "Gnat", "Goat", "Goose", "Goshawk", "Greyhound", "Gryphon", "Hare",
    "Hare", "Hart", "Hart", "Hawk", "Hedgehog", "Swan", "Hog", "Horsefly", "Hound", "Hounds",
    "Kestrel", "Kitten", "Lamb", "Leopard", "Lion", "Lynx", "Mastiff", "Mice", "Mole", "Monkey",
    "Mouse", "Mule", "Newt", "Ostrich", "Otter", "Owl", "Ox", "Oxen", "Palfrey", "Panther",
    "Parrot", "Peacock", "Pheasant", "Pig", "Pigeon", "Quail", "Rabbit", "Ram", "Rat", "Raven",
    "Robin", "Roebuck", "Rooster", "Satyr", "Sheep", "Snake", "Sparrow", "Spider", "Squirrel", "Stag",
    "Stallion", "Thrush", "Tortoise", "Turtle", "Walrus", "Warhorse", "Wolf", "Wren", "Frog", "Toad",
    "Fish", "Trout", "Salmon", "Minnow", "Beetle", "Bird", "Swallow", "Bat", "Stirge", "Dragon"
]
# Table 29-10: All Tavern Animal (100 entries)
ALL_TAVERN_ANIMAL = [
    "Antelope", "Ape", "Badger", "Bear", "Beaver", "Bison", "Bluejay", "Boar", "Bull", "Butterfly",
    "Camel", "Canary", "Cat", "Cattle", "Cow", "Crow", "Cub", "Doe", "Dog", "Dogs",
    "Dove", "Dragonfly", "Duck", "Eagle", "Elephant", "Fox", "Fox", "Gazelle", "Giraffe", "Gnat",
    "Goat", "Goose", "Goshawk", "Greyhound", "Gryphon", "Hare", "Hares", "Hart", "Hart", "Hawk",
    "Hedgehog", "Hippogriff", "Hog", "Horsefly", "Hound", "Hounds", "Hummingbird", "Kestrel", "Kitten", "Lamb",
    "Leopard", "Lion", "Lynx", "Mastiff", "Mice", "Mole", "Monkey", "Mouse", "Mule", "Newt",
    "Octopus", "Ostrich", "Otter", "Owl", "Ox", "Oxen", "Palfrey", "Panther", "Parrot", "Peacock",
    "Pelican", "Pheasant", "Pig", "Pigeon", "Porcupine", "Quail", "Rabbit", "Ram", "Rat", "Raven",
    "Rhinoceros", "Robin", "Roebuck", "Rooster", "Salamander", "Satyr", "Sheep", "Snake", "Sparrow", "Spider",
    "Squirrel", "Stag", "Stallion", "Thrush", "Tortoise", "Turtle", "Unicorn", "Walrus", "Warhorse", "Wolf"
]

# Table 29-11: Tavern Person (100 entries)
TAVERN_PERSON = [
    "Alchemist", "Almoner", "Artist", "Assassin", "Bailiff", "Baker", "Bandit", "Barber", "Bard", "Baron",
    "Beggar", "Bishop", "Blacksmith", "Brewer", "Burglar", "Butcher", "Captain", "Charlatan", "Chieftain", "Cleric",
    "Clothier", "Crone", "Dancer", "Doctor", "Druid", "Duchess", "Duke", "Dwarf", "Elf", "Emperor",
    "Empress", "Farmer", "Fool", "Forester", "Forger", "Guard", "Halfling", "Herdsman", "Hermit", "Hunter",
    "Huntsman", "Jester", "Jongleur", "Juggler", "Kidnapper", "King", "Knight", "Lady", "Lawyer", "Mage",
    "Mage", "Magician", "Maiden", "Merchant", "Milkmaid", "Miller", "Minstrel", "Monk", "Murderer", "Necromancer",
    "Nomad", "Oracle", "Peasant", "Philosopher", "Pikeman", "Plowman", "Poet", "Priest", "Priestess", "Prince",
    "Prisoner", "Queen", "Ranger", "Reeve", "Rider", "Scholar", "Scribe", "Sculptor", "Shepherd", "Sheriff",
    "Shoemaker", "Singer", "Smith", "Soldier", "Sorcerer", "Sorceress", "Squire", "Tailor", "Teamster", "Thief",
    "Troubadour", "Tyrant", "Virgin", "Wanderer", "Warden", "Warrior", "Weaver", "Witch", "Wizard", "Woodcarver"
]

# Table 29-12: Tavern Abstract Item (100 entries)
TAVERN_ABSTRACT_ITEM = [
    "Arms", "Head", "Greeting", "Pact", "Dilemma", "Problem", "Wife (or Husband)", "Son", "Daughter", "Friend",
    "Foe", "Riddle", "Treaty", "Meet", "Haunt", "House", "Shadow", "Glove", "Dream", "Puzzle",
    "Quest", "Path", "Mark", "Mouth", "Hand", "Song", "Map", "Task", "Helper", "Test",
    "Bane", "Curse", "Last Word", "Ending", "Tragedy", "Comedy", "Conclusion", "Reward", "Prize", "Revenge",
    "Answer", "Question", "Triumph", "Victory", "Last Card", "Last Coin", "Virtue", "Honor", "Fame", "Laurels",
    "Tribute", "Payment", "Haven", "Hat", "Coat", "Lament", "Song", "Dance", "Banquet", "Feast",
    "Long Walk", "Reverie", "March", "Guardian", "Quill", "Testament", "Gravestone", "Pyre", "Good Advice", "Good Deed",
    "Deed", "Question", "Journey", "Adventure", "Venture", "Tale", "Mistake", "Gambit", "Gamble", "Tree",
    "Mead", "Barrel", "Wild Ride", "Odd Dream", "Lost Key", "Temptation", "Dispute", "Bad Idea", "Night Out", "Penny",
    "Shilling", "Five Sons", "Fall", "Rest", "Reprieve", "Bed", "Chair", "Field", "Garden", "Post"
]

def generate_tavern_name():
    """Generates a tavern name using one of 10 formulas."""
    formula = random.randint(1, 10)
    
    # helper for common elements
    short_item_pool = SHORT_TAVERN_ITEMS_1 + SHORT_TAVERN_ITEMS_2
    
    if formula == 1:
        # 1) The [Short Tavern Item]
        return f"The {random.choice(short_item_pool)}"
    
    elif formula == 2:
        # 2) The [Short Tavern Item Adjective] [Short Tavern Item]
        return f"The {random.choice(SHORT_TAVERN_ITEM_ADJECTIVE)} {random.choice(short_item_pool)}"
    
    elif formula == 3:
        # 3) The [Short Tavern Living Adjective] [Short Tavern Animal]
        return f"The {random.choice(SHORT_TAVERN_LIVING_ADJECTIVE)} {random.choice(SHORT_TAVERN_ANIMAL)}"
    
    elif formula == 4:
        # 4) The [All Tavern Adjective] [All Tavern Animal]
        return f"The {random.choice(ALL_TAVERN_ADJECTIVES)} {random.choice(ALL_TAVERN_ANIMAL)}"
    
    elif formula == 5:
        # 5) The [Tavern Person]'s [Short Tavern Item]
        return f"The {random.choice(TAVERN_PERSON)}'s {random.choice(short_item_pool)}"
    
    elif formula == 6:
        # 6) The [Tavern Person]'s [Tavern Abstract Item]
        return f"The {random.choice(TAVERN_PERSON)}'s {random.choice(TAVERN_ABSTRACT_ITEM)}"
    
    elif formula == 7:
        # 7) The [Short Tavern Item] and [Short Tavern Item]
        return f"The {random.choice(short_item_pool)} and {random.choice(short_item_pool)}"
    
    elif formula == 8:
        # 8) The [Short Tavern Item] and the [Short Tavern Item]
        return f"The {random.choice(short_item_pool)} and the {random.choice(short_item_pool)}"
    
    elif formula == 9:
        # 9) The [Long Tavern Item]
        return f"The {random.choice(LONG_TAVERN_ITEMS)}"
    
    else: # formula 10
        # 10) The [All Tavern Adjective] [Long Tavern Item]
        return f"The {random.choice(ALL_TAVERN_ADJECTIVES)} {random.choice(LONG_TAVERN_ITEMS)}"
