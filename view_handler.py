import arcade

from screen_configuration import ScreenConfiguration
from views import Views


class ViewHandler:
    def __init__(self, config: ScreenConfiguration, views: Views):
        self.__views = views

    def show_menu(self):
        arcade.get_window().show_view(self.__views.menu_view)

    def show_main_game(self):
        arcade.get_window().show_view(self.__views.game_view)


def main():
    """ Main function """
    config = ScreenConfiguration()
    window = arcade.Window(config.width, config.height, config.screen_title, fullscreen=True)
    views = Views(config)
    view_handler = ViewHandler(config, views)
    view_handler.show_menu()
    arcade.run()


if __name__ == "__main__":
    main()
