import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """ Overall class to manage game assets and behaviour """

    def __init__(self):
        """ Initialise the game and create resources """
        pygame.init()
        self.settings = Settings()
        self._set_screen_mode()
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        # Sets of bullets and aliens
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.create_fleet()

    def _set_screen_mode(self):
        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _update_bullets(self):
        self.bullets.update()
        self._remove_old_bullets()
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Check for any bullets that have hit aliens
        # If so, get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # If no aliens left, destroy any remaining bullets and create a new fleet
        if not self.aliens:
            self.bullets.empty()
            self.create_fleet()

    def _update_aliens(self):
        """ Check if any alien in the fleet is at either edge """
        self._check_fleet_edges()
        """ Update the position of all the aliens in the fleet """
        self.aliens.update()

    def _remove_old_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_fleet_edges(self):
        """ Respond appropriately if any aliens have reached an edge """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        """ Drop the entire fleet down and change the fleet's direction """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        # Set the background colour
        self.screen.fill(self.settings.bg_color)
        """ Draw the ship on the screen """
        self.ship.blitme()
        """ Update images on the screen and flip (refresh?) to the new screen """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Draw the aliens on the screen
        self.aliens.draw(self.screen)

        # make the most recently drawn screen visible
        pygame.display.flip()

    def _check_events(self):
        # Respond to keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # Helper methods start with a single _
    # They are not instance methods i.e. similar to private class methods in java
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def create_fleet(self):
        """ Create a fleet of aliens """
        # Create one alien to find the number of aliens in a row
        # Spacing between each alien is equal to one alien width
        # so each alien effectively needs 2 x its width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_across = self.settings.screen_width - (2 * alien_width)
        number_aliens_across = available_space_across // (2 * alien_width)

        # Determine the number of rows of aliens we can fit before reaching the ship at the bottom
        ship_height = self.ship.rect.height
        available_space_down = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_down // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_across):
                # Create an alien and place it in the row
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + (2 * alien_width * alien_number)
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
        self.aliens.add(alien)


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
