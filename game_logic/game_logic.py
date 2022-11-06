from game_logic.strategies.strategycontext import StrategyContext
from play_areas.computer_card_sprites_area import ComputerCardSpritesArea
from play_areas.main_card_sprites_playing_area import MainCardSpritesPlayingArea
from play_areas.players_card_sprites_area import PlayersCardSpritesArea

class GameLogic:
    def __init__(self, player: PlayersCardSpritesArea, computer: ComputerCardSpritesArea,
                 main: MainCardSpritesPlayingArea):
        self.player = player
        self.computer = computer
        self.main = main
        self.trump_card = None
        self.strategy = StrategyContext()

    def set_trump_card(self, card):
        self.trump_card = card

    def validate_defence(self, bottom_card, top_card):
        if bottom_card.suit == top_card.suit:
            if top_card.value > bottom_card.value:
                return True
        elif top_card.suit == self.trump_card.suit and bottom_card.suit != self.trump_card.suit:
            return True
        return False


