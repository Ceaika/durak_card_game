import arcade

from Constants import PLAYER_AREA, COMPUTER_AREA, MAIN_AREA
from play_areas.computer_card_sprites_area import ComputerCardSpritesArea
from play_areas.main_card_sprites_playing_area import MainCardSpritesPlayingArea
from play_areas.not_active_cards import NotActiveCards
from play_areas.player_area import PlayerArea
from play_areas.players_card_sprites_area import PlayersCardSpritesArea


class Utils:

    def __init__(self, player: PlayerArea, computer: PlayerArea,
                 main: MainCardSpritesPlayingArea, not_active_cards: NotActiveCards):
        self.player = player
        self.computer = computer
        self.main = main
        self.not_active = not_active_cards

    def list_all_cards(self):
        all_cards = [self.player.cards, self.computer.cards, self.main.cards, self.not_active.cards]
        return all_cards

    def get_area_for_card(self, card):
        """ What area is this card in? """
        for index, area in enumerate(self.list_all_cards()):
            if card in area:
                return index

    def remove_card_and_mat_from_area(self, area_index, card_index):
        """ Remove card and mat from whatever area it was in. """
        if area_index == PLAYER_AREA:
            self.player.remove_card_and_mat(card_index)
        elif area_index == COMPUTER_AREA:
            self.computer.remove_card_and_mat(card_index)
        elif area_index == MAIN_AREA:
            self.main.remove_card_and_mat(card_index)

    def add_card_and_mat_to_area(self, area_index, mat_index, card):
        """ Add card and mat to whatever area it was in. """
        if area_index == PLAYER_AREA:
            self.player.add_card_and_mat(mat_index, card)
        elif area_index == COMPUTER_AREA:
            self.computer.add_card_and_mat(mat_index, card)
        elif area_index == MAIN_AREA:
            self.main.add_card_and_mat(mat_index, card)

    # reset the card positions on invalid move

