import arcade

from gui.screen_configuration import ScreenConfiguration


class PlayersCardSpritesArea:
    def __init__(self, config: ScreenConfiguration):
        self.config = config
        self.mat_list: arcade.SpriteList = arcade.SpriteList()
        self.start_x_position = self.config.start_x + self.config.x_spacing
        self.cards = []
        self.__init_with_six_sprites()

    def __init_with_six_sprites(self):
        self.start_x_position = self.config.start_x
        # define
        for i in range(6):
            self.add_new_sprite(self.config.bottom_y)

    def add_new_sprite(self, y_pos):
        mat = arcade.SpriteSolidColor(self.config.mat_width, self.config.mat_height, self.config.sprite_color)
        mat.position = self.start_x_position, y_pos
        self.start_x_position += self.config.x_spacing
        self.mat_list.append(mat)

    def main_count_of_sprites(self):
        return len(self.mat_list)

    def add_new_card(self, card):
        self.cards.append(card)
