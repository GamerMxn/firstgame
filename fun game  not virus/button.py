import pygame


class Button:
    #Buttons on start and end screen

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.play_buttons = [pygame.image.load('images/play_button_1.png').convert_alpha(), pygame.image.load('images/play_button_2.png').convert_alpha(), pygame.image.load('images/play_button_3.png').convert_alpha(), pygame.image.load('images/play_button_4.png').convert_alpha(), pygame.image.load('images/play_button_5.png').convert_alpha(), pygame.image.load('images/play_button_6.png').convert_alpha(), pygame.image.load('images/play_button_7.png').convert_alpha(), pygame.image.load('images/play_button_8.png').convert_alpha(), pygame.image.load('images/play_button_9.png').convert_alpha(), pygame.image.load('images/play_button_10.png').convert_alpha(), pygame.image.load('images/play_button_11.png').convert_alpha(), pygame.image.load('images/play_button_12.png').convert_alpha(), pygame.image.load('images/play_button_13.png').convert_alpha(), pygame.image.load('images/play_button_14.png').convert_alpha(), pygame.image.load('images/play_button_15.png').convert_alpha()]
        self.play_button_rect = self.play_buttons[0].get_rect()
        self.play_button_rect.center = self.screen_rect.center
        self.playbuttonanime = 0

    def draw_play_button(self):
        #Draw the play button

        if self.playbuttonanime >= 150:
            self.playbuttonanime = 0
        self.screen.blit(self.play_buttons[self.playbuttonanime//10], self.play_button_rect)
        self.playbuttonanime += 1
