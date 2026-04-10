import random
from ecs import Registry
from components import TavernComponent, TavernNPCComponent, MenuComponent, IdentityComponent, NameComponent
from generators import tavern_logic, dungeon_tavern_logic
from generators.name_generators.tavern_names import generate_tavern_name

class TavernGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_tavern(self, name=None, is_dungeon=False):
        if name is None:
            name = generate_tavern_name()
            if is_dungeon:
                name = f"Dungeon Tavern: {name}" # Or use specialized dungeon tavern names later

        # 2) Decoration
        logic = dungeon_tavern_logic if is_dungeon else tavern_logic
        decor_count = random.randint(1, 2)
        decorations = random.sample(list(logic.DECORATIONS.values()), decor_count)

        # 5) Patrons
        patrons_most = logic.PATRONS_MOST[random.randint(1, 8 if is_dungeon else 12)]
        specific_customer = random.choice(tavern_logic.PATRONS_SPECIFIC) # Stay common for now or add dungeon ones

        # 6) Entertainment
        entertainers = tavern_logic.ENTERTAINERS[random.randint(1, 20)]
        act_count = random.randint(1, 3)
        activities = random.sample(tavern_logic.ACTIVITIES, act_count)

        # 7) Rooms
        best_room = tavern_logic.ROOMS_BEST[random.randint(1, 6)]
        special_room = None
        if random.randint(1, 6) == 1:
            special_room = random.choice(tavern_logic.ROOMS_SPECIAL)

        # 8) Outside
        amenities = []
        if not is_dungeon:
            amen_count = random.randint(1, 3)
            amenities = random.sample(tavern_logic.OUTSIDE_AMENITIES, amen_count)
        else:
            amenities = ["Underground well", "Fungal garden"]

        sign = {
            "shape": self._get_from_dict(logic.SIGN_SHAPES, random.randint(1, 4 if is_dungeon else 20)),
            "material": "Stone" if is_dungeon else random.choice(tavern_logic.SIGN_MATERIALS),
            "position": "Above the door" if is_dungeon else self._get_from_dict(tavern_logic.SIGN_POSITIONS, random.randint(1, 20)),
            "mounting": "Iron chains" if is_dungeon else random.choice(tavern_logic.SIGN_MOUNTING),
            "illustration": random.choice(logic.SIGN_ILLUSTRATIONS if is_dungeon else tavern_logic.SIGN_ILLUSTRATIONS),
            "special": "Nothing special" if is_dungeon else self._get_from_dict(tavern_logic.SIGN_SPECIAL, random.randint(1, 20)),
            "subpanel": "No sub-panel" if is_dungeon else self._get_from_dict(tavern_logic.SIGN_SUBPANELS, random.randint(1, 12))
        }

        # Create Tavern Entity
        tavern = self.registry.create_entity()

        # 3) Bartender
        if is_dungeon:
            bt_traits = [random.choice(dungeon_tavern_logic.BARTENDER_TRAITS), "Suspicious"]
        else:
            bt_traits = [random.choice(tavern_logic.BARTENDER_TRAIT_1), random.choice(tavern_logic.BARTENDER_TRAIT_2)]
        bartender = self.registry.create_entity()
        self.registry.add_component(bartender, TavernNPCComponent(tavern.id, "Bartender", bt_traits))
        self.registry.add_component(bartender, NameComponent("The Bartender"))
        self.registry.add_component(bartender, IdentityComponent("TavernNPC"))
        self.context.dial_gen.apply_dialogue(bartender, "Bartender")

        # 4) Servers
        server_count = random.randint(1, 3)
        common_trait = None
        if random.randint(1, 6) == 1:
            common_trait = random.choice(tavern_logic.SERVER_COMMON_TRAITS)
        
        for i in range(server_count):
            traits = []
            if common_trait: traits.append(common_trait)
            traits.append(random.choice(tavern_logic.SERVER_INDIVIDUAL_TRAITS))
            traits.append(random.choice(tavern_logic.BARTENDER_TRAIT_1))
            
            server = self.registry.create_entity()
            self.registry.add_component(server, TavernNPCComponent(tavern.id, "Server", traits))
            self.registry.add_component(server, NameComponent(f"Server {i+1}"))
            self.registry.add_component(server, IdentityComponent("TavernNPC"))

        # 9) Menu
        menu_type = random.choice(["Specials", "Traveler", "Full Course"])
        menu_items = {}
        if menu_type == "Specials":
            menu_items["Main Dish"] = random.choice(tavern_logic.MAIN_DISHES)
            menu_items["Soup"] = random.choice(tavern_logic.SOUPS)
        elif menu_type == "Traveler":
            menu_items["Snack"] = random.choice(tavern_logic.SNACKS)
            menu_items["Soup"] = random.choice(tavern_logic.SOUPS)
        else:
            menu_items["Soup"] = random.choice(tavern_logic.SOUPS)
            menu_items["Appetizer"] = random.choice(tavern_logic.APPETIZERS)
            menu_items["Main Dish"] = random.choice(tavern_logic.MAIN_DISHES)
            menu_items["Dessert"] = random.choice(tavern_logic.DESSERTS)
        
        # Drinks
        menu_items["Drinks"] = random.sample(logic.DRINKS, 3)
        
        menu = self.registry.create_entity()
        self.registry.add_component(menu, MenuComponent(tavern.id, menu_type, menu_items))
        self.registry.add_component(menu, IdentityComponent("TavernMenu"))
        
        self.registry.add_component(tavern, TavernComponent(name, decorations, patrons_most, specific_customer, entertainers, activities, best_room, special_room, amenities, sign, menu_id=menu.id))
        self.registry.add_component(tavern, NameComponent(name))
        self.registry.add_component(tavern, IdentityComponent("Tavern"))

        return tavern

    def _get_from_dict(self, d, roll):
        keys = sorted(d.keys())
        last_val = d[keys[0]]
        for k in keys:
            if roll >= k:
                last_val = d[k]
            else:
                break
        return last_val
