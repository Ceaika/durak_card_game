# import arcade.gui
#
# import view_handler
# from screen_configuration import ScreenConfiguration
#
#
# class QuitButton(arcade.gui.UIFlatButton):
#     def on_click(self, event: arcade.gui.UIOnClickEvent):
#         arcade.exit()
#
# class StartButton(arcade.gui.UIFlatButton):
#     def __init__(self, screen_config: ScreenConfiguration):
#         super(StartButton, self).__init__(text="Start Game", width=200)
#         self.config = screen_config
#     def on_click(self, event: arcade.gui.UIOnClickEvent):
#         view_handler.show_game()
#
# class MenuView(arcade.View):
#     def __init__(self, screen_config: ScreenConfiguration):
#         super().__init__()
#         self.configuration = screen_config
#         # --- Required for all code that uses UI element,
#         # a UIManager to handle the UI.
#         self.manager = arcade.gui.UIManager()
#         self.manager.enable()
#
#         # Set background color
#         arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
#
#         # Create a vertical BoxGroup to align buttons
#         self.v_box = arcade.gui.UIBoxLayout()
#
#         # Create the buttons
#         start_button = StartButton(self.configuration)
#         self.v_box.add(start_button.with_space_around(bottom=20))
#
#         # Again, method 1. Use a child class to handle events.
#         quit_button = QuitButton(text="Quit", width=200)
#         self.v_box.add(quit_button)
#
#         # Create a widget to hold the v_box widget, that will center the buttons
#         self.manager.add(
#             arcade.gui.UIAnchorWidget(
#                 anchor_x="center_x",
#                 anchor_y="center_y",
#                 child=self.v_box)
#         )
#
#     def on_draw(self):
#         self.clear()
#         self.manager.draw()
#
# def main():
#     """ Main function """
#     config = ScreenConfiguration()
#     window = arcade.Window(config.width, config.height, config.screen_title, fullscreen=True)
#     menu_view = MenuView(config)
#     window.show_view(menu_view)
#     arcade.run()
#
#
# if __name__ == '__main__':
#     main()