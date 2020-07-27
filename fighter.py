import pygame


class Fighter:
    def __init__(self, tdu_game):
        """Initialize the ship and set its starting position"""
        # tdu_game is an instance of the Tetris Dump Universe, giving Fighter access to all the game resources from tdu
        # assign screen to an attribute of Fighter for easy access
        self.screen = tdu_game.screen
        # gets the screen rect att and assign it to self, to place the fighter on desire location
        self.screen_rect = tdu_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/fighter.bmp')  # return surface
        # assign new image to out fighter
        self.rect = self.image.get_rect()

        # Start each new ship at bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom  # matching fighter with screen

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
