import pygame
import random

class FishingMiniGame:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.balance = 0
        self.fish_force = 0
        self.balance_speed = 1.2
        self.fish_force_speed = random.uniform(0.1, 0.2)
        self.max_balance = 100
        
        self.catch_progress = 0
        self.catch_goal = 200

        self.active = True


    def update(self):
        keys = pygame.key.get_pressed()

        self.fish_force += random.uniform(-1, 1) * self.fish_force_speed
        self.balance += self.fish_force

        if keys[pygame.K_a]:
            self.balance -= self.balance_speed
        if keys[pygame.K_d]:
            self.balance += self.balance_speed

        if self.balance < -150:
            self.balance = -150
        if self.balance > 150:
            self.balance = 150

        if abs(self.balance) < 40:
            self.catch_progress += 1
        else:
            self.catch_progress -=1
            if self.catch_progress <0:
                self.catch_progress = 0

        #Minigame Victory
        if self.catch_progress >= self.catch_goal:
            return "success"
        
        #Minigame Loss
        if abs(self.balance) >= self.max_balance:
            return "fail"
        
        return "continue"

    def draw(self, screen):
        center_x = self.screen_width // 2
        center_y = self.screen_height // 2

        font = pygame.font.SysFont(None, 36)
        text = font.render("Keep pointer in target zone!", True, (255, 255, 255))
        screen.blit(text, (center_x - text.get_width() // 2, center_y - 60))

        progress_text = font.render(f"{self.catch_progress}/{self.catch_goal}", True, (255, 255, 255))
        screen.blit(progress_text, (center_x - progress_text.get_width() // 2, center_y + 80))

        #Grey bar
        pygame.draw.rect(screen, (50, 50, 50), (center_x - 150, center_y, 300, 20), border_radius =10)
        #Target bar
        pygame.draw.rect(screen, (0, 200, 0), (center_x - 40, center_y, 80, 20),)
        pygame.draw.rect(screen, (0, 255, 0), (center_x - 40, center_y, 80, 20), 3,) #Target bar outline

        #Pointer
        indicator_x = center_x + self.balance
        pygame.draw.rect(screen, (255, 255, 255), (indicator_x - 5, center_y - 10, 10, 40), border_radius=5)
        pygame.draw.rect(screen, (255, 255, 255), (indicator_x - 5, center_y - 10, 10, 40), border_radius=5)
        pygame.draw.rect(screen, (255, 255, 255), (indicator_x - 7, center_y - 12, 14, 44), 2, border_radius=7)

        #Progress bar
        pygame.draw.rect(screen, (80, 80, 80), (center_x - 150, center_y + 50, 300, 20), border_radius=10)
        progress_width = (self.catch_progress / self.catch_goal) * 300
        pygame.draw.rect(screen, (200, 100, 50), (center_x - 150, center_y + 50, progress_width, 20), border_radius=10)