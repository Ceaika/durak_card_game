import os

import arcade
import arcade.gui

from gui.screen_configuration import ScreenConfiguration
import gui.view_manager


class RulesButton(arcade.gui.UIFlatButton):
    def __init__(self, config: ScreenConfiguration):
        super(RulesButton, self).__init__(text="Rules", width=200)
        self.config = config

    def on_click(self, event: arcade.gui.UIOnClickEvent):
        # webbrowser.open('https://de.wikipedia.org/wiki/Durak_(Kartenspiel)', 2, True)
        view_manager = gui.view_manager.ViewManager()
        view_manager.show_rules_view()
