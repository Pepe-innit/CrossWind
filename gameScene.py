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
        self.near_dock = False

        player_rect = pygame.Rect(
            self.game.player.x - self.game.player.radius,
            self.game.player.y - self.game.player.radius,
            self.game.player.radius * 2,
            self.game.player.radius * 2
        )
        if player_rect.colliderect(self.game.dock.rect):
            self.near_dock = True
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
        if self.near_dock:
            font = pygame.font.SysFont(None, 40)
            text = font.render("Press E to enter the shop", True, (0, 0, 0))

            dock_rect = self.game.dock.rect

            text_x = dock_rect.x + dock_rect.width // 2 - text.get_width() // 2
            text_y = dock_rect.y - text.get_height() - 10

            screen.blit(text, (10, text_y))

        mouse_pos = pygame.mouse.get_pos()

        for rect, fish in self.game.inventory_positions:
            if rect.collidepoint(mouse_pos):
                font = pygame.font.SysFont(None, 32)
                text = font.render(f"{fish.weight} kg", True, (255, 255, 255))
            
                tx = rect.x + rect.width // 2 - text.get_width() // 2
                ty = rect.y - text.get_height() - 5

                screen.blit(text, (tx, ty))
                break
        