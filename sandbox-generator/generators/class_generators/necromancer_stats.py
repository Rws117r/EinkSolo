import random

# Level: (HD_dice, HD_mod, THAC0, THAC0_bonus, (D, W, P, B, S), (L1, L2, L3, L4, L5, L6))
NECROMANCER_PROGRESSION = {
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
    1: ["Chill Touch", "Command Dead", "Corpse Visage", "Decay", "Deathlight", "Detect Undead", "Marionette", "Pass Undead", "Protection From Evil", "Read Magic", "Skull Speech", "Undead Servitor"],
    2: ["Bone Armour", "Choke", "Death Recall", "Detect Magic", "Feign Death", "Paralysing Touch", "Seal Tomb", "Skeletal Steed", "Skull Sight", "Silence 15' Radius", "Speak With Dead", "Spectral Hand"],
    3: ["Animate Dead, Temporary", "Bone Staff", "Carrion Stench", "Crypt Sight", "Death Ward", "Drag From Death's Door", "Fear", "Grave Breath", "Hold Person", "Protection From Evil 10' Radius", "Skull Trap", "Vampiric Touch"],
    4: ["Command Undead", "Corpse Clairvoyance", "Corpse Mask", "Curse", "Dispel Magic", "Inter", "Reassemble", "Rotting Touch", "Skeletal Wings", "Swarm Transformation", "Wall of Bones", "Wound Transference"],
    5: ["Animate Dead", "Bonewrack", "Cloudkill", "Commune With Spirit", "Gaseous Form", "Guardian Spirit", "Hold Undead", "Magic Jar", "Spirit Vision", "Summon Undead", "Veil of Life", "Wall of Gloom"],
    6: ["Bonesteel", "Deathlessness", "Death Spell", "Doomveil", "Energy Drain", "Eternal Quest", "Necrotic Gaze", "Protection From Undead", "Sacrificial Resurrection", "Skeletal Army", "Spirit Shield", "Undead Regeneration"]
}

def generate_necromancer_stats(level):
    level = max(1, min(level, 14))
        
    hd_dice, hd_mod, thac0, thac0_bonus, saves, spells = NECROMANCER_PROGRESSION[level]
    
    # Calculate initial HP from dice pool (1d4 for Necromancer)
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
