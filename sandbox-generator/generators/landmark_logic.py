# Landmark Logic Tables

TYPES = {
    (1, 3): "Natural",
    (4, 5): "Artificial",
    (6, 6): "Magic"
}

NATURAL_CATEGORIES = {
    1: "Fauna",
    2: "Flora (A)",
    3: "Flora (B)",
    4: "Geology (A)",
    5: "Geology (B)",
    6: "Hydrology"
}

ARTIFICIAL_CATEGORIES = {
    1: "Labor",
    2: "Mystery",
    3: "Ruin",
    4: "Small structure",
    5: "Travel",
    6: "Worship"
}

MAGIC_CATEGORIES = {
    1: "Area under a spell",
    2: "Enchanted item",
    3: "Magic path",
    4: "Magic remains",
    5: "Place of power",
    6: "Strange phenomenon"
}

# Sub-tables (1-10)
NATURAL = {
    "Fauna": {
        1: "Animal boneyard", 2: "Anthill", 3: "Beaver dam", 4: "Giant animal (exo)skeleton",
        5: "Giant bird nest", 6: "Giant snail shell", 7: "Huge galleries", 8: "Location covered with crows",
        9: "Predator’s hunting ground", 10: "Ransacked area"
    },
    "Flora (A)": {
        1: "Berry bush", 2: "Bramble overgrown area", 3: "Burnt area", 4: "Centennial tree",
        5: "Dead tree", 6: "Exotic tree", 7: "Fallen tree", 8: "Flower circle",
        9: "Fruit tree", 10: "Giant flower"
    },
    "Flora (B)": {
        1: "Giant mushroom", 2: "Hollow tree", 3: "Impenetrable thicket", 4: "Mushroom circle",
        5: "Mushroom spot", 6: "Mycelial proliferation", 7: "Rare plant spot", 8: "Root arch",
        9: "Tree alignment", 10: "Water-filled plant"
    },
    "Geology (A)": {
        1: "Animal shaped rock", 2: "Cave", 3: "Chasm", 4: "Crater",
        5: "Crystalline proliferation", 6: "Giant crystal", 7: "Lava pool", 8: "Mudpit",
        9: "Pit", 10: "Precious metal vein"
    },
    "Geology (B)": {
        1: "Ravine", 2: "Rift", 3: "Rock hole", 4: "Rock needle",
        5: "Scree", 6: "Sinkhole", 7: "Stone arch", 8: "Stone bridge",
        9: "Stone stairs", 10: "Very big rock"
    },
    "Hydrology": {
        1: "Ford", 2: "Hotspring", 3: "Lake", 4: "Pond",
        5: "Rapids", 6: "River", 7: "Spring", 8: "Stream",
        9: "Water-filled cave", 10: "Waterfall"
    }
}

ARTIFICIAL = {
    "Labor": {
        1: "Barn", 2: "Felled trees", 3: "Field", 4: "Granary",
        5: "Labor camp", 6: "Meadow", 7: "Quarry", 8: "Straw man",
        9: "Swidden field", 10: "Water tower"
    },
    "Mystery": {
        1: "Carved rock", 2: "Dolmen", 3: "Hanging bones", 4: "Heads on spikes",
        5: "Masks", 6: "Pile of bones", 7: "Rock stack", 8: "Standing stones",
        9: "Straw dolls", 10: "Totem"
    },
    "Ruin": {
        1: "Abandoned tavern", 2: "Burnt barn", 3: "Collapsed mine entrance", 4: "Decrepit mansion",
        5: "Desecrated church", 6: "Destroyed house", 7: "Overgrown tower", 8: "Pile of rubble",
        9: "Razed village", 10: "Ruined castle"
    },
    "Small structure": {
        1: "Bench", 2: "Bivouac area", 3: "Gazebo", 4: "Hunter’s cabin",
        5: "Hunting tower", 6: "Kennel", 7: "Outhouse", 8: "Palisade",
        9: "Well", 10: "Wooden fence"
    },
    "Travel": {
        1: "Boardwalks", 2: "Boundary stone", 3: "Bridge", 4: "Broken bridge",
        5: "Danger sign", 6: "Ledge", 7: "Signboard", 8: "Stairs",
        9: "Suspension bridge", 10: "Zipline"
    },
    "Worship": {
        1: "Bell/Gong", 2: "Calvary", 3: "Cemetery", 4: "Cross",
        5: "Holy place", 6: "Idol", 7: "Shrine", 8: "Tomb",
        9: "Tumulus", 10: "Vault"
    }
}

