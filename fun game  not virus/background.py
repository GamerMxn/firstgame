import pygame


class Background(pygame.sprite.Sprite):
    #Manage background image

    def __init__(self, image_file, location):
        #Initialize selected background image

        pygame.sprite.Sprite.__init__(self)
        self.background = pygame.image.load(f'images/{image_file}').convert_alpha()
        self.background_rect = self.background.get_rect()
        self.background_rect.left, self.background_rect.top = location