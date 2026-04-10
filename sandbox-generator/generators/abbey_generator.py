import random
from ecs import Registry
from components import AbbeyComponent, IdentityComponent, NameComponent, DeityComponent, AlchemyComponent
from generators import abbey_logic
from generators.relic_generator import RelicGenerator

class AbbeyGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_abbey(self, deity_id=None):
        # 1) Name
        name = abbey_logic.generate_name()
        
        # 2) Residents Type
        residents_type = random.choice(["Monks", "Nuns"])
        leader_title = "Abbot" if residents_type == "Monks" else "Abbess"
        leader_level = random.randint(9, 12)
        
        # 3) Size
        size_roll = random.randint(1, 6)
        size = "Small" if size_roll <= 5 else "Major"
        
        # 4) Population
        if size == "Small":
            pop = random.randint(1, 4) * 10 + 20
            if pop >= 50:
                leader_level += 1
        else:
            pop = random.randint(1, 24) * 10 + 90
            leader_level += (pop // 100)
            
        # 5) Relic and Fame
        relic_id = None
        fame = None
        
        # Try to find a deity if not provided
        if deity_id is None:
            deities = list(self.registry.view(DeityComponent))
            if deities:
                deity_entity = random.choice(deities)
                deity_id = deity_entity.id

        if size == "Major":
            relic_id = self.context.relic_gen.generate_relic(deity_id)
            fame_roll = random.randint(1, 20)
            if fame_roll <= 11:
                fame = abbey_logic.FAME_REASONS[fame_roll-1]
            else:
                fame = "Religious artifact"
        
        # 6) Locations
        locations = list(abbey_logic.CORE_LOCATIONS)
        for cat in abbey_logic.ADDITIONAL_LOCATIONS:
            locations.append(random.choice(abbey_logic.ADDITIONAL_LOCATIONS[cat]))
            
        # 7) Activities
        farming = random.sample(abbey_logic.ACTIVITIES["Farming"], 2)
        workshop = random.choice(abbey_logic.ACTIVITIES["Workshop"])
        other_act = random.choice(abbey_logic.ACTIVITIES["Other"])
        activities = farming + [workshop, other_act]
        
        # 8) History
        history = abbey_logic.generate_history()
        
        # 9) Event (1 in 6)
        event = None
        if random.randint(1, 6) == 1:
            timing = random.choice(abbey_logic.EVENT_TIMING)
            nature = random.choice(abbey_logic.EVENT_NATURE)
            event = f"{nature} ({timing})"
        
        # Create Entity
        abbey_entity = self.registry.create_entity()
        comp = AbbeyComponent(
            name, residents_type, leader_title, leader_level, size, 
            pop, locations, activities, fame, history, event, relic_id, deity_id
        )
        self.registry.add_component(abbey_entity, comp)
        self.registry.add_component(abbey_entity, NameComponent(name))
        self.registry.add_component(abbey_entity, IdentityComponent("Abbey"))
        
        # 10) Alchemy (Medicinal supplies)
        if "Infirmary" in locations or random.random() < 0.3:
            # Abbey alchemy is more "herbal/medicinal"
            ingredients = [self.context.alchemy_gen.generate_ingredient() for _ in range(2)]
            potions = [self.context.alchemy_gen.generate_potion()] 
            self.registry.add_component(abbey_entity, AlchemyComponent(ingredients, potions))

        # 11) Books (Scriptorium or Major size)
        notable_ids = []
        if size == "Major" or "Scriptorium" in locations:
            num_books = random.randint(1, 3)
            for _ in range(num_books):
                book = self.context.book_gen.generate_book()
                notable_ids.append(book.id)
        
        comp.notable_ids = notable_ids

        return abbey_entity
