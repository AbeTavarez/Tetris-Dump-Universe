import pygame


class Fighter:
    def __init__(self, tdu_game):
        """Initialize the ship and set its starting position"""
        self.screen = tdu_game.screen
        self.screen_rect = tdu_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/fighter.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
