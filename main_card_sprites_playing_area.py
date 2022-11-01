import arcade

from screen_configuration import ScreenConfiguration


class MainCardSpritesPlayingArea:
    def __init__(self, pile_mat_list, screen_configuration: ScreenConfiguration):
        self.config = screen_configuration
        self.pile_mat_list = pile_mat_list
        self.start_x_position = self.config.start_x + self.config.x_spacing

    def add_new_sprite(self):
        pile = arcade.SpriteSolidColor(self.config.mat_width, self.config.mat_height, self.config.sprite_color)
        pile.position = self.start_x_position, self.config.middle_y
        self.start_x_position += self.config.x_spacing
        self.pile_mat_list.append(pile)
