
# If we fan out unused_cards stacked on each other, how far apart to fan them?
# CARD_VERTICAL_OFFSET = CARD_HEIGHT * CARD_SCALE * 0.3

# Constants that represent "what pile is what" for the game
PLAYER_AREA = 0
COMPUTER_AREA = 1
MAIN_AREA = 2

# Amout of init Cards for every player
INIT_CARDS = 6

# How fast to move, and how fast to run the animation
MOVEMENT_SPEED = 5
UPDATES_PER_FRAME = 5

ANIMATION_STEPS = 30

# Difficulties
EASY = 0
MEDIUM = 1
HARD = 2

# Win/Lose png relative path
WIN = f'resources/win.png'
LOSE = f'resources/lose.png'
