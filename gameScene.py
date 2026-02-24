import pygame
from scene import Scene
from game import Game

class GameScene(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.game = Game()

    def handle_events(self, events):
        pass

    def update(self):
        #--- Dock Interaction ---
        player_rect = pygame.Rect(
            self.game.player.x - self.game.player.radius,
            self.game.player.y - self.game.player.radius,
            self.game.player.radius * 2,
            self.game.player.radius * 2
        )
        if player_rect.colliderect(self.game.dock.rect):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                from shopScene import ShopScene
                self.manager.set_scene(self.manager.shop_scene)
                return
            
        #--- Fishing Update ---
        self.game.fishingManager.update()
        if not self.game.fishingManager.minigame:
            self.game.player.update()

    def draw(self, screen):
        self.game.draw_objects()
        