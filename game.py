import pygame
import sys
from player import Player



class Game:

    def __init__(self):
        self.width = 1728
        self.height = 972
        self.background_colour = (102, 190, 255)

        self.game_window = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()
        
        self.player = Player(self.width/2, self.height/2, 200, 100)

#--- Methods ---        
    def draw_objects(self):
        self.game_window.fill(self.background_colour)

        self.player.draw(self.game_window)

        pygame.display.update()

    def run_game_loop(self):

        while True:

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                else:
                    pass
            
            self.player.update()
                    
            self.draw_objects()

            self.clock.tick(100)
