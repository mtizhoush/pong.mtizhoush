import pygame
from pygame.sprite import Sprite

class Paddle_Bottom(Sprite):
    def __init__(self, ai_settings, screen):
        super(Paddle_Bottom, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/paddle2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start paddle at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx * 1.5
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for paddle_bottom center
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.paddle_bottom_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.paddle_bottom_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Paddle_Top(Sprite):
    def __init__(self, ai_settings, screen):
        super(Paddle_Top, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/paddle2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start paddle at top center of screen
        self.rect.centerx = self.screen_rect.centerx * 1.5
        self.rect.top = self.screen_rect.top

        # Store a decimal value for paddle
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.paddle_top_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.paddle_top_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Paddle_Right(Sprite):
    def __init__(self, ai_settings, screen):
        super(Paddle_Right, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/paddle3.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start paddle at right center of screen
        self.rect.right = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for paddle_right
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.paddle_right_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.paddle_right_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

