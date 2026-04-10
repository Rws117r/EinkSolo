import random

# Level: (HD_dice, HD_mod, THAC0, THAC0_bonus, (D, W, P, B, S), (L1, L2, L3, L4, L5))
CLERIC_PROGRESSION = {
    1:  (1, 0, 19, 0, (11, 12, 14, 16, 15), (0, 0, 0, 0, 0)),
    2:  (2, 0, 19, 0, (11, 12, 14, 16, 15), (1, 0, 0, 0, 0)),
    3:  (3, 0, 19, 0, (11, 12, 14, 16, 15), (2, 0, 0, 0, 0)),
    4:  (4, 0, 19, 0, (11, 12, 14, 16, 15), (2, 1, 0, 0, 0)),
    5:  (5, 0, 17, 2, (9, 10, 12, 14, 12), (2, 2, 0, 0, 0)),
    6:  (6, 0, 17, 2, (9, 10, 12, 14, 12), (2, 2, 1, 1, 0)),
    7:  (7, 0, 17, 2, (9, 10, 12, 14, 12), (2, 2, 2, 1, 1)),
    8:  (8, 0, 17, 2, (9, 10, 12, 14, 12), (3, 3, 2, 2, 1)),
    9:  (9, 0, 14, 5, (6, 7, 9, 11, 9), (3, 3, 3, 2, 2)),
    10: (9, 1, 14, 5, (6, 7, 9, 11, 9), (4, 4, 3, 3, 2)),
    11: (9, 2, 14, 5, (6, 7, 9, 11, 9), (4, 4, 4, 3, 3)),
    12: (9, 3, 14, 5, (6, 7, 9, 11, 9), (5, 5, 4, 4, 3)),
    13: (9, 4, 12, 7, (3, 5, 7, 8, 7), (5, 5, 5, 4, 4)),
    14: (9, 5, 12, 7, (3, 5, 7, 8, 7), (6, 5, 5, 5, 4)),
}

SPELL_LIST = {
    1: ["Cure Light Wounds", "Detect Evil", "Detect Magic", "Light", "Protection from Evil", "Purify Food and Water", "Remove Fear", "Resist Cold"],
    2: ["Bless", "Find Traps", "Hold Person", "Know Alignment", "Resist Fire", "Silence 15' Radius", "Snake Charm", "Speak with Animals"],
    3: ["Continual Light", "Cure Disease", "Growth of Animal", "Locate Object", "Remove Curse", "Striking"],
    4: ["Create Water", "Cure Serious Wounds", "Neutralize Poison", "Protection from Evil 10' Radius", "Speak with Plants", "Sticks to Snakes"],
    5: ["Commune", "Create Food", "Dispel Evil", "Insect Plague", "Quest", "Raise Dead"]
}

def generate_cleric_stats(level):
    level = max(1, min(level, 14))
        
    hd_dice, hd_mod, thac0, thac0_bonus, saves, spells = CLERIC_PROGRESSION[level]
    
    # Calculate initial HP from dice pool (1d6 for Clerics)
    hp = sum(random.randint(1, 6) for _ in range(hd_dice)) + hd_mod
    
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
        "hit_dice": f"{hd_dice}d6{f'+{hd_mod}' if hd_mod > 0 else ''}",
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
