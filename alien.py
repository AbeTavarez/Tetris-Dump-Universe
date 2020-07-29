import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represenmt a single alien in the fleet """

    def __init__(self, tdu_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = tdu_game.screen

        # * Load alien image and set its rect attribute
        self.image = pygame.image.load("images/green.bmp")
        self.rect = self.image.get_rect()

        # * Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact horizontal position
        self.x = float(self.rect.x)
