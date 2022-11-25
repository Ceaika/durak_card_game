import arcade
import arcade.gui

from gui.buttons.easy_button import EasyButton
from gui.buttons.hard_button import HardButton
from gui.buttons.medium_button import MediumButton
from gui.screen_configuration import ScreenConfiguration


class DifficultyView(arcade.View):
    def __init__(self, screen_config: ScreenConfiguration):
        super().__init__()
        self.config = screen_config

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Add the difficulty buttons
        self.easy_button = EasyButton(self.config, self.manager)
        self.medium_button = MediumButton(self.config, self.manager)
        self.hard_button = HardButton(self.config, self.manager)
        self.v_box.add(self.easy_button)
        self.v_box.add(self.medium_button)
        self.v_box.add(self.hard_button)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_draw(self):
        self.clear()
        self.manager.draw()
