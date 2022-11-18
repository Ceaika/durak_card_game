from game_logic.strategies.computer_strategy import Strategy


class AdvancedStrategy(Strategy):
    def compute_best_defense_move(self):
        pass

    def compute_best_attack_move(self):

        # possible strategy
        # 1. select the suit based on the number of cards already played in that suit or
        # the number of cards in the hand. Each suit contains 9 possible cards in total.
        # e.g. 2 Spades in the hand, 3 Spades already played, 4 Spades in the deck left.
        #      3 Diamonds in the hand, 3 Diamonds already played, 3 Diamonds in the deck left.
        #    --> Diamonds is the best suit to play


        pass
        # card_to_play = None
        # if len(self.main_card_sprites_playing_area.mat_list) == 1:
        #     print("First move")
        #     card_to_play = min(self.computer_area.cards, key=lambda card: card.value)
        # else:
        #     # Get all the unused_cards from the main area
        #     cards = self.main_card_sprites_playing_area.get_all_cards()
        #     # empty set of playable unused_cards
        #     playable_cards = set()
        #     # Get the unused_cards with the same value
        #     for card in cards:
        #         playable_cards.update(self.computer_area.get_cards_with_same_value(card))
        #         # Filter out the unused_cards with the same suit as the trump card
        #         playable_cards = {card for card in playable_cards if card.suit != self.not_active_cards.trump_card.suit}
        #         # Get the card with the lowest value
        #         card_to_play = min(playable_cards, key=lambda card: card.value, default=None)
        #
        # return card_to_play
