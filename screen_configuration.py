import math

import arcade


class ScreenConfiguration:
    def __init__(self):
        self.height = 1080
        self.width = 1920
        self.screen_title = "Durak"

        pass

    def init_current_screen(self):
        self.current_x, self.current_y = arcade.get_window().get_size()
        self.current_ratio = self,
        self.screen_ratio = self.calculate_aspect(self.width, self.height)
        self.__init_card_sizes()

    def __init_card_sizes(self):
        self.card_scale = 0.25 * self.screen_ratio
        self.card_width = 500 * self.card_scale
        self.card_height = 726 * self.card_scale
        self.__init_mat_sizes()

    def __init_mat_sizes(self):
        self.mat_percent_oversize = 1.25 * self.screen_ratio
        self.mat_height = int(self.card_height * self.mat_percent_oversize)
        self.mat_width = int(self.card_width * self.mat_percent_oversize)
        self.__init_spacing()

    def __init_spacing(self):
        self.vertical_margin_percent = 0.10
        self.horizontal_margin_percent = 0.10
        self.bottom_y = self.mat_height / 2 + self.mat_height * self.vertical_margin_percent
        # The X of where to start putting things on the left side
        self.start_x = self.mat_width / 2 + self.mat_width * self.horizontal_margin_percent
        # The Y of the top row
        self.top_y = self.current_y - self.mat_height / 2 - self.mat_height * self.vertical_margin_percent
        # The Y of the middle row
        self.middle_y = self.top_y - self.mat_height - self.mat_height * self.vertical_margin_percent
        # How far apart each pile goes
        self.x_spacing = self.mat_width + self.mat_width * self.horizontal_margin_percent
        self.__init_values()

    def __init_values(self):
        self.sprite_color = arcade.csscolor.DARK_OLIVE_GREEN
        self.card_values = ["6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
        self.card_suites = ["clubs", "hearts", "spades", "diamonds"]

    def calculate_aspect(self, width: int, height: int) -> tuple[int, int]:
        temp = 0

        def gcd(a, b):
            """The GCD (greatest common divisor) is the highest number that evenly divides both width and height."""
            return a if b == 0 else gcd(b, a % b)

        if width == height:
            return width, height

        if width < height:
            temp = width
            width = height
            height = temp

        divisor = gcd(width, height)

        x = int(width / divisor) if not temp else int(height / divisor)
        y = int(height / divisor) if not temp else int(width / divisor)

        return x, y
