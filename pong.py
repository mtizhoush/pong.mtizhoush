import sys
import pygame

from settings import Settings
from paddles import Paddle_Bottom
from paddles import Paddle_Top
from paddles import Paddle_Right

from ball import Ball
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Pong")

    #Make paddles
    paddle_bottom = Paddle_Bottom(ai_settings, screen)
    paddle_top = Paddle_Top(ai_settings, screen)
    paddle_right = Paddle_Right(ai_settings, screen)

    #Make a ball
    ball = Ball(ai_settings, screen)

    while True:
        gf.check_events(paddle_bottom, paddle_top)
        paddle_bottom.update()
        paddle_top.update()
        paddle_right.update()
        gf.update_ball(ball)
        gf.update_screen(ai_settings, screen, paddle_bottom, paddle_top, paddle_right, ball)


run_game()