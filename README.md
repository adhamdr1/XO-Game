# XO-Game (Tic-Tac-Toe)

A classic Tic-Tac-Toe game implemented in Python with an unbeatable AI opponent using the Minimax algorithm.

## 🎮 Features

- **Two Game Modes:**
  - Player vs Player:  Play against a friend locally
  - Player vs AI:  Challenge an unbeatable AI opponent

- **Intelligent AI:** Uses the Minimax algorithm to calculate the optimal move every time
- **Clean CLI Interface:** Simple and intuitive command-line gameplay
- **Input Validation:** Prevents invalid moves and handles errors gracefully

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone the repository:
```bash
git clone https://github.com/adhamdr1/XO-Game.git
cd XO-Game
```

2. Run the game:
```bash
python XO.py
```

## 🎯 How to Play

1. When you start the game, you'll be prompted to select a game mode:
   - Enter `1` for Player vs Player
   - Enter `2` for Player vs AI (Unbeatable)

2. The board positions are numbered 1-9:
   ```
   1 | 2 | 3
   ---+---+---
   4 | 5 | 6
   ---+---+---
   7 | 8 | 9
   ```

3. Players take turns entering their desired position (1-9)
4. The first player to get three marks in a row (horizontally, vertically, or diagonally) wins
5. If all 9 positions are filled with no winner, the game ends in a draw

## 🧠 Technical Details

### Minimax Algorithm

The AI uses the **Minimax algorithm**, a decision-making algorithm that:
- Simulates all possible game outcomes
- Evaluates each position with a score (win:  +10, loss: -10, draw: 0)
- Chooses the move that maximizes the AI's chances of winning while minimizing the opponent's chances
- Makes the AI impossible to beat (you can only draw or lose)

### Code Structure

- `print_board()`: Displays the current game board
- `check_winner()`: Checks if a player has won
- `check_draw()`: Checks if the game is a draw
- `minimax()`: Implements the Minimax algorithm for AI decision-making
- `get_best_move()`: Finds the optimal move for the AI
- `play_game()`: Main game loop handling player input and game flow

## 📝 Example Gameplay

```
Welcome to Tic-Tac-Toe!
1. Player vs Player
2. Player vs AI (Unbeatable)
Select mode (1 or 2): 2

   |   |   
---+---+---
   |   |   
---+---+---
   |   |   

Player X's turn.
Enter position (1-9): 5

   |   |   
---+---+---
   | X |   
---+---+---
   |   |   

AI is thinking...
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  Feel free to check the issues page. 

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Adham** - [@adhamdr1](https://github.com/adhamdr1)

---

Enjoy playing!  Can you beat the AI? 🎯
