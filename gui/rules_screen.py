import arcade
import arcade.gui
from screen_configuration import ScreenConfiguration


# class Rules(arcade.gui.UITextArea):
#     def __int__(self):
#         super(Rules, self)
#         self.fit_content()


class RulesView(arcade.View):
    def __init__(self, config: ScreenConfiguration):
        super().__init__()

        self.config = config

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create Vertical Box to place the items in
        self.v_box = arcade.gui.UIBoxLayout()

        # open File and read Rules
        f = open('../resources/Rules.txt', 'r', encoding='UTF-8')
        self.rules = f.read()
        f.close()

        arcade.set_background_color(arcade.color.WHITE_SMOKE)

        # Text Field to be put in V_Box
        self.rules = arcade.gui.UITextArea(self.config.width / 2, self.config.height / 2,
                      self.config.width * 0.7, self.config.height * 0.7, self.rules, 'arial', 25,
                      arcade.color.BLACK)
        self.rules.fit_content()
        self.rules.scroll_speed = 5.5

        self.v_box.add(self.rules)

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

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            from start_screen import MenuView
            arcade.get_window().show_view(MenuView(self.config))
