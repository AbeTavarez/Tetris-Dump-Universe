import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represenmt a single alien in the fleet """

    def __init__(self, tdu_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = tdu_game.screen
        self.settings = tdu_game.settings  # access settingsClass
        # * Load alien image and set its rect attribute
        self.image = pygame.image.load("images/green.bmp")
        self.rect = self.image.get_rect()

        # * Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right"""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)  # alien position
        self.rect.x = self.x  # update position

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
