PALE_LILAC = (197, 202, 233)
LIGHT_BLUE = (187, 222, 251)
BLACK = (0, 0, 0)

class Settings:
    """ A class to store all the settings for Alien Invasion """

    def __init__(self):
        """ Initialise the game's settings """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # Let's have a default for fullscreen mode
        self.fullscreen = False
        self.bg_color = BLACK
        self.ship_speed = 1.5

