import pygame
from sceneManager import SceneManager
from mainMenu import MainMenu

from gameScene import GameScene
from mainMenu import MainMenu
from shopScene import ShopScene

pygame.init()

screen = pygame.display.set_mode((1728, 972))
clock = pygame.time.Clock()

manager = SceneManager()

manager.main_menu = MainMenu(manager)
manager.game_scene = GameScene(manager)
manager.shop_scene = ShopScene(manager)

manager.set_scene(manager.main_menu)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    manager.handle_events(events)
    manager.update()
    manager.draw(screen)

    pygame.display.update()
    clock.tick(60)