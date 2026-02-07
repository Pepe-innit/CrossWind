import pygame
import os

class GameObject:

    def __init__(self, x, y, width, height, image_path = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        

        if image_path:
            base_path = os.path.dirname(__file__)
            full_path = os.path.join(base_path, image_path)

            image = pygame.image.load(full_path)
            self.image = pygame.transform.scale(image, (width, height))
        else:
            self.image = None

# --- Methods ---

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,(self.x, self.y, self.width, self.height))