MAGIC = {
    "Area under a spell": {
        1: "Always snowy area", 2: "Anti-magic zone", 3: "Area bringing back the dead", 4: "Area where nothing grows",
        5: "Bad luck area", 6: "Dome of darkness", 7: "Force field", 8: "Incessant cyclone",
        9: "Protection from Evil", 10: "Time is frozen"
    },
    "Enchanted item": {
        1: "Curative basin", 2: "Enchanted bell", 3: "Fertility stone", 4: "Magic fountain/spring",
        5: "Magic fruits tree", 6: "Mutation pit", 7: "Stone of knowledge", 8: "Sword stuck in a rock",
        9: "Visions pool", 10: "Witch cauldron"
    },
    "Magic path": {
        1: "Breathable water", 2: "Glowing mushrooms trail", 3: "Illusory path", 4: "Invisible bridge",
        5: "Levitating staircase", 6: "Magic mirror", 7: "Rainbow bridge", 8: "Riddle bridge",
        9: "Walkable water", 10: "Wormhole"
    },
    "Magic remains": {
        1: "Area covered with fairy dust", 2: "Bloody altar", 3: "Corpse covered in crystals", 4: "Corrupt area",
        5: "Destroyed golem", 6: "Magic battlefield", 7: "Old shrine", 8: "Petrified travelers",
        9: "Remnants of a ceremony", 10: "Signs of an explosion"
    },
    "Place of power": {
        1: "Ancient burial grounds", 2: "Birthplace/Tomb of a saint", 3: "Magic beacon", 4: "Mana well",
        5: "Neolithic rock monument", 6: "Preserved natural place", 7: "Root of the World Tree", 8: "Sacred waters",
        9: "Sun focal point", 10: "Ziggurat of old"
    },
    "Strange phenomenon": {
        1: "Everburning tree", 2: "Evermelting ice", 3: "Floating crystal", 4: "Ghost building",
        5: "Luminous engravings", 6: "Reverse waterfall", 7: "Singing crystal", 8: "Strong magnetism",
        9: "Talking rock", 10: "Whispers in the wind"
    }
}

# Content Tables
CONTENT = {
    1: "Hazard",
    (2, 3): "Empty",
    4: "Special",
    (5, 6): "Monsters"
}

HAZARDS = {
    1: "Acid pits", 2: "Allergenic plants", 3: "Ancient dormant illness", 4: "Curse",
    5: "Dangerous footing", 6: "Easy to get lost", 7: "Fog", 8: "Fumes (smoke, toxic, etc.)",
    9: "Ghosts", 10: "Hallucinogenic spores", 11: "Hidden pits", 12: "Hunting traps",
    13: "Magic corruption", 14: "Plague", 15: "Quicksands", 16: "Radiations",
    17: "Sabotage/Trap", 18: "Unstable/Likely to break", 19: "Venomous animals (hornets, snakes, scorpions, etc.)", 20: "Volcanic area"
}

EMPTY_INFO = {
    (1, 5): "Info. about nearby monsters (ecology, lair, weakness, etc.)",
    6: "Alchemy recipe", 7: "Curative effects (water, plant)", 8: "Directions to a settlement",
    9: "Dungeon location", 10: "Future event", 11: "Important past event", 12: "Legend/Myth",
    13: "Local custom", 14: "Password", 15: "Secret passage location", 16: "Spell/Ritual",
    17: "Tale about a magic weapon", 18: "Toxicity of something", 19: "Upcoming weather",
    20: "Words from a (random) monster language"
}

EMPTY_METHOD = {
    1: "Clues left by monsters", 2: "Depicted on an old fresco/mosaic", 3: "Etched/Drawn on something",
    4: "Told by a (dying) NPC", 5: "Vision when near the landmark", 6: "Written in a book or on a scroll"
}

SPECIAL_GEN = {
    1: "Arbitrate a dispute",
    2: "Prevent a threat",
    3: "Solve a puzzle/riddle",
    (4, 6): "Uncover a mystery",
    (7, 9): "NPC(s)/Monster(s) in need",
    (10, 12): "Related to landmark"
}

DISPUTES = {
    1: "Adultery", 2: "Broken trade agreement", 3: "Division of an inheritance",
    4: "Murder investigation", 5: "Territorial boundaries", 6: "Trial"
}

THREATS = {
    1: "Evil ceremony", 2: "Flood", 3: "Frenzied migratory animals",
    4: "Magic corruption", 5: "Plague", 6: "Wildfire"
}

MYSTERIES = {
    1: "Abductions", 2: "Alleged ghost", 3: "Curse", 4: "Miracle",
    5: "Missing items", 6: "Mutations", 7: "Odd footprints/tracks", 8: "Stalker",
    9: "Strange lights/noises", 10: "Unexplained deaths"
}

NPC_PROBLEMS = {
    1: "Amnesia", 2: "Attacked/Chased", 3: "Disappearance", 4: "Hunger/Thirst",
    5: "Imprisoned/Enslaved", 6: "Injured/Sick", 7: "Lost", 8: "Stuck/Bogged down",
    9: "Theft", 10: "Trapped"
}
