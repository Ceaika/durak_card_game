import arcade

from gui.screen_configuration import ScreenConfiguration


class PlayerArea:

    def __init__(self, beginning_x, beginning_y, x_spacing):
        self.x_spacing = x_spacing
        self.beginning_x = beginning_x
        self.beginning_y = beginning_y
        self.cards = arcade.SpriteList()
        self.is_attacking = True
        self.is_turn = True
        self.is_taking = False

    def get_cards(self):
        return self.cards
    def add_new_card(self, card):
        card.position = self.beginning_x, self.beginning_y
        self.beginning_x += self.x_spacing
        self.cards.append(card)

    def remove_card(self, card_index):
        if card_index < len(self.cards):
            self.beginning_x -= self.x_spacing
            self.cards.remove(self.cards[card_index])
            self.move_card(card_index)

    def move_card(self, card_index):
        for card in self.cards[card_index:]:
            card.center_x -= self.x_spacing

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
