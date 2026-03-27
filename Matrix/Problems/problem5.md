# Problem 5: Grid Constraints (Valid Sudoku)

## Problem Statement
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
A Sudoku board (partially filled) could be valid but is not necessarily solvable.

## Input Format
- A 9 x 9 character matrix `board`.

## Example
**Input:** board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],...]  
**Output:** True
