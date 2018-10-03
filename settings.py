import random
class Settings():

    def __init__(self):

        #Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (10, 150, 200)
        self.bg_start_color = (0, 0, 0)

        #Paddle settings
        self.paddle_bottom_speed_factor = 2
        self.paddle_top_speed_factor = 2
        self.paddle_right_speed_factor = 2

        #Ball settings
        self.ballx_speed_factor = 1
        self.bally_speed_factor = 1
        self.ballx_direction = 1
        self.bally_direction = 1
        self.ball_limit = 1

class GameStats():
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Start game in an inactive state
        self.game_active = False

        #High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        self.balls_left = self.ai_settings.ball_limit
        self.score = 0
        self.level = 1