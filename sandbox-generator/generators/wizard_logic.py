import random

def roll_dice(sides):
    return random.randint(1, sides)

def roll_2d6():
    return random.randint(1, 6) + random.randint(1, 6)

def roll_1d12():
    return random.randint(1, 12)

def roll_1d4():
    return random.randint(1, 4)

def get_wizard_level(roll):
    if roll == 2:
        return 7
    elif 3 <= roll <= 5:
        return 8
    elif 6 <= roll <= 8:
        return 9
    elif 9 <= roll <= 11:
        return 10
    elif roll == 12:
        return 11
    return 1

def get_wizard_specialty(roll):
    if 1 <= roll <= 5:
        return "Generalist"
    elif roll == 6:
        return "Druid"
    elif roll == 7:
        sub_roll = roll_1d4()
        elements = {1: "Air", 2: "Earth", 3: "Fire", 4: "Water"}
        return f"Elemental magic ({elements[sub_roll]})"
    elif roll == 8:
        return "Illusion"
    elif roll == 9:
        return "Invocation"
    elif roll == 10:
        return "Necromancy"
    elif roll == 11:
        return "Unique domain"
    elif roll == 12:
        return "Cleric"
    return "Generalist"

def get_robe_color(specialty):
    colors = {
        "Generalist": "Gray",
        "Druid": "Sage Green",
        "Elemental magic (Air)": "Light Blue",
        "Elemental magic (Earth)": "Brown",
        "Elemental magic (Fire)": "Red",
        "Elemental magic (Water)": "Blue",
        "Illusion": "Purple",
        "Invocation": "Yellow",
        "Necromancy": "Black",
        "Unique domain": "Prismatic",
        "Cleric": "White"
    }
    return colors.get(specialty, "Gray")

def get_wizard_appearance(roll, specialty):
    # Always include the robe color as part of the description if it's robe-based
    if 1 <= roll <= 5:
        color = get_robe_color(specialty)
        return f"{color} robe and pointy hat"
    elif roll == 6:
        return "Casual clothes"
    elif roll == 7:
        return "Corrupted by magic"
    elif roll == 8:
        return "Formal attire"
    elif roll == 9:
        color = get_robe_color(specialty)
        return f"{color} robes that leave no doubt about their specialty"
    elif roll == 10:
        return "Mysterious"
    elif roll == 11:
        return "Plain clothes & scrawny body"
    elif roll == 12:
        return "Scruffy"
    return "Plain clothes"

def get_wizard_goal(roll):
    goals = {
        (1, 5): "Lust for power",
        6: "Altruism",
        7: "Creating a new spell",
        8: "Impressing someone",
        9: "Madness",
        10: "Money",
        11: "Quest for immortality",
        12: "Revenge"
    }
    if 1 <= roll <= 5:
        return goals[(1, 5)]
    return goals.get(roll, "Study magic")

def get_wizard_staff():
    materials = ["Bone/Ivory", "Copper/Bronze", "Crystal", "Gold-plated", "Mithral", 
                 "Obsidian", "Otherworldly material", "Silver-plated", "Steel", "Wood"]
    tops = ["Angel", "Claw", "Crystal/Precious stone", "Deer head", "Dragon head", 
            "Eagle", "Eye", "Fish head", "Heart", "Holy symbol", "Orb", "Plain", 
            "Pointy", "Shaped like a question mark", "Skeletal hand", "Skull", 
            "Snake head", "Sun/Moon/Star", "Talking skull", "Weighted"]
    bottoms = ["Blade", "Burnt", "Orb", "Plain", "Pointy", "Same as the top", "Skeletal foot", "Weighted"]
    shapes = ["Straight", "Straight", "Straight", "Straight", "Angular", "Curved", "Shaped like a lightning bolt", "Twisted"]
    details = ["Cracked", "Decorated with feathers", "Engraved with runes", "Hollow", "Reinforced with rope", "Used"]
    
    mat = materials[roll_dice(10)-1]
    top = tops[roll_dice(20)-1]
    bot = bottoms[roll_dice(8)-1]
    shape = shapes[roll_dice(8)-1]
    det = details[roll_dice(6)-1]
    
    return mat, top, bot, shape, det
