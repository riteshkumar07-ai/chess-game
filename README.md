# ♟️ Python Chess Game

A simple and interactive **Chess Game built with Python and Pygame**. This project demonstrates GUI development, game logic, board representation, piece movement, mouse interaction, and turn-based gameplay.

## 🚀 Features

* ♟️ 8×8 Chess Board
* ♔ White and Black Chess Pieces
* 🖱️ Mouse-based piece selection and movement
* 🔄 Turn-based gameplay
* ⚔️ Piece capturing
* ♙ Pawn movement
* ♞ Knight movement
* ♝ Bishop movement
* ♜ Rook movement
* ♛ Queen movement
* ♚ King movement
* 🎯 Selected-square highlighting
* 🏆 Basic win/game-over detection
* 🔄 Easy game restart functionality

## 🛠️ Technologies Used

* **Python 3**
* **Pygame**
* 2D Lists
* Functions
* Loops
* Conditional Statements
* Event Handling

## 📂 Project Structure

```text
ChessGame/
│
├── chess.py
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/chess-game-python.git
```

### 2. Open the project

```bash
cd chess-game-python
```

### 3. Install Pygame

```bash
pip install pygame
```

Or:

```bash
python -m pip install pygame
```

### 4. Run the game

```bash
python chess.py
```

## 🎮 How to Play

1. Run `chess.py`.
2. Click on one of your pieces.
3. Click on the destination square.
4. The game automatically changes turns.
5. Capture your opponent's pieces.
6. The game ends when the opponent's king is captured.

### Controls

| Action       | Control          |
| ------------ | ---------------- |
| Select Piece | Left Mouse Click |
| Move Piece   | Left Mouse Click |
| Close Game   | Close Window     |

## 🧠 How It Works

The chess board is represented using a **2D Python list**.

```python
board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]
```

Uppercase letters represent **White pieces**, while lowercase letters represent **Black pieces**.

```text
P → White Pawn
R → White Rook
N → White Knight
B → White Bishop
Q → White Queen
K → White King

p → Black Pawn
r → Black Rook
n → Black Knight
b → Black Bishop
q → Black Queen
k → Black King
```

## 📌 Learning Concepts

This project helped me practice:

* Python fundamentals
* Object/game logic
* 2D arrays
* Functions
* Conditional statements
* Loops
* Event-driven programming
* GUI development
* Coordinate systems
* Basic algorithmic thinking

## 🔮 Future Improvements

The project can be extended with:

* ✅ Check detection
* ✅ Checkmate detection
* ♜ Castling
* ♟️ En Passant
* 👑 Pawn Promotion
* 🤝 Stalemate detection
* 🔊 Sound effects
* 🎨 Improved graphics
* 📊 Move history
* ↩️ Undo/Redo
* 🤖 Chess AI using Minimax
* ⚡ Alpha-Beta Pruning
* 🌐 Multiplayer mode

## 📸 Demo

Add a screenshot or GIF of your game here:

```text
![Chess Game Screenshot](screenshot.png)
```

## 🎯 Project Goal

The main goal of this project is to understand how a graphical game can be developed using Python while implementing chess board representation, piece movement, user interaction, and game logic.

## 👨‍💻 Author

**Ritesh Kumar**

B.Tech – Information Technology
Interested in **Artificial Intelligence & Machine Learning**

### Connect With Me

* GitHub: [riteshkumar07-ai](https://github.com/riteshkumar07-ai)
* LinkedIn: [Ritesh Kumar](https://www.linkedin.com/in/ritesh-kumar-255234318)

---

⭐ If you found this project useful, consider giving it a **star**!

**Made with ❤️ using Python & Pygame**
