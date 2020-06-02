import pygame


class Button:
    #Buttons on start and end screen

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.play_button = pygame.image.load('images/play.png')
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.center = self.screen_rect.center

    def draw_play_button(self):
        #Draw the play button

        self.screen.blit(self.play_button, self.play_button_rect)