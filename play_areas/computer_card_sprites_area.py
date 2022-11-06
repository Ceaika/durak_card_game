import arcade

from gui.screen_configuration import ScreenConfiguration


class ComputerCardSpritesArea:
    def __init__(self, config: ScreenConfiguration):
        self.config = config
        self.x_position = self.config.start_x_top# + self.config.x_spacing
        self.y_pos = self.config.top_y
        self.cards = []

    def add_next_x_position(self):
        self.x_position -= self.config.x_spacing
    def get_x_y(self):
        return self.x_position + self.config.x_spacing , self.y_pos

    def add_card(self,card):
        self.cards.append(card)

    def remove_card(self, card):
        index = self.cards.index(card)
        self.cards.remove(card)
        #if last card taken do nothíng
        if index == len(self.cards):
            self.x_position += self.config.x_spacing
        else:
            for card in self.cards[index:]:
                self.x_position = card.center_x
                card.center_x += self.config.x_spacing


