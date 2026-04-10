HOUSE_TYPES = {
    "Peasant": {
        "description": "Generally, one room is dedicated to storage and the other serves as a living room. Can accommodate a family of 4 to 5 people.",
        "levels": "1 level",
        "rooms": ["Storage Room", "Living Room"],
        "loot_table": {
            1: "Nothing", 2: "Nothing", 3: "Nothing", 4: "Nothing",
            5: "1 ration",
            6: "1d2 gp"
        }
    },
    "Merchant": {
        "description": "City house par excellence. Ground floor is a store or craft workshop (front) and storeroom/kitchen (back). First floor has bedrooms and bath.",
        "levels": "2 levels + attic + cellar",
        "rooms": {
            "Ground Floor": ["Store/Workshop", "Storeroom", "Kitchen"],
            "First Floor": ["Bedrooms", "Bath"],
            "Other": ["Attic", "Cellar"]
        },
        "loot_table": {
            1: "Nothing", 2: "Nothing", 3: "Nothing",
            4: "1d10 gp",
            5: "Silverware",
            6: "Expensive bottle of wine"
        }
    },
    "Noble": {
        "description": "Dwelling characterized by a library, office, dining hall, and chapel. Spreads out on the ground before rising. Numerous rooms for family and servants.",
        "levels": "Multiple levels, spreading layout",
        "rooms": ["Library", "Office", "Dining Hall", "Chapel", "Family Bedrooms", "Servant Bedrooms"],
        "loot_table": {
            1: "Nothing", 2: "Nothing",
            3: "1d20 gp",
            4: "Valuable book",
            5: "Artpiece",
            6: "1d2 gems"
        }
    }
}
