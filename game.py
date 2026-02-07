import pygame
import sys
import random
import math
from player import Player
from fishingSpot import FishingSpot
from fishingManager import FishingManager


class Game:
    def __init__(self):
        self.width = 1728
        self.height = 972
        self.background_colour = (102, 190, 255)

        self.game_window = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()
        
        self.player = Player(self.width/2, self.height/2, 200, 100)

        #Fishing spots generation
        self.font = pygame.font.SysFont(None, 36)
        spot_width = 100
        spot_height = 50

        self.fishingSpots = [
            FishingSpot(random.uniform(self.width/100 + spot_width, self.width - 10 - spot_width), random.uniform(self.height/100 + spot_height, self.height - 10 - spot_height), spot_width, spot_height),
            FishingSpot(random.uniform(self.width/100 + spot_width, self.width - 10 - spot_width), random.uniform(self.height/100 + spot_height, self.height - 10 - spot_height), spot_width, spot_height),
            FishingSpot(random.uniform(self.width/100 + spot_width, self.width - 10 - spot_width), random.uniform(self.height/100 + spot_height, self.height - 10 - spot_height), spot_width, spot_height)
        ]

        self.fishingManager = FishingManager(self.player, self.fishingSpots)

#--- Methods ---        
    def draw_objects(self):
        self.game_window.fill(self.background_colour)

        for spot in self.fishingSpots:
            spot.draw(self.game_window)

        self.player.draw(self.game_window)

        if self.fishingManager.closest_spot:
            text = self.font.render("Press E to catch fish", True, (0, 0, 0))
            spot = self.fishingManager.closest_spot
            self.game_window.blit(text, (spot.x - 80, spot.y - 60))

        pygame.display.update()

    def run_game_loop(self):

        while True:

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                else:
                    pass
            
            self.fishingManager.update()
            self.player.update()                  
            self.draw_objects()
            self.clock.tick(60)           
