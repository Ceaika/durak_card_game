from game_logic.strategies.computer_strategy import Strategy
from play_areas.playground import Playground
from play_areas.not_active_cards import NotActiveCards
from play_areas.player_area import PlayerArea


class MediumStrategy(Strategy):
    def __init__(self, computer_area: PlayerArea, main_card_sprites_playing_area: Playground,
                 not_active_cards: NotActiveCards, player_area: PlayerArea):
        super().__init__(computer_area, main_card_sprites_playing_area, not_active_cards, player_area)
        self.all_possible_cards = {"Clubs": [6, 7, 8, 9, 10, 11, 12, 13, 14],
                                   "Diamonds": [6, 7, 8, 9, 10, 11, 12, 13, 14],
                                   "Hearts": [6, 7, 8, 9, 10, 11, 12, 13, 14],
                                   "Spades": [6, 7, 8, 9, 10, 11, 12, 13, 14]}

    def remove_played_cards(self):
        played_cards = self.not_active_cards.played_cards
        for card in played_cards:
            if card in self.all_possible_cards[card.suit]:
                self.all_possible_cards[card.suit].remove(card.value)

    def calc_bot_hand(self):
        # get the available card suits
        available_cards = {}
        for card in self.computer_area.cards:
            if card.suit != self.not_active_cards.trump_card.suit:
                if card.suit not in available_cards:
                    available_cards[card.suit] = []
                available_cards[card.suit].append(card.value)
        return available_cards

    def highest_values(self, bot_hand):
        # Get the highest value for each suit
        highest_values = {}
        for suit in bot_hand:
            highest_values[suit] = max(bot_hand[suit])

        return highest_values

    def reduce_dict(self, bot_cards):
        help_dict = self.all_possible_cards.copy()
        for suit in bot_cards:
            # Remove all cards that are lower than the highest card in the suit
            help_dict[suit] = [card for card in help_dict[suit] if card > bot_cards[suit]]

        return help_dict

    def find_card(self, suit, value):
        suit_lst = self.computer_area.get_cards_with_same_suit_str(suit)
        value_lst = self.computer_area.get_cards_with_same_value_int(value)
        return suit_lst.intersection(value_lst)

    def compute_best_attack_move(self):
        card_to_play = None
        self.remove_played_cards()
        bot_cards = self.calc_bot_hand()
        if len(self.plaground.mat_list) == 1:
            highest_values = self.highest_values(bot_cards)
            help_dict = self.reduce_dict(highest_values)
            # Get the suit with the shortest list
            suit = min(help_dict, key=lambda suit: len(help_dict[suit]))
            # If suit is a set, get the first element
            if isinstance(suit, set):
                suit = suit.pop()
            card_to_play = self.find_card(suit, highest_values[suit])
            # What if bot has only trump cards?
            if card_to_play is None and len(bot_cards[self.not_active_cards.trump_card.suit]) > 0:
                card_to_play = min(bot_cards[self.not_active_cards.trump_card.suit])
                card_to_play = self.find_card(self.not_active_cards.trump_card.suit, card_to_play)

            # If card_to_play is a set, get the first element
            if isinstance(card_to_play, set):
                card_to_play = card_to_play.pop()

        else:
            # Get all the unused_cards from the main area
            cards = self.plaground.get_all_cards()
            playable_cards = set()
            # Get the unused_cards with the same value
            for card in cards:
                playable_cards.update(self.computer_area.get_cards_with_same_value_as_card(card))
                # Filter out the unused_cards with the same suit as the trump card
                playable_cards = {card for card in playable_cards if card.suit != self.not_active_cards.trump_card.suit}
                # Get the card with the lowest value
                card_to_play = min(playable_cards, key=lambda card: card.value, default=None)

        return card_to_play

    def compute_best_defense_move(self):
        # Filter out the unused_cards that are not playable
        bottom_card = self.plaground.get_bottom_card()
        # Filter the computer_area cards with the same suit as the bottom card
        cards_with_same_suit = self.computer_area.get_cards_with_same_suit_as_card(bottom_card)
        # Get the card with the lowest value that is higher than the bottom card from cards_with_same_suit
        # card_to_play = min(cards_with_same_suit, key=lambda card: card.value, default=None)
        # Filter out the cards that have a value lower than the bottom card
        cards_with_same_suit = {card for card in cards_with_same_suit if card.value > bottom_card.value}
        # Get the card with the lowest value
        card_to_play = min(cards_with_same_suit, key=lambda card: card.value, default=None)

        if card_to_play is None and bottom_card.suit != self.not_active_cards.trump_card.suit:
            trump_cards = self.computer_area.get_cards_with_same_suit_as_card(self.not_active_cards.trump_card)
            if len(trump_cards) > 0:
                card_to_play = min(trump_cards, key=lambda card: card.value)

        return card_to_play


