import arcade

from constants import START_X, X_SPACING, MAT_WIDTH, MAT_HEIGHT, SPRITE_COLOR, MIDDLE_Y


class MainCardSpritesPlayingArea:
    def __init__(self, pile_mat_list):
        self.pile_mat_list = pile_mat_list
        self.start_x_position = START_X + X_SPACING

    def add_new_sprite(self):
        pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, SPRITE_COLOR)
        pile.position = self.start_x_position, MIDDLE_Y
        self.start_x_position += X_SPACING
        self.pile_mat_list.append(pile)
