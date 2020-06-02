import pygame
vec = pygame.math.Vector2


class Ship:
    #Manage main player ship

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.settings = self.ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.png').convert_alpha()
        self.image_rotate = pygame.image.load('images/ship.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.settings = ai_game.settings
        self.angle = 0
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.pos = (self.screen_rect.centerx, self.screen_rect.centery)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.bullet_dir = "Top"

    def _update_angle(self):
        #Update ship angle based on keys pressed

        if self.moving_right and not self.moving_left: 
            if self.moving_up and not self.moving_down:
                self.image = pygame.transform.rotate(self.image_rotate, -45)
                self.bullet_dir = "Top Right"
            elif self.moving_down and not self.moving_up:
                self.image = pygame.transform.rotate(self.image_rotate, -135)
                self.bullet_dir = "Bottom Right"
            else:
                self.image = pygame.transform.rotate(self.image_rotate, -90)
                self.bullet_dir = "Right"

        elif self.moving_left and not self.moving_right: 
            if self.moving_up and not self.moving_down:
                self.image = pygame.transform.rotate(self.image_rotate, 45)
                self.bullet_dir = "Top Left"
            elif self.moving_down and not self.moving_up:
                self.image = pygame.transform.rotate(self.image_rotate, 135)
                self.bullet_dir = "Bottom Left"
            else:
                self.image = pygame.transform.rotate(self.image_rotate, 90)
                self.bullet_dir = "Left"

        elif self.moving_up and not self.moving_down:
            if self.moving_right and not self.moving_left:
                self.image = pygame.transform.rotate(self.image_rotate, -45)
                self.bullet_dir = "Top Right"
            elif self.moving_left and not self.moving_right:
                self.image = pygame.transform.rotate(self.image_rotate, 45)
                self.bullet_dir = "Top Left"
            else:
                self.image = pygame.transform.rotate(self.image_rotate, 0)
                self.bullet_dir = "Top"

        elif self.moving_down and not self.moving_up: 
            if self.moving_right and not self.moving_left:
                self.image = pygame.transform.rotate(self.image_rotate, -135)
                self.bullet_dir = "Bottom Right"
            elif self.moving_left and not self.moving_right:
                self.image = pygame.transform.rotate(self.image_rotate, 135)
                self.bullet_dir = "Bottom Left"
            else:
                self.image = pygame.transform.rotate(self.image_rotate, 180)
                self.bullet_dir = "Bottom"

    def update(self):
        #Update ships location based on key flags

        self.acc = vec(0, 0)
        self._update_angle()
        if self.moving_right and not self.moving_left and self.rect.right < self.screen_rect.right - 20:
            self.acc.x = self.settings.player_acc
        if self.moving_left and not self.moving_right and self.rect.left > 20:
            self.acc.x = -self.settings.player_acc
        if self.moving_up and not self.moving_down and self.rect.top > 20:
            self.acc.y = -self.settings.player_acc
        if self.moving_down and not self.moving_up and self.rect.bottom < self.screen_rect.bottom - 20:
            self.acc.y = self.settings.player_acc

        self.acc += self.vel * self.settings.player_friction
        self.vel += self.acc
        self.pos += self.vel + (0.5 * self.acc)
        self.rect.center = self.pos

        #Check for screen boundaries

        if self.pos.x < self.screen_rect.left + 20:
            self.pos.x = self.screen_rect.left + 20
        if self.pos.x > self.screen_rect.right - 20:
            self.pos.x = self.screen_rect.right - 20
        if self.pos.y < self.screen_rect.top + 20:
            self.pos.y = self.screen_rect.top + 20
        if self.pos.y > self.screen_rect.bottom - 20:
            self.pos.y = self.screen_rect.bottom - 20

    def center_ship(self):
        #Re-centers ship after death / game start

        self.angle = 0
        self.bullet_dir = "Top"
        self.image = pygame.transform.rotate(self.image_rotate, 0)
        self.pos = (self.screen_rect.centerx, self.screen_rect.centery)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def blitme(self):
        #Draws shop on screen
        
        self.screen.blit(self.image, self.rect)
        self.ai_game.ammo.blitme()