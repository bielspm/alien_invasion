import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf

def run_game():
    """
    Inicializa o jogo e cria um objeto para a a tela
    """
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption(settings.game_name)

    ship = Ship(settings, screen)
    bullets = Group()

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(settings, screen, ship, bullets)      # Observa eventos de teclado e de mouse
        ship.update()
        bullets.update()
        gf.update_screen(settings, screen, ship, bullets)

run_game()