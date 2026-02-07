import pygame
import math
from gameObject import GameObject


class FishingSpot(GameObject):

    def __init__(self, x , y, width, height, image_path = None):
        super().__init__(x, y, width, height, image_path = None)

        self.color = (255, 255, 255)

#--- Methods ---
    def draw(self, screen):
        if self.image:
            pass
        else:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.width // 2)
       
                
            
