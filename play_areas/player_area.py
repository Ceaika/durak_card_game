import arcade

from gui.screen_configuration import ScreenConfiguration


class PlayerArea:

    def __init__(self, beginning_x, beginning_y, x_spacing,current_x):
        self.current_x = current_x
        self.x_spacing_cfg = x_spacing
        self.x_spacing = self.x_spacing_cfg
        self.beginning_x_cfg = beginning_x
        self.beginning_x = self.beginning_x_cfg
        self.beginning_y = beginning_y
        self.cards = arcade.SpriteList()
        self.is_attacking = True
        self.is_turn = True
        self.is_taking = False

    def out_of_bound(self):

        if (self.cards[-1].position[0] + self.x_spacing) < 0 or (
                self.cards[-1].position[0] + self.x_spacing) > self.current_x - self.x_spacing:
            while (True):
                if abs(len(self.cards) * self.x_spacing) > self.current_x:
                    sum = self.current_x - self.x_spacing - self.beginning_x_cfg
                    self.x_spacing = sum / len(self.cards)
                else:
                    break

            self.new_pos_all()

    def in_bound(self):
        if self.beginning_x_cfg + len(self.cards) * self.x_spacing_cfg < self.current_x - self.x_spacing_cfg:
            self.x_spacing = self.x_spacing_cfg
            self.new_pos_all()

    def new_pos_all(self):

        self.beginning_x = self.beginning_x_cfg
        for i in range(len(self.cards)):
            self.cards[i].destination_point = self.beginning_x + i * self.x_spacing, self.beginning_y

    def get_cards(self):
        return self.cards

    def add_new_card(self, card):
        #card.position = self.beginning_x, self.beginning_y
        card.destination_point = self.beginning_x, self.beginning_y
        self.beginning_x += self.x_spacing
        self.cards.append(card)

        #self.out_of_bound()

    def remove_card(self, card):
        if card is not None:
            self.beginning_x -= self.x_spacing
            card_index = self.find_card(card)
            #self.move_card(card_index)
            self.cards.remove(card)
            self.move_card(card_index)

    def move_card(self, card_index):
        move_position = self.beginning_x - self.x_spacing
        # Iterate backwards through the list
        for card in self.cards[card_index:][::-1]:
            card.destination_point = move_position, self.beginning_y
            move_position -= self.x_spacing

    def find_card(self, card):
        if card in self.cards:
            return self.cards.index(card)
        else:
            return None

    def get_cards_with_same_suit_as_card(self, bottom_card):
        # return list of unused_cards with same suit as bottom card
        return [card for card in self.cards if card.suit == bottom_card.suit]

    def get_cards_with_same_value_as_card(self, available_card):
        # Create empty set
        cards_with_same_value = set()
        # Add all unused_cards with same value to set
        for card in self.cards:
            if card.value == available_card.value:
                cards_with_same_value.add(card)

        return cards_with_same_value

    def get_cards_with_same_value_int(self, value):
        # Create empty set
        cards_with_same_value = set()
        # Add all cards with same value to set
        for card in self.cards:
            if card.value == value:
                cards_with_same_value.add(card)

        return cards_with_same_value

    def get_cards_with_same_suit_str(self, suit):
        # Create empty set
        cards_with_same_suit = set()
        # Add all cards with same suit to set
        for card in self.cards:
            if card.suit == suit:
                cards_with_same_suit.add(card)

        return cards_with_same_suit
