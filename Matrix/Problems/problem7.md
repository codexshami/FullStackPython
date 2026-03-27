# Problem 7: Adversarial Grid Logic (Tic-Tac-Toe Design)

## Problem Statement
Design a Tic-Tac-Toe game that is played on an `n x n` grid between two players.
You may assume the following rules:
1. A move is guaranteed to be valid and is placed on an empty block.
2. Once a winning condition is reached, no more moves is allowed.
3. A player who succeeds in placing `n` of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the `TicTacToe` class:
- `TicTacToe(int n)` Initializes the object the size of the board `n`.
- `int move(int row, int col, int player)` Indicates that the player with id `player` plays at the cell `(row, col)`. The player will be either 1 or 2.

## Input Format
- Method calls.

## Example
**Input:** ["TicTacToe", "move", "move", "move"] [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1]]  
**Output:** [null, 0, 0, 1]
