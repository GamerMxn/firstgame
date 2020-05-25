import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from ammo import Ammo
from aliens import Alien
from time import sleep
from game_stats import GameStats
from button import Button

class AlienInvaders:
    #Manage game asssets and game behaviours

    def __init__(self):
        #Initialize the game and create game resources
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)
        self.stats = GameStats(self)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invaders")
        self.ship = Ship(self)
        self.bullet = Bullet(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.ammo = Ammo(self)
        self.cur_ammo = self.settings.bullet_limit
        self.a1_kill_amount = 0
        self.play_button = Button(self)
        
    def run_game(self):
        #Start the game
        while True:
            #Detect keyboard and mouse events
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            
    def _check_events(self):
        #Respond to events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            if event.type == pygame.KEYUP:
                self._check_keyup(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.stats.game_active:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play(mouse_pos)
                elif event.button == 1:
                    self._fire_bullet()

    def _check_keydown(self, event):
        if event.key == pygame.K_r or event.key == pygame.K_SPACE:
            self.cur_ammo = self.settings.bullet_limit
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            self.ship.moving_down = True

    def _check_keyup(self, event):
        if event.key == pygame.K_ESCAPE:
                    sys.exit()
        elif event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False
    
    def _fire_bullet(self):
        #Create a new bullet
        if self.cur_ammo > 0:
            self.cur_ammo -= 1
            new_bullet = Bullet(self)
            new_bullet.bullet_angle()
            self.bullets.add(new_bullet)

    def _update_aliens(self):
        #Update alien positions
        self._create_aliens()
        for alien in self.aliens.copy():
            alien.update()
        
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _update_bullets(self):
        #Update bullet positions and delete old bullets
        for bullet in self.bullets.copy():
            bullet.update()
            if bullet.rect.bottom <= 0 or bullet.rect.bottom >= self.settings.screen_height or bullet.rect.x <= 0 or bullet.rect.x >= self.settings.screen_width:
                self.bullets.remove(bullet)
        alien_n = len(self.aliens.copy())
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if len(self.aliens) < alien_n:
            self.a1_kill_amount += 1
            self._spawn_alien1()
            self._spawn_alien1()

    def _create_aliens(self):
        if self.a1_kill_amount == 5:
            self._spawn_alien2()
        if not len(self.aliens):
            self._spawn_alien1()

    def _spawn_alien1(self):
        alien = Alien(self)
        alien.type = 1
        alien.rect = alien.rect1
        self.aliens.add(alien)
        
    def _spawn_alien2(self):
        self.a1_kill_amount = 0
        alien = Alien(self)
        alien.type = 2
        alien.rect = alien.rect2
        self.aliens.add(alien)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for alien in self.aliens.sprites():
            alien.draw_alien()
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _ship_hit(self):
        #Respond if ship is hit by alien
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._spawn_alien1()
            self.cur_ammo = 3
            self.ship.center_ship()
            sleep(.5)
        else:
            self.stats.game_active = False

    def _check_play(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True
            self.stats.reset_stats()
            self.cur_ammo = 3
            self.ship.center_ship()
            self.aliens.empty()
            self.bullets.empty()


if __name__ == "__main__":
    #Make a game instance and run it
    ai = AlienInvaders()
    ai.run_game()