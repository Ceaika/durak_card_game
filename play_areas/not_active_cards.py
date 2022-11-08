import random

import arcade

from gui.card import Card
from gui.screen_configuration import ScreenConfiguration


class NotActiveCards:
    def __init__(self, config: ScreenConfiguration):
        self.unused_cards = arcade.SpriteList()
        self.played_cards = arcade.SpriteList()
        self.config = config
        self.trump_card = None

    def add_new_card(self, card):
        self.unused_cards.append(card)

    # remove and return card from the list at index
    def remove_card(self, index):
        return self.unused_cards.pop(index)

    # remove and return last card from the list
    def remove_last_card(self):
        return self.unused_cards.pop()

    def set_trump_card(self, card):
        self.trump_card = card

    def add_played_card(self, card: Card):
        random_angle = random.randint(0, 360)
        random_offset = random.randint(0, 5)
        card.center_y = self.config.current_y / 2 + random_offset
        card.center_x = self.config.start_x + self.config.x_spacing * 2 + random_offset
        card.angle = random_angle
        card.face_down()
        self.played_cards.append(card)