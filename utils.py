import arcade

from Constants import PLAYER_AREA, COMPUTER_AREA, MAIN_AREA
from gui.screen_configuration import ScreenConfiguration
from play_areas.main_card_sprites_playing_area import MainCardSpritesPlayingArea
from play_areas.Player import Player

class Utils:

    def __init__(self, player: Player, computer: Player,
                 main: MainCardSpritesPlayingArea, screen_configuration: ScreenConfiguration):
        self.player = player
        self.computer = computer
        self.main = main
        self.config = screen_configuration

    def list_all_mats(self):
        # add all the mats to a list
        all_mats = arcade.SpriteList()
        all_mats.extend(self.player.mat_list)
        all_mats.extend(self.computer.mat_list)
        all_mats.extend(self.main.mat_list)
        return all_mats

    def list_all_usable_mats(self):
        return self.main.mat_list

    # def list_all_mat_areas(self):
    #     all_areas = [self.main.mat_list]
    #     return all_areas

    def list_all_active_cards(self):
        all_cards = [self.player.cards, self.computer.cards, self.main.cards]
        return all_cards

    def get_area_for_card(self, card):
        """ What area is this card in? """
        for index, area in enumerate(self.list_all_active_cards()):
            if card in area:
                return index

    # def get_area_for_mat(self, mat):
    #     """ What area is this mat in? """
    #     if mat in self.main.mat_list:
    #         return self.main.mat_list.index(mat)

    # def remove_card_and_mat_from_area(self, area_index, card_index):
    #     """ Remove card and mat from whatever area it was in. """
    #     if area_index == PLAYER_AREA:
    #         self.player.remove_card_and_mat(card_index)
    #     elif area_index == COMPUTER_AREA:
    #         self.computer.remove_card_and_mat(card_index)
    #     elif area_index == MAIN_AREA:
    #         self.main.remove_card_and_mat(card_index)
    #
    # def remove_mat_from_area(self, area_index, card_index):
    #     if area_index == PLAYER_AREA:
    #         self.player.remove_mat(card_index)
    #     elif area_index == COMPUTER_AREA:
    #         self.computer.remove_mat(card_index)
    #     elif area_index == MAIN_AREA:
    #         self.main.remove_mat(card_index)
    # def add_card_and_mat_to_area(self, area_index, mat_index, card):
    #     """ Add card and mat to whatever area it was in. """
    #     if area_index == PLAYER_AREA:
    #         self.player.add_card_and_mat(mat_index, card)
    #     elif area_index == COMPUTER_AREA:
    #         self.computer.add_card_and_mat(mat_index, card)
    #     elif area_index == MAIN_AREA:
    #         self.main.add_card_and_mat(mat_index, card)
    def making_a_move(self,player,dropped_card,mat,mat_index,reset_position):
        dy = 0
        count = self.main.get_count_of_cards_on_pile(mat_index)
        if count < 2:
            if count == 0:
                dy = 0
            elif count == 1:
                dy = self.config.card_vertical_offset

            dropped_card.position = mat.center_x, mat.center_y - dy

            # Add the new card to the pile
            self.main.add_new_card(dropped_card, mat_index)

            # Remove dropped card from players lists
            player.remove_card(dropped_card)

            # Success, don't reset position of cards
            reset_position = False