import sys
import os
import pygame
import random

# Make sure we can import from the parent directory
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "sandbox-generator"))

from features.tower_feature import TowerFeature
from features.castle_feature import CastleFeature

class MockupApp:
    def __init__(self):
        pygame.init()
        self.width, self.height = 648, 480
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("E-Ink System Tools Mockup")
        
        # Colors (E-Ink style)
        self.bg_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.accent_color = (128, 128, 128) 
        
        # Fonts
        fonts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Fonts")
        self.huge_font = pygame.font.Font(os.path.join(fonts_dir, "KH Giga TRIAL", "OTF", "KHGigaTRIAL-Bold.otf"), 46)
        self.title_font = pygame.font.Font(os.path.join(fonts_dir, "KH Giga TRIAL", "OTF", "KHGigaTRIAL-Bold.otf"), 32)
        self.h2_font = pygame.font.Font(os.path.join(fonts_dir, "KH Giga TRIAL", "OTF", "KHGigaTRIAL-Medium.otf"), 18)
        self.body_font = pygame.font.Font(os.path.join(fonts_dir, "KH Teka Trial", "OTF", "KHTekaTRIAL-Regular.otf"), 13)
        self.body_bold = pygame.font.Font(os.path.join(fonts_dir, "KH Teka Trial", "OTF", "KHTekaTRIAL-Bold.otf"), 13)
        
        # Features
        self.features = [
            TowerFeature(self),
            CastleFeature(self)
        ]
        self.menu_options = ["TOWER GENERATOR", "CASTLE GENERATOR", "DUNGEON DEPTHS", "ALCHEMY LAB"]
        self.menu_index = 0
        self.current_feature = None # None means Menu
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.render()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.current_feature:
                        self.current_feature = None
                    else:
                        self.running = False
                    return

                if self.current_feature:
                    self.current_feature.handle_event(event)
                else:
                    self.handle_menu_event(event)

    def handle_menu_event(self, event):
        if event.key == pygame.K_UP:
            self.menu_index = (self.menu_index - 1) % len(self.menu_options)
        elif event.key == pygame.K_DOWN:
            self.menu_index = (self.menu_index + 1) % len(self.menu_options)
        elif event.key in [pygame.K_SPACE, pygame.K_RETURN, pygame.K_RIGHT]:
            if self.menu_index < len(self.features):
                self.current_feature = self.features[self.menu_index]
                self.current_feature.generate()

    def render(self):
        self.screen.fill(self.bg_color)
        
        if self.current_feature:
            self.current_feature.render(self.screen)
            instr = self.current_feature.get_instructions()
        else:
            self.render_menu()
            instr = "UP/DOWN: Navigate | SPACE: Select | ESC: Exit"
            
        # Instruction bar
        instr_surf = self.body_font.render(instr, True, self.accent_color)
        instr_rect = instr_surf.get_rect(midbottom=(self.width//2, self.height - 5))
        self.screen.blit(instr_surf, instr_rect)
        
        pygame.display.flip()
        
        # --- Screenshot logic ---
        if "--screenshot" in sys.argv:
            pygame.image.save(self.screen, "feature_mockup_menu.png")
            self.menu_index = 0 # Tower
            self.current_feature = self.features[0]
            self.current_feature.generate()
            sys.argv.remove("--screenshot")
            sys.argv.append("--screenshot_tower_summary")
        elif "--screenshot_tower_summary" in sys.argv:
            pygame.image.save(self.screen, "feature_mockup_tower_summary.png")
            # Go to overview
            self.current_feature.state = 1
            sys.argv.remove("--screenshot_tower_summary")
            sys.argv.append("--screenshot_tower_overview")
        elif "--screenshot_tower_overview" in sys.argv:
            pygame.image.save(self.screen, "feature_mockup_tower_overview.png")
            # Go to castle
            self.menu_index = 1 # Castle
            self.current_feature = self.features[1]
            self.current_feature.generate()
            sys.argv.remove("--screenshot_tower_overview")
            sys.argv.append("--screenshot_castle")
        elif "--screenshot_castle" in sys.argv:
            pygame.image.save(self.screen, "feature_mockup_castle.png")
            self.running = False

    def render_menu(self):
        title = "SYSTEM TOOLS"
        tw = self.get_tracked_width(title, self.title_font, 4)
        self.render_tracked_line(self.screen, title, self.title_font, self.text_color, ((self.width - tw) // 2, 60), 4)
        pygame.draw.line(self.screen, self.text_color, (self.width//4, 110), (self.width*3//4, 110), 2)
        
        start_y = 160
        for i, opt in enumerate(self.menu_options):
            is_sel = (i == self.menu_index)
            color = self.text_color if is_sel else self.accent_color
            if is_sel:
                pygame.draw.rect(self.screen, self.text_color, (self.width//4 - 40, start_y + 4, 10, 10))
            f = self.title_font if is_sel else self.h2_font
            ow = self.get_tracked_width(opt, f, 1)
            self.render_tracked_line(self.screen, opt, f, color, ((self.width - ow) // 2, start_y), 1)
            start_y += 50

    # --- Utility Methods ---
    def get_tracked_width(self, text, font, tracking):
        if not text: return 0
        return sum(font.size(char)[0] + tracking for char in text) - tracking

    def render_tracked_line(self, surface, text, font, color, pos, tracking):
        x, y = pos
        for char in text:
            char_surf = font.render(char, True, color)
            surface.blit(char_surf, (x, y))
            x += font.size(char)[0] + tracking

    def draw_wrapped_text(self, surface, text, font, color, rect, line_spacing=5, tracking=1):
        y = rect.top
        lines = text.split('\n')
        for line in lines:
            words = line.split(' ')
            current_line = []
            for word in words:
                current_line.append(word)
                if self.get_tracked_width(' '.join(current_line), font, tracking) > rect.width:
                    current_line.pop()
                    self.render_tracked_line(surface, ' '.join(current_line), font, color, (rect.left, y), tracking)
                    y += font.size('A')[1] + line_spacing
                    current_line = [word]
            if current_line:
                self.render_tracked_line(surface, ' '.join(current_line), font, color, (rect.left, y), tracking)
                y += font.size('A')[1] + line_spacing
        return y

    def draw_rich_text(self, surface, text, font_reg, font_bold, color, rect, line_spacing=5, tracking=1):
        y = rect.top
        lines = text.split('\n')
        space_w = font_reg.size(' ')[0] + tracking
        for line in lines:
            words = line.split(' ')
            x = rect.left
            is_bold = False
            for word in words:
                parts = word.split('**')
                word_w = 0
                temp_bold = is_bold
                for i, p in enumerate(parts):
                    if i > 0: temp_bold = not temp_bold
                    if p:
                        f = font_bold if temp_bold else font_reg
                        word_w += self.get_tracked_width(p, f, tracking)
                if x + word_w > rect.right and x > rect.left:
                    x = rect.left
                    y += font_reg.size('A')[1] + line_spacing
                for i, p in enumerate(parts):
                    if i > 0: is_bold = not is_bold
                    if p:
                        f = font_bold if is_bold else font_reg
                        for char in p:
                            surface.blit(f.render(char, True, color), (x, y))
                            x += f.size(char)[0] + tracking
                x += space_w
            y += font_reg.size('A')[1] + line_spacing
        return y

if __name__ == "__main__":
    app = MockupApp()
    app.run()
