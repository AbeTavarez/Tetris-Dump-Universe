import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, tdu_game):
        """Create a bullet object at the fighter's current position"""
        super().__init__()
        self.screen = tdu_game.screen
        self.settings = tdu_game.settings
        self.color = self.settings.bullet_color

        # Create a Bullet rect at (0,0) and then correct position of the Fighter
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = tdu_game.fighter.rect.midtop

        # Store the bullets position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        # bullet moves up by decreasing the y coodinate
        self.y -= self.settings.bullet_speed

        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
