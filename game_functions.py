import sys
import pygame
from time import sleep

def check_events(ai_settings, stats, play_button, paddle_bottom, paddle_top, paddle_right, sb, sb2):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle_bottom, paddle_top, paddle_right)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle_bottom, paddle_top, paddle_right)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, sb, sb2, stats, play_button, mouse_x, mouse_y)

def check_play_button(ai_settings,sb, sb2, stats, play_button, mouse_x, mouse_y):

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:

        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)

        #reset game
        stats.reset_stats()
        stats.game_active = True

        #reset score
        sb.prep_score_ai()
        sb2.prep_score_user()

def update_screen(ai_settings, start_up, screen, stats, sb, sb2, paddle_bottom_ai, paddle_left_ai, paddle_top_ai, paddle_bottom, paddle_top, paddle_right, ball, play_button):
    screen.fill(ai_settings.bg_color)
    paddle_bottom.blitme()
    paddle_top.blitme()
    paddle_right.blitme()
    ball.blitme()
    paddle_bottom_ai.blitme()
    paddle_left_ai.blitme()
    paddle_top_ai.blitme()

    pygame.draw.line(screen, (255, 255, 255), (500, 600), (500, -600))

    #Draw the score info
    sb.show_score_ai()
    sb2.show_score_user()

    #Draw the play button and start screen if game is inactive
    if not stats.game_active:
        screen.fill(ai_settings.bg_start_color)
        start_up.blitme()
        play_button.draw_button()

    pygame.display.flip()


def check_keydown_events(event, paddle_bottom, paddle_top, paddle_right):
    if event.key == pygame.K_RIGHT:
        paddle_bottom.moving_right = True
        paddle_top.moving_right = True
    elif event.key == pygame.K_LEFT:
        paddle_bottom.moving_left = True
        paddle_top.moving_left = True
    elif event.key == pygame.K_UP:
        paddle_right.moving_up = True
    elif event.key == pygame.K_DOWN:
        paddle_right.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, paddle_bottom, paddle_top, paddle_right):
    if event.key == pygame.K_RIGHT:
        paddle_bottom.moving_right = False
        paddle_top.moving_right = False
    elif event.key == pygame.K_LEFT:
        paddle_bottom.moving_left = False
        paddle_top.moving_left = False
    elif event.key == pygame.K_UP:
        paddle_right.moving_up = False
    elif event.key == pygame.K_UP:
        paddle_right.moving_up = False
    elif event.key == pygame.K_DOWN:
        paddle_right.moving_down = False

def change_ballx_direction(ai_settings):
    ai_settings.ballx_direction *= -1

def change_bally_direction(ai_settings):
    ai_settings.bally_direction *= -1

def update_ball(ai_settings, stats, screen, ball, paddle_bottom, paddle_top, paddle_right, paddle_bottom_ai, paddle_top_ai, paddle_left_ai):

    check_ball_hit_wall(ai_settings, stats, screen, ball)

    ball.update()

    #Ball and Paddle collisions
    if pygame.sprite.collide_rect(paddle_bottom, ball):
        change_ballx_direction(ai_settings)

    if pygame.sprite.collide_rect(paddle_top, ball):
        change_ballx_direction(ai_settings)

    if pygame.sprite.collide_rect(paddle_right, ball):
        change_ballx_direction(ai_settings)

    if pygame.sprite.collide_rect(paddle_bottom_ai, ball):
        change_ballx_direction(ai_settings)

    if pygame.sprite.collide_rect(paddle_top_ai, ball):
        change_ballx_direction(ai_settings)

    if pygame.sprite.collide_rect(paddle_left_ai, ball):
        change_bally_direction(ai_settings)

def check_ball_hit_wall(ai_settings, stats, screen, ball):

    screen_rect = screen.get_rect()
    if ball.rect.bottom >= screen_rect.bottom:
        wall_hit(ai_settings, stats, screen, ball)


def wall_hit(ai_settings, stats, screen, ball):
    if stats.balls_left > 0:
        #Decrement balls_left
        stats.balls_left -= 1

        #Pause
        sleep(0.5)
    else:
        stats.game_active = False

def update_paddle_bottom_ai(paddle_bottom_ai, ball):

    if paddle_bottom_ai.check_edge() and ball.x >= paddle_bottom_ai.x:
        paddle_bottom_ai.update()
    if paddle_bottom_ai.check_edge() and ball.x <= paddle_bottom_ai.x:
        paddle_bottom_ai.update()