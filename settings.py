
class Settings:
    """Store all settings for the game"""
    # Screen settings

    def __init__(self):
        self.screen_width = 1200  # dimensions of Surface
        self.screen_height = 800
        self.bg_color = (54, 54, 54)  # Sets screen bg (background) color
        self.fighter_speed = 2.5
        # Bullets settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3
