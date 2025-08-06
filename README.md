# Tic Tac Toe Player

This module implements an AI player for the game of Tic Tac Toe using the Minimax algorithm.
It includes functions to simulate gameplay, determine optimal moves, and evaluate game states.

## ✨ Features

## 📦 Installation

Before running the program, make sure to install the required Python packages:
```bash
pip install -r requirements.txt
```
Or install individually:
```bash
pip install pygame
pip install pdoc
```
## 🔧 Usage

```bash
python tictactoe/runner.py
```
## 🔑 Variables
```python
X = "X"         # The representation of the "X" player
O = "O"         # The representation of the "O" player
EMPTY = None    # The representation of square in the grid that is empty.
```
## 🧠 Functions

### `initial_state(board)`

Returns starting state of the board.

**Returns:** Initial state of the board. A 2-D 3x3 list array of `EMPTY` elements.


### `player(board)`

Determines which player's turn it is given the current board.

**Parameters:** 
board (list): The current state of the Tic-Tac-Toe board.

**Returns:** 
The corresponding player whose turn it is currently (`X` or `O`) 

### `actions(board)`

Determines all possible actions (i, j)that are available on the board for a player.

**Parameters:** 
board (list): The current state of the Tic-Tac-Toe board.

**Returns:** 
actions (set): Set of tuples containing all posible actions (row,col) given the current board.

### `result(board, action)`

Find out the new state of the board given an action taht was taken.

**Parameters:**
| Name | Type | Description |
|---|---|---|
| board | list | Current state of the board. |
| action | tuple | Placing a player marker on a given location (i,j).  |

**Returns:** 
| Name | Type | Description |
|---|---|---|
| new_board | list | The new state of the board given said action. |

### `winner()`

Searches for a representation of whichever player won by obtaining a vertical, horizontal or diagonal of 3 markers in a row.

**Parameters:** 
board (list): The current state of the Tic-Tac-Toe board.

**Returns:** 
`X` or `O` if winner is found
`None` otherwise.

### `terminal(board)`

Give a boolean representation of the completion of the game.

**Parameters:** 
board (list): The current state of the Tic-Tac-Toe board.

**Returns:** 
Boolean: True if the game is over, Flase if not.

### `utility(board)`

Assigning `X` the role of the maximizing player and `O` the role of the minimizing player.

**Parameters:** 
board (list): The current state of the Tic-Tac-Toe board.

**Returns:** 
int: The minimum utility value reachable from this board state. 
Returns 1 if X wins, -1 if O wins, 0 if draw.

### `minimax(board)`

Returns the optimal action for the current player on the board.

**Parameters:** 
board (list): The current state of the Tic-Tac-Toe board.

**Returns:** 
`tuple:` The optimal action as a (row, column) tuple, or None if the game is over.

### `min_value(board)`

Returns the minimum utility value that can be achieved from the current board state,
assuming the opponent plays optimally.

**Parameters:** board (list): The current state of the Tic-Tac-Toe board.

**Returns:** 
`int:` The minimum utility value reachable from this board state.
Returns 1 if X wins, -1 if O wins, 0 if draw.

### `max_value()`

Returns the maximum utility value that can be achieved from the current board state,
assuming the current player plays optimally.

**Parameters:** 
board (list): The current state of the Tic-Tac-Toe board.

**Returns:** 
`int:` The maximum utility value reachable from this board state.
Returns 1 if X wins, -1 if O wins, 0 if draw.