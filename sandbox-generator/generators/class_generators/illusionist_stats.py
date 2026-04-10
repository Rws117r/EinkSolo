import random

# Level: (HD_dice, HD_mod, THAC0, THAC0_bonus, (D, W, P, B, S), (L1, L2, L3, L4, L5, L6))
ILLUSIONIST_PROGRESSION = {
    1:  (1, 0, 19, 0, (13, 14, 13, 16, 15), (1, 0, 0, 0, 0, 0)),
    2:  (2, 0, 19, 0, (13, 14, 13, 16, 15), (2, 0, 0, 0, 0, 0)),
    3:  (3, 0, 19, 0, (13, 14, 13, 16, 15), (2, 1, 0, 0, 0, 0)),
    4:  (4, 0, 19, 0, (13, 14, 13, 16, 15), (2, 2, 0, 0, 0, 0)),
    5:  (5, 0, 19, 0, (13, 14, 13, 16, 15), (2, 2, 1, 0, 0, 0)),
    6:  (6, 0, 17, 2, (11, 12, 11, 14, 12), (2, 2, 2, 0, 0, 0)),
    7:  (7, 0, 17, 2, (11, 12, 11, 14, 12), (3, 2, 2, 1, 0, 0)),
    8:  (8, 0, 17, 2, (11, 12, 11, 14, 12), (3, 3, 2, 2, 0, 0)),
    9:  (9, 0, 17, 2, (11, 12, 11, 14, 12), (3, 3, 3, 2, 1, 0)),
    10: (9, 1, 17, 2, (11, 12, 11, 14, 12), (3, 3, 3, 3, 2, 0)),
    11: (9, 2, 14, 5, (8, 9, 8, 11, 8), (4, 3, 3, 3, 2, 1)),
    12: (9, 3, 14, 5, (8, 9, 8, 11, 8), (4, 4, 3, 3, 3, 2)),
    13: (9, 4, 14, 5, (8, 9, 8, 11, 8), (4, 4, 4, 3, 3, 3)),
    14: (9, 5, 14, 5, (8, 9, 8, 11, 8), (4, 4, 4, 4, 3, 3)),
}

SPELL_LIST = {
    1: ["Auditory Illusion", "Chromatic Orb", "Colour Spray", "Dancing Lights", "Detect Illusion", "Glamour", "Hypnotism", "Light (Darkness)", "Phantasmal Force", "Read Magic", "Spook", "Wall of Fog"],
    2: ["Blindness / Deafness", "Blur", "Detect Magic", "False Aura", "Fascinate", "Hypnotic Pattern", "Improved Phantasmal Force", "Invisibility", "Magic Mouth", "Mirror Image", "Quasimorph", "Whispering Wind"],
    3: ["Blacklight", "Dispel Illusion", "Fear", "Hallucinatory Terrain", "Invisibility 10' Radius", "Nondetection", "Paralysation", "Phantom Steed", "Rope Trick", "Spectral Force", "Suggestion", "Wraithform"],
    4: ["Confusion", "Dispel Magic", "Emotion", "Illusory Stamina", "Improved Invisibility", "Massmorph", "Minor Creation", "Phantasmal Killer", "Rainbow Pattern", "Shadow Monsters", "Solid Fog", "Veil of Abandonment"],
    5: ["Chaos", "Demi-Shadow Monsters", "Illusion", "Looking Glass", "Major Creation", "Maze of Mirrors", "Projected Image", "Seeming", "Shadowcast", "Shadowy Transformation", "Time Flow", "Visitation"],
    6: ["Acid Fog", "Dream Quest", "Impersonation", "Manifest Dream", "Mass Suggestion", "Mislead", "Permanent Illusion", "Shades", "Through the Looking Glass", "Triggered Illusion", "True Seeing", "Vision"]
}

def generate_illusionist_stats(level):
    level = max(1, min(level, 14))
        
    hd_dice, hd_mod, thac0, thac0_bonus, saves, spells = ILLUSIONIST_PROGRESSION[level]
    
    # Calculate initial HP from dice pool
    hp = sum(random.randint(1, 4) for _ in range(hd_dice)) + hd_mod
    
    # Randomly prepare spells based on slot counts
    prepared_spells = []
    for lvl_idx, count in enumerate(spells):
        if count > 0:
            lvl = lvl_idx + 1
            available_spells = len(SPELL_LIST[lvl])
            sample_size = min(count, available_spells) 
            selected = random.sample(SPELL_LIST[lvl], sample_size)
            prepared_spells.extend(selected)
            
            if count > available_spells:
                prepared_spells.extend(random.choices(SPELL_LIST[lvl], k=(count - available_spells)))
    
    return {
        "level": level,
        "hp": hp,
        "hit_dice": f"{hd_dice}d4{f'+{hd_mod}' if hd_mod > 0 else ''}",
        "thac0": thac0,
        "attack_bonus": f"+{thac0_bonus}",
        "saves": {
            "Death/Poison": saves[0],
            "Wands": saves[1],
            "Paralysis/Petrify": saves[2],
            "Breath": saves[3],
            "Spells/Rods/Staves": saves[4]
        },
        "spells": spells,
        "prepared_spells": prepared_spells
    }
