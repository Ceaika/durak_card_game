import arcade

from gui.screen_configuration import ScreenConfiguration


class PlayersCardSpritesArea:
    def __init__(self, config: ScreenConfiguration):
        self.config = config
        self.x_position = self.config.start_x_bottom
        self.y_pos = self.config.bottom_y
        self.cards = []
        self.move_const = self.config.x_spacing

    #add a new x position to place the cards
    def add_next_x_position(self):
        self.x_position += self.config.x_spacing

    #add a new Card to the list
    def add_card(self,card):
        self.cards.append(card)
    #get the x,y of the last Card from right to left
    def get_x_y(self):
        return self.x_position - self.config.x_spacing , self.config.bottom_y

    #remove a card and move the rest together
    def remove_card(self,card):
        index = self.cards.index(card)
        self.cards.remove(card)
        #if last card taken do nothíng
        if index == len(self.cards):
            self.x_position -= self.config.x_spacing
        else:
            for card in self.cards[index:]:
                self.x_position = card.center_x
                card.center_x -= self.config.x_spacing

