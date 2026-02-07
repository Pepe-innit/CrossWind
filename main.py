import pygame
from game import Game
from fishingMiniGame import FishingMiniGame
pygame.init()

game = Game()
game.run_game_loop()

pygame.quit()
quit()