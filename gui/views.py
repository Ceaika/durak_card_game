import arcade
import arcade.gui

from game_logic.game_logic import GameLogic
from gui.card import Card
from play_areas.computer_card_sprites_area import ComputerCardSpritesArea

from play_areas.main_card_sprites_playing_area import MainCardSpritesPlayingArea
from play_areas.not_active_cards import NotActiveCards
from play_areas.players_card_sprites_area import PlayersCardSpritesArea
from gui.screen_configuration import ScreenConfiguration
from Constants import PLAYER_AREA, COMPUTER_AREA, MAIN_AREA
from utils import Utils


class GameView(arcade.View):
    """ Main application class. """

    def __init__(self, screen_config: ScreenConfiguration):
        self.config = screen_config
        super().__init__()

        # This scales the cards and the rest of the play area according to screen size
        self.config.init_current_screen()

        # Sprite list with all the cards, no matter what area they are in.
        self.card_list = None

        arcade.set_background_color(arcade.color.AMAZON)

        # List of cards we are dragging with the mouse
        self.held_card = None

        # Original location of cards we are dragging with the mouse in case
        # they have to go back.
        self.held_card_original_position = None

        # Sprite list with all the mats that cards lay on.
        self.mat_list: arcade.SpriteList = arcade.SpriteList()

        # Flag for checking if card was moved to new area
        self.card_moved = False

        # Initialize the sprite lists
        self.main_card_sprites_playing_area = MainCardSpritesPlayingArea(self.config)
        self.players_card_sprites_area = PlayersCardSpritesArea(self.config)
        self.computer_card_sprites_area = ComputerCardSpritesArea(self.config)
        self.not_active_cards = NotActiveCards()

        # Initialize the utils so we can use helper functions
        self.utils = Utils(self.players_card_sprites_area, self.computer_card_sprites_area,
                           self.main_card_sprites_playing_area, self.not_active_cards)
        self.game_logic = GameLogic(self.players_card_sprites_area, self.computer_card_sprites_area, self.main_card_sprites_playing_area,
                                    self.not_active_cards)

        self.setup()

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # List of cards we are dragging with the mouse
        self.held_card = arcade.Sprite

        # Original location of cards we are dragging with the mouse in case
        # they have to go back.
        self.held_card_original_position = ()

        # init main playing area with one sprite
        self.main_card_sprites_playing_area.add_new_sprite()

        # Sprite list with all the cards, no matter what play area they are in.
        self.card_list = arcade.SpriteList()

        # Create every card
        for card_suit in self.config.card_suites:
            for card_value in self.config.card_values:
                card = Card(card_suit, card_value, self.config.card_scale)
                card.position = self.config.start_x, self.config.middle_y
                self.card_list.append(card)

        # Shuffle the cards
        self.card_list.shuffle()

        # Put all the cards face down in the not active area
        for card in self.card_list:
            self.not_active_cards.add_new_card(card)

        for index in range(0, 12):
            card = self.not_active_cards.remove_last_card()
            if index < 6:
                card.face_up()
                self.players_card_sprites_area.add_new_card(card)
                card.position = self.players_card_sprites_area.mat_list[index].position
                self.pull_to_top(card)
            else:
                self.computer_card_sprites_area.add_new_card(card)
                card.position = self.computer_card_sprites_area.mat_list[index - 6].position
                self.pull_to_top(card)

        # Pick the trump card
        trump_card: Card = self.not_active_cards.cards[0]
        self.not_active_cards.set_trump_card(trump_card)
        trump_card.face_up()
        trump_card.angle = 90
        trump_card.center_x = self.config.card_width * 1.2


    # def init_animation(self):
    #     # - Pull from that pile into the middle piles, all face-down
    #     # Loop for each pile
    #     for pile_no in range(0, self.players_card_sprites_area.main_count_of_sprites()):
    #         # Pop the card off the deck we are dealing from
    #         card = self.piles[BOTTOM_FACE_DOWN_PILE].pop()
    #         # Put in the proper pile
    #         self.piles[pile_no].append(card)
    #         x_mat, y_mat = self.mat_list[pile_no].position
    #         round(x_mat, 0)
    #         round(y_mat, 0)
    #         while (True):
    #             x, y = card.position
    #             if (x_mat != x):
    #                 x += 1
    #             if (y_mat != y):
    #                 y += 1
    #             if (x_mat == x and y_mat == y):
    #                 break
    #             card.position = x, y
    #             time.sleep(1)
    #         # Move card to same position as pile we just put it in
    #         card.position = self.mat_list[pile_no].position

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()

        # Draw the mats the cards go on to
        # Draw the mats for the players cards
        self.players_card_sprites_area.mat_list.draw()
        # Draw the mats for the computer cards
        self.computer_card_sprites_area.mat_list.draw()
        # Draw the mats for the main card area
        self.main_card_sprites_playing_area.mat_list.draw()

        # Draw the cards
        self.card_list.draw()

    def pull_to_top(self, card: arcade.Sprite):
        """ Pull card to top of rendering order (last to render, looks on-top) """

        # Remove, and append to the end
        self.card_list.remove(card)
        self.card_list.append(card)


    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of cards we've clicked on
        cards: list[Card] = arcade.get_sprites_at_point((x, y), self.card_list)
        print(len(self.not_active_cards.cards))

        # Have we clicked on a card?
        if len(cards) > 0:
            # Might be a stack of cards, get the top one
            self.held_card = cards[-1]


            # Figure out in which play area the card is
            area_index = self.utils.get_area_for_card(self.held_card)

            # If area_index is not 0, then it is not the players card area, so we shouldn't be able to move it
            if area_index != PLAYER_AREA:
                return

            # Get the index of the card in the list

            card_index = self.players_card_sprites_area.cards.index(self.held_card)
            # All other cases, grab the face-up card we are clicking on
            # Save the position
            self.held_card_original_position = self.held_card.position
            # Put on top in drawing order
            self.pull_to_top(self.held_card)

            self.held_card.original_card_area = area_index
            self.held_card.original_card_index = card_index

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """

        # If we don't have any cards, who cares
        if not isinstance(self.held_card, Card):
            return

        # Find the closest mat, in case we are in contact with more than one
        mat, distance = arcade.get_closest_sprite(self.held_card, self.utils.list_all_usable_mats())
        reset_position = True

        # See if we are in contact with the closest mat
        if arcade.check_for_collision(self.held_card, mat):

            # If there won't be any problems, we don't need to reset the position
            reset_position = False

            # Which play area is it?
            area_index = self.utils.get_area_for_mat(mat)
            mat_index = 0
            if area_index == PLAYER_AREA:
                mat_index = self.players_card_sprites_area.mat_list.index(mat)
                # Check if there is a card in the mat
                if len(self.players_card_sprites_area.cards) > mat_index:
                    # There is a card in the mat, so we can't put our card there
                    reset_position = True

            elif area_index == COMPUTER_AREA:
                mat_index = self.computer_card_sprites_area.mat_list.index(mat)
                # Check if there is a card in the mat
                if len(self.computer_card_sprites_area.cards) > mat_index:
                    # There is a card in the mat, so we can't put our card there
                    reset_position = True

            elif area_index == MAIN_AREA:
                mat_index = self.main_card_sprites_playing_area.mat_list.index(mat)
                # Check if index is empty
                if len(self.main_card_sprites_playing_area.cards) > mat_index:
                    if len(self.main_card_sprites_playing_area.cards[mat_index]) >= 2:
                        # There are two cards in the mat, so we can't put our card there
                        reset_position = True
                    elif len(self.main_card_sprites_playing_area.cards[mat_index]) == 1:

                        # We can put the card there
                        reset_position = self.game_logic.validate_player_defence(self.main_card_sprites_playing_area.cards[mat_index][-1], self.held_card)


            # Move cards to proper position
            self.held_card.position = mat.center_x, mat.center_y

            # Release on top play mat? And only one card held?
        if reset_position:
            # Where-ever we were dropped, it wasn't valid. Reset the card's position
            # to its original spot.
            self.held_card.position = self.held_card_original_position
        else:
            # We were dropped on a valid spot. If we were dropped on a main play  mat  TODO: This is just added, so I won't forget
            # Add the card and mat to the list
            self.utils.add_card_and_mat_to_area(area_index, mat_index, self.held_card)
            # # area, we need to check for a win.
            # if area_index == MAIN_AREA:
            #     self.check_for_win()
            # Remove the card and mat from original area and index
            hand_card: Card = self.held_card
            self.utils.remove_card_and_mat_from_area(hand_card.original_card_area, hand_card.original_card_index)

        # We are no longer holding cards
        self.held_card = None

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """

        # If we are holding cards, move them with the mouse
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

        if len(self.main_card_sprites_playing_area.cards[-1]) == 1:
            print("One card in main area")
        if len(self.main_card_sprites_playing_area.cards[-1]) == 2:
            self.main_card_sprites_playing_area.cards.append([[]])
            self.main_card_sprites_playing_area.add_new_sprite()


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


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

        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = StartButton(self.configuration)
        self.v_box.add(start_button.with_space_around(bottom=20))

        # Again, method 1. Use a child class to handle events.
        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

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
