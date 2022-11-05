import arcade


class NotActiveCards:
    def __init__(self):
        self.cards = arcade.SpriteList()

    def add_new_card(self, card):
        self.cards.append(card)

    # remove and return card from the list at index
    def remove_card(self, index):
        return self.cards.pop(index)

    # remove and return last card from the list
    def remove_last_card(self):
        return self.cards.pop()