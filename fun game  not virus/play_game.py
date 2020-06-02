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
from scoreboard import Scoreboard
from background import Background
from powerups import PowerUp
from fps import Get_FPS



class AlienInvaders:
    #Manage game asssets and game behaviours

    def __init__(self):
        #Initialize the game and create game resources

        pygame.init()
        pygame.display.set_caption("Alien Invaders")
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)
        self.bg = Background('background_image.png', [0,0])
        self.screen_rect = self.screen.get_rect()
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullet = Bullet(self)
        self.ammo = Ammo(self)
        self.sb = Scoreboard(self)
        self.play_button = Button(self)
        self.fps = Get_FPS(self)
        self.bullets = pygame.sprite.Group()
        self.aliens1 = pygame.sprite.Group()
        self.aliens2 = pygame.sprite.Group()
        self.scores = []
        self.cur_ammo = self.settings.bullet_limit
        self.spawn_alien2_count = self.settings.spawn_alien2
        self.a1_kill_amount = 0

    def run_game(self):
        #Start the game

        while True:
            #Detect keyboard and mouse events
            self._check_events()
            self.fps.update_fps()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)
       
    def _check_events(self):
        #Respond to events and player inputs

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            if event.type == pygame.KEYUP:
                self._check_keyup(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.stats.game_active and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play(mouse_pos)
                elif self.stats.game_active and event.button == 1:
                    self._fire_bullet()

    def _check_keydown(self, event):
        #Moves player based on the key pressed

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
        #Stops player based on the key released

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

        if len(self.aliens1) + len(self.aliens2) == 0:
            self._create_aliens()
        for alien in self.aliens1.copy():
            alien.update()
        for alien in self.aliens2.copy():
            alien.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens1) or pygame.sprite.spritecollideany(self.ship, self.aliens2):
            self._ship_hit()

    def _update_bullets(self):
        #Update bullet positions and delete old bullets

        for bullet in self.bullets.copy():
            bullet.update()
            if bullet.rect.bottom <= 0 or bullet.rect.bottom >= self.screen_rect.bottom or bullet.rect.x <= 0 or bullet.rect.x >= self.screen_rect.right:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        #Check for bullet and alien collisions - remove bullet and alien and increase score

        aliens1 = len(self.aliens1.copy())
        aliens2 = len(self.aliens2.copy())
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens1, True, True)
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens2, True, True)
        
        if  aliens2 > len(self.aliens2):
            for i in range(aliens2 - len(self.aliens2)):
                self.stats.score += self.settings.alien2_points
                self._create_aliens()
                self._create_aliens()

        if  aliens1 > len(self.aliens1):
            for i in range(aliens1 - len(self.aliens1)):
                self.stats.score += self.settings.alien1_points
                self.a1_kill_amount += 1
                self._create_aliens()

    def _create_aliens(self):
        #Spawn boss alien after killing n minions

        if self.a1_kill_amount > self.spawn_alien2_count:
            self.spawn_alien2_count += 1
            self.a1_kill_amount = 0
            self._spawn_alien2()
        else:
            self._spawn_alien1()

    def _spawn_alien1(self):
        #Spawn minion alien

        alien1 = Alien(self)
        alien1.type = 1
        alien1.rect = alien1.rect1
        self.aliens1.add(alien1)
        
    def _spawn_alien2(self):
        #Spawn boss alien

        alien2 = Alien(self)
        alien2.type = 2
        alien2.rect = alien2.rect2
        self.aliens2.add(alien2)

    def _inti_scores(self):
        #Initialize scoreboard numbers

        for i in range(1, 11):
            score = Scoreboard(self)
            score.place = i
            self.scores.append(score)

    def _ship_hit(self):
        #Respond if ship is hit by alien
        
        if self.stats.ships_left - 1 != 0:
            self.stats.ships_left -= 1
            self.spawn_alien2_count = self.settings.spawn_alien2
            self.a1_kill_amount = 0
            self.aliens1.empty()
            self.aliens2.empty()
            self.bullets.empty()
            self.cur_ammo = self.settings.bullet_limit
            self.ship.center_ship()
            sleep(.5)
        else:
            self.stats.game_active = False
            sleep(1)
            pygame.mouse.set_visible(True)

    def _check_play(self, mouse_pos):
        #Ending and start screen buttons

        if self.play_button.play_button_rect.collidepoint(mouse_pos):
            self.stats.reset_stats()
            self.spawn_alien2_count = self.settings.spawn_alien2
            self.a1_kill_amount = 0
            self.aliens1.empty()
            self.aliens2.empty()
            self.bullets.empty()
            self.scores.clear()
            self._spawn_alien1()
            self._inti_scores()
            self.cur_ammo = self.settings.bullet_limit
            self.ship.center_ship()
            self.stats.game_active = True
            pygame.mouse.set_visible(False)

    def _get_fps(self):
        if self.cur_fps != int(clock.get_fps()):
            self.fps = font.render(str(int(clock.get_fps())), True, pg.Color('white'))
        self.cur_fps = int(clock.get_fps())

    def _update_screen(self):
        #Update objects on the screen

        self.screen.blit(self.bg.image, self.bg.rect)
        self.fps.blitme()
        self.sb.show_score()

        for score in self.scores.copy():
            score._check_score()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for alien in self.aliens1.sprites():
            alien.draw_alien()
        for alien in self.aliens2.sprites():
            alien.draw_alien()
        
        self.ship.blitme()

        if not self.stats.game_active:
            self.play_button.draw_play_button()

        pygame.display.flip()


if __name__ == "__main__":
    #Make a game instance and run it from the main module

    ai = AlienInvaders()
    ai.run_game()
    