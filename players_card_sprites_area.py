import arcade

from constants import START_X, X_SPACING, MAT_WIDTH, MAT_HEIGHT, SPRITE_COLOR, BOTTOM_Y


class PlayersCardSpritesArea:
    def __init__(self, pile_mat_list):
        self.pile_mat_list = pile_mat_list
        self.start_x_position = START_X + X_SPACING
        self.__init_with_six_sprites()

    def __init_with_six_sprites(self):
        for i in range(6):
            self.add_new_sprite()

    def add_new_sprite(self):
        pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, SPRITE_COLOR)
        pile.position = self.start_x_position, BOTTOM_Y
        self.start_x_position += X_SPACING
        self.pile_mat_list.append(pile)
