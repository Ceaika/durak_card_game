class GameLogic:
    def validate_defence(self, bottom_card, top_card):
        if bottom_card.suit == top_card.suit:
            if top_card.value > bottom_card.value:
                return True
        return False
