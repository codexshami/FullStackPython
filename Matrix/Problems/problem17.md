# Problem 17: Territorial Enclosure (Surrounded Regions)

## Problem Statement
Given an `m x n` matrix `board` containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

## Input Format
- A 2D character matrix `board`.

## Example
**Input:** board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]  
**Output:** [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
**Explanation:** The 'O' at the bottom edge is not surrounded, so it stays. All other 'O's are flipped.
