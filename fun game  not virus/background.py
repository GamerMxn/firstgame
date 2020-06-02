import pygame


class Background(pygame.sprite.Sprite):
    #Initialize background image
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/background.png').convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location