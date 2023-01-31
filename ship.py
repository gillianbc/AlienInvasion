import pygame
class Ship:
    """ A class to manage the ship """

    def __init__(self, ai_game):
        """ Initialise the ship and set its starting position """
        # Not sure why we're making copies of ai_game's properties within a ship
        # rather than just accessing them from ship.ai_game as and when...
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ship's x value based on the movement flag and the speed """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update the rect object of the ship based on its x value
        self.rect.x = self.x

    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)

    def centre_ship(self):
        """ Centre the ship on the screen """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
