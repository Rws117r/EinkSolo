import random

# Table 2-8 & 2-9 share Parts 2, 3, and 4
PART_1A = ["A", "I", "E", "O", "U", "A", "I", "E", "O", "U", "A", "I", "E", "O", "U", "A", "A", "E", "E", "U"]
PART_1B = ["Ba", "Da", "Ga", "Ha", "Ka", "La", "Ma", "Na", "Ra", "Sa", "Ta", "Za", "Be", "Me", "Ne", "Re", "Se", "Ze", "Ke", "Su"]

PART_2 = ["b", "lr", "d", "ph", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "z", "sh", "sht", "ld"]
PART_3 = ["a", "i", "e", "o", "u", "a", "i", "e", "o", "u", "a", "i", "e", "o", "u", "a", "a", "a", "e", "e"]
PART_4 = [
    "ziel", "thioth", "thior", "zioth", "zior", "za'el", "tiel", "zor", 
    "riel", "miel", "rioth", "mioth", "zal", "rial", "kiel", "roth", 
    "ral", "giel", "bial", "biel"
]

# Table 2-10: Angelic Epithets
EPITHETS = [
    "The Defender", "The Protector", "The Sigil", "The Orb", "The Guardian", "The Candle", "The Lantern", "The Scepter", "The Hawk", "The Tiger",
    "The Leopard", "The Crown", "The Blossom", "The Rain", "The Seer", "The Phoenix", "The Oracle", "The Hand", "The Face", "The Shield",
    "The Sapphire", "The Falcon", "The Lens", "The Eye", "The Root", "The Earth-Shaker", "The Wind-Rider", "The Rescuer", "The Savior", "The Armor",
    "The Helm", "The Flame", "The Wyvern", "The Wand", "The Messenger", "The Deliverer", "The Artificer", "The Counselor", "The Mystic", "The Redeemer"
]

def generate_angelic_name(include_epithet=False):
    # Choose between Table 2-8 (1A) and 2-9 (1B)
    p1 = random.choice(PART_1A if random.random() < 0.5 else PART_1B)
    p2 = random.choice(PART_2)
    p3 = random.choice(PART_3)
    p4 = random.choice(PART_4)
    
    name = f"{p1}{p2}{p3}{p4}"
    
    if include_epithet:
        name += f", {random.choice(EPITHETS)}"
        
    return name
