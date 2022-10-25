import arcade


class Card(arcade.Sprite):
    """ Card sprite """

    def __init__(self, suit, value, scale=1):
        """ Card constructor """

        # Attributes for suit and value
        self.suit = suit
        self.value = value

        # Image to use for the sprite when face up
        if self.value == "jack" or self.value == "queen" or self.value == "king":
            self.image_file_name = f"playing_cards/{self.value}_of_{self.suit}2.png"
        else:
            self.image_file_name = f"playing_cards/{self.value}_of_{self.suit}.png"

        # Call the parent
        super().__init__(self.image_file_name, scale, hit_box_algorithm="None")
