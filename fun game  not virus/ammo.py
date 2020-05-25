import pygame

class Ammo:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.ammo3 = pygame.image.load('images/ammo3.png')
        self.ammo2 = pygame.image.load('images/ammo2.png')
        self.ammo1 = pygame.image.load('images/ammo1.png')
        self.ammo0 = pygame.image.load('images/ammo0.png')
        self.rect3 = self.ammo3.get_rect()
        self.rect2 = self.ammo2.get_rect()
        self.rect1 = self.ammo1.get_rect()
        self.rect0 = self.ammo0.get_rect()

    def blitme(self):
        self.rect3.x = self.ai_game.ship.x - 30
        self.rect3.y = self.ai_game.ship.y
        self.rect2.x = self.ai_game.ship.x - 30
        self.rect2.y = self.ai_game.ship.y
        self.rect1.x = self.ai_game.ship.x - 30
        self.rect1.y = self.ai_game.ship.y
        self.rect0.x = self.ai_game.ship.x - 30
        self.rect0.y = self.ai_game.ship.y

        if self.ai_game.cur_ammo == 3:
            self.screen.blit(self.ammo3, self.rect3)
        elif self.ai_game.cur_ammo == 2:
            self.screen.blit(self.ammo2, self.rect2)
        elif self.ai_game.cur_ammo == 1:
            self.screen.blit(self.ammo1, self.rect1)
        elif self.ai_game.cur_ammo == 0:
            self.screen.blit(self.ammo0, self.rect0)
        
