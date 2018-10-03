import pygame
from pygame.sprite import Sprite

class Paddle_Bottom_Ai(Sprite):
    def __init__(self, ai_settings, screen):
        super(Paddle_Bottom_Ai, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/paddle4.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start paddle at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx // 2
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

class Paddle_Top_Ai(Sprite):
    def __init__(self, ai_settings, screen):
        super(Paddle_Top_Ai, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/paddle4.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start paddle at top center of screen
        self.rect.centerx = self.screen_rect.centerx // 2
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

class Paddle_Left_Ai(Sprite):
    def __init__(self, ai_settings, screen):
        super(Paddle_Left_Ai, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/paddle5.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start paddle at right center of screen
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for paddle_left_ai
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_down and self.rect.bottom < self.ai_settings.paddle_right_speed_factor:
            self.centery += self.ai_settings.paddle_right_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.paddle_right_speed_factor

        if self.moving_up or self.moving_down:
            self.rect.centery = self.centery
        if self.moving_left or self.moving_right:
            self.rect.centerx = self.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)