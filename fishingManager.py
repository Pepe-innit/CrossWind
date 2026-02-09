import pygame
import math
import random
from fishingSpot import FishingSpot
from fishingMiniGame import FishingMiniGame

class FishingManager:

    def __init__(self, player, fishing_spots, width, height):
        self.player = player
        self.fishing_spots = fishing_spots
        self.width = width
        self.height = height
        self.minigame = None

    def update(self):

        if self.minigame:
            result = self.minigame.update()

            if result == "success":
                print("Fish caught!")
                self.minigame = None
            elif result == "fail":
                print("Fish lost!")
                self.minigame = None
            return

        self.closest_spot = None

        if not self.fishing_spots:
             return

        keys = pygame.key.get_pressed()

        for spot in self.fishing_spots:
            distance = math.dist((self.player.x, self.player.y), (spot.x, spot.y))
            
            if distance < 200 and keys[pygame.K_e]:
                if self.minigame is None:
                    self.minigame = FishingMiniGame(self.width, self.height)
                self.fishing_spots.remove(spot)
                self.spawn_new_spot()
            elif distance < 200:
                self.closest_spot = spot
                break
    
    def spawn_new_spot(self):
        spot_width = 32*4
        spot_height = 32*4
        MIN_DISTANCE = 200

        while True:
            x = random.uniform(self.width/100 + spot_width, self.width - 10 - spot_width)
            y = random.uniform(self.height/100 + spot_height, self.height - 10 - spot_height)

            too_close = False

            for spot in self.fishing_spots:
                distance = math.dist((x, y), (spot.x, spot.y))
                if distance < MIN_DISTANCE:
                    too_close = True
                    break

            if not too_close:
                break

        new_spot = FishingSpot(x, y , spot_width, spot_height, 'assets/CrossWinds_Bubbles.png')
        self.fishing_spots.append(new_spot)
