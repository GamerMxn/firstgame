import pygame
import numpy as np
from pygame.sprite import Sprite

class Alien(Sprite):
    #Represents a single alien
    def __init__(self, ai_game):
        super().__init__()
        self.ai_game = ai_game
        self.settings = self.ai_game.settings
        self.spawn_coord1 = [200, -200, 250, -250, 300, -300, 350, -350, 400, -400]
        self.spawn_coord2 = [400, -400, 450, -450, 500, -500, 550, -550, 600, -600]
        self.screen = ai_game.screen
        self.alien1 = pygame.image.load('images/alien1.png')
        self.alien2 = pygame.image.load('images/alien2.png')
        self.rect1 = self.alien1.get_rect()
        self.rect2 = self.alien2.get_rect()
        self.rand_dir1 = [self.settings.alien1_speed, -self.settings.alien1_speed]
        self.rand_dir2 = [self.settings.alien2_speed, -self.settings.alien2_speed]
        self.rect1.x = self.ai_game.ship.rect.x + self.spawn_coord1[np.random.randint(10)]
        self.rect1.y = self.ai_game.ship.rect.y + self.spawn_coord1[np.random.randint(10)]
        self.rect2.x = self.ai_game.ship.rect.x + self.spawn_coord2[np.random.randint(10)]
        self.rect2.y = self.ai_game.ship.rect.y + self.spawn_coord2[np.random.randint(10)]
        self.randmove1 = 0
        self.randmove2 = 0
        self.type = ''
        self.rect = ''

    def draw_alien(self):
        #Draw each alien
        if self.type == 1:
            self.screen.blit(self.alien1, self.rect1)
        elif self.type == 2:
            self.screen.blit(self.alien2, self.rect2)

    def update(self):
        if self.type == 1:
            if np.random.randint(120) == 0 and self.randmove1 == 0:
                self.randmove1 = 50
                self.dir1 = np.random.randint(2)
            if self.randmove1 == 0:
                if self.rect1.x < self.ai_game.ship.rect.x:
                    self.rect1.x += self.settings.alien1_speed
                elif self.rect1.x > self.ai_game.ship.rect.x:
                    self.rect1.x -= self.settings.alien1_speed
                if self.rect1.y < self.ai_game.ship.rect.y:
                    self.rect1.y += self.settings.alien1_speed
                elif self.rect1.y > self.ai_game.ship.rect.y:
                    self.rect1.y -= self.settings.alien1_speed
            elif self.randmove1 != 0:
                self.randmove1 -= 1
                self.rect1.x += self.rand_dir1[self.dir1]
                self.rect1.y += self.rand_dir1[self.dir1]
            
        elif self.type == 2:
            if np.random.randint(100) == 0 and self.randmove2 == 0:
                self.randmove2 = 30
                self.dir2 = np.random.randint(2)
            if self.randmove2 == 0:
                if self.rect2.x < self.ai_game.ship.rect.x:
                    self.rect2.x += self.settings.alien2_speed
                elif self.rect2.x > self.ai_game.ship.rect.x:
                    self.rect2.x -= self.settings.alien2_speed
                if self.rect2.y < self.ai_game.ship.rect.y:
                    self.rect2.y += self.settings.alien2_speed
                elif self.rect2.y > self.ai_game.ship.rect.y:
                    self.rect2.y -= self.settings.alien2_speed
            elif self.randmove2 != 0:
                self.randmove2 -= 1
                self.rect2.x += self.rand_dir2[self.dir2]
                self.rect2.y += self.rand_dir2[self.dir2]