from abc import ABC, abstractmethod

from gui.card import Card
from play_areas.computer_card_sprites_area import ComputerCardSpritesArea
from play_areas.main_card_sprites_playing_area import MainCardSpritesPlayingArea
from play_areas.not_active_cards import NotActiveCards


class Strategy(ABC):

    def __init__(self, computer_card_sprites_area: ComputerCardSpritesArea, main_card_sprites_playing_area: MainCardSpritesPlayingArea,
                 not_active_cards: NotActiveCards):
        super().__init__()
        self.computer_card_sprites_area = computer_card_sprites_area
        self.main_card_sprites_playing_area = main_card_sprites_playing_area
        self.not_active_cards = not_active_cards

    @abstractmethod
    def compute_best_attack_move(self):
        pass

    @abstractmethod
    def compute_best_defense_move(self):
        pass

    def validate_defence_move(self, bottom_card, top_card):
        if bottom_card.suit == top_card.suit:
            if top_card.value > bottom_card.value:
                return True
        elif top_card.suit == self.not_active_cards.trump_card.suit and bottom_card.suit != self.not_active_cards.trump_card.suit:
            return True
        return False

    def validate_attack_move(self, top_card):
        if self.main_card_sprites_playing_area.cards[0].is_empty() and isinstance(top_card, Card):
            return True
        else:
            # Get all the cards from the main area
            cards = self.main_card_sprites_playing_area.get_all_cards()
            # empty set of playable cards
            playable_cards = set()
            # Get the cards with the same value
            for card in cards:
                playable_cards.update(self.computer_card_sprites_area.get_cards_with_same_value(card))
                # Filter out the cards with the same suit as the trump card
                playable_cards = {card for card in playable_cards if card.suit != self.not_active_cards.trump_card.suit}
            if top_card in playable_cards:
                return True
        return False

