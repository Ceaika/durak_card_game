import arcade


class NotActiveCards:
    def __init__(self):
        self.cards = arcade.SpriteList()
        self.trump_card = None

    def add_new_card(self, card):
        self.cards.append(card)

    # remove and return card from the list at index
    def remove_card(self, index):
        return self.cards.pop(index)

    # remove and return last card from the list
    def remove_last_card(self):
        return self.cards.pop()

    def set_trump_card(self, card):
        self.trump_card = card