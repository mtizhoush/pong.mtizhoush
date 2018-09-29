import sys

import pygame

def check_events(paddle_bottom, paddle_top):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle_bottom, paddle_top)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle_bottom, paddle_top)

def update_screen(ai_settings, screen, paddle_bottom, paddle_top, paddle_left, ball):
    screen.fill(ai_settings.bg_color)
    paddle_bottom.blitme()
    paddle_top.blitme()
    paddle_left.blitme()
    ball.blitme()

    pygame.display.flip()

def check_keydown_events(event, paddle_bottom, paddle_top, paddle_right):
    if event.key == pygame.K_RIGHT:
        paddle_bottom.moving_right = True
        paddle_top.moving_right = True
    elif event.key == pygame.K_LEFT:
        paddle_bottom.moving_left = True
        paddle_top.moving_right = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_UP:
        paddle_right.moving_up = True

def check_keyup_events(event, paddle_bottom, paddle_top, paddle_right):
    if event.key == pygame.K_RIGHT:
        paddle_bottom.moving_right = False
        paddle_top.moving_right = False
    elif event.key == pygame.K_LEFT:
        paddle_bottom.moving_left = False
        paddle_top.moving_right = False
    elif event.key == pygame.K_UP:
        paddle_right.moving_up = False

def update_ball(ball):
    ball.update()