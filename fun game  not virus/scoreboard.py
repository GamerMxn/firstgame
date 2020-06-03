import pygame
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    #Game scoreboard

    def __init__(self, ai_game):
        #Initialize digits 0-9

        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.scoreboard = pygame.image.load('images/scoreboard.png').convert_alpha()
        self.sb_rect = self.scoreboard.get_rect()
        self.sb_rect.top = self.screen_rect.top + 10
        self.sb_rect.right = self.screen_rect.right - 10
        self.font = pygame.font.SysFont('malgungothicsemilight', 32, True, False)
        self.points = self.font.render(f'{self.ai_game.stats.score:010d}', True, pygame.Color('black')).convert_alpha()
        self.points_rect = self.points.get_rect()
        self.points_rect.top = self.sb_rect.top - 2
        self.points_rect.left = self.sb_rect.left + 16
        self.cur_points = self.ai_game.stats.score
        self.cur_lives = 0
        self.ships_left()

    def update(self):
        #Update the scoreboard

        if self.cur_points != self.ai_game.stats.score:
            self.points = self.font.render(f'{self.ai_game.stats.score:010d}', True, pygame.Color('black')).convert_alpha()
        self.cur_points = self.ai_game.stats.score

    def ships_left(self):
        #Manages ship lives

        if self.cur_lives != self.stats.ships_left:
            self.ship_lives = Group()
            for i in range(self.stats.ships_left - 1):
                ship = Ship(self.ai_game)
                ship.rect.right = self.sb_rect.left - 16 - (48 * i)
                ship.rect.centery = self.sb_rect.centery
                self.ship_lives.add(ship)
        self.cur_lives = self.stats.ships_left

    def show_score(self):
        #Draw score on screen

        self.screen.blit(self.scoreboard, self.sb_rect)
        self.screen.blit(self.points, self.points_rect)
        self.ship_lives.draw(self.screen)
