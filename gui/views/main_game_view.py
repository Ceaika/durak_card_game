import arcade
import arcade.gui

from game_logic.game_logic import GameLogic
from gui.card import Card
from gui.screen_configuration import ScreenConfiguration
import gui.view_manager
from play_areas.main_card_sprites_playing_area import MainCardSpritesPlayingArea
from play_areas.not_active_cards import NotActiveCards
from play_areas.player_area import PlayerArea


class MainGameView(arcade.View):
    """ Main application class. """

    def __init__(self, screen_config: ScreenConfiguration, difficulty: int):
        self.config = screen_config
        super().__init__()

        # This scales the unused_cards and the rest of the play area according to screen size
        self.config.init_current_screen()

        # This is the view_manager used to switch between views
        self.view_manager = gui.view_manager.ViewManager()

        arcade.set_background_color(arcade.color.AMAZON)

        # List of unused_cards we are dragging with the mouse
        self.held_card = None

        # Original location of unused_cards we are dragging with the mouse in case
        # they have to go back.
        self.held_card_original_position = None

        # Sprite list with all the mats that unused_cards lay on.
        self.mat_list: arcade.SpriteList = arcade.SpriteList()

        # Flag for checking if card was moved to new area
        self.card_moved = False

        # Initialize the sprite lists
        self.main_card_sprites_playing_area = MainCardSpritesPlayingArea(self.config)
        self.human_player = PlayerArea(self.config.start_x_bottom, self.config.bottom_y,
                                       self.config.x_spacing)
        self.computer_player = PlayerArea(self.config.start_x_top, self.config.top_y,
                                          -self.config.x_spacing)
        self.not_active_cards = NotActiveCards(self.config)

        # Initialize the utils so we can use helper functions
        self.game_logic = GameLogic(self.human_player, self.computer_player, self.main_card_sprites_playing_area,
                                    self.not_active_cards, difficulty)
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        self.finish_move_button = arcade.gui.UIFlatButton(text="Finish move", width=200)
        self.v_box.add(self.finish_move_button.with_space_around(bottom=20))

        self.take_cards_button = arcade.gui.UIFlatButton(text="Take cards", width=200)
        self.v_box.add(self.take_cards_button.with_space_around(bottom=20))

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_y=self.config.bottom_y - self.config.card_height * 2,
                child=self.v_box)
        )
        self.hint_text = "Your turn!\nAttack!"
        self.computer_text = ""

        self.setup()

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # List of unused_cards we are dragging with the mouse
        self.held_card = arcade.Sprite

        # Original location of unused_cards we are dragging with the mouse in case
        # they have to go back.
        self.held_card_original_position = ()

        # init main playing area with one sprite
        self.main_card_sprites_playing_area.add_new_sprite()

        # Create every card
        for card_suit in self.config.card_suites:
            for card_value in self.config.card_values:
                card = Card(card_suit, card_value, self.config.card_scale)
                card.position = self.config.start_x, self.config.middle_y
                self.not_active_cards.add_new_card(card)

        # Shuffle the unused_cards
        self.not_active_cards.unused_cards.shuffle()

        for index in range(0, 12):
            card = self.not_active_cards.remove_last_card()
            if index < 6:
                card.face_up()
                self.human_player.add_new_card(card)
            else:
                self.computer_player.add_new_card(card)

        # Pick the trump card
        trump_card: Card = self.not_active_cards.unused_cards[0]
        self.not_active_cards.set_trump_card(trump_card)
        trump_card.face_up()
        trump_card.angle = 90
        trump_card.center_x = self.config.card_width * 1.2
        self.finish_move_button.on_click = self.finish_move
        self.take_cards_button.on_click = self.take_cards

    def finish_move(self, event):
        if len(self.main_card_sprites_playing_area.cards[-1]) == 0:
            self.finish_turn()

    def finish_turn(self):
        if self.computer_player.is_taking:
            self.game_logic.computer_take_cards()
            self.computer_player.is_taking = False
            self.human_player.is_turn = True
        elif self.human_player.is_turn:
            self.human_player.is_turn = False

        self.game_logic.finish_turn()

    def take_cards(self, event):
        if self.human_player.is_turn and len(self.main_card_sprites_playing_area.cards[-1]) == 1:
            self.game_logic.take_all_cards_human()
            self.human_player.is_turn = False
            self.human_player.is_taking = True

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()
        # Draw v_box with buttons
        self.manager.draw()

        # Draw the mats for the main card area
        self.main_card_sprites_playing_area.mat_list.draw()

        # if any cards placed in the playground draw them
        if len(self.main_card_sprites_playing_area.cards) != 0:
            self.main_card_sprites_playing_area.get_all_cards().draw()

        # draw not active cards
        self.not_active_cards.unused_cards.draw()
        self.not_active_cards.played_cards.draw()
        # draw player cards
        self.human_player.cards.draw()
        # draw computer cards
        self.computer_player.cards.draw()
        # draw the label
        arcade.draw_text(self.hint_text, self.config.start_x, self.config.bottom_y + self.config.card_height,
                         arcade.color.BLACK, 24)
        arcade.draw_text(self.computer_text, self.config.start_x, self.config.top_y - (self.config.card_height * 1.5),
                         arcade.color.BLACK, 24)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of unused_cards we've clicked on
        cards: list[Card] = arcade.get_sprites_at_point((x, y), self.human_player.cards)

        # Have we clicked on a card?
        if len(cards) > 0:
            # Might be a stack of unused_cards, get the top one
            self.held_card = cards[-1]

            card_index = self.human_player.find_card(self.held_card)

            # Check if card is in human player area
            if card_index is None:
                self.held_card = None
                return

            # Get the index of the card in the list

            self.held_card_original_position = self.held_card.position
            # Put on top in drawing order
            # self.pull_to_top(self.held_card)

            self.held_card.original_card_index = card_index

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """

        # If we don't have any unused_cards, who cares
        if not isinstance(self.held_card, Card):
            return

        # Find the closest mat, in case we are in contact with more than one
        mat, distance = arcade.get_closest_sprite(self.held_card, self.main_card_sprites_playing_area.mat_list)
        reset_position = True

        # See if we are in contact with the closest mat
        if arcade.check_for_collision(self.held_card, mat):

            # If there won't be any problems, we don't need to reset the position
            reset_position = False

            # Check if the card can be placed on the mat
            mat_index = self.main_card_sprites_playing_area.mat_list.index(mat)
            # Check if index is empty
            if len(self.main_card_sprites_playing_area.cards) > mat_index:
                if len(self.main_card_sprites_playing_area.cards[mat_index]) >= 2:
                    # There are two unused_cards in the mat, so we can't put our card there
                    reset_position = True
                elif len(self.main_card_sprites_playing_area.cards[mat_index]) == 1:
                    # There is one card in the mat, so we need to check if the new card can be put there
                    reset_position = not self.game_logic.validate_player_defence(
                        self.main_card_sprites_playing_area.cards[mat_index][-1], self.held_card)
                elif len(self.main_card_sprites_playing_area.cards[mat_index]) == 0:
                    # There are no unused_cards in the mat, so we need to check if the new card can be put there
                    reset_position = not self.game_logic.validate_player_attack(self.held_card)

            # Move unused_cards to proper position
            self.held_card.position = mat.center_x, mat.center_y

            # Release on top play mat? And only one card held?
        if reset_position:
            # Where-ever we were dropped, it wasn't valid. Reset the card's position
            # to its original spot.
            self.held_card.position = self.held_card_original_position
        else:
            # Add the card and mat to the main unused_cards list
            self.main_card_sprites_playing_area.add_new_card(self.held_card)

            # remove card from human player
            self.human_player.remove_card(self.human_player.find_card(self.held_card))
            self.human_player.is_turn = False

        # We are no longer holding unused_cards
        self.held_card = None

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """

        # If we are holding unused_cards, move them with the mouse
        if isinstance(self.held_card, Card):
            self.held_card.center_x += dx
            self.held_card.center_y += dy

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.view_manager.show_menu_view()
        if symbol == arcade.key.ENTER:
            pass
            # self.init_Animation()

    def on_update(self, delta_time: 1):
        """ Movement and game logic """
        # self.card_list.update()
        # if isinstance(self.held_card, Card):
        #     if self.held_card.collides_with_list(self.main_card_sprites_playing_area.mat_list):
        #         print("Collides with main mat")
        if self.computer_player.is_taking:
            self.hint_text = "Add more cards or finish turn"
            if len(self.main_card_sprites_playing_area.cards[-1]) == 1:
                self.main_card_sprites_playing_area.cards.append([])
                self.main_card_sprites_playing_area.add_new_sprite()
        elif self.human_player.is_taking:
            self.main_card_sprites_playing_area.cards.append([])
            self.main_card_sprites_playing_area.add_new_sprite()
            if not self.game_logic.make_computer_attack_move():
                self.human_player.is_turn = False
                self.human_player.is_taking = False
                self.game_logic.finish_turn()

        else:
            if len(self.main_card_sprites_playing_area.cards[-1]) == 0:
                if not self.human_player.is_turn:
                    self.computer_text = "Computer attacked"
                    if not self.game_logic.make_computer_attack_move() or len(self.human_player.cards) == 0:
                        self.game_logic.finish_turn()
                        self.human_player.is_turn = True
                        self.computer_text = "Computer finished his turn"
                else:
                    self.hint_text = "Your turn!\nAttack or finish move"

            elif len(self.main_card_sprites_playing_area.cards[-1]) == 1:
                if not self.human_player.is_turn:
                    self.computer_text = "Computer defended"
                    if not self.game_logic.make_computer_defence_move():
                        # self.game_logic.finish_turn()
                        self.computer_player.is_taking = True
                        self.human_player.is_turn = True
                        self.computer_text = "Computer is taking the cards"
                else:
                    self.hint_text = "Your turn!\nDefend or take cards"
                    if len(self.computer_player.cards) == 0:
                        self.finish_turn()

            elif len(self.main_card_sprites_playing_area.cards[-1]) == 2:
                self.main_card_sprites_playing_area.cards.append([])
                self.main_card_sprites_playing_area.add_new_sprite()

        # if self.human_player.is_taking:
        #     pass
        # if self.computer_player.is_taking:
        #     pass

        if len(self.not_active_cards.unused_cards) == 0 and len(self.human_player.cards) == 0:
            self.view_manager.show_win_view()
        elif len(self.not_active_cards.unused_cards) == 0 and len(self.computer_player.cards) == 0:
            self.view_manager.show_lose_view()