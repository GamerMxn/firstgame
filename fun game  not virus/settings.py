class Settings():
    '''
    Store settings for Alien Invaders
    '''
    def __init__(self):
        self.screen_width = 0
        self.screen_height = 0
        self.bg_color = (0, 0, 30)

        self.ship_limit = 3
        self.player_acc = 0.06
        self.player_friction = -.02

        self.alien1_acc = 0.05
        self.alien1_friction = -.03
        self.alien1_points = 50

        self.alien2_acc = 0.08
        self.alien2_friction = -.03
        self.alien2_points = 500

        self.bullet_speed = 4.0
        self.bullet_width = 9.0
        self.bullet_height = 16.0
        self.bullet_limit = 3