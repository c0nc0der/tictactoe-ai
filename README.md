# Module Docstring

Tic Tac Toe Player

This module implements an AI player for the game of Tic Tac Toe using the Minimax algorithm.
It includes functions to simulate gameplay, determine optimal moves, and evaluate game states.

## Function `initial_state()`

Returns starting state of the board.

## Function `player()`

Returns player who has the next turn on a board.

## Function `actions()`

Returns set of all possible actions (i, j) available on the board.

## Function `result()`

Returns the board that results from making move (i, j) on the board.

## Function `winner()`

Returns the winner of the game, if there is one.

## Function `terminal()`

Returns True if game is over, False otherwise.

## Function `utility()`

Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

## Function `minimax()`

Returns the optimal action for the current player on the board.

## Function `min_value()`

Returns the minimum utility value that can be achieved from the current board state,
assuming the opponent plays optimally.

## Function `max_value()`

Returns the maximum utility value that can be achieved from the current board state,
assuming the current player plays optimally.

