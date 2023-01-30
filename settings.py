PALE_LILAC = (197, 202, 233)
LIGHT_BLUE = (187, 222, 251)
BLACK = (0, 0, 0)
LIGHT_GREY = (227, 227, 227)
DARK_GRAY = (60, 60, 60)
class Settings:
    """ A class to store all the settings for Alien Invasion """

    def __init__(self):
        """ Initialise the game's settings """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # Let's have a default for fullscreen mode
        self.fullscreen = False
        self.bg_color = LIGHT_GREY
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = DARK_GRAY
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed = 0.5
        self.alien_drop_speed = 5.0
        # fleet_direction 1 means right, fleet_direction -1 means left
        self.fleet_direction = 1


