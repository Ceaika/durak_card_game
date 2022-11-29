from game_logic.strategies.computer_strategy import Strategy


class StrategyContext:
    def __init__(self, strategy: Strategy, main_card_sprites_playing_area, computer_card_sprites_area) -> None:
        self.main_card_sprites_playing_area = main_card_sprites_playing_area
        self.computer_card_sprites_area = computer_card_sprites_area
        self.__strategy = strategy
        self.is_turn = False
        self.is_attack = False

    @property
    def strategy(self) -> Strategy:
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self.__strategy = strategy

    def make_computer_move(self, is_attack):
        card_to_play = self.pick_card(is_attack)
        if card_to_play is not None:
            card_to_play.face_up()
            # Add the card and mat to the main area
            #self.main_card_sprites_playing_area.add_new_card(card_to_play)
            # Remove the card and mat from the computer area
            self.computer_card_sprites_area.remove_card(card_to_play)
            return card_to_play
        elif card_to_play is None:
            # # Take the unused_cards from the main area
            # cards = self.take_cards_from_main_area()
            # # Add the unused_cards to the computer area
            # for card in cards:
            #     card.face_down()
            #     self.computer_card_sprites_area.add_new_card(card)
            return None





    def pick_card(self, is_attack):
        if is_attack:
            return self.strategy.compute_best_attack_move()
        else:
            return self.strategy.compute_best_defense_move()

    def validate_defence_move(self, bottom_card, top_card):
        return self.strategy.validate_defence_move(bottom_card, top_card)

    def validate_attack_move(self, card):
        return self.strategy.validate_attack_move(card)

    def take_cards_from_main_area(self):
        return self.main_card_sprites_playing_area.get_and_remove_all_cards()


