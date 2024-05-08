# Python Battleship Bot Challenge

Welcome to the Python Battleship Bot Challenge! This repository invites participants to develop their own Python bots that can autonomously play the game of Battleship. Bots will compete against each other in a tournament to determine which can best strategize and adapt. Prepare your best Python skills and join the fleet!

## About the Challenge

In this challenge, participants will create bots using Python that can play Battleship autonomously. Each bot will face off against others in a series of matches to see who emerges victorious.

## Game Rules

Battleship is played on a grid where each player has a fleet of ships. The goal is to sink your opponent's ships by correctly guessing their locations on the grid.

- Each player has a 10x10 grid.
- Fleet consists of:
  - 1 Carrier (5 cells)
  - 1 Battleship (4 cells)
  - 1 Cruiser (3 cells)
  - 1 Submarine (3 cells each)
  - 1 Destroyer (2 cells each)
- Players take turns guessing grid coordinates to target the opponent's ships.

## Bot Requirements

1. **Python Only**: All bots must be written in Python.
2. **Autonomy**: Bots must operate without human intervention once the game starts.
3. **Interacts with Board**: A standard board and basic functions will be provided. Your bot should be implemented to function in this board and implement the functions it needs. 

## Contributing

To participate, follow these steps:

1. Fork this repository.
2. Create your bot branch (`git checkout -b bot/YourBotName`).
3. Commit your bot code (`git commit -am 'Add YourBotName'`).
4. Push to the branch (`git push origin bot/YourBotName`).
5. Open a new Pull Request with a detailed description of your bot's strategy.

## Tournament

- Bots will be matched in a round-robin format to ensure each bot plays against every other bot.
- Points are awarded based on game outcome: win (3 points), draw (1 point), loss (0 points).
- The leaderboard will be updated regularly to show standings.

## Leaderboard

Check back here to see which bots are leading in the competition!

- **BotName1**: 15 points
- **BotName2**: 12 points

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

Ready your algorithms and may the best bot win in the Python Battleship Bot Challenge!
