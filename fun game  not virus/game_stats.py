class GameStats:
    #Tracks points

    def __init__(self, ai_game):
        #Initialize points and ship lives

        self.settings = ai_game.settings
        self.score = 0
        self.reset_stats()
        self.game_active = False
        self.ships_left = self.settings.ship_limit

    def reset_stats(self):
        #Reset lives and score

        self.ships_left = self.settings.ship_limit
        self.score = 0