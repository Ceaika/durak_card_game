import arcade
import arcade.gui

from gui.buttons.start_button import StartButton
from gui.buttons.to_menu_button import ToMenuButton
from gui.screen_configuration import ScreenConfiguration


class WinView(arcade.View):
    def __init__(self, config: ScreenConfiguration):
        super().__init__()

        self.config = config

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.win_image = arcade.load_texture('../resources/win.png')

        # Create Vertical Box to place the items in
        self.v_box = arcade.gui.UIBoxLayout()

        arcade.set_background_color(arcade.color.BLACK)

        self.v_box.add(StartButton(self.config, self.manager).with_space_around(bottom=20))
        self.v_box.add(ToMenuButton(self.config, self.manager).with_space_around(bottom=20))

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                child=self.v_box)
        )

    def on_draw(self):
        # This command has to happen before we start drawing
        self.clear()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured((self.config.current_x / 2) - 585 * self.config.screen_ratio,
                                            (self.config.current_y / 2) - 85 * self.config.screen_ratio,
                                            1170 * self.config.screen_ratio, 170 * self.config.screen_ratio,
                                            self.win_image)
        self.manager.draw()
