import arcade

from gui.screen_configuration import ScreenConfiguration


class ComputerCardSpritesArea:
    def __init__(self, config: ScreenConfiguration):
        self.config = config
        self.mat_list: arcade.SpriteList = arcade.SpriteList()
        self.start_x_position = self.config.start_x + self.config.x_spacing
        self.__init_with_six_sprites()
        self.cards = []

    def __init_with_six_sprites(self):
        self.start_x_position = self.config.start_x
        # define
        for i in range(6):
            self.add_new_sprite(self.config.top_y)

    def add_new_sprite(self, y_pos):
        mat = arcade.SpriteSolidColor(self.config.mat_width, self.config.mat_height, self.config.sprite_color)
        mat.position = self.start_x_position, y_pos
        self.start_x_position += self.config.x_spacing
        self.mat_list.append(mat)

    def main_count_of_sprites(self):
        return len(self.mat_list)

    def add_new_card(self, card):
        self.cards.append(card)

    def remove_card_and_mat(self, card_index):
        self.cards.remove(self.cards[card_index])
        self.mat_list.remove(self.mat_list[card_index])
        self.move_card_and_mat(card_index)

    def add_card_and_mat(self, mat_index, card):

        # check if mat_index is in range of cards
        if mat_index < len(self.cards):
            self.cards.insert(mat_index, card)
        else:
            self.cards.append(card)

        if len(self.mat_list) == len(self.cards):
            self.add_new_sprite(self.config.top_y)

    def move_card_and_mat(self, card_index):

        for card in self.cards[card_index:]:
            card.center_x -= self.config.x_spacing
        for mat in self.mat_list[card_index:]:
            mat.center_x -= self.config.x_spacing

    def get_cards_with_same_suit(self, bottom_card):
        # return list of cards with same suit as bottom card
        return [card for card in self.cards if card.suit == bottom_card.suit]

    def get_cards_with_same_value(self, available_card):
        # return list of cards with same value as available_card
        return [card for card in self.cards if card.value == available_card.value]


