import random
from components import DungeonComponent, DungeonLevelComponent, IdentityComponent, NameComponent
from generators import dungeon_logic
from generators.dungeon_level_generator import DungeonLevelGenerator
from generators.name_generators.cthonic import generate_cthonic
from generators.name_generators.colossoponderous import generate_colossoponderous

class DungeonGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context
        self.level_gen = DungeonLevelGenerator(context)
        self.area_count = 0 
        self.area_entities = [] # List of area entity IDs

    def generate_new_area(self, name=None):
        """
        Main entry point when a 'Dungeon' is rolled on the hex map.
        Adds a new area to the world's megadungeon cross-section.
        """
        self.area_count += 1
        area_id = self.area_count
        
        # 1) Theme
        theme_roll = random.randint(1, 20)
        theme = dungeon_logic.THEMES.get(theme_roll, "None")
        
        # 2) Levels
        num_levels = random.randint(1, 6)
        level_ids = []
        depths = []
        for _ in range(num_levels):
            d = random.randint(1, 6)
            depths.append(d)
        depths.sort()
        
        for d in depths:
            level_entity = self.level_gen.generate_level(area_id, d)
            level_ids.append(level_entity.id)

        # Create Area Entity
        area_entity = self.registry.create_entity()
        comp = DungeonComponent(area_id, theme, level_ids)
        self.registry.add_component(area_entity, comp)
        
        # Generate evocative name if none provided
        if not name:
            if random.random() < 0.7:
                dname = generate_cthonic()
            else:
                dname = generate_colossoponderous()
        else:
            dname = name
            
        if theme != "None":
            dname += f" ({theme})"
            
        self.registry.add_component(area_entity, NameComponent(dname))
        self.registry.add_component(area_entity, IdentityComponent("Dungeon"))

        # 3) Links to the Area on the Left (Previous Area)
        if self.area_entities:
            prev_area_id = self.area_entities[-1]
            self._link_areas(prev_area_id, area_entity.id)

        self.area_entities.append(area_entity.id)
        return area_entity

    def _link_areas(self, left_area_id, right_area_id):
        """
        Links levels of the left area to levels of the right area.
        """
        left_area = self.registry.get_entity_by_id(left_area_id)
        right_area = self.registry.get_entity_by_id(right_area_id)
        
        left_comp = self.registry.get_component(left_area, DungeonComponent)
        right_comp = self.registry.get_component(right_area, DungeonComponent)
        
        # Get levels for right area indexed by depth
        right_levels_by_depth = {}
        for l_id in right_comp.level_ids:
            l_ent = self.registry.get_entity_by_id(l_id)
            l_comp = self.registry.get_component(l_ent, DungeonLevelComponent)
            if l_comp.depth not in right_levels_by_depth:
                right_levels_by_depth[l_comp.depth] = []
            right_levels_by_depth[l_comp.depth].append(l_id)

        # For each level on the left, roll for links to levels on the right
        for l_id in left_comp.level_ids:
            l_ent = self.registry.get_entity_by_id(l_id)
            l_comp = self.registry.get_component(l_ent, DungeonLevelComponent)
            d = l_comp.depth
            
            # Roll for number of links (1d8)
            link_roll = random.randint(1, 8)
            num_links = 0
            is_secret = False
            
            if link_roll in [5, 6]: num_links = 1
            elif link_roll == 7: num_links = 2
            elif link_roll == 8: num_links = 1; is_secret = True
            
            if num_links == 0: continue
            
            # Possible depths: Same, Above (d-1), Below (d+1)
            target_depths = [d, d-1, d+1]
            possible_targets = []
            for td in target_depths:
                if td in right_levels_by_depth:
                    possible_targets.extend(right_levels_by_depth[td])
            
            if not possible_targets: continue
            
            for _ in range(num_links):
                target_id = random.choice(possible_targets)
                l_comp.links.append({
                    "to": target_id,
                    "secret": is_secret,
                    "type": "Horizontal"
                })
