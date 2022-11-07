import arcade


class Player:
    def __init__(self, x_start_position, y_start_position, x_spacing):
        self.x_position = x_start_position
        self.y_pos = y_start_position
        self.x_spacing = x_spacing
        self.cards = []

    #add a new Card to the list
    def add_card(self,card):
        self.cards.append(card)
        self.x_position += self.x_spacing
    #get the x,y of the last Card from right to left
    def get_x_y(self):
        return self.x_position, self.y_pos

    #remove a card and move the rest together
    def remove_card(self,card):
        index = self.cards.index(card)
        self.cards.remove(card)
        if index == len(self.cards):
            self.x_position -= self.x_spacing
        else:
            for card in self.cards[index:]:
                self.x_position = card.center_x
                card.center_x -= self.x_spacing

