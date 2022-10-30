from main_game import GameView
from menu_window import MenuView
from screen_configuration import ScreenConfiguration


class Views:

    def __init__(self, screen_configuration: ScreenConfiguration):
        self.game_view = GameView(screen_configuration)
        self.menu_view = MenuView(screen_configuration)

