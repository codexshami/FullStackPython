# Problem 19: Watershed Convergence (Pacific Atlantic Water Flow)

## Problem Statement
There is an `m x n` rectangular island that borders both the Pacific Ocean (left and top edges) and the Atlantic Ocean (right and bottom edges).
The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.
Rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates `result` where `result[i] = [ri, ci]` means that rain water can flow from cell `(ri, ci)` to both the Pacific and Atlantic oceans.

## Input Format
- A 2D integer matrix `heights`.

## Example
**Input:** heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]  
**Output:** [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
