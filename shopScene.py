import pygame
from scene import Scene

class ShopScene(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.font = pygame.font.SysFont(None,60)

    def handle_events(self, events):
          for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    from gameScene import GameScene
                    self.manager.set_scene(self.manager.game_scene)

    def draw(self, screen):
        screen.fill((20, 20, 20))
        text = self.font.render("Shop - Pres ESC to return", True, (255, 255, 255))
        screen.blit(text, (200, 200))
        