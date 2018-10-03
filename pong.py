import pygame

from settings import Settings
from paddles import Paddle_Bottom
from paddles import Paddle_Top
from paddles import Paddle_Right
from paddles_ai import Paddle_Bottom_Ai
from paddles_ai import Paddle_Top_Ai
from paddles_ai import Paddle_Left_Ai
from button import Button
from settings import GameStats
from ball import Ball
from scoreboard import Score_Ai
from scoreboard import Score_User
from startup import Start_Up
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Pong")

    stats = GameStats(ai_settings)
    sb = Score_Ai(ai_settings, screen, stats)
    sb2 = Score_User(ai_settings, screen, stats)

    #Make the play button
    play_button = Button(ai_settings, screen, "Play Game")

    #start menu
    start_up = Start_Up(ai_settings, screen)

    #Make paddles
    paddle_bottom = Paddle_Bottom(ai_settings, screen)
    paddle_top = Paddle_Top(ai_settings, screen)
    paddle_right = Paddle_Right(ai_settings, screen)
    paddle_bottom_ai = Paddle_Bottom_Ai(ai_settings, screen)
    paddle_top_ai = Paddle_Top_Ai(ai_settings, screen)
    paddle_left_ai = Paddle_Left_Ai(ai_settings, screen)

    #Make a ball
    ball = Ball(ai_settings, screen)

    while True:
        gf.check_events(ai_settings,stats, play_button, paddle_bottom, paddle_top, paddle_right, sb, sb2)

        if stats.game_active:
            paddle_bottom.update()
            paddle_top.update()
            paddle_right.update()
            paddle_bottom_ai.update()
            paddle_top_ai.update()
            paddle_left_ai.update()
            gf.update_ball(ai_settings, stats, screen, ball, paddle_bottom, paddle_top, paddle_right, paddle_bottom_ai, paddle_top_ai, paddle_left_ai)

        gf.update_screen(ai_settings, start_up, screen, stats, sb, sb2, paddle_bottom_ai, paddle_left_ai, paddle_top_ai, paddle_bottom, paddle_top, paddle_right, ball, play_button)

run_game()