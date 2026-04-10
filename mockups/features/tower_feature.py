import pygame
import random
import os
from .feature_base import Feature
from ecs import Registry
from generators.generator_context import GeneratorContext
from generators.tower_generator import TowerGenerator
from components import (
    TowerComponent, TowerLevelComponent, NameComponent, 
    LevelComponent, SpecialtyComponent, AppearanceComponent, 
    GoalComponent, StaffComponent, IdentityComponent
)

class TowerFeature(Feature):
    def __init__(self, app):
        super().__init__(app)
        self.selected_level_index = 0
        self.state = 0 # 0: Summary, 1: Overview Grid, 2: Detail
        
        # Load Icons
        icons_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "icons")
        self.icon_tower = pygame.image.load(os.path.join(icons_dir, "stone-tower.png"))
        self.icon_hat = pygame.image.load(os.path.join(icons_dir, "pointy-hat.png"))
        self.icon_tower = pygame.transform.scale(self.icon_tower, (100, 100))
        self.icon_hat = pygame.transform.scale(self.icon_hat, (28, 20))

    def generate(self):
        # 1. GENERATE DATA (using the actual Generator)
        self.registry = Registry()
        self.context = GeneratorContext(self.registry)
        gen = TowerGenerator(self.context)
        tower_ent = gen.generate_tower()
        
        # 2. EXTRACT DATA FOR UI
        tower_comp = self.registry.get_component(tower_ent, TowerComponent)
        
        # Resident Data
        wiz_id = tower_comp.resident_id
        wiz_ent = self.registry.get_entity_by_id(wiz_id)
        wiz_name = self.registry.get_component(wiz_ent, NameComponent).name
        level = self.registry.get_component(wiz_ent, LevelComponent).level
        specialty = self.registry.get_component(wiz_ent, SpecialtyComponent).specialty
        appearance = self.registry.get_component(wiz_ent, AppearanceComponent).appearance
        goal = self.registry.get_component(wiz_ent, GoalComponent).goal
        staff_str = str(self.registry.get_component(wiz_ent, StaffComponent))

        # Title mapping
        titles = {"Necromancy": "Necromancer", "Illusion": "Illusionist", "Invocation": "Invoker", "Generalist": "Wizard", "Cleric": "Cleric", "Druid": "Druid"}
        title = titles.get(specialty, "Elementalist" if "Elemental" in specialty else specialty)

        # OSE Stats
        # OSE Stats - Picking the right generator function based on specialty
        s_low = specialty.lower()
        if "necromancy" in s_low:
            from generators.class_generators.necromancer_stats import generate_necromancer_stats
            mu_stats = generate_necromancer_stats(level)
        elif "illusion" in s_low:
            from generators.class_generators.illusionist_stats import generate_illusionist_stats
            mu_stats = generate_illusionist_stats(level)
        elif "druid" in s_low:
            from generators.class_generators.druid_stats import generate_druid_stats
            mu_stats = generate_druid_stats(level)
        elif "cleric" in s_low:
            from generators.class_generators.cleric_stats import generate_cleric_stats
            mu_stats = generate_cleric_stats(level)
        else:
            from generators.class_generators.magic_user_stats import generate_magic_user_stats
            mu_stats = generate_magic_user_stats(level)
        saves = mu_stats['saves']
        sv_str = f"D{saves['Death/Poison']} W{saves['Wands']} P{saves['Paralysis/Petrify']} B{saves['Breath']} S{saves['Spells/Rods/Staves']}"

        # Levels
        levels_data = []
        for lid in tower_comp.level_ids:
            lent = self.registry.get_entity_by_id(lid)
            lcomp = self.registry.get_component(lent, TowerLevelComponent)
            
            # Format interactions (remove icon placeholders, they are added in render)
            inters = [line.strip() for line in lcomp.equipment.split('\n') if line.strip()]
            
            levels_data.append({
                "number": str(lcomp.index + 1) if lcomp.level_type != "Ground" else "G",
                "title": lcomp.usage,
                "description": lcomp.appearance,
                "interactions": inters
            })

            if lcomp.level_type == "Ground":
                self.selected_level_index = len(levels_data) - 1

        self.data = {
            "name": tower_comp.name,
            "summary": f"This {tower_comp.shape} {tower_comp.material} tower is visually characterized by its {', '.join(tower_comp.details)}. Internally, its floors are navigated entirely by {tower_comp.connection}. It is currently the domain of the {title} {wiz_name}.",
            "wizard_name": wiz_name,
            "wizard_title": title,
            "wizard_summary": f"Visually described as {appearance.lower()}. {staff_str.capitalize()} Their primary ambition is {goal.lower()}.",
            "stats_line": (
                f"**AC** 9 [10], **HD** {mu_stats['hit_dice']} ({mu_stats['hp']}hp), **Att** 1 x staff ({mu_stats['attack_bonus']} or by spell), "
                f"**THAC0** {mu_stats['thac0']} [+0], **MV** 120' (40'), "
                f"**SV** {sv_str} ({mu_stats['level']}), "
                f"**ML** 8, **AL** Lawful, **Spells** {'/'.join(map(str, [s for s in mu_stats['spells'] if s > 0]))}, "
                f"**Specialty** {specialty}"
            ),
            "prepared": mu_stats['prepared_spells'],
            "levels": levels_data
        }
        self.state = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.generate()
                return True
            elif event.key == pygame.K_RIGHT:
                self.state = (self.state + 1) % 3
                return True
            elif event.key == pygame.K_LEFT:
                if self.state == 0:
                    self.app.current_feature = None
                    return True
                self.state = (self.state - 1) % 3
                return True
            elif self.state == 1: # Overview Grid
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    idx = int(event.unicode) - 1
                    if idx < len(self.data['levels']):
                        self.selected_level_index = idx
                        self.state = 2
                        return True
        return False

    def render(self, screen):
        if self.state == 0: self._render_summary(screen)
        elif self.state == 1: self._render_overview(screen)
        else: self._render_detail(screen)

    def _render_summary(self, screen):
        app = self.app
        margin = 35
        mid_x = app.width // 2
        lx = margin
        title_mid_x = mid_x // 2
        screen.blit(self.icon_tower, (title_mid_x - 50, 40))
        
        # Split TOWER OF [NAME]
        app.render_tracked_line(screen, "TOWER", app.title_font, app.text_color, (title_mid_x - app.get_tracked_width("TOWER", app.title_font, 2)//2, 150), 2)
        app.render_tracked_line(screen, "OF", app.h2_font, app.text_color, (title_mid_x - app.get_tracked_width("OF", app.h2_font, 2)//2, 185), 2)
        
        name_text = self.data['name'].replace("Tower of ", "").upper()
        name_font = app.huge_font if len(name_text) < 10 else app.title_font
        app.render_tracked_line(screen, name_text, name_font, app.text_color, (title_mid_x - app.get_tracked_width(name_text, name_font, 2)//2, 220), 2)
        
        app.draw_wrapped_text(screen, self.data['summary'], app.body_font, app.text_color, pygame.Rect(lx, 290, mid_x - margin - 10, 150))

        # Right
        rx, ry = mid_x + 10, 30
        col_w = app.width - rx - margin
        header_rect = pygame.Rect(rx, ry, col_w, 32)
        pygame.draw.rect(screen, app.text_color, header_rect)
        header_txt = f"{self.data['wizard_title'].upper()} {self.data['wizard_name'].upper()}"
        screen.blit(app.h2_font.render(header_txt, True, app.bg_color), (rx + 8, ry + 6))
        screen.blit(self.icon_hat, (rx + col_w - 36, ry + 6))
        
        ry += 45
        ry = app.draw_wrapped_text(screen, self.data['wizard_summary'], app.body_font, app.text_color, pygame.Rect(rx, ry, col_w, 80))
        ry += 10
        pygame.draw.line(screen, app.text_color, (rx, ry), (rx + col_w, ry), 1)
        ry += 8
        ry = app.draw_rich_text(screen, self.data['stats_line'], app.body_font, app.body_bold, app.text_color, pygame.Rect(rx, ry, col_w, 150))
        ry += 5
        pygame.draw.line(screen, app.text_color, (rx, ry), (rx + col_w, ry), 1)
        ry += 10
        
        spell_text = f"**Prepared Spells:** {', '.join(self.data['prepared'])}"
        pygame.draw.rect(screen, app.text_color, (rx, ry + 4, 8, 8), 1) 
        pygame.draw.rect(screen, app.text_color, (rx + 2, ry + 6, 4, 4))
        app.draw_rich_text(screen, spell_text, app.body_font, app.body_bold, app.text_color, pygame.Rect(rx + 15, ry, col_w - 15, 120))

    def _render_overview(self, screen):
        app = self.app
        margin = 35
        title = f"LEVEL OVERVIEW: {self.data['name'].upper()}"
        app.render_tracked_line(screen, title, app.title_font, app.text_color, (margin, 40), 1)
        cell_w = (app.width - margin*3) // 2
        cell_h = 150
        for i in range(min(4, len(self.data['levels']))):
            level = self.data['levels'][i]
            col, row = i % 2, i // 2
            cx, cy = margin + col * (cell_w + margin), 100 + row * (cell_h + 30)
            
            num_surf = app.huge_font.render(level['number'], True, app.text_color)
            screen.blit(num_surf, (cx, cy))
            screen.blit(app.title_font.render(level['title'], True, app.text_color), (cx + 35, cy + 12))
            pygame.draw.line(screen, app.text_color, (cx, cy + 50), (cx + cell_w, cy + 50), 2)
            
            dy = cy + 60
            app.draw_rich_text(screen, level['description'], app.body_font, app.body_bold, app.text_color, pygame.Rect(cx, dy, cell_w, 60), line_spacing=2)
            iy = dy + 50
            for inter in level['interactions'][:2]:
                pygame.draw.rect(screen, app.text_color, (cx + cell_w//2, iy + 4, 6, 6), 1)
                pygame.draw.rect(screen, app.text_color, (cx + cell_w//2 + 2, iy + 6, 2, 2))
                app.draw_rich_text(screen, inter, app.body_font, app.body_bold, app.text_color, pygame.Rect(cx + cell_w//2 + 12, iy, cell_w//2 - 12, 30), line_spacing=1)
                iy += 22

    def _render_detail(self, screen):
        app = self.app
        level = self.data['levels'][self.selected_level_index]
        margin = 35
        mid_x = app.width // 2
        app.render_tracked_line(screen, f"LEVEL {level['number']}: {level['title'].upper()}", app.title_font, app.text_color, (margin, 50), 2)
        pygame.draw.line(screen, app.text_color, (margin, 90), (app.width - margin, 90), 2)
        app.draw_rich_text(screen, level['description'], app.body_font, app.body_bold, app.text_color, pygame.Rect(margin, 110, mid_x - margin, 350))
        rx, ry = mid_x + 20, 110
        screen.blit(app.body_bold.render("INTERACTIONS", True, app.text_color), (rx, ry))
        ry += 30
        for inter in level['interactions']:
            pygame.draw.rect(screen, app.text_color, (rx - 15, ry + 4, 8, 8), 1)
            pygame.draw.rect(screen, app.text_color, (rx - 13, ry + 6, 4, 4))
            ry = app.draw_rich_text(screen, inter, app.body_font, app.body_bold, app.text_color, pygame.Rect(rx, ry, mid_x - 50, 70), line_spacing=10)

    def get_instructions(self):
        if self.state == 0: return "SPACE: Reroll | LEFT: Menu | RIGHT: Grid View"
        elif self.state == 1: return "SPACE: Reroll | LEFT: Summary | RIGHT/1-4: Details"
        return "UP/DOWN: Nav Spire | LEFT: Overview | ESC: Menu"
