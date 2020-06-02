import pygame


class Scoreboard():
    #Game scoreboard

    def __init__(self, ai_game):
        #Initialize digits 0-9

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.scoreboard = pygame.image.load('images/scoreboard.png')
        self.sb_rect = self.scoreboard.get_rect()
        self.sb_rect.top = self.screen_rect.top + 10
        self.sb_rect.right = self.screen_rect.right - 10
        self.score0 = pygame.image.load('images/score0.png')
        self.score0_rect = self.score0.get_rect()
        self.score0_rect.top = self.screen_rect.top + 19
        self.score1 = pygame.image.load('images/score1.png')
        self.score1_rect = self.score1.get_rect()
        self.score1_rect.top = self.screen_rect.top + 19
        self.score2 = pygame.image.load('images/score2.png')
        self.score2_rect = self.score2.get_rect()
        self.score2_rect.top = self.screen_rect.top + 19
        self.score3 = pygame.image.load('images/score3.png')
        self.score3_rect = self.score3.get_rect()
        self.score3_rect.top = self.screen_rect.top + 19
        self.score4 = pygame.image.load('images/score4.png')
        self.score4_rect = self.score4.get_rect()
        self.score4_rect.top = self.screen_rect.top + 19
        self.score5 = pygame.image.load('images/score5.png')
        self.score5_rect = self.score5.get_rect()
        self.score5_rect.top = self.screen_rect.top + 19
        self.score6 = pygame.image.load('images/score6.png')
        self.score6_rect = self.score6.get_rect()
        self.score6_rect.top = self.screen_rect.top + 19
        self.score7 = pygame.image.load('images/score7.png')
        self.score7_rect = self.score7.get_rect()
        self.score7_rect.top = self.screen_rect.top + 19
        self.score8 = pygame.image.load('images/score8.png')
        self.score8_rect = self.score8.get_rect()
        self.score8_rect.top = self.screen_rect.top + 19
        self.score9 = pygame.image.load('images/score9.png')
        self.score9_rect = self.score9.get_rect()
        self.score9_rect.top = self.screen_rect.top + 19
        self.score_rect_list = [self.score0_rect, self.score1_rect, self.score2_rect, self.score3_rect, self.score4_rect, self.score5_rect, self.score6_rect, self.score7_rect, self.score8_rect, self.score9_rect]
        self.score_list = [self.score0, self.score1, self.score2, self.score3, self.score4, self.score5, self.score6, self.score7, self.score8, self.score9]
        self.place = 0

    def _check_score(self):
        #Update digit shown in each place based on score

        if self.place == 1:
            num = self.stats.score % 10
            self.score_rect_list[num].right = self.screen_rect.right - 17
            self.screen.blit(self.score_list[num], self.score_rect_list[num])

        elif self.place == 2:
            num = (self.stats.score // 10) % 10
            self.score_rect_list[num].right = self.screen_rect.right - 56
            self.screen.blit(self.score_list[num], self.score_rect_list[num])

        elif self.place == 3:
            num = (self.stats.score // 100) % 10
            self.score_rect_list[num].right = self.screen_rect.right - 95
            self.screen.blit(self.score_list[num], self.score_rect_list[num])

        elif self.place == 4:
            num = (self.stats.score // 1_000) % 10
            self.score_rect_list[num].right = self.screen_rect.right - 134
            self.screen.blit(self.score_list[num], self.score_rect_list[num])

        elif self.place == 5:
            num = (self.stats.score // 10_000) % 10
            self.score_rect_list[num].right = self.screen_rect.right - 173
            self.screen.blit(self.score_list[num], self.score_rect_list[num])

        elif self.place == 6:
            num = (self.stats.score // 100_000) % 10
            self.score_rect_list[num].right = self.screen_rect.right - 212
            self.screen.blit(self.score_list[num], self.score_rect_list[num])

        elif self.place == 7:
            num = (self.stats.score // 1_000_000) % 10
            self.score_rect_list[num].right = self.screen_rect.right - 251
            self.screen.blit(self.score_list[num], self.score_rect_list[num])

        elif self.place == 8:
            num = (self.stats.score // 10_000_000) % 10
            self.score_rect_list[num].right = self.screen_rect.right - 290
            self.screen.blit(self.score_list[num], self.score_rect_list[num])

        elif self.place == 9:
            num = (self.stats.score // 100_000_000) % 10
            self.score_rect_list[num].right = self.screen_rect.right - 329
            self.screen.blit(self.score_list[num], self.score_rect_list[num])

        elif self.place == 10:
            num = (self.stats.score // 1_000_000_000) % 10
            self.score_rect_list[num].right = self.screen_rect.right - 368
            self.screen.blit(self.score_list[num], self.score_rect_list[num])


    def show_score(self):
        #Draw score on screen

        self.screen.blit(self.scoreboard, self.sb_rect)
        


