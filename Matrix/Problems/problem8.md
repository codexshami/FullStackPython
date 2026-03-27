# Problem 8: Serpentine Dynamics (Snake Game Design)

## Problem Statement
Design a Snake game that is played on a device with screen size `height x width`. The snake is initially located at the top-left corner `(0, 0)` with a length of 1 unit.
You are given a list of food's coordinates in order of appearance. When a snake eats food, its length increases by 1 and the next food appears.
The game is over if the snake goes out of boundary or crashes into its own body.
Implement the `SnakeGame` class:
- `SnakeGame(int width, int height, int[][] food)` Initializes the object.
- `int move(String direction)` Returns the score after the move. Score = length - 1. If game over, return -1.

## Input Format
- Method calls.

## Example
**Input:** ["SnakeGame", "move", "move"] [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"]]  
**Output:** [null, 0, 1]
