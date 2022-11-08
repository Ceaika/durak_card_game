from game_logic.strategies.simple_strategy import SimpleStrategy
from game_logic.strategies.strategycontext import StrategyContext
from play_areas.main_card_sprites_playing_area import MainCardSpritesPlayingArea
from play_areas.not_active_cards import NotActiveCards
from play_areas.player_area import PlayerArea

class GameLogic:
    def __init__(self, player: PlayerArea, computer: PlayerArea,
                 main: MainCardSpritesPlayingArea, not_active_cards: NotActiveCards):
        self.player = player
        self.computer = computer
        self.main = main
        self.not_active_cards = not_active_cards
        self.strategy = SimpleStrategy(computer, main, not_active_cards)
        self.strategy_context = StrategyContext(self.strategy, self.main, self.computer)

    def validate_player_defence(self, bottom_card, top_card):
        return self.strategy_context.validate_defence_move(bottom_card, top_card)

    def gameplay(self):
        self.strategy_context.make_computer_move()

    def validate_player_attack(self, held_card):
        return self.strategy_context.validate_attack_move(held_card)

    def finish_turn(self):
        # First we take unused unused_cards from the not active unused_cards and add them to the computer and player area
        for i in range(6):
            if len(self.player.cards) < 6:
                card = self.not_active_cards.remove_last_card()
                card.face_up()
                self.player.add_new_card(card)

        # We must also remove all cards from the main area
        lst = self.main.get_and_remove_all_cards()
        # Now add them to the used cards
        for card in lst:
            print(card)
            self.not_active_cards.add_played_card(card)

