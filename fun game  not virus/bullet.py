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
        self.bullet1 = pygame.image.load('images/bullet1.png')
        self.bullet1_rotate = pygame.image.load('images/bullet1.png')
        self.rect = self.bullet1.get_rect()
        self.rect.center = ai_game.ship.rect.center
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.dir = ""

    def bullet_angle(self):
        #Change bullet angle based on ship angle

        if self.ai_game.ship.bullet_dir == "Top": 
            self.bullet1 = pygame.transform.rotate(self.bullet1_rotate, 0)
            self.dir = "Top"
        elif self.ai_game.ship.bullet_dir == "Bottom":
            self.bullet1 = pygame.transform.rotate(self.bullet1_rotate, 180)
            self.dir = "Bottom"
        elif self.ai_game.ship.bullet_dir == "Right":
            self.bullet1 = pygame.transform.rotate(self.bullet1_rotate, -90)
            self.dir = "Right"
        elif self.ai_game.ship.bullet_dir == "Left": 
            self.bullet1 = pygame.transform.rotate(self.bullet1_rotate, 90)
            self.dir = "Left"
        elif self.ai_game.ship.bullet_dir == "Top Right":
            self.bullet1 = pygame.transform.rotate(self.bullet1_rotate, -45)
            self.dir = "Top Right"
        elif self.ai_game.ship.bullet_dir == "Top Left":
            self.bullet1 = pygame.transform.rotate(self.bullet1_rotate, 45)
            self.dir = "Top Left"
        elif self.ai_game.ship.bullet_dir == "Bottom Right":
            self.bullet1 = pygame.transform.rotate(self.bullet1_rotate, -135)
            self.dir = "Bottom Right"
        elif self.ai_game.ship.bullet_dir == "Bottom Left":
            self.bullet1 = pygame.transform.rotate(self.bullet1_rotate, 135)
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
        
        self.screen.blit(self.bullet1, self.rect)
        