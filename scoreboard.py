import pygame.font
from pygame.sprite import Group
from ball import Ball

class Score_Ai():

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #Font settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the initial score image
        self.prep_score_ai()

    def prep_score_ai(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #Display the score at the top center of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx - 20
        self.score_rect.top = 20

    def show_score_ai(self):
        self.screen.blit(self.score_image, self.score_rect)

class Score_User():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #Font settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the initial score image
        self.prep_score_user()

    def prep_score_user(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #Display the score at the top center of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx + 20
        self.score_rect.top = 20

    def show_score_user(self):
        self.screen.blit(self.score_image, self.score_rect)