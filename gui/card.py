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
