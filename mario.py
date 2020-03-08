import pygame


class Mario:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/mario.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centery

    def blitme(self):
        """
        Desenha a espaçonave em sua posição atual.
        """
        self.screen.blit(self.image, self.rect)