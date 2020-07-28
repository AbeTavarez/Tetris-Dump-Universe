import pygame


class Fighter:
    def __init__(self, tdu_game):
        """Initialize the ship and set its starting position"""
        # tdu_game is an instance of the Tetris Dump Universe, giving Fighter access to all the game resources from tdu
        # assign screen to an attribute of Fighter for easy access
        self.screen = tdu_game.screen

        # setting attribute to be use in update() method
        # so we can update the fighter position by a fraction of a pixel
        self.settings = tdu_game.settings

        # gets the screen rect att and assign it to self, to place the fighter on desire location
        self.screen_rect = tdu_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/fighter.bmp')  # return surface
        # assign new image to out fighter
        self.rect = self.image.get_rect()

        # Start each new ship at bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom  # matching fighter with screen

        # Store a decimal value for the fighter's horizontal position
        self.x = float(self.rect.x)

        # * Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        # Update the shop's x value not the rect
        # we check if the value of location is less than the right size of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.fighter_speed
        # we check if the value of location is less than the left size of the screen
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.fighter_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the fighter to the screen"""
        self.screen.blit(self.image, self.rect)
