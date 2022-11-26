import arcade
import arcade.gui

from Constants import EASY
from gui.screen_configuration import ScreenConfiguration
import gui.view_manager


class EasyButton(arcade.gui.UIFlatButton):
    def __init__(self, screen_config: ScreenConfiguration, manager):
        super().__init__(
            text="Easy",
            center_x=0,
            center_y=0,
            width=200,
            height=50,
        )
        self.config = screen_config
        self.manager = manager

    def on_click(self, event):
        view_manager = gui.view_manager.ViewManager()
        view_manager.show_game_view(EASY)
        self.manager.disable()