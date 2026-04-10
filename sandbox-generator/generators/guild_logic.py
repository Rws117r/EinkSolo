# 1) Fields and Sub-fields
FIELDS = {
    1: "Adventuring", 2: "Crafts", 3: "Hobbies", 4: "Magic",
    5: "Merchants", 6: "Resources", 7: "Sciences", 8: "Spectacle"
}

SUB_FIELDS = {
    "Adventuring": ["Bounty hunting", "Investigation", "Mercenaries", "Monster hunting", "Scavenging", "Scouting"],
    "Crafts": ["Blacksmithing", "Building", "Knife making", "Shoemaking", "Tailoring", "Tanning"],
    "Hobbies": ["Books", "Cooking", "Fishing", "Gardening", "Painting", "Pottery"],
    "Magic": ["Alchemy", "Astrology", "Demonology", "Divination", "Enchanting", "Spells"],
    "Merchants": ["Baking", "Brewing/Winemaking", "Butchery", "Cheese", "Distant lands trading", "Fruits/Vegetables"],
    "Resources": ["Farming", "Hunting", "Mining", "Mushrooms cultivation", "Stonecutting", "Woodcutting"],
    "Sciences": ["Astronomy", "Botany", "Engineering", "Entomology", "Geography", "Philosophy"],
    "Spectacle": ["Acting", "Dancing", "Fashion", "Music", "Poetry", "Singing"]
}

# 2) Expertise
EXPERTISE = {
    1: "None", 2: "Basic", 5: "Expert", 9: "Companion", 12: "Master"
}

# 3) Name structures
NAME_STRUCTURES = {
    1: "The {field} Guild", 
    6: "The Sisters/Brothers of {field}",
    7: "The {field} Circle",
    8: "The {field} Club",
    9: "The {field} Enthusiasts",
    10: "The {field} Lovers",
    11: "The {field} Society",
    12: "The Friendly {field}"
}

# 4) Power
RENOWN = {
    1: "Secret", 2: "Unknown", 5: "Known", 9: "Famous", 12: "Known everywhere"
}

RESOURCES = {
    1: "None", 2: "Low", 5: "Average", 9: "High", 12: "Infinite"
}

GUILDHOUSES = {
    1: "A few ones", 3: "A lot", 5: "Only one building", 6: "Ubiquitous"
}

SPECIAL_ASSETS = {
    1: "None", 7: "Ancient knowledge", 8: "Blessing", 9: "High-level contacts",
    10: "Patrons", 11: "Prisoner", 12: "Relic"
}

MOTIVATION = {
    1: "Wealth", 4: "Renown", 6: "Power", 8: "Charity"
}

# 5) Members
INITIATIONS = {
    1: "No initiation", 6: "Alcohol", 11: "Braving a taboo",
    13: "Giving up their past life", 15: "Humiliation", 16: "Mutilation",
    17: "Scary ceremony", 18: "Sport", 19: "Taking an oath", 20: "Trials"
}

APPEARANCES = {
    1: "None", 11: "Animal traits", 12: "Distinctive tattoo",
    13: "Item related to their field", 14: "Jewelry", 15: "Mutation",
    16: "Mutilation", 17: "Particular hairstyle", 18: "Specific makeup",
    19: "Uniform", 20: "Work injury"
}

QUIRKS = {
    1: "None", 11: "Always seem angry/happy", 12: "Extremely paranoid",
    13: "Hide something", 14: "Inexplicably old/young",
    15: "Make puns related to their field", 16: "Never speak",
    17: "Never stop trying to recruit", 18: "Passionate about their field",
    19: "Travel in processions", 20: "Worship their craft"
}

# 6) Events
EVENTS_COMMON = {
    1: "Demonstration/Strike", 2: "Open-house", 3: "Procession", 4: "Recruiting"
}

EVENTS_FIELD = {
    "Adventuring": {5: "Show off", 6: "Trophy/Medal showcase"},
    "Crafts": {5: "Crafting contest", 6: "Traveling market"},
    "Hobbies": {5: "Ball", 6: "Exhibition"},
    "Magic": {5: "Magic congress", 6: "Spellcasting contest"},
    "Merchants": {5: "Big sale", 6: "Market"},
    "Resources": {5: "Festival", 6: "Technical seminar"},
    "Sciences": {5: "Congress", 6: "New discoveries fair"},
    "Spectacle": {5: "Performance", 6: "Tour across the country"}
}

# 7) Problems
PROBLEMS_COMMON = {
    1: "Bankruptcy", 2: "Members leaving", 3: "New law hindering the guild", 4: "New rival guild"
}

PROBLEMS_FIELD = {
    "Adventuring": {5: "Death of a guild member", 6: "Treason"},
    "Crafts": {5: "Scarcity of raw materials", 6: "Work accident"},
    "Hobbies": {5: "Loss of interest", 6: "Theft"},
    "Magic": {5: "Magic has a bad reputation", 6: "Spell gone wrong"},
    "Merchants": {5: "Bad season", 6: "Pests invasion"},
    "Resources": {5: "Prices raise", 6: "Weather related incident"},
    "Sciences": {5: "Failed experiment", 6: "Library fire"},
    "Spectacle": {5: "Sick lead", 6: "Stolen designs/script/text"}
}
