import pygame

class Ammo:
    #Control ammo sprites

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.ammo3 = pygame.image.load('images/ammo3.png')
        self.ammo2 = pygame.image.load('images/ammo2.png')
        self.ammo1 = pygame.image.load('images/ammo1.png')
        self.ammo0 = pygame.image.load('images/ammo0.png')
        self.rect = self.ammo0.get_rect()

    def blitme(self):
        #Draw ammo sprite based on current ammo

        if self.ai_game.cur_ammo == 3:
            self.rect.centerx = self.ai_game.ship.rect.centerx - 30
            self.rect.centery = self.ai_game.ship.rect.centery
            self.screen.blit(self.ammo3, self.rect)

        elif self.ai_game.cur_ammo == 2:
            self.rect.centerx = self.ai_game.ship.rect.centerx - 30
            self.rect.centery = self.ai_game.ship.rect.centery
            self.screen.blit(self.ammo2, self.rect)

        elif self.ai_game.cur_ammo == 1:
            self.rect.centerx = self.ai_game.ship.rect.centerx - 30
            self.rect.centery = self.ai_game.ship.rect.centery
            self.screen.blit(self.ammo1, self.rect)
            
        elif self.ai_game.cur_ammo == 0:
            self.rect.centerx = self.ai_game.ship.rect.centerx - 30
            self.rect.centery = self.ai_game.ship.rect.centery
            self.screen.blit(self.ammo0, self.rect)
        
