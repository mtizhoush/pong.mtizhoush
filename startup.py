import pygame.font

class Start_Up():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('images/menu.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def blitme(self):
        self.screen.blit(self.image, self.rect)

