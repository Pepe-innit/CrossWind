import pygame
from scene import Scene

class MainMenu(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.font = pygame.font.SysFont(None, 80)

    #--- Methods ---

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    from gameScene import GameScene
                    self.manager.set_scene(self.manager.game_scene)

    def draw(self, screen):
        screen.fill((50, 100, 200))
        text = self.font.render("Press Enter to Play", True, (255, 255, 255))
        screen.blit(text, (300, 300))
        