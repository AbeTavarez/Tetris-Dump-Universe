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


# *********************** FUNCTION *********************************************

    def run_game(self):
        """Start main loop for the game"""
        # while loop: manage Event loop and Screen updates
        while True:
            # Event Loop: Watch for keyboard and mouse events
            self._check_events()
            self.figther.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():  # returns list of events
            if event.type == pygame.QUIT:
                sys.exit()
            # * On KEYDOWN = True
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            # * On KEYUP = False
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move the fighter to the right
            self.figther.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the fighter left
            self.figther.moving_left = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.figther.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.figther.moving_left = False

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.figther.blitme()
        # Make the most recently drawn screen visible (updates loc of game elements)
        pygame.display.flip()

# *********************** INIT ********************************************


if __name__ == '__main__':
    # Make a game instance and run the game
    tdu = TetrisDumpUniverse()
    tdu.run_game()
