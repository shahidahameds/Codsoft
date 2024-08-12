# Rock-Paper-Scissors Game

A simple Rock-Paper-Scissors game implemented using the Kivy framework in Python. This game allows you to play against the computer with a graphical user interface.

## Features

- Play Rock-Paper-Scissors against the computer.
- Display results of each round.
- Option to play another round or quit the game.

## Requirements

- Python 3.x
- Kivy

## Installation

1. **Clone the repository:**
    ```bash
    https://github.com/shahidahameds/Codsoft.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd Task02
    ```

3. **Install the required packages:**
    ```bash
    pip install kivy
    ```

## Usage

1. **Run the game:**
    ```bash
    python rock-paper-scissor.py
    ```

2. **Play the game:**
   - Click on one of the buttons: Rock, Paper, or Scissors.
   - The game will display the result and ask if you want to play again.
   - Click "Yes" to play another round or "No" to exit the game.

## Code Overview

- **RockPaperScissorsGame**: The main application class extending `App`.
- **build()**: Sets up the layout and widgets.
- **determine_winner(player, computer)**: Determines the result of the game.
- **draw()**: Updates the result label and enables buttons for replay.
- **play_next_round()**: Resets the game state for the next round.
- **yes_pressed()**: Starts a new round.
- **no_pressed()**: Exits the game.
- **rock_pressed(), paper_pressed(), scissors_pressed()**: Handle player choices and compute results.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.

## Contact

If you have any questions or suggestions, feel free to reach out to me at [shahidahamed3214@gmail.com](shahidahamed3214@gmail.com).

---

Enjoy playing Rock-Paper-Scissors!

