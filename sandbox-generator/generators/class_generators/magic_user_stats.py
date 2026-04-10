import random

# Level: (HD_dice, HD_mod, THAC0, THAC0_bonus, (D, W, P, B, S), (L1, L2, L3, L4, L5, L6))
MAGIC_USER_PROGRESSION = {
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
    1: ["Charm Person", "Detect Magic", "Floating Disc", "Hold Portal", "Light", "Magic Missile", "Protection from Evil", "Read Languages", "Read Magic", "Shield", "Sleep", "Ventriloquism"],
    2: ["Continual Light", "Detect Evil", "Detect Invisible", "ESP", "Invisibility", "Knock", "Levitate", "Locate Object", "Mirror Image", "Phantasmal Force", "Web", "Wizard Lock"],
    3: ["Clairvoyance", "Dispel Magic", "Fire Ball", "Fly", "Haste", "Hold Person", "Infravision", "Invisibility 10' Radius", "Lightning Bolt", "Protection from Evil 10' Radius", "Protection from Normal Missiles", "Water Breathing"],
    4: ["Charm Monster", "Confusion", "Dimension Door", "Growth of Plants", "Hallucinatory Terrain", "Massmorph", "Polymorph Others", "Polymorph Self", "Remove Curse", "Wall of Fire", "Wall of Ice", "Wizard Eye"],
    5: ["Animate Dead", "Cloudkill", "Conjure Elemental", "Contact Higher Plane", "Feeblemind", "Hold Monster", "Magic Jar", "Pass-Wall", "Telekinesis", "Teleport", "Transmute Rock to Mud", "Wall of Stone"],
    6: ["Anti-Magic Shell", "Control Weather", "Death Spell", "Disintegrate", "Geas", "Invisible Stalker", "Lower Water", "Move Earth", "Part Water", "Projected Image", "Reincarnation", "Stone to Flesh"]
}

def generate_magic_user_stats(level):
    level = max(1, min(level, 14)) # Cap between 1 and 14 based on ruleset
        
    hd_dice, hd_mod, thac0, thac0_bonus, saves, spells = MAGIC_USER_PROGRESSION[level]
    
    # Calculate initial HP from dice pool
    hp = sum(random.randint(1, 4) for _ in range(hd_dice)) + hd_mod
    
    # Randomly prepare spells based on slot counts
    prepared_spells = []
    for lvl_idx, count in enumerate(spells):
        if count > 0:
            lvl = lvl_idx + 1
            available_spells = len(SPELL_LIST[lvl])
            # Ensure we don't sample more than available unique spells
            sample_size = min(count, available_spells) 
            selected = random.sample(SPELL_LIST[lvl], sample_size)
            prepared_spells.extend(selected)
            
            # If for some reason slot count exceeded unique spells, permit duplicates (rare/custom rules)
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
