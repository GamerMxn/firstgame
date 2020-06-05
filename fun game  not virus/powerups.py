import pygame


class PowerUp:
    #Creates powerups for the player

    def __init__(self, ai_game):
        #Initialize player powerup

        self.ai_game = ai_game
        self.screen = self.ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.shield_image = 0 #pygame.image.load('images/.png').convert_alpha()
        self.laser_image = 0 #pygame.image.load('images/.png').convert_alpha()
        self.engine_image = 0 #pygame.image.load('images/.png').convert_alpha()
        self.extra_ammo_image = 0 #pygame.image.load('images/.png').convert_alpha()
        self.extra_bullet_image = 0 #pygame.image.load('images/.png').convert_alpha()
        self.slow_time_image = 0 #pygame.image.load('images/.png').convert_alpha()

    def shield(self):
        pass

    def laser(self):
        pass

    def engine(self):
        pass

    def extra_ammo(self):
        pass

    def extra_bullet(self):
        pass

    def slow_time(self):
        pass

