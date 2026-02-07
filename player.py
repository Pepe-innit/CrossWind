import pygame
import math
from gameObject import GameObject

class Player(GameObject):

    def __init__(self, x , y, width, height, image_path = None):
        super().__init__(x, y, width, height, image_path = None)

        self.angle = 270
        self.speed = 4
        self.rotation_speed = 1
        self.color = (84, 59, 26)

    #--- Methods --- 

    #--- Movement --- 
    def update(self):
        keys = pygame.key.get_pressed()

        #Turning
        if keys[pygame.K_a]:
            self.angle -= self.rotation_speed
        if keys[pygame.K_d]:
            self.angle += self.rotation_speed
        
        #Moving Forwards
        if keys[pygame. K_w]:
            rad = math.radians(self.angle)
            self.x += math.cos(rad) * self.speed
            self.y += math.sin(rad) * self.speed
        
    def draw(self, screen):
        if self.image:
            rotated_image = pygame.transform.rotate(self.image, -self.angle)
            rect = rotated_image.get_rect(center=(self.x, self.y))
            screen.blit(rotated_image, rect)
        else:
            rect_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            pygame.draw.rect(rect_surface, self.color, (0, 0, self.width, self.height))
            rotated_surface = pygame.transform.rotate(rect_surface, -self.angle)
            rect = rotated_surface.get_rect(center=(self.x, self.y))
            screen.blit(rotated_surface, rect)


