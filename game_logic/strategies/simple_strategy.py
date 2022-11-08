from game_logic.strategies.computer_strategy import Strategy


class SimpleStrategy(Strategy):
    def compute_best_attack_move(self):
        card_to_play = None
        if self.main_card_sprites_playing_area.cards[0].is_empty():
            card_to_play = min(self.computer_area.cards, key=lambda card: card.value)
        else:
            # Get all the cards from the main area
            cards = self.main_card_sprites_playing_area.get_all_cards()
            # empty set of playable cards
            playable_cards = set()
            # Get the cards with the same value
            for card in cards:
                playable_cards.update(self.computer_area.get_cards_with_same_value(card))
                # Filter out the cards with the same suit as the trump card
                playable_cards = {card for card in playable_cards if card.suit != self.not_active_cards.trump_card.suit}
                # Get the card with the lowest value
                card_to_play = min(playable_cards, key=lambda card: card.value)

        return card_to_play

    def compute_best_defense_move(self):
        # Filter out the cards that are not playable
        bottom_card = self.main_card_sprites_playing_area.get_bottom_card()
        # Filter the cards with the same suit
        cards_with_same_suit = self.computer_area.get_cards_with_same_suit(bottom_card)
        # Get the card with the lowest value that is higher than the bottom card from cards_with_same_suit
        card_to_play = min(cards_with_same_suit, key=lambda card: card.value)

        if card_to_play is not None and bottom_card.suit != self.not_active_cards.trump_card.suit:
            trump_cards = self.computer_area.get_cards_with_same_suit(self.not_active_cards.trump_card)
            if len(trump_cards) > 0:
                card_to_play = min(trump_cards, key=lambda card: card.value)

        return card_to_play
