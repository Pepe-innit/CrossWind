import pygame
import sys
import random
import math
from player import Player
from fishingSpot import FishingSpot
from fishingManager import FishingManager
from fishingMiniGame import FishingMiniGame
from dock import Dock

class Game:
    def __init__(self):
        self.width = 1728
        self.height = 972
        self.background_colour = (102, 190, 255)

        self.game_window = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()
        
        self.player = Player(self.width/2, self.height/2, 16*10, 16*10, self.width, self.height, 'assets/CrossWinds_Boat.png')

        self.dock = Dock(0, self.height/ 2, 50, 150)

        #Fishing spots generation
        self.font = pygame.font.SysFont(None, 36)
        spot_width = 32*4
        spot_height = 32*4

        self.fishingSpots = [
            FishingSpot(random.uniform(self.width/100 + spot_width, self.width - 10 - spot_width),
                        random.uniform(self.height/100 + spot_height, self.height - 10 - spot_height),
                        spot_width, spot_height, 'assets/CrossWinds_Bubbles.png'),
            FishingSpot(random.uniform(self.width/100 + spot_width, self.width - 10 - spot_width),
                        random.uniform(self.height/100 + spot_height, self.height - 10 - spot_height),
                        spot_width, spot_height, 'assets/CrossWinds_Bubbles.png'),
            FishingSpot(random.uniform(self.width/100 + spot_width, self.width - 10 - spot_width),
                        random.uniform(self.height/100 + spot_height, self.height - 10 - spot_height),
                        spot_width, spot_height, 'assets/CrossWinds_Bubbles.png')
        ]

        self.fishingManager = FishingManager(self.player, self.fishingSpots, self.width, self.height)

#--- Methods ---        
    def draw_objects(self):
        self.game_window.fill(self.background_colour)

        #--- Fishing Spot Display ---
        for spot in self.fishingSpots:
            spot.draw(self.game_window)
        
        #--- Dock Entry Display ---
        self.dock.draw(self.game_window)

        #--- Player Display ---
        self.player.draw(self.game_window)

        #--- Hint Display ---
        if self.fishingManager.closest_spot:
            text = self.font.render("Press E to catch fish", True, (0, 0, 0))
            spot = self.fishingManager.closest_spot
            self.game_window.blit(text, (spot.x - 80, spot.y - 60))

        #--- Inventory Display ---
        y = 10
        for name, amount in self.player.inventory.get_items().items():
            text = self.font.render(f"{name}: {amount}", True, (0, 0, 0))
            self.game_window.blit(text, (10, y))
            y += 30

        #--- Minigame Display ---
        if self.fishingManager.minigame:
            self.fishingManager.minigame.draw(self.game_window)

    def run_game_loop(self):

        while True:

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                else:
                    pass

            self.fishingManager.update()
            if not self.fishingManager.minigame:
                self.player.update()     

            self.draw_objects()

            pygame.display.update()
            self.clock.tick(60)           