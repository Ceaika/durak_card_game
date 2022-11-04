import arcade

from gui.screen_configuration import ScreenConfiguration


class PlayersCardSpritesArea:
    def __init__(self, config: ScreenConfiguration):
        self.config = config
        self.mat_list: arcade.SpriteList = arcade.SpriteList()
        self.start_x_position = self.config.start_x_bottom# + self.config.x_spacing
        self.cards = []
        self.__init_with_six_sprites()
        self.move_const = self.config.x_spacing

    def __init_with_six_sprites(self):
        #self.start_x_position = self.config.start_x_bottom
        # define
        for i in range(6):
            self.add_new_sprite(self.config.bottom_y)

    def add_new_sprite(self, y_pos):
        mat = arcade.SpriteSolidColor(self.config.mat_width, self.config.mat_height, self.config.sprite_color)
        mat.position = self.start_x_position, y_pos
        self.start_x_position += self.config.x_spacing
        self.mat_list.append(mat)

    def get_x_y(self):
        return self.start_x_position - self.config.x_spacing , self.config.bottom_y
    def get_cards(self):
        return self.cards
    def move_cards(self, cards):
        if len(cards) > 0:
            for card in cards:
                card.move(-self.move_const, 0)

    def main_count_of_sprites(self):
        return len(self.mat_list)

    def add_new_card(self, card):
        self.cards.append(card)

    def remove_card_and_mat(self, card_index):
        self.cards.remove(self.cards[card_index])
        self.mat_list.remove(self.mat_list[card_index])
        self.move_card_and_mat(card_index)

    def rempve_mats(self):
        self.mat_list.clear(True)
    def remove_mat(self, card_index):
        self.mat_list.remove(self.mat_list[card_index])
    def add_card_and_mat(self, mat_index, card):

        # check if mat_index is in range of cards
        if mat_index < len(self.cards):
            self.cards.insert(mat_index, card)
        else:
            self.cards.append(card)

        if len(self.mat_list) == len(self.cards):
            self.add_new_sprite(self.config.bottom_y)

    def move_card_and_mat(self, card_index):

        for card in self.cards[card_index:]:
            card.center_x -= self.config.x_spacing
        for mat in self.mat_list[card_index:]:
            mat.center_x -= self.config.x_spacing
