class Settings():
    '''
    Store settings for Alien Invaders
    '''
    def __init__(self):
        self.screen_width = 0
        self.screen_height = 0
        self.bg_color = (0, 0, 30)
        self.ship_speed = 2
        self.ship_limit = 3
        self.alien1_speed = 1
        self.alien2_speed = 2

        self.bullet_speed = 4.0
        self.bullet_width = 9.0
        self.bullet_height = 16.0
        self.bullet_limit = 3