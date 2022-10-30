import arcade

from screen_configuration import ScreenConfiguration
from views import Views


class ViewHandler:
    def __init__(self, config: ScreenConfiguration, window: arcade.Window, views: Views):
        self.active_window = window
        self.__views = views

    def show_menu(self):
        self.active_window.show_view(self.__views.menu_view)

    def show_main_game(self):
        self.active_window.show_view(self.__views.game_view)


def main():
    """ Main function """
    config = ScreenConfiguration()
    window = arcade.Window(config.width, config.height, config.screen_title, fullscreen=True)
    views = Views(config)
    view_handler = ViewHandler(config, window, views)
    view_handler.show_menu()
    arcade.run()


if __name__ == "__main__":
    main()
