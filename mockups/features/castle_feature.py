import pygame
import random
import os
from .feature_base import Feature
from ecs import Registry

class CastleFeature(Feature):
    def __init__(self, app):
        super().__init__(app)
        self.state = 0 # 0: Summary, 1: Details
        
        # Load Icons
        icons_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "icons")
        self.icon_castle = pygame.image.load(os.path.join(icons_dir, "castle.png"))
        self.icon_castle = pygame.transform.scale(self.icon_castle, (100, 100))

    def generate(self):
        from generators.castle_generator import CastleGenerator
        from generators.generator_context import GeneratorContext
        from components import CastleComponent
        
        # Using a clean registry
        self.registry = Registry()
        self.context = GeneratorContext(self.registry)
        gen = CastleGenerator(self.context)
        castle_ent = gen.generate_castle()
        
        c = self.registry.get_component(castle_ent, CastleComponent)
        
        people_list = [f"{p[0]}: {p[1]}" for p in c.people]
        def_list = list(c.defenses)
        if c.gatehouse: def_list.append(f"Gatehouse: {c.gatehouse}")
        if c.moat: def_list.append(f"Moat: {c.moat}")
        
        keep_str = "No central keep."
        if c.keep:
            k = c.keep
            keep_str = f"A **{k['shape']}** keep with {k['levels']} levels. Features: {k['defensive']} (def), {k['non_defensive']} (non-def). Stocks: {k['supplies']}. Jails: {k['jails']}."

        g = c.garrison
        garr_str = f"Led by a **{g['Lord']}**, total force of {g['Total Fighters']} fighters."
        dist_str = ", ".join([f"{k}: {v}" for k, v in g['Distribution'].items() if v > 0])

        self.data = {
            "name": c.name,
            "summary": f"This {c.type_name.lower()} is in {c.condition.lower()} condition. Its most striking feature is its {c.unusual}.",
            "defense": def_list,
            "keep": keep_str,
            "garrison": garr_str,
            "distribution": dist_str,
            "people": people_list,
            "disposition": c.disposition,
            "event": c.event or "Peaceful period"
        }
        self.state = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.generate()
                return True
            elif event.key == pygame.K_RIGHT:
                self.state = (self.state + 1) % 2
                return True
            elif event.key == pygame.K_LEFT:
                if self.state == 0:
                    self.app.current_feature = None
                    return True
                self.state = (self.state - 1) % 2
                return True
        return False

    def render(self, screen):
        if self.state == 0: self._render_summary(screen)
        else: self._render_details(screen)

    def _render_summary(self, screen):
        app = self.app
        margin = 35
        mid_x = app.width // 2
        lx = margin
        title_mid_x = mid_x // 2
        screen.blit(self.icon_castle, (title_mid_x - 50, 40))
        
        # Title Styling
        app.render_tracked_line(screen, "CASTLE", app.title_font, app.text_color, (title_mid_x - app.get_tracked_width("CASTLE", app.title_font, 2)//2, 150), 2)
        app.render_tracked_line(screen, "OF", app.h2_font, app.text_color, (title_mid_x - app.get_tracked_width("OF", app.h2_font, 2)//2, 185), 2)
        
        name_text = self.data['name'].upper()
        name_font = app.huge_font if len(name_text) < 10 else app.title_font
        app.render_tracked_line(screen, name_text, name_font, app.text_color, (title_mid_x - app.get_tracked_width(name_text, name_font, 2)//2, 220), 2)
        
        app.draw_wrapped_text(screen, self.data['summary'], app.body_font, app.text_color, pygame.Rect(lx, 290, mid_x - margin - 10, 150))

        # Right Column
        rx, ry = mid_x + 10, 30
        col_w = app.width - rx - margin
        
        # Garrison Header
        header_rect = pygame.Rect(rx, ry, col_w, 32)
        pygame.draw.rect(screen, app.text_color, header_rect)
        screen.blit(app.h2_font.render("GARRISON & STAFF", True, app.bg_color), (rx + 8, ry + 6))
        
        ry += 45
        ry = app.draw_rich_text(screen, f"**Force Details:** {self.data['garrison']}", app.body_font, app.body_bold, app.text_color, pygame.Rect(rx, ry, col_w, 100))
        ry += 10
        pygame.draw.line(screen, app.text_color, (rx, ry), (rx + col_w, ry), 1)
        ry += 8
        ry = app.draw_rich_text(screen, f"**Current Event:** {self.data['event']}", app.body_font, app.body_bold, app.text_color, pygame.Rect(rx, ry, col_w, 100))
        ry += 10
        
        # Key Personnel
        screen.blit(app.body_bold.render("NOTABLE RESIDENTS:", True, app.text_color), (rx, ry))
        ry += 20
        for person in self.data['people'][:3]:
            pygame.draw.rect(screen, app.text_color, (rx, ry + 4, 6, 6), 1)
            pygame.draw.rect(screen, app.text_color, (rx + 2, ry + 6, 2, 2))
            app.draw_rich_text(screen, person, app.body_font, app.body_bold, app.text_color, pygame.Rect(rx + 12, ry, col_w - 12, 30), line_spacing=1)
            ry += 22

    def _render_details(self, screen):
        app = self.app
        margin = 35
        mid_x = app.width // 2
        app.render_tracked_line(screen, f"FORTRESS DETAILS: {self.data['name'].upper()}", app.title_font, app.text_color, (margin, 50), 2)
        pygame.draw.line(screen, app.text_color, (margin, 90), (app.width - margin, 90), 2)
        
        # Defenses
        lx, ly = margin, 110
        screen.blit(app.body_bold.render("EXTERIOR DEFENSES", True, app.text_color), (lx, ly))
        ly += 25
        for d in self.data['defense']:
            pygame.draw.rect(screen, app.text_color, (lx, ly + 4, 6, 6), 1)
            app.draw_rich_text(screen, d, app.body_font, app.body_bold, app.text_color, pygame.Rect(lx + 12, ly, mid_x - margin - 20, 40))
            ly += 22
            
        # Keep Details
        rx, ry = mid_x + 20, 110
        screen.blit(app.body_bold.render("CENTRAL KEEP", True, app.text_color), (rx, ry))
        ry += 25
        app.draw_rich_text(screen, self.data['keep'], app.body_font, app.body_bold, app.text_color, pygame.Rect(rx, ry, mid_x - margin - 20, 200))
        
        # Disposition
        ry += 150
        screen.blit(app.body_bold.render("LOCAL DISPOSITION", True, app.text_color), (rx, ry))
        ry += 25
        app.draw_rich_text(screen, self.data['disposition'], app.body_font, app.body_bold, app.text_color, pygame.Rect(rx, ry, mid_x - margin - 20, 100))

    def get_instructions(self):
        if self.state == 0: return "SPACE: Reroll | LEFT: Menu | RIGHT: Grid View"
        return "SPACE: Reroll | LEFT: Summary | ESC: Menu"
