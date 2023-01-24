import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ A class to manage bullets fired from the ship.  A bullet is a simple grey rectangle that we create
     using pygame rather than using an image.  Inheriting from Sprite will allow us to group elements and act on
     the group """

    def __init__(self, ai_game):
        """ Create a bullet object at the ship's current position """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) i.e. top left corner, and then set the correct position """
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's y position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """ Move the bullet up the screen """
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet to the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)


