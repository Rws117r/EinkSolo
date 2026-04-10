import random

# Adventure Hook Foundations

# WHO (The Instigator or Victim)
WHO = {
    (1, 10): "A disgraced noble",
    (11, 20): "A paranoid wizard",
    (21, 30): "A dying mercenary",
    (31, 40): "A local merchant guild",
    (41, 50): "An undercover cultist",
    (51, 60): "A child with strange dreams",
    (61, 70): "A vengeful spirit",
    (71, 80): "A double agent",
    (81, 90): "An eccentric collector",
    (91, 100): "A secret society"
}

# ACTION (The verb)
ACTION = {
    (1, 10): "seeks the recovery of",
    (11, 20): "needs to destroy",
    (21, 30): "wants to smuggle",
    (31, 40): "must protect",
    (41, 50): "is obsessed with finding",
    (51, 60): "is terrified of",
    (61, 70): "demands the sacrifice of",
    (71, 80): "seeks to awaken",
    (81, 90): "intends to replicate",
    (91, 100): "is hiding"
}

# WHAT (The focus)
WHAT = {
    (1, 10): "a cursed relic",
    (11, 20): "a map to a megadungeon",
    (21, 30): "a forbidden ritual",
    (31, 45): "a lost family heirloom",
    (46, 60): "a powerful enchantment",
    (61, 75): "a political secret",
    (76, 90): "a biological weapon (monster eggs)",
    (91, 100): "the true name of a deity"
}

# WHERE (The destination or source)
WHERE = {
    (1, 15): "deep within a nearby dungeon",
    (16, 30): "in the vaults of a specific city",
    (31, 45): "at the summit of a distant peak",
    (46, 60): "hidden in a humble village house",
    (61, 75): "carried by a rogue faction patrol",
    (76, 90): "buried under a local landmark",
    (91, 100): "behind the walls of a wizard tower"
}

# WHY (The twist or motivation)
TWIST = {
    (1, 20): "...but they are actually the villain.",
    (21, 40): "...and it must be done before the next full moon.",
    (41, 60): "...because they signed a contract with a demon.",
    (61, 80): "...and the reward is a complete lie.",
    (81, 100): "...but success will trigger a greater catastrophe."
}

def generate_hook_text():
    who = _roll(WHO)
    action = _roll(ACTION)
    what = _roll(WHAT)
    where = _roll(WHERE)
    twist = _roll(TWIST) if random.randint(1, 6) == 1 else ""
    
    return f"{who} {action} {what} {where}{twist}"

def _roll(table):
    r = random.randint(1, 100)
    for k, v in table.items():
        if k[0] <= r <= k[1]:
            return v
    return list(table.values())[-1]
