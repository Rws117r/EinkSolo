import random
from ecs import Registry
from components import HamletComponent, IdentityComponent, NameComponent
from generators import hamlet_logic
from generators.house_generator import HouseGenerator
from generators.name_generators import dreamlandish_places

class HamletGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_hamlet(self):
        # 1) Main Building (d12)
        building_roll = random.randint(1, 12)
        building = hamlet_logic.MAIN_BUILDINGS[building_roll]

        # 2) Houses (a few)
        num_houses = random.randint(1, 4) + 1
        house_ids = []
        for _ in range(num_houses):
            house_entity = self.context.house_gen.generate_house("Peasant")
            house_ids.append(house_entity.id)

        # 3) Initial Disposition (2d6)
        disp_roll = random.randint(1, 6) + random.randint(1, 6)
        # Using a helper logic to get from dict range
        keys = sorted(hamlet_logic.DISPOSITIONS.keys())
        disposition = hamlet_logic.DISPOSITIONS[keys[-1]]
        for k in keys:
            if disp_roll <= k:
                disposition = hamlet_logic.DISPOSITIONS[k]
                break

        # 4) Secret (1d6 -> 1)
        secret = None
        if random.randint(1, 6) == 1:
            secret_roll = random.randint(1, 6)
            secret = hamlet_logic.SECRETS[secret_roll]

        # Create Entity
        entity = self.registry.create_entity()
        comp = HamletComponent(building, house_ids, disposition, secret)
        self.registry.add_component(entity, comp)

        # Name
        place_name = dreamlandish_places.generate_place_name()
        name = f"Hamlet of {place_name}"
        self.registry.add_component(entity, NameComponent(name))
        self.registry.add_component(entity, IdentityComponent("Hamlet"))

        return entity
