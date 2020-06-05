import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    #Manage bullets fired from ship

    def __init__(self, ai_game):
        #Create a bullet from ship's current position

        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bullets = [pygame.image.load('images/bullet_1.png').convert_alpha(), pygame.image.load('images/bullet_2.png').convert_alpha(), pygame.image.load('images/bullet_3.png').convert_alpha(), pygame.image.load('images/bullet_4.png').convert_alpha()]
        self.rect = self.bullets[0].get_rect()
        self.rect.center = ai_game.ship.rect.center
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.bulletanime = 0
        self.dir = ""

    def bullet_angle(self):
        #Change bullet angle based on ship angle

        if self.ai_game.ship.bullet_dir == "Top": 
            self.dir = "Top"

        elif self.ai_game.ship.bullet_dir == "Bottom":
            for i in range(len(self.bullets)):
                self.bullets[i] = pygame.transform.rotate(self.bullets[i], 180)
            self.rect = self.bullets[0].get_rect()
            self.rect.center = self.ai_game.ship.rect.center
            self.dir = "Bottom"

        elif self.ai_game.ship.bullet_dir == "Right":
            for i in range(len(self.bullets)):
                self.bullets[i] = pygame.transform.rotate(self.bullets[i], -90)
            self.rect = self.bullets[0].get_rect()
            self.rect.center = self.ai_game.ship.rect.center
            self.dir = "Right"

        elif self.ai_game.ship.bullet_dir == "Left": 
            for i in range(len(self.bullets)):
                self.bullets[i] = pygame.transform.rotate(self.bullets[i], 90)
            self.rect = self.bullets[0].get_rect()
            self.rect.center = self.ai_game.ship.rect.center
            self.dir = "Left"

        elif self.ai_game.ship.bullet_dir == "Top Right":
            for i in range(len(self.bullets)):
                self.bullets[i] = pygame.transform.rotate(self.bullets[i], -45)
            self.rect = self.bullets[0].get_rect()
            self.rect.center = self.ai_game.ship.rect.center
            self.dir = "Top Right"

        elif self.ai_game.ship.bullet_dir == "Top Left":
            for i in range(len(self.bullets)):
                self.bullets[i] = pygame.transform.rotate(self.bullets[i], 45)
            self.rect = self.bullets[0].get_rect()
            self.rect.center = self.ai_game.ship.rect.center
            self.dir = "Top Left"

        elif self.ai_game.ship.bullet_dir == "Bottom Right":
            for i in range(len(self.bullets)):
                self.bullets[i] = pygame.transform.rotate(self.bullets[i], -135)
            self.rect = self.bullets[0].get_rect()
            self.rect.center = self.ai_game.ship.rect.center
            self.dir = "Bottom Right"

        elif self.ai_game.ship.bullet_dir == "Bottom Left":
            for i in range(len(self.bullets)):
                self.bullets[i] = pygame.transform.rotate(self.bullets[i], 135)
            self.rect = self.bullets[0].get_rect()
            self.rect.center = self.ai_game.ship.rect.center
            self.dir = "Bottom Left"

    def update(self):
        #Update bullet position based on its angle

        if self.dir == "Top":
            self.y -= self.settings.bullet_speed
            self.rect.y = self.y

        elif self.dir == "Bottom":
            self.y += self.settings.bullet_speed
            self.rect.y = self.y

        elif self.dir == "Right":
            self.x += self.settings.bullet_speed
            self.rect.x = self.x

        elif self.dir == "Left":
            self.x -= self.settings.bullet_speed
            self.rect.x = self.x

        elif self.dir == "Top Right":
            self.y -= self.settings.bullet_speed
            self.rect.y = self.y
            self.x += self.settings.bullet_speed
            self.rect.x = self.x

        elif self.dir == "Top Left":
            self.y -= self.settings.bullet_speed
            self.rect.y = self.y
            self.x -= self.settings.bullet_speed
            self.rect.x = self.x

        elif self.dir == "Bottom Right":
            self.y += self.settings.bullet_speed
            self.rect.y = self.y
            self.x += self.settings.bullet_speed
            self.rect.x = self.x

        elif self.dir == "Bottom Left":
            self.y += self.settings.bullet_speed
            self.rect.y = self.y
            self.x -= self.settings.bullet_speed
            self.rect.x = self.x

    def draw_bullet(self):
        #Draw the bullet on the screen

        if self.bulletanime >= 20:
            self.bulletanime = 0
        self.screen.blit(self.bullets[self.bulletanime//5], self.rect)
        self.bulletanime += 1
        