import arcade

class Card(arcade.Sprite):
    """ Card sprite """

    def __init__(self, suit, value, scale=1):
        """ Card constructor """

        # Attributes for suit and value
        self.suit = suit
        self.value = value

        # Face down image
        self.face_down_image = "playing_cards/cardBack_black2.png"

        # Image to use for the sprite when face up
        if self.value == "jack" or self.value == "queen" or self.value == "king":
            self.image_file_name = f"playing_cards/{self.value}_of_{self.suit}2.png"
        else:
            self.image_file_name = f"playing_cards/{self.value}_of_{self.suit}.png"

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
        # Call the parent
        super().__init__(self.image_file_name, scale, hit_box_algorithm="None")
