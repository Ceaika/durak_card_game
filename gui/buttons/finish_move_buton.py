import arcade.gui


class FinishMoveButton(arcade.gui.UIFlatButton):

    def __init__(self, playground, game_logic, human, computer):
        super(FinishMoveButton, self).__init__(text="Finish", width=200)
        self.playground = playground
        self.game_logic = game_logic
        self.human = human
        self.computer = computer

    def on_click(self, event):

        if len(self.playground.get_cards()[-1]) == 0:
            self.finish_turn()

    def finish_turn(self):

        if self.computer.is_taking:
            self.game_logic.computer_take_cards()
            self.computer.is_taking = False
            self.human.is_turn = True
        elif self.human.is_turn:
            self.human.is_turn = False

        self.game_logic.finish_turn()
