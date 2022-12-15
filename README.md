# Durak

Durak is a popular Russian card game, and this repository implements a singleplayer version of the game in Python, using the arcade framework. The player can choose between three different difficulty levels to play against a bot opponent.

## Requirements

To run this game, you will need the following dependencies:

- Python 3.7 or later
- Arcade 2.0 or later

## Running the game

To run the game, clone the repository and run the following command:

```bash
python3 main.py
```


This will start the game and you can choose your difficulty level and play against the bot.

## Game rules

The rules of Durak are as follows:

- The game is played with a deck of 36 cards (6-10, Jack, Queen, King, Ace in each of the four suits)
- The game starts with each player being dealt a hand of 6 cards
- The remaining cards form the draw pile
- The player with the lowest trump card starts the game
- The starting player begins the game by attacking with a card from their hand
- The defending player must respond by playing a card of the same suit, if possible. If they cannot, they must use a trump card
- If the defender successfully responds to the attack, the attacker must continue the attack by playing another card
- If the defender cannot respond, they must pick up the cards played so far and add them to their hand
- The defender becomes the attacker and can start a new attack against the player to their left
- If a player runs out of cards, they are eliminated from the game
- The game ends when all players except one are eliminated

## Development

To contribute to the development of this game, please follow these steps:

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your changes
4. Make your changes and commit them to your branch
5. Push your branch to your fork on GitHub
6. Create a pull request from your branch to the `master` branch of the main repository

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
