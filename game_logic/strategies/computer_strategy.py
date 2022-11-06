from abc import ABC, abstractmethod

from game_logic.game_logic import GameLogic
from play_areas.computer_card_sprites_area import ComputerCardSpritesArea
from play_areas.main_card_sprites_playing_area import MainCardSpritesPlayingArea


class Strategy(ABC):

    def __init__(self, computer_card_sprites_area: ComputerCardSpritesArea, main_card_sprites_playing_area: MainCardSpritesPlayingArea,
                 game_logic: GameLogic):
        super().__init__()
        self.computer_card_sprites_area = computer_card_sprites_area
        self.main_card_sprites_playing_area = main_card_sprites_playing_area
        self.game_logic = game_logic

    @abstractmethod
    def compute_best_attack_move(self):
        pass

    @abstractmethod
    def compute_best_defense_move(self):
        pass
