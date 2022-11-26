import arcade
import arcade.gui

from Constants import EASY, MEDIUM, HARD
from gui.screen_configuration import ScreenConfiguration
import gui.view_manager


class DifficultyView(arcade.View):
    def __init__(self, screen_config: ScreenConfiguration):
        super().__init__()

        # This is the manager used to switch between views
        self.view_manager = gui.view_manager.ViewManager()

        self.config = screen_config

        self.scaling_x = self.config.current_x / 9
        self.scaling_y = self.config.current_y / 15
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Add the difficulty buttons
        self.easy_button = arcade.gui.UIFlatButton(text="Easy", height=self.scaling_y,
                                                   width=self.scaling_x)
        self.medium_button = arcade.gui.UIFlatButton(text="Medium", height=self.scaling_y,
                                                     width=self.scaling_x)
        self.hard_button = arcade.gui.UIFlatButton(text="Hard", height=self.scaling_y,
                                                   width=self.scaling_x)

        # Add to V_Box with spacing
        self.v_box.add(self.easy_button.with_space_around(bottom=self.scaling_y / 3))
        self.v_box.add(self.medium_button.with_space_around(bottom=self.scaling_y / 3))
        self.v_box.add(self.hard_button)

        # Add events
        self.easy_button.on_click = self.easy_button_clicked
        self.medium_button.on_click = self.medium_button_clicked
        self.hard_button.on_click = self.hard_button_clicked

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def easy_button_clicked(self, event):
        self.button_clicked(EASY)

    def medium_button_clicked(self, event):
        self.button_clicked(MEDIUM)

    def hard_button_clicked(self, event):
        self.button_clicked(HARD)

    def button_clicked(self, mode):
        self.view_manager.show_game_view(mode)
        self.manager.disable()

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.view_manager.show_menu_view()
            self.manager.disable()
