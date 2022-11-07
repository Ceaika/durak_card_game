import math
from time import sleep

import arcade
import arcade.gui


from gui.card import Card
from play_areas.Player import Player

from play_areas.main_card_sprites_playing_area import MainCardSpritesPlayingArea
from play_areas.not_active_cards import NotActiveCards
from gui.screen_configuration import ScreenConfiguration
from Constants import PLAYER_AREA, COMPUTER_AREA, MAIN_AREA, INIT_CARDS
from utils import Utils


class GameView(arcade.View):
    """ Main application class. """

    def __init__(self, screen_config: ScreenConfiguration):
        self.config = screen_config
        super().__init__()

        print("START")
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

        # Initialize the sprite lists
        self.main_card_sprites_playing_area = MainCardSpritesPlayingArea(self.config)
        self.player = Player(self.config.start_x_bottom, self.config.bottom_y, self.config.x_spacing)
        self.bot = Player(self.config.start_x_top, self.config.top_y, -(self.config.x_spacing))
        self.not_active_cards = NotActiveCards()

        # Initialize the utils so we can use helper functions
        self.utils = Utils(self.player, self.bot,
                           self.main_card_sprites_playing_area,self.config)

        self.setup()

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # init main playing area with one sprite
        self.main_card_sprites_playing_area.add_new_sprite()

        # Sprite list with all the cards, no matter what play area they are in.
        self.card_list = arcade.SpriteList()

        # Create every card
        for card_suit in self.config.card_suites:
            for card_value in self.config.card_values:
                card = Card(card_suit, card_value, self.config.card_scale)
                card.position = self.config.start_x_bottom, self.config.middle_y
                self.card_list.append(card)

        # Shuffle the cards
        self.card_list.shuffle()

        # Put all the cards face down in the not active area
        for card in self.card_list:
            self.not_active_cards.add_new_card(card)

        for index in range(0, 2*INIT_CARDS):
            card = self.not_active_cards.remove_last_card()
            if index % 2 == 0:
                card.position = self.player.get_x_y()
                self.player.add_card(card)
            else:
                card.position = self.bot.get_x_y()
                self.bot.add_card(card)


    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()

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
        cards = arcade.get_sprites_at_point((x, y), self.card_list)

        # Have we clicked on a card?
        if len(cards) > 0:
            # Might be a stack of cards, get the top one
            primary_card = cards[-1]

            # Figure out in which play area the card is
            area_index = self.utils.get_area_for_card(primary_card)

            # If area_index is not 0, then it is not the players card area, so we shouldn't be able to move it
            if area_index != PLAYER_AREA:
                return

            # Get the index of the card in the list
            card_index = self.player.cards.index(primary_card)

            # All other cases, grab the face-up card we are clicking on
            self.held_card = primary_card
            # Save the position
            self.held_card_original_position = self.held_card.position
            # Put on top in drawing order
            self.pull_to_top(self.held_card)

            if primary_card.is_face_down:
                # Is the card face down? In one of those middle 7 piles? Then flip up
                primary_card.face_up()


    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """

        # If we don't have any cards, who cares
        if self.held_card is None:
            return

        # Find the closest mat, in case we are in contact with more than one
        mat, distance = arcade.get_closest_sprite(self.held_card, self.utils.list_all_usable_mats())
        reset_position = True

        # See if we are in contact with the closest mat
        if arcade.check_for_collision(self.held_card, mat):

            mat_index = self.main_card_sprites_playing_area.mat_list.index(mat)

            dropped_card = self.held_card

            dy = 0
            count = self.main_card_sprites_playing_area.get_count_of_cards_on_pile(mat_index)
            if count < 2:
                if count == 0:
                    dy = 0
                elif count == 1:
                    dy = self.config.card_vertical_offset

                dropped_card.position = mat.center_x, mat.center_y - dy

                # Add the new card to the pile
                self.main_card_sprites_playing_area.add_new_card(dropped_card, mat_index)

                # Remove dropped card from players lists
                self.player.remove_card(dropped_card)

                # Success, don't reset position of cards
                reset_position = False
            else:
                self.main_card_sprites_playing_area.check_count()
        # Release on top play mat? And only one card held?
        if reset_position:
            # Where-ever we were dropped, it wasn't valid. Reset the card's position
            # to its original spot.
            self.held_card.position = self.held_card_original_position

        # We are no longer holding cards
        self.held_card = None





    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        # If we are holding cards, move them with the mouse
        if self.held_card is not None:
            self.held_card.center_x += dx
            self.held_card.center_y += dy


    def draw_a_card_from_stack(self,player,area_index):
        #player.add_next_x_position()
        card = self.not_active_cards.remove_last_card()
        card.position = player.get_x_y()
        player.add_card(card)



    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
        if symbol == arcade.key.ENTER:
            self.draw_a_card_from_stack(self.player,PLAYER_AREA)
            self.draw_a_card_from_stack(self.bot, PLAYER_AREA)


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
