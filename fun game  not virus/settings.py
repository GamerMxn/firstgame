class Settings():
    #Store settings for Alien Invaders

    def __init__(self):
        #Default player ship settings

        self.ship_limit = 4
        self.player_acc = 0.25
        self.player_friction = -.03

        #Minion alien settings

        self.alien1_acc = 0.15
        self.alien1_friction = -.03
        self.alien1_points = 50
        self.alien1_random_move_chance = 80
        self.alien1_random_move_duration = 30

        #Boss alien settings

        self.alien2_acc = 0.18
        self.alien2_friction = -.02
        self.alien2_points = 500
        self.spawn_alien2 = 4
        self.alien2_random_move_chance = 100
        self.alien2_random_move_duration = 20

        #Player bullet settings

        self.bullet_speed = 16.0
        self.bullet_width = 9.0
        self.bullet_height = 16.0
        self.bullet_limit = 3