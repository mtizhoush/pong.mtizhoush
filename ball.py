import pygame
from pygame.sprite import Sprite

class Ball(Sprite):

    def __init__(self, ai_settings, screen):
        super(Ball, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery

        #Store the ball's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def center_ball(self):
        self.x = self.screen_rect.centerx
        self.y = self.screen_rect.centery

    def check_user_edges(self):
        screen_rect = self.screen.get_rect()
        if self.x <= screen_rect.left - 50:
            return True
        elif self.y <= (screen_rect.top - 50) and self.x <= (screen_rect.right // 2):
            return True

    def check_comp_edges(self):
        screen_rect = self.screen.get_rect()
        if self.x >= screen_rect.right + 50:
            return True
        elif self.y <= (screen_rect.top - 50) and self.x >= (screen_rect.right // 2):
            return True

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Move ball right or left
        self.x += (self.ai_settings.ballx_speed_factor * self.ai_settings.ballx_direction)
        self.rect.x = self.x

        # Move ball up or down
        self.y += (self.ai_settings.bally_speed_factor * self.ai_settings.bally_direction)
        self.rect.y = self.y






