import random

# NPC Barks and Specialized Dialogue Lines

GENERIC_BARKS = [
    "Fine day for a journey, isn't it?",
    "Keep your wits about you in the wilds.",
    "The gods are watching, for better or worse.",
    "I've seen stranger things than you, traveler.",
    "Rumors are just shadows of truth.",
    "The coins are heavy but the work is light.",
    "Mind your business and I'll mind mine.",
    "There's profit in the shadows, if you dare."
]

SPECIALTY_DIALOGUE = {
    "Wizard": [
        "The weave is thin in these parts.",
        "My research requires... silence.",
        "A spell is merely a thought made manifest.",
        "Rare components are worth more than gold."
    ],
    "Bartender": [
        "First drink is for the thirst, second is for the stories.",
        "I hear everything, but I remember little for free.",
        "Try the house specialty; it's mostly edible.",
        "No fighting in the taproom!"
    ],
    "Monarch": [
        "Our kingdom is vast, but our patience is short.",
        "Heavy is the crown, and heavier the tax.",
        "Justice is the sword of the sovereign.",
        "State your business and be brief."
    ],
    "Mercenary": [
        "Blood is the only currency I trust.",
        "Steel doesn't lie, unlike poets.",
        "I've fought for worse causes than this.",
        "Payment upfront, or no steel today."
    ]
}

def get_dialogue(specialty=None):
    if specialty and specialty in SPECIALTY_DIALOGUE:
        if random.random() < 0.6:
            return random.choice(SPECIALTY_DIALOGUE[specialty])
    return random.choice(GENERIC_BARKS)
