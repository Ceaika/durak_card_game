import arcade

from screen_configuration import ScreenConfiguration


class PlayersCardSpritesArea:
    def __init__(self, pile_mat_list, config: ScreenConfiguration):
        self.config = config
        self.pile_mat_list = pile_mat_list
        self.start_x_position = self.config.start_x + self.config.x_spacing
        self.__init_with_six_sprites()

    def __init_with_six_sprites(self):
        for i in range(6):
            self.add_new_sprite()

    def add_new_sprite(self):
        pile = arcade.SpriteSolidColor(self.config.mat_width, self.config.mat_height, self.config.sprite_color)
        pile.position = self.start_x_position, self.config.bottom_y
        self.start_x_position += self.config.x_spacing
        self.pile_mat_list.append(pile)
