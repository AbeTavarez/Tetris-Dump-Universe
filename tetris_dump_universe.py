import sys
import pygame


class TetrisDumpUniverse:
    """Main Class to manage game assests and behavior"""

    def __init__(self):
        """Inits game and create game resources"""
        # inits background setting for pygame
        pygame.init()
        # * creates Surface display window, for drawing game
        # self.screen makes the Surface available in all methods of the class
        self.screen = pygame.display.set_mode(
            (1200, 800))  # dimensions of Surface

        pygame.display.set_caption("Tetris Dump Universe")

    def run_game(self):
        """Start main loop for the game"""
        # while loop: manage Event loop and Screen updates
        while True:
            # Event Loop: Watch for keyboard and mouse events
            for event in pygame.event.get():  # returns list of events
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible (updates loc of game elements)
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game
    tdu = TetrisDumpUniverse()
    tdu.run_game()
