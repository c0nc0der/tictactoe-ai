"""
Tic Tac Toe Player

This module implements an AI player for the game of Tic Tac Toe using the Minimax algorithm.
It includes functions to simulate gameplay, determine optimal moves, and evaluate game states.
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0
    for row in board:
        count_x += row.count(X)
        count_o += row.count(O)
    if count_x == count_o:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    col = action[1]
    if board[row][col] is not EMPTY:
        raise Exception("Can't go there")

    new_board = copy.deepcopy(board)
    new_board[row][col] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board [0][j] is not EMPTY:
            return board[0][j]
    if board[0][0] == board[1][1] == board[2][2] and board[2][2] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Determines the optimal move for the current player using the Minimax algorithm.

    This function recursively evaluates all possible future game states resulting from
    available actions, assuming both players play optimally. It selects the move that 
    maximizes the current player's chances of winning (or minimizes loss in worst-case).
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_score = -math.inf
        best_action = None
        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_action = action
        return best_action
    
    else:
        best_score = math.inf
        best_action = None
        for action in actions(board):
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_action = action
        return best_action
        
def min_value(board):
    """
    Calculates the minimum utility value that the minimizing player (O) can force 
    from the current board state, assuming the maximizing player (X) plays optimally.

    This function is called recursively by the Minimax algorithm.
    """
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def max_value(board):
    """
    Calculates the maximum utility value that the maximizing player (X) can achieve 
    from the current board state, assuming the minimizing player (O) plays optimally.

    This function is called recursively by the Minimax algorithm.
    """
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
