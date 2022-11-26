import arcade
import arcade.gui

import gui.menu_view
import gui.views.menu_view
from gui.screen_configuration import ScreenConfiguration


class Views:

    def __init__(self, screen_configuration: ScreenConfiguration):
        self.game_view = main_game.MainGameView(screen_configuration)
        self.menu_view = gui.views.menu_view.MenuView(screen_configuration, view_controller)



class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


class StartButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        pass

