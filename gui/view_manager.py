import arcade

from gui.screen_configuration import ScreenConfiguration
from gui.views.difficulty_view import DifficultyView
from gui.views.lose_view import LoseView
from gui.views.main_game_view import MainGameView
from gui.views.menu_view import MenuView
from gui.views.rules_view import RulesView
from gui.views.win_view import WinView


class ViewManager(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(ViewManager, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.view = None
        self.config = ScreenConfiguration()
        self.__rules_view = RulesView(self.config)

    def show_game_view(self, difficulty):
        arcade.get_window().show_view(MainGameView(self.config, difficulty))

    def show_rules_view(self):
        arcade.get_window().show_view(self.__rules_view)

    def show_difficulty_view(self):
        arcade.get_window().show_view(DifficultyView(self.config))

    def show_menu_view(self):
        arcade.get_window().show_view(MenuView(self.config))

    def show_win_view(self):
        arcade.get_window().show_view(WinView(self.config))

    def show_lose_view(self):
        arcade.get_window().show_view(LoseView(self.config))


