import random

# --- CONTAINERS ---

CONTAINER_TYPE_ROLL = {
    (1, 25): "Small Container with special feature",
    (26, 50): "Large Container with special feature",
    (51, 75): "Bizarre Container",
    (76, 100): "Numerous choices of large containers"
}

SMALL_CONTAINERS = {
    (1, 5): ("Basket, small", "Covered, concealed, or illusion"),
    (6, 10): ("Bird’s nest", "Dangerous location: Natural feature"),
    (11, 15): ("Box (jewelry)", "Dangerous location: Natural feature"),
    (16, 20): ("Box (spice)", "Dangerous location: Architectural feature"),
    (21, 25): ("Earthenware pot", "Dangerous location: Architectural feature"),
    (26, 30): ("Flower pot", "Dangerous location: Traps"),
    (31, 35): ("Glass globe", "Dangerous location: Traps"),
    (36, 40): ("Goblet", "In a marked area"),
    (41, 45): ("Hollow sword handle", "In a marked area"),
    (46, 50): ("Ivory globe", "Inaccessible but visible (puzzle/game)"),
    (51, 55): ("Locket", "Visible but across a challenge"),
    (56, 60): ("Niche", "Located amidst duplicates (race against time)"),
    (61, 65): ("Pocket dimension", "Located amidst duplicates (race against time)"),
    (66, 70): ("Pouch", "Amidst other mundane items"),
    (71, 75): ("Salt cellar", "Located within another container"),
    (76, 80): ("Spice cabinet", "Within another container (possibly locked)"),
    (81, 85): ("Statue’s throat", "Container itself is trapped"),
    (86, 90): ("Tankard, with lid", "Container itself is trapped"),
    (91, 95): ("Under flagstone", "Stuck: Requires strength + race against time"),
    (96, 100): ("Under floorboard", "Stuck: Requires strength + race against time")
}

LARGE_CONTAINERS = {
    (1, 4): ("Amphora", "Covered, concealed, or illusion"),
    (5, 8): ("Bag", "Dangerous location: Natural feature"),
    (9, 12): ("Barrel", "Dangerous location: Natural feature"),
    (13, 16): ("Basket (large)", "Dangerous location: Architectural feature"),
    (17, 20): ("Bin (grain/coal/wood)", "Dangerous location: Architectural feature"),
    (21, 24): ("Box", "Dangerous location: Traps"),
    (25, 28): ("Cabinet", "Dangerous location: Traps"),
    (29, 32): ("Cart", "In a marked area"),
    (33, 36): ("Cask", "In a marked area"),
    (37, 40): ("Cauldron", "Inaccessible but visible (puzzle/game)"),
    (41, 44): ("Chest", "Visible but across a challenge"),
    (45, 48): ("Compartment", "Located amidst duplicates (race against time)"),
    (49, 52): ("Crate", "Located amidst duplicates (race against time)"),
    (53, 56): ("Hamper, laundry", "Amidst other mundane items"),
    (57, 60): ("Jar", "Locked in an ordinary fashion"),
    (61, 64): ("Keg", "Located within another container"),
    (65, 68): ("Pot", "Container itself is trapped"),
    (69, 72): ("Sack", "Container itself is trapped"),
    (73, 76): ("Sarcophagus/coffin", "Stuck: Requires strength + race against time"),
    (77, 80): ("Statue, hollow", "Stuck: Requires strength + race against time"),
    (81, 84): ("Taxidermy (animal)", "Climbing or gadget required to reach opening"),
    (85, 88): ("Trunk or locker", "Completely sealed and locked"),
    (89, 92): ("Tub", "Roll for two results"),
    (93, 96): ("Urn", "Roll for two results"),
    (97, 100): ("Wardrobe", "Roll for three results")
}

BIZARRE_CONTAINERS = {
    (1, 10): "Force field (globe, wall, pyramid, etc).",
    (11, 20): "Inside monster",
    (21, 30): "Interdimensional portal or pocket dimension",
    (31, 40): "Multiple colors/features, contents depend on timing",
    (41, 50): "Multiple illusions protect a mundane container",
    (51, 60): "Multiple openings with different contents",
    (61, 70): "Nested containers (Matryoshka dolls / false bottoms)",
    (71, 80): "Spin wheel (randomized opening + randomized contents)",
    (81, 90): "Strongbox/Safe with multiple dials",
    (91, 100): "Vehicle"
}

# --- FURNITURE ---

FURNITURE_UNUSUAL = {
    (1, 4): ("Armchair", "Constructed of magical force"),
    (5, 8): ("Bed", "Floats/levitates, shifts location"),
    (9, 12): ("Bed (pet)", "Floats/levitates, stationary"),
    (13, 16): ("Bench", "Folds up"),
    (17, 20): ("Chair", "Gem encrusted"),
    (21, 24): ("Chandelier", "Bas-relief carvings"),
    (25, 28): ("Chest of drawers", "Mosaic pattern"),
    (29, 32): ("Couch", "Has spikes"),
    (33, 36): ("Desk", "Incorporates statuary"),
    (37, 40): ("Display case", "Inlaid with semi-precious stone"),
    (41, 44): ("Easel or writing desk", "Inlaid with wood"),
    (45, 48): ("Fire pit", "Invisible"),
    (49, 52): ("Lamp", "Made of bone"),
    (53, 56): ("Lectern", "Made of bronze or metal"),
    (57, 60): ("Lighting sconces", "Unusual or rare wood"),
    (61, 64): ("Privacy screen", "Unusual stone"),
    (65, 68): ("Shelves", "Shorter than normal"),
    (69, 72): ("Stool", "Sideways"),
    (73, 76): ("Storage chest", "Spins"),
    (77, 80): ("Table, banquet", "Taller than normal"),
    (81, 84): ("Table, dining", "Tilted on slope"),
    (85, 88): ("Table, display", "Uneven surface"),
    (89, 92): ("Table, workbench", "Unusually large"),
    (93, 96): ("Throne", "Unusually small"),
    (97, 100): ("Toilet/privy", "Upside down")
}

# --- UTILITIES ---

def get_from_table(table, roll):
    for (low, high), value in table.items():
        if low <= roll <= high:
            return value
    return "Unknown"

def roll_d100(): return random.randint(1, 100)
