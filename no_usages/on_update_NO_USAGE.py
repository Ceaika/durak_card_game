# def on_update(self, delta_time: 1):
#     """ Movement and game logic """
#     # print(len(self.playground.get_mats()))
#     # print("list von cards", len(self.playground.get_cards()))
#     # self.card_list.update()
#     # if isinstance(self.held_card, Card):
#     #     if self.held_card.collides_with_list(self.playground.get_mats()):
#     #         print("Collides with main mat")
#     if self.do_animation:
#         # print(str(self.animation.get_dx()) + " " + str(self.animation.get_dy()))
#
#         self.do_animation, self.animated_card = self.animation.do_animation(self.animated_card, self.playground)
#
#     else:
#
#         if self.computer_player.is_taking:
#             self.hint_text = "Add more cards or finish turn"
#             if len(self.playground.get_cards()[-1]) == 1:
#                 self.playground.add_new_sprite()
#         elif self.human_player.is_taking:
#             self.playground.add_new_sprite()
#             if self.game_logic.make_computer_attack_move() == None:
#                 self.human_player.is_turn = False
#                 self.human_player.is_taking = False
#                 self.game_logic.finish_turn()
#
#         else:
#             pass
#         # playground_cards = self.playground.get_cards()[-1]
#         #
#         # if len(playground_cards) == 0:
#         #     if not self.human_player.is_turn:
#         #         #self.computer_text = "Computer attacked"
#         #         card = self.game_logic.make_computer_attack_move()
#         #         if card == None or len(self.computer_player.get_cards()) == 0:
#         #             self.game_logic.finish_turn()
#         #             self.human_player.is_turn = True
#         #             #self.computer_text = "Computer finished his turn"
#         #             self.show_btn = False
#         #         else:
#         #             self.animated_card = card
#         #
#         #             self.animation = Animation(self.playground.get_mats()[-1].position, card.position)
#         #             self.do_animation = True
#         #     # else:
#         #     #     self.hint_text = "Your turn!\nAttack"
#         #
#         #
#         # elif len(playground_cards) == 1:
#         #     if not self.human_player.is_turn:
#         #         #self.computer_text = "Computer defended"
#         #         card = self.game_logic.make_computer_defence_move()
#         #         if card == None:
#         #             # self.game_logic.finish_turn()
#         #             self.computer_player.is_taking = True
#         #             self.human_player.is_turn = True
#         #             #self.computer_text = "Computer is taking the cards"
#         #             if len(self.computer_player.get_cards()) == 0:
#         #                 self.game_logic.finish_player_turn()
#         #         else:
#         #             self.animated_card = card
#         #             self.animation = Animation(playground_cards[0].position, card.position)
#         #             self.do_animation = True
#         #
#         #     else:
#         #         self.hint_text = "Your turn!\nDefend or take cards"
#         #         if len(self.computer_player.get_cards()) == 0:
#         #             self.game_logic.finish_player_turn()
#         #
#         # elif len(self.playground.get_cards()[-1]) == 2:
#         #     self.playground.add_new_sprite()
#
#     if len(self.not_active_cards.get_unused_cards()) == 0 and len(self.human_player.get_cards()) == 0:
#         self.view_manager.show_win_lose_view(WIN, self.config)
#     elif len(self.not_active_cards.get_unused_cards()) == 0 and len(self.computer_player.get_cards()) == 0:
#         self.view_manager.show_win_lose_view(LOSE, self.config)
