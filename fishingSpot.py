import pygame
from gameObject import GameObject


class FishingSpot(GameObject):

    def __init__(self, x , y, width, height, image_path = None):
        super().__init__(x, y, width, height, image_path)

        self.color = (255, 255, 255)

#--- Methods ---
    def draw(self, screen):
        if self.image:
            rect = self.image.get_rect(center=(self.x, self.y))
            screen.blit(self.image, rect)
        else:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.width // 2)
       
                
            
