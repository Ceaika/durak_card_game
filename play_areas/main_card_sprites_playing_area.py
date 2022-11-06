import arcade

from gui.screen_configuration import ScreenConfiguration


class MainCardSpritesPlayingArea:
    def __init__(self, screen_configuration: ScreenConfiguration):
        self.config = screen_configuration
        self.mat_list: arcade.SpriteList = arcade.SpriteList()
        self.start_x_position = self.config.middle_x
        self.cards = []
        self.cards_mats = {}
        self.move_const = self.config.x_spacing/2

    def add_new_sprite(self):
        #self.move_mats()
        mat = arcade.SpriteSolidColor(self.config.mat_width, self.config.mat_height, self.config.sprite_color)
        mat.position = self.start_x_position, self.config.middle_y
        self.cards_mats = {mat: []}
        self.start_x_position += self.config.x_spacing
        self.mat_list.append(mat)

    def get_count_of_cards_on_pile(self, mat_index):
        mat = self.mat_list.__getitem__(mat_index)
        if self.cards_mats.get(mat) is not None :
            return len(self.cards_mats.get(mat))
        else:
            return 0

    def add_new_card(self, card, mat_index):
        self.cards.append(card)
        mat = self.mat_list.__getitem__(mat_index)
        count = len(self.cards_mats.get(mat))
        if count < 2:
            self.cards_mats[mat].append(card)
        self.check_count()

    def check_count(self):
        at_least_one = True
        for mat in self.cards_mats.keys():
            if len(self.cards_mats.get(mat)) == 0 or len(self.cards_mats.get(mat)) == 1:
                at_least_one = False


        if at_least_one:
            self.add_new_sprite()

    def move_mats(self):

        len = self.mat_list.__len__()
        if len > 1:
            if len % 2:
                self.mat_list.move(-self.move_const, 0)
                self.start_x_position -= self.move_const
            else:
                self.mat_list.move(self.move_const, 0)
                self.start_x_position += self.move_const

    def add_card_and_mat(self, mat_index, card):

        # check if mat_index is in range of cards
        if mat_index < len(self.cards):
            self.cards.insert(mat_index, card)
        else:
            self.cards.append(card)

        if len(self.mat_list) == len(self.cards):
            self.add_new_sprite()

    def get_size(self):
        return len(self.cards)

    def remove_card_and_mat(self, card_index):
        self.cards.remove(self.cards[card_index])
        self.mat_list.remove(self.mat_list[card_index])
        self.move_card_and_mat(card_index)

    def move_card_and_mat(self, card_index):

        for card in self.cards[card_index:]:
            card.center_x -= self.config.x_spacing
        for mat in self.mat_list[card_index:]:
            mat.center_x -= self.config.x_spacing
