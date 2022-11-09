import webbrowser

import arcade
import arcade.gui

from game_logic.game_logic import GameLogic
from gui.card import Card

from play_areas.main_card_sprites_playing_area import MainCardSpritesPlayingArea
from play_areas.not_active_cards import NotActiveCards
from play_areas.player_area import PlayerArea
from gui.screen_configuration import ScreenConfiguration


class GameView(arcade.View):
    """ Main application class. """

    def __init__(self, screen_config: ScreenConfiguration):
        self.config = screen_config
        super().__init__()

        # This scales the unused_cards and the rest of the play area according to screen size
        self.config.init_current_screen()

        # Sprite list with all the unused_cards, no matter what area they are in.
        self.card_list = None

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

        self.game_logic = GameLogic(self.human_player, self.computer_player, self.main_card_sprites_playing_area,
                                    self.not_active_cards)
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
                anchor_x="right",
                anchor_y="bottom",
                child=self.v_box)
        )

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

        # Sprite list with all the unused_cards, no matter what play area they are in.
        self.card_list = arcade.SpriteList()

        # Create every card
        for card_suit in self.config.card_suites:
            for card_value in self.config.card_values:
                card = Card(card_suit, card_value, self.config.card_scale)
                card.position = self.config.start_x, self.config.middle_y
                self.card_list.append(card)

        # Shuffle the unused_cards
        self.card_list.shuffle()

        # Put all the unused_cards face down in the not active area
        for card in self.card_list:
            self.not_active_cards.add_new_card(card)

        for index in range(0, 12):
            card = self.not_active_cards.remove_last_card()
            if index < 6:
                card.face_up()
                self.human_player.add_new_card(card)
                self.pull_to_top(card)
            else:
                self.computer_player.add_new_card(card)
                self.pull_to_top(card)

        # Pick the trump card
        trump_card: Card = self.not_active_cards.unused_cards[0]
        self.not_active_cards.set_trump_card(trump_card)
        trump_card.face_up()
        trump_card.angle = 90
        trump_card.center_x = self.config.card_width * 1.2
        self.finish_move_button.on_click = self.finish_move
        self.take_cards_button.on_click = self.take_cards

    def finish_move(self, event):
        if self.human_player.is_turn:
            self.game_logic.finish_turn()
            self.human_player.is_turn = False


    def take_cards(self, event):
        if self.human_player.is_turn:
            self.game_logic.take_all_cards()
            self.human_player.is_turn = False
            self.game_logic.finish_turn()

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()
        # Draw the mats for the main card area
        self.main_card_sprites_playing_area.mat_list.draw()

        # Draw the unused_cards
        self.card_list.draw()
        self.manager.draw()

    def pull_to_top(self, card: arcade.Sprite):
        """ Pull card to top of rendering order (last to render, looks on-top) """

        # Remove, and append to the end
        self.card_list.remove(card)
        self.card_list.append(card)


    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of unused_cards we've clicked on
        cards: list[Card] = arcade.get_sprites_at_point((x, y), self.card_list)

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
            self.pull_to_top(self.held_card)

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
                    reset_position = not self.game_logic.validate_player_defence(self.main_card_sprites_playing_area.cards[mat_index][-1], self.held_card)
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
            arcade.close_window()
        if symbol == arcade.key.ENTER:
            pass
            # self.init_Animation()

    def on_update(self, delta_time: float):
        """ Movement and game logic """
        # self.card_list.update()
        # if isinstance(self.held_card, Card):
        #     if self.held_card.collides_with_list(self.main_card_sprites_playing_area.mat_list):
        #         print("Collides with main mat")
        if len(self.main_card_sprites_playing_area.cards[-1]) == 0:
            if not self.human_player.is_turn:
                if not self.game_logic.make_computer_attack_move():
                    self.game_logic.finish_turn()
                    self.human_player.is_turn = True

        if len(self.main_card_sprites_playing_area.cards[-1]) == 1:
            if not self.human_player.is_turn:
                if not self.game_logic.make_computer_defence_move():
                    self.game_logic.finish_turn()
                    self.human_player.is_turn = True


        if len(self.main_card_sprites_playing_area.cards[-1]) == 2:
            self.main_card_sprites_playing_area.cards.append([])
            self.main_card_sprites_playing_area.add_new_sprite()


class QuitButton(arcade.gui.UIFlatButton):
    def __init__(self):
        super(QuitButton, self).__init__(text="Quit Game", width=200)
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class RulesButton(arcade.gui.UIFlatButton):
    def __init__(self):
        super(RulesButton, self).__init__(text="Rules", width=200)

    def on_click(self, event: arcade.gui.UIOnClickEvent):
        webbrowser.open('https://de.wikipedia.org/wiki/Durak_(Kartenspiel)', 2, True)
class StartButton(arcade.gui.UIFlatButton):
    def __init__(self, screen_config: ScreenConfiguration):
        super(StartButton, self).__init__(text="Start Game", width=200)
        self.config = screen_config

    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.get_window().show_view(GameView(self.config))


class MenuView(arcade.View):
    def __init__(self, screen_config: ScreenConfiguration):
        super().__init__()
        self.configuration = screen_config
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.rgb = [125, 1, 1]
        self.multilikator = 1
        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = StartButton(self.configuration)
        self.v_box.add(start_button.with_space_around(bottom=20))

        rules_button = RulesButton()
        self.v_box.add(rules_button.with_space_around(bottom=20))

        # Again, method 1. Use a child class to handle events.
        quit_button = QuitButton()
        self.v_box.add(quit_button)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_update(self, delta_time:0.25):
        #self.rgb[0] += self.multilikator*1
        self.rgb[1] += self.multilikator*2
        self.rgb[2] += self.multilikator*4
        for f in self.rgb[1:]:
            if f > 255:
                self.multilikator = -1
            elif f < 0:
                self.multilikator = 1

        arcade.set_background_color(self.rgb)
    def on_draw(self):
        self.clear()
        self.manager.draw()


def main():
    """ Main function """
    config = ScreenConfiguration()
    window = arcade.Window(config.width, config.height, config.screen_title, fullscreen=True)
    menu_view = MenuView(config)
    window.show_view(menu_view)
    arcade.run()


if __name__ == '__main__':
    main()
