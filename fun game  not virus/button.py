import pygame.font


class Button:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/play.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def draw_button(self):
        self.screen.blit(self.image, self.rect)