import arcade
import arcade.gui

from gui.screen_configuration import ScreenConfiguration


class Views:

    def __init__(self, screen_configuration: ScreenConfiguration):
        self.game_view = main_game.GameView(screen_configuration)
        self.menu_view = menu_window.MenuView(screen_configuration)



class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


class StartButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        pass

