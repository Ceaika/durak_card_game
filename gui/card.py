import math
import os

import arcade


class Card(arcade.Sprite):
    """ Card sprite """

    def __init__(self, suit, value, scale=1):
        """ Card constructor """

        # Attributes for suit and value
        self.suit = suit
        self.value = value
        self.original_card_area = None
        self.original_card_index = None
        self.current_card_area = None
        self.current_card_index = None

        # get current working directory
        cwd = os.getcwd()

        # get the path to the images folder
        images_path = os.path.join(cwd, "playing_cards")

        # Face down image
        self.face_down_image = f"{images_path}/cardBack_black2.png"

        # Image to use for the sprite when face up and defining the value
        if self.value == "jack" or self.value == "queen" or self.value == "king" or self.value == "ace":
            self.image_file_name = f"{images_path}/{self.value}_of_{self.suit}2.png"
            if self.value == "jack":
                self.value = 11
            elif self.value == "queen":
                self.value = 12
            elif self.value == "king":
                self.value = 13
            elif self.value == "ace":
                self.value = 14
        else:
            self.image_file_name = f"{images_path}/{self.value}_of_{self.suit}.png"
            self.value = int(self.value)

        self.is_face_up = False

        # Destination point is where we are going
        self._destination_point = None

        # # Max speed
        # self.speed = 5
        #
        # # Max speed we can rotate
        # self.rot_speed = 5
        self.x_diff = 0
        self.y_diff = 0
        super().__init__(self.face_down_image, scale, hit_box_algorithm="None")

    def face_down(self):
        """ Turn card face-down """
        self.texture = arcade.load_texture(self.face_down_image)
        self.is_face_up = False

    def face_up(self):
        """ Turn card face-up """
        self.texture = arcade.load_texture(self.image_file_name)
        self.is_face_up = True

    @property
    def is_face_down(self):
        """ Is this card face down? """
        return not self.is_face_up

    @property
    def destination_point(self):
        return self._destination_point

    @destination_point.setter
    def destination_point(self, destination_point):
        self._destination_point = destination_point

    def on_update(self, delta_time: float = 1 / 60):
        if not self._destination_point:
            return

        # Get the current position
        current_x = self.center_x
        current_y = self.center_y

        # Get the destination position
        dest_x, dest_y = self._destination_point

        #Calculate the speed in the x and y directions
        self.x_diff = (dest_x - current_x) / 20
        self.y_diff = (dest_y - current_y) / 20
        # if self.x_diff == 0 and self.y_diff == 0:
        #     self.x_diff = (dest_x - current_x) / 60
        #     self.y_diff = (dest_y - current_y) / 60

        # Set the sprite's speed

        self.change_x = self.x_diff
        self.change_y = self.y_diff

        # Update the sprite
        super().update()

        # Set the destination point to None if we are close enough to it
        if math.isclose(current_x, dest_x, abs_tol=0.2) and math.isclose(current_y, dest_y, abs_tol=0.2):
            self._destination_point = None
            self.x_diff = 0
            self.y_diff = 0
