class GameStats:
    """ Track statistics for the Alien Invasion """

    def __init__(self, ai_game):
        """ Initialise statistics """
        self.score = None
        self.ships_remaining = None
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """ Init statistics that change during the game """
        self.ships_remaining = self.settings.ship_limit
        self.score = 0


