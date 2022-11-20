from game_logic.strategies.computer_strategy import Strategy
from play_areas.main_card_sprites_playing_area import MainCardSpritesPlayingArea
from play_areas.not_active_cards import NotActiveCards
from play_areas.player_area import PlayerArea


class DifficultStrategy(Strategy):
    def __init__(self, computer_area: PlayerArea, main_card_sprites_playing_area: MainCardSpritesPlayingArea,
                 not_active_cards: NotActiveCards, player_area: PlayerArea):
        super().__init__(computer_area, main_card_sprites_playing_area, not_active_cards, player_area)
        self.not_played_cards = {"clubs": [range(6, 15)], "diamonds": [range(6, 15)], "hearts": [range(6, 15)]}

    def remove_played_cards(self):
        for card in self.not_active_cards.played_cards:
            if card in self.not_played_cards[card.suit]:
                self.not_played_cards[card.suit].remove(card.value)

    def calc_bot_hand(self):
        # get the available card suits
        available_cards = {}
        for card in self.computer_area.cards:
            if card.suit != self.not_active_cards.trump_card.suit:
                if card.suit not in available_cards:
                    available_cards[card.suit] = []
                available_cards[card.suit].append(card.value)

        return available_cards

    def lenght_of_suit_not_played(self):
        # Get the lenght of each suit
        lenght_of_suit = {}
        for suit in self.not_played_cards:
            lenght_of_suit[suit] = len(self.not_played_cards[suit])

        # sort the dict by value
        lenght_of_suit = {k: v for k, v in sorted(lenght_of_suit.items(), key=lambda item: item[1])}

        return lenght_of_suit

    def find_card(self, suit, value):
        suit_lst = self.computer_area.get_cards_with_same_suit_str(suit)
        value_lst = self.computer_area.get_cards_with_same_value_int(value)
        return suit_lst.intersection(value_lst)

    def validate_bot_hand(self, bot_hand):
        # Create a set with all the values that are in the main area
        values = set()
        for card in self.main_card_sprites_playing_area.get_all_cards():
            values.add(card.value)

        valid_bot_hand = {}

        # Remove the values that are not in the main area
        for suit in bot_hand:
            for value in bot_hand[suit]:
                if value in values:
                    if suit not in valid_bot_hand:
                        valid_bot_hand[suit] = []
                    valid_bot_hand[suit].append(value)

        return valid_bot_hand

    def compute_best_attack_move(self):
        card_to_play = None
        lenght_of_suit_not_played = self.lenght_of_suit_not_played()
        if len(self.main_card_sprites_playing_area.mat_list) == 1:
            bot_hand = self.calc_bot_hand()
            bot_hand_trump = None
            if self.not_active_cards.trump_card.suit in bot_hand:
                # Remove trump suit from the bot hand in extra dict
                bot_hand_trump = bot_hand[self.not_active_cards.trump_card.suit]
                # Remove trump suit from the bot hand
                bot_hand.pop(self.not_active_cards.trump_card.suit)

            for suit in lenght_of_suit_not_played:
                if suit in bot_hand:
                    card_to_play = min(bot_hand[suit])
                    # print the instance of the card
                    card_to_play = self.find_card(suit, card_to_play)
                    # Get the card out of the set
                    card_to_play = card_to_play
                    break

            if card_to_play is None:
                # Get the minimum value of bot_hand_trump
                card_to_play = min(bot_hand_trump)
                card_to_play = self.find_card(self.not_active_cards.trump_card.suit, card_to_play)

        else:
            hand = self.calc_bot_hand()
            valid_bot_hand = self.validate_bot_hand(hand)
            #lenght_of_suit_bot = self.lenght_of_suit_bot(valid_bot_hand)

            if self.not_active_cards.trump_card.suit in valid_bot_hand:
                # Remove trump suit from the bot hand
                valid_bot_hand.pop(self.not_active_cards.trump_card.suit)
            for suit in lenght_of_suit_not_played:
                if suit in valid_bot_hand:
                    card_to_play = min(valid_bot_hand[suit], default=None)
                    card_to_play = self.find_card(suit, card_to_play)
                    break

        if card_to_play is None or len(card_to_play) == 0:
            return None
        else:
            return card_to_play.pop()

    def compute_best_defense_move(self):
        # Filter out the unused_cards that are not playable
        bottom_card = self.main_card_sprites_playing_area.get_bottom_card()
        # Filter the computer cards with the same suit as the bottom card
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
