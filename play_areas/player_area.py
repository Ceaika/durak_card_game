import arcade

from gui.screen_configuration import ScreenConfiguration


class PlayerArea:

    def __init__(self, config: ScreenConfiguration, beginning_y):
        self.config = config
        self.beginning_x = self.config.start_x + self.config.x_spacing
        self.beginning_y = beginning_y
        self.cards = []
        self.is_attacking = True

    def add_new_card(self, card):
        self.beginning_x += self.config.x_spacing
        card.position = self.beginning_x, self.beginning_y
        self.cards.append(card)

    def remove_card(self, card_index):
        if card_index < len(self.cards):
            self.beginning_x -= self.config.x_spacing
            self.cards.remove(self.cards[card_index])
            self.move_card(card_index)

    def move_card(self, card_index):
        for card in self.cards[card_index:]:
            card.center_x -= self.config.x_spacing

    def find_card(self, card):
        if card in self.cards:
            return self.cards.index(card)
        else:
            return None

    def get_cards_with_same_suit(self, bottom_card):
        # return list of cards with same suit as bottom card
        return [card for card in self.cards if card.suit == bottom_card.suit]

    def get_cards_with_same_value(self, available_card):
        # return list of cards with same value as available_card
        return [card for card in self.cards if card.value == available_card.value]
