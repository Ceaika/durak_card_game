import arcade

from play_areas.computer_card_sprites_area import ComputerCardSpritesArea
from play_areas.main_card_sprites_playing_area import MainCardSpritesPlayingArea
from play_areas.players_card_sprites_area import PlayersCardSpritesArea


class Utils:

    def __init__(self, player: PlayersCardSpritesArea, computer: ComputerCardSpritesArea,
                 main: MainCardSpritesPlayingArea):
        self.player = player
        self.computer = computer
        self.main = main

    def list_all_mats(self):
        # add all the mats to a list
        all_mats = arcade.SpriteList()
        all_mats.extend(self.player.mat_list)
        all_mats.extend(self.computer.mat_list)
        all_mats.extend(self.main.mat_list)
        return all_mats

    def list_all_usable_mats(self):
        # add all the mats to a list
        all_mats = arcade.SpriteList()
        all_mats.extend(self.player.mat_list)
        all_mats.extend(self.main.mat_list)
        return all_mats

    def list_all_mat_areas(self):
        all_areas = [self.player.mat_list, self.computer.mat_list, self.main.mat_list]
        return all_areas

    def list_all_active_cards(self):
        all_cards = [self.player.cards, self.computer.cards, self.main.cards]
        return all_cards
