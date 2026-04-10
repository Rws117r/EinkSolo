import pygame

class Feature:
    def __init__(self, app):
        self.app = app
        self.data = None
        self.state = 0 # 0 for summary/main, 1+ for detail views

    def generate(self):
        """Generate new data for this feature."""
        pass

    def handle_event(self, event):
        """Return True if handled, False otherwise."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.generate()
                return True
        return False

    def render(self, screen):
        """Draw the feature to the screen."""
        pass

    def get_instructions(self):
        """Return instruction text for the bottom bar."""
        return "SPACE: Reroll | ESC: Menu"
