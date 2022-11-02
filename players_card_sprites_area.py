import arcade

from screen_configuration import ScreenConfiguration


class PlayersCardSpritesArea:
    def __init__(self, config: ScreenConfiguration):
        self.config = config
        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()
        self.start_x_position = self.config.start_x + self.config.x_spacing
        self.__init_with_six_sprites()
        self.piles = []

    def __init_with_six_sprites(self):
        self.start_x_position = self.config.start_x
        #define
        for i in range(6):
            self.add_new_sprite(self.config.bottom_y)

    def add_new_sprite(self, y_pos):
        pile = arcade.SpriteSolidColor(self.config.mat_width, self.config.mat_height, self.config.sprite_color)
        pile.position = self.start_x_position, y_pos
        self.start_x_position += self.config.x_spacing
        self.pile_mat_list.append(pile)
        # add empty list to piles
        self.piles.append([])
        print(self.piles)

    def main_count_of_sprites(self):
        return len(self.pile_mat_list)