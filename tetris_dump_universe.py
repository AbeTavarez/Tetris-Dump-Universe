import sys
import pygame
from settings import Settings
from fighter import Fighter


class TetrisDumpUniverse:
    """Main Class to manage game assests and behavior"""

    def __init__(self):
        """Inits game and create game resources"""
        # * inits background setting for pygame
        pygame.init()

        # * creates Surface display window, for drawing game
        # instance of Settings
        self.settings = Settings()

        # *  create screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Tetris Dump Universe")

        # * Fighter instance
        # Fighter requires one instance of TDU game so we pass self for the current intance of the TDU game class
        self.figther = Fighter(self)

    def run_game(self):
        """Start main loop for the game"""
        # while loop: manage Event loop and Screen updates
        while True:
            # Event Loop: Watch for keyboard and mouse events
            for event in pygame.event.get():  # returns list of events
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.figther.blitme()

            # Make the most recently drawn screen visible (updates loc of game elements)
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game
    tdu = TetrisDumpUniverse()
    tdu.run_game()
