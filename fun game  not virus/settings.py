import pygame


class Settings():
    #Store settings for Alien Invaders

    def __init__(self, ai_game):
        #Game settings

        self.background_choices = ['background.png']
        self.fps_limit = 120
        self.wall_bounce = 5.0

        #Default player ship settings

        self.ship_limit = 6
        self.player_acc = 0.30
        self.player_friction = -0.05

        #Minion alien settings

        self.alien1_acc = 0.25
        self.alien1_friction = -0.08
        self.alien1_points = 50
        self.alien1_random_move_chance = 80
        self.alien1_random_move_duration = 40

        #Boss alien settings

        self.alien2_acc = 0.28
        self.alien2_friction = -0.08
        self.alien2_points = 500
        self.spawn_alien2 = 4
        self.alien2_random_move_chance = 80
        self.alien2_random_move_duration = 40

        #Player bullet settings

        self.bullet_speed = 16
        self.bullet_limit = 3