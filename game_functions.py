import sys
import pygame

def check_keydown_events(event, ship):
    """
    Responde a pressionamentos de tecla
    """
    if event.key == pygame.K_RIGHT:
        ship.moviment_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """
    Responde a solturas de tecla
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """
    Responde a eventos de pressionamento de teclas e mouse
    """
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(settings, screen, ship):
    """
    Atualiza as imagens na tela e alterna para a nova tela
    """
    screen.fill(settings.bg_color)   # Redesenha a tela a cada laço
    ship.blitme()                       # Desenha a nave
    pygame.display.flip()               # Deixa a tela mais recente visivel