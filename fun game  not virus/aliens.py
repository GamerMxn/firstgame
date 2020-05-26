import pygame
import numpy as np
from pygame.sprite import Sprite
vec = pygame.math.Vector2


class Alien(Sprite):
    #Represents a single alien
    def __init__(self, ai_game):
        super().__init__()
        self.ai_game = ai_game
        self.settings = self.ai_game.settings
        self.screen = ai_game.screen
        self.type = ''

        self.alien1 = pygame.image.load('images/alien1.png')
        self.rect1 = self.alien1.get_rect()
        self.rand_dir1 = [self.settings.alien1_acc, -self.settings.alien1_acc]
        self.spawn_coord1 = [200, -200, 250, -250, 300, -300, 350, -350, 400, -400]
        self.rect1.centerx = self.ai_game.ship.rect.x + self.spawn_coord1[np.random.randint(10)]
        self.rect1.centery = self.ai_game.ship.rect.y + self.spawn_coord1[np.random.randint(10)]
        self.randmove1 = 0
        self.pos1 = (self.rect1.centerx, self.rect1.centery)
        self.vel1 = vec(0, 0)
        self.acc1 = vec(0, 0)

        self.alien2 = pygame.image.load('images/alien2.png')
        self.rect2 = self.alien2.get_rect()
        self.rand_dir2 = [self.settings.alien2_acc, -self.settings.alien2_acc]
        self.spawn_coord2 = [400, -400, 450, -450, 500, -500, 550, -550, 600, -600]
        self.rect2.centerx = self.ai_game.ship.rect.x + self.spawn_coord2[np.random.randint(10)]
        self.rect2.centery = self.ai_game.ship.rect.y + self.spawn_coord2[np.random.randint(10)]
        self.randmove2 = 0
        self.pos2 = (self.rect2.centerx, self.rect2.centery)
        self.vel2 = vec(0, 0)
        self.acc2 = vec(0, 0)

    def draw_alien(self):
        #Draw each alien
        if self.type == 1:
            self.screen.blit(self.alien1, self.rect1)
        elif self.type == 2:
            self.screen.blit(self.alien2, self.rect2)

    def _update_alien1_acc(self):
        self.acc1 = vec(0, 0)
        if np.random.randint(120) == 0 and self.randmove1 == 0:
            self.randmove1 = 50
            self.dir1 = np.random.randint(2)
        if self.randmove1 == 0:
            if self.rect1.centerx < self.ai_game.ship.rect.centerx:
                self.acc1.x = self.settings.alien1_acc
            elif self.rect1.centerx > self.ai_game.ship.rect.centerx:
                self.acc1.x = -self.settings.alien1_acc
            if self.rect1.centery < self.ai_game.ship.rect.centery:
                self.acc1.y = self.settings.alien1_acc
            elif self.rect1.centery > self.ai_game.ship.rect.centery:
                self.acc1.y = -self.settings.alien1_acc
        elif self.randmove1 != 0:
            self.randmove1 -= 1
            self.acc1.x += self.rand_dir1[self.dir1]
            self.acc1.y += self.rand_dir1[self.dir1]

    def _update_alien2_acc(self):
        self.acc2 = vec(0, 0)
        if np.random.randint(100) == 0 and self.randmove2 == 0:
            self.randmove2 = 30
            self.dir2 = np.random.randint(2)
        if self.randmove2 == 0:
            if self.rect2.centerx < self.ai_game.ship.rect.centerx:
                self.acc2.x = self.settings.alien2_acc
            elif self.rect2.centerx > self.ai_game.ship.rect.centerx:
                self.acc2.x = -self.settings.alien2_acc
            if self.rect2.centery < self.ai_game.ship.rect.centery:
                self.acc2.y = self.settings.alien2_acc
            elif self.rect2.centery > self.ai_game.ship.rect.centery:
                self.acc2.y = -self.settings.alien2_acc
        elif self.randmove2 != 0:
            self.randmove2 -= 1
            self.acc2.x = self.rand_dir2[self.dir2]
            self.acc2.y = self.rand_dir2[self.dir2]

    def _update_alien1_pos(self):
        self.acc1 += self.vel1 * self.settings.alien1_friction
        self.vel1 += self.acc1
        self.pos1 += self.vel1 + (0.5 * self.acc1)
        self.rect1.center = self.pos1

    def _update_alien2_pos(self):
        self.acc2 += self.vel2 * self.settings.alien2_friction
        self.vel2 += self.acc2
        self.pos2 += self.vel2 + (0.5 * self.acc2)
        self.rect2.center = self.pos2

    def update(self):
        if self.type == 1:
            self._update_alien1_acc()
            self._update_alien1_pos()
            
        elif self.type == 2:
            self._update_alien2_acc()
            self._update_alien2_pos()