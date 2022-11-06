from game_logic.game_logic import GameLogic
from game_logic.strategies.computer_strategy import Strategy


class StrategyContext:
    def __init__(self, strategy: Strategy, game_logic: GameLogic, main_card_sprites_playing_area, computer_card_sprites_area) -> None:
        self.main_card_sprites_playing_area = main_card_sprites_playing_area
        self.computer_card_sprites_area = computer_card_sprites_area
        self.__strategy = strategy
        self.is_turn = False
        self.is_attack = False
        self.game_logic = game_logic

    @property
    def strategy(self) -> Strategy:
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self.__strategy = strategy

    def make_move(self):
        card_to_play = self.pick_card()
        # Get the mat that corresponds to the card
        mat = self.computer_card_sprites_area.get_mat_for_card(card_to_play)
        # Get the index of the card and the mat
        card_index = self.computer_card_sprites_area.cards.index(card_to_play)
        mat_index = self.computer_card_sprites_area.mat_list.index(mat)
        # Remove the card and mat from the computer area
        self.computer_card_sprites_area.remove_card_and_mat(card_index)
        # Add the card and mat to the main area
        self.main_card_sprites_playing_area.add_card_and_mat(mat_index, card_to_play)


    def pick_card(self):
        if self.is_attack:
            return self.strategy.compute_best_attack_move()
        else:
            return self.strategy.compute_best_defense_move()
