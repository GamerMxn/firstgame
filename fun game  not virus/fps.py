import pygame


class Get_FPS:
    def __init__(self, ai_game):
        #Manage FPS counter

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont('malgungothicsemilight', 32)
        self.fps = self.font.render(str(int(self.ai_game.clock.get_fps())), True, pygame.Color('white'))
        self.cur_fps = int(self.ai_game.clock.get_fps())
        self.fps_rect = self.fps.get_rect()
        self.fps_rect.top = self.screen_rect.top + 5
        self.fps_rect.left = self.screen_rect.left + 10

    def update_fps(self):
        #Updates FPS counter

        if self.cur_fps != int(self.ai_game.clock.get_fps()):
            self.fps = self.font.render(str(int(self.ai_game.clock.get_fps())), True, pygame.Color('white'))
        self.cur_fps = int(self.ai_game.clock.get_fps())

    def blitme(self):
        #Draws FPS counter

        self.screen.blit(self.fps, self.fps_rect)

    