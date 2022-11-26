# import arcade
#
# from gui.screen_configuration import ScreenConfiguration
#
#
# class GameWindow(arcade.Window):
#     def __init__(self, config: ScreenConfiguration):
#         self.configuration = config
#         super().__init__(config.width, config.height, config.screen_title)
#
#
#
#
# def main():
#     """ Main function """
#     config = ScreenConfiguration()
#     #window = arcade.Window(config.width, config.height, config.screen_title, fullscreen=True)
#     window = GameWindow(config)
#     menu_view = MenuView(config)
#     window.show_view(menu_view)
#     arcade.run()
#
# if __name__ == '__main__':
#     main()