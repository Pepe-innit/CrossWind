import pygame
import math

class FishingManager:

    def __init__(self, player, fishing_spots):
        self.player = player
        self.fishing_spots = fishing_spots

    def update(self):
        self.closest_spot = None

        if not self.fishing_spots:
             return

        keys = pygame.key.get_pressed()

        for spot in self.fishing_spots:
            distance = math.dist((self.player.x, self.player.y), (spot.x, spot.y))
            
            if distance < 200 and keys[pygame.K_e]:
                print("Fish caught!")
                self.fishing_spots.remove(spot)
            elif distance < 200:
                self.closest_spot = spot
                break
