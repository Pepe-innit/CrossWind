import pygame
from scene import Scene

class ShopScene(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.font = pygame.font.SysFont(None,60)

        self.sell_button = pygame.Rect(200, 200, 370, 80)
        self.upgrade_boat_button = pygame.Rect(200, 320, 370, 80)
        self.upgrade_rod_button = pygame.Rect(200, 440, 370, 80)

    def handle_events(self, events):
          for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    from gameScene import GameScene
                    self.manager.set_scene(self.manager.game_scene)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos

                #--- Sell all---
                if self.sell_button.collidepoint(mx, my):
                    player = self.manager.game_scene.game.player
                    inv = player.inventory

                    total_value = inv.get_total_value()
                    player.money += round(total_value)
                    inv.items.clear()

                    print(f"Sold all fish for {total_value} coins!")

                #--- Boat upgrade ---
                if self.upgrade_boat_button.collidepoint(mx, my):
                    player = self.manager.game_scene.game.player

                    cost = 100
                    if player.money >= cost:
                        player.money -= cost
                        player.inventory.max_items +=2
                        player.inventory.max_weight += 5
                        player.speed += 0.3
                        print("Boat upgraded")
                    else:
                        print("Not enough money")

                #--- Rod upgrade ---
                if self.upgrade_rod_button.collidepoint(mx, my):
                    player = self.manager.game_scene.game.player

                    cost = 80
                    if player.money >= cost:
                        player.money -=cost

                        player.fishing_upgrade = True
                        print("Rod upgraded!")
                    else:
                        print("Not enough money!")


    def draw(self, screen):
        screen.fill((20, 20, 20))

        #--- Heading ---
        title = self.font.render("Shop", True, (255, 255, 255))
        screen.blit(title, (200, 50))

        #--- Buttons ---
        pygame.draw.rect(screen, (100, 200, 100), self.sell_button)
        pygame.draw.rect(screen, (100, 100, 200), self.upgrade_boat_button)
        pygame.draw.rect(screen, (200, 100, 100), self.upgrade_rod_button)

        screen.blit(self.font.render("Sell All Fish", True, (255, 255, 255)), (210, 210))
        screen.blit(self.font.render("Upgrade Boat 100", True, (255, 255, 255)), (210, 330))
        screen.blit(self.font.render("Upgrade Rod 80", True, (255, 255, 255)), (210, 450))

        #--- Money Display ---
        player = self.manager.game_scene.game.player
        money_text = self.font.render(f"Money: {player.money}", True, (255, 255, 0))
        screen.blit(money_text, (200, 100))

        #--- ESC hint ---
        esc_text = self.font.render("Press ESC to exit", True, (200, 200, 200))
        screen.blit(esc_text, (200, 650))

    