from play_areas.not_active_cards import NotActiveCards
from play_areas.player_area import PlayerArea


class Endgame:
    def __init__(self, human: PlayerArea, computer: PlayerArea, not_active_cards: NotActiveCards):
        self.not_active_cards = not_active_cards
        self.human = human
        self.computer = computer
        self.human_cards = None
        self.computer_cards = None
        self.main_area_cards = [[]]

    def update_cards(self):
        self.human_cards = self.human.cards
        self.computer_cards = self.computer.cards

    def get_main_area_cards(self):
        for card_pair in self.main_area_cards:
            for card in card_pair:
                yield card

    def validate_attack(self, card):
        cards = self.get_main_area_cards()
        card_values = set()
        for card in cards:
            card_values.add(card.value)

        if card.value in card_values:
            return True
        else:
            return False

    def validate_defence_move(self, top_card):
        bottom_card = self.main_area_cards[-1][0]
        if top_card.suit == bottom_card.suit:
            if top_card.value > bottom_card.value:
                return True
            else:
                return False
        else:
            if top_card.suit == self.not_active_cards.trump_suit and bottom_card.suit != self.not_active_cards.trump_suit:
                return True
            else:
                return False

    def bot_start(self):
        for card in self.computer_cards:
            pass

    def make_move(self):
        # The computer will always make the first move, because this method is only called when it's his move
        if len(self.main_area_cards) == 1:
            # There are no cards in the main area, so the computer can choose whichever card he wants
            pass
        pass


