import sys
import pygame
from settings import Settings
from fighter import Fighter
from bullet import Bullet


class TetrisDumpUniverse:
    """Main Class to manage game assests and behavior"""

    def __init__(self):
        """Inits game and create game resources"""
        # * inits background setting for pygame
        pygame.init()

        # * creates Surface display window, for drawing game
        # instance of Settings
        self.settings = Settings()

        # *  ASSIGNS MAIN DISPLAY SURFACE
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # *  CREATE FULLSCREEN
        # self.screen = pygame.display.set_mode(
        #     (0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Tetris Dump Universe")

        # * FIGHTER INSTANCE
        # Fighter requires one instance of TDU game so we pass self for the current intance of the TDU game class
        self.fighter = Fighter(self)

        # * BULLETS INSTANCES
        self.bullets = pygame.sprite.Group()


# *********************** FUNCTIONS *********************************************

    def run_game(self):
        """Start MAIN LOOP for the game"""
        # while loop: manage Event loop and Screen updates
        while True:
            # Event Loop: Watch for keyboard and mouse events
            self._check_events()
            self.fighter.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """DETECTS REVELANT USER INPUT EVENTS"""
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
            self.fighter.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the fighter left
            self.fighter.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
            # shoots bullet
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.fighter.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.fighter.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        # first we check the elngth of bullets that are active
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet position
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Redraw the screen during each pass through the loop"""
        self.screen.fill(self.settings.bg_color)
        self.fighter.blitme()
        # bullets.sprite returns a list of all sprites in bullets
        for bullet in self.bullets.sprites():
            # calls draw_bullet() on bullet
            bullet.draw_bullet()
        # Make the most recently drawn screen visible (updates loc of game elements)
        pygame.display.flip()

# *********************** INIT ********************************************


if __name__ == '__main__':
    # * Make a game instance and run the game
    tdu = TetrisDumpUniverse()
    tdu.run_game()
