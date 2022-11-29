import arcade

from gui.screen_configuration import ScreenConfiguration


class Playground:
    def __init__(self, screen_configuration: ScreenConfiguration):
        self.config = screen_configuration
        self.mat_list = arcade.SpriteList()
        # self.start_x_position = self.config.start_x + self.config.x_spacing
        self.start_x_position = self.config.current_x / 2
        self.cards = []

    def get_cards(self) -> [arcade.SpriteList()]:
        return self.cards

    def add_new_sprite(self):
        mat = arcade.SpriteSolidColor(self.config.mat_width, self.config.mat_height, self.config.sprite_color)
        mat.position = self.start_x_position, self.config.middle_y
        self.start_x_position += self.config.x_spacing
        self.mat_list.append(mat)
        self.cards.append(arcade.SpriteList())

    def remove_card_and_mat(self, card_index):
        self.cards.remove(self.cards[card_index])
        self.mat_list.remove(self.mat_list[card_index])
        self.move_card_and_mat(card_index)

    def add_new_card(self, card):
        if len(self.cards[-1]) == 0:
            card.center_x = self.mat_list[-1].center_x
            card.center_y = self.mat_list[-1].center_y
            self.cards[-1].append(card)

        elif len(self.cards[-1]) == 1:
            card.center_x = self.mat_list[-1].center_x
            card.center_y = self.mat_list[-1].center_y - self.config.card_height / 4
            self.cards[-1].append(card)

    def move_card_and_mat(self, card_index):

        for card in self.cards[card_index:]:
            card.center_x -= self.config.x_spacing
        for mat in self.mat_list[card_index:]:
            mat.center_x -= self.config.x_spacing

    def get_bottom_card(self):
        return self.cards[-1][0]

    def get_mats(self):
        return self.mat_list

    def get_all_cards(self):
        lst = arcade.SpriteList()
        for card_pair in self.cards:
            for card in card_pair:
                lst.append(card)
        return lst

    def get_and_remove_all_cards(self):
        lst = []
        for card_pair in self.cards:
            for card in card_pair:
                lst.append(card)

        self.cards.clear()
        self.mat_list.clear()
        self.start_x_position = self.config.current_x / 2
        self.add_new_sprite()

        return lst
