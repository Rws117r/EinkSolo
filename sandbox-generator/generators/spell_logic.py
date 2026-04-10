import random

# Table 3-172: Attack Spells
ATTACK_PART_ONE = [
    "Fiery", "Ghostly", "Terrifying", "Black", "Watery", "Liquid", "Incorporeal", "Accurate", "Corrosive", "Unexpected",
    "Surprising", "Icy", "Unearthly", "Acidic", "Fearsome", "Poisonous", "Phosphorescent", "Glowing", "Clutching", "Grim",
    "Piercing", "Hissing", "Eviscerating", "Blasting", "Paralyzing", "Binding", "Shrieking", "Inescapable", "Mind-numbing", "Aging",
    "Electrical", "Soporific", "Lethal", "Weakening", "Soul-sucking", "Iron", "Silent", "Shadowy", "Mighty", "Crushing",
    "Burrowing", "Excruciating", "Mental", "Freezing", "Suffocating", "Narcotic", "False", "Dimensional", "Enervating", "Dehydrating"
]

ATTACK_PART_TWO = [
    "Envelope", "Pincers", "Skull", "Face", "Teeth", "Claws", "Tentacles", "Rain", "Hail", "Explosion",
    "Coils", "Pressure", "Darts", "Hand", "Stinger", "Barbs", "Spikes", "Sword", "Kiss", "Shock",
    "Shadow", "Net", "Apparition", "Summons", "Evocation", "Sound", "Trap", "Rune", "Belaborment", "Seeds",
    "Encrustation", "Growths", "Pustules", "Mist", "Smoke", "Tube", "Wisps", "Fixative", "Shell", "Sphere",
    "Thorns", "Gesture", "Insanity", "Insects", "Irritant", "Discomfiture", "Serpent", "Prison", "Breeze", "Image"
]

# Table 3-173: Generalized Spell Effects
GENERAL_EFFECTS = {
    1: "Acidic effect", 2: "Affect armor using special effect", 3: "Affect climbing", 4: "Affect falling",
    5: "Affect general health for good or ill", 6: "Affect weapon using special effect", 7: "Affects animals",
    8: "Affects particular mineral", 9: "Affects plants", 10: "Affects vision", 11: "Alters self (appearance)",
    12: "Alters self (to another set of abilities)", 13: "Alters state of matter without changing temperature",
    14: "Bravery or removal of fear", 15: "Brings to life or animates inorganic substance",
    16: "Brings to life or animates organic substance", 17: "Cause alertness (possibly to the point of causing harm)",
    18: "Cause wound", 19: "Clairaudience of varying power", 20: "Clairvoyance of varying power", 21: "Combustion effect",
    22: "Contagious effect (any condition that might be caused by a spell)", 23: "Conveys improved attribute (strength, dexterity, etc)",
    24: "Corrosion effect", 25: "Creates a blockade from elemental force (ice, air, fire, earth, electric, acid, force, etc)",
    26: "Creates a blockade from objects nearby or created objects", 27: "Creates cloud or obfuscation",
    28: "Creates element or force", 29: "Creates mental binding", 30: "Creates physical binding",
    31: "Creates servant, incorporeal", 32: "Creates servant, inorganic", 33: "Creates servant, organic",
    34: "Creates simultaneity of event, action, or spell", 35: "Creates smell", 36: "Creates visible illusion",
    37: "Crushing effect using substance", 38: "Cure wound", 39: "Cutting effect using substance",
    40: "Death using some special effect", 41: "Deciphers to greater or lesser degree", 42: "Delays magical effect until trigger event",
    43: "Delays or prevents particular magical effect", 44: "Detects ambushes or prevents surprises of some kind",
    45: "Detects particular conditions", 46: "Detects particular events", 47: "Detects particular objects",
    48: "Detects particular patterns", 49: "Disease effect", 50: "Disharmony effect", 51: "Dismiss spell effects",
    52: "Dismissal of something that has arrived", 53: "Dissolves or disintegrates", 54: "Electrical effect",
    55: "Fear effect", 56: "Fire effect", 57: "Frost effect", 58: "Gain abilities of particular animal",
    59: "Gain attack form of a particular monster", 60: "Gain spirit-type attributes", 61: "Grants magical power to someone’s gaze",
    62: "Grants magical power to someone’s touch", 63: "Grows items or creatures", 64: "Harmony effect", 65: "Heats or cools",
    66: "Improve functioning of one or more senses", 67: "Increase power of something (magical or physical)",
    68: "Increase range of something (possibly a magical effect)", 69: "Insanity of some degree caused by special effect",
    70: "Instant travel over, through, between, or at distance", 71: "Lengthens particular magical effect",
    72: "Lifts or raises", 73: "Light or dark effect", 74: "Opens", 75: "Pain effect", 76: "Paralyzes",
    77: "Persuasive speech (either from caster or elsewhere)", 78: "Premonitions", 79: "Provide shelter of varying degree",
    80: "Pulls", 81: "Pushes", 82: "Rains down element (ice, air, fire, earth, electric, acid)", 83: "Raises temperature",
    84: "Read or affect thoughts", 85: "Reduces attribute (strength, dexterity, etc)", 86: "Reduces temperature",
    87: "Restore lost qualities", 88: "Restricts motion to particular area", 89: "Send something somewhere",
    90: "Shrinks items or creatures", 91: "Sickness effect", 92: "Silence or noise effect",
    93: "Sleep or lethargy caused by special effect", 94: "Summons element from ground or air (ice, air, fire, earth, electric, acid)",
    95: "Summons servant from other place", 96: "Time effect on inorganic substance", 97: "Time effect on organic substance",
    98: "Unlocks or unfastens", 99: "Voodoo (caster’s motions cause similar effect elsewhere)", 100: "Water or moisture effect"
}

# Table 3-174: Command Words and Magic Words
COMMAND_FIRST = ["Bara", "Mira", "Abara", "Ocus", "Dias", "Lea", "Ro", "Sha", "Za", "Ul", "O", "Oca", "Re", "Lo", "Ba", "Bo", "Po", "Mia", "Acro", "A"]
COMMAND_SECOND = ["bo", "bi", "ca", "po", "coxi", "sa", "sixa", "loba", "za", "pana", "sci", "miri", "da", "paa", "tsa", "tua", "soa", "mura", "a", "mi"]
COMMAND_ENDING = ["lis", "lune", "dabra", "sicus", "po", "x", "nda", "m", "n", "r", "rix", "pir", "la", "lion", "xon", "cto", "cta", "sta", "sto", "nto"]

def roll_d100():
    return random.randint(1, 100)
