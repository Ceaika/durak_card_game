# Screen title and size
import arcade
from screeninfo import get_monitors

screen_width = screen_height = 0

for monitor in get_monitors():
    if monitor.is_primary:
        screen_width = monitor.width
        screen_height = monitor.height
        print(screen_height, screen_width)

# Constants for sizing of Screen
SCREEN_SCALE = 0.85
SCREEN_WIDTH = round(screen_width * SCREEN_SCALE)
SCREEN_HEIGHT = round(screen_height * SCREEN_SCALE)
SCREEN_TITLE = "Durak"


# Constants for sizing
CARD_SCALE = 0.25

# How big are the cards?
CARD_WIDTH = 500 * CARD_SCALE
CARD_HEIGHT = 726 * CARD_SCALE

# How big is the mat we'll place the card on?
MAT_PERCENT_OVERSIZE = 1.0
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)

# How much space do we leave as a gap between the mats?
# Done as a percent of the mat size.
VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10

# The Y of the bottom row
BOTTOM_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# The X of where to start putting things on the left side
START_X = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

# The Y of the top row
TOP_Y = SCREEN_HEIGHT - MAT_HEIGHT / 2 - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# The Y of the middle row
MIDDLE_Y = TOP_Y - MAT_HEIGHT - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# How far apart each pile goes
X_SPACING = MAT_WIDTH + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

SPRITE_COLOR = arcade.csscolor.DARK_OLIVE_GREEN

# Card constants
CARD_VALUES = ["6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
CARD_SUITS = ["clubs", "hearts", "spades", "diamonds"]
