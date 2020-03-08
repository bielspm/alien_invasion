import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    Uma classe que administra projéteis disparados pela espaçonave
    """

    def __init__(self, settings, screen, ship):
        """
        Cria um objeto para o projétil na posição atual da espaçonave
        """
        super(Bullet, self).__init__()
        self.screen = screen

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """
        Move o projeto para cima na tela
        """
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Desenha a bala na tela
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
