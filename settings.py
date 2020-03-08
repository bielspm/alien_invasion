"""
Arquivo para configurações do jogo
"""


class Settings:
    """
    Armazena as configurações do jogo
    """
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (75, 0, 130)
        self.game_name = "Alien Invasion"
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60