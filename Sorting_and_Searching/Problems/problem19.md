# Problem 19: Planar Quadrant Update

## Problem Statement
Given a 2D matrix `matrix`, handle multiple queries of the following types:
1. `update(row, col, val)`: Updates the value of the cell `(row, col)` to be `val`.
2. `sumRegion(row1, col1, row2, col2)`: Returns the sum of the elements of `matrix` inside the rectangle defined by its upper left corner `(row1, col1)` and lower right corner `(row2, col2)`.

## Input Format
- Matrix initialization and method calls.

## Example
**Input:** ["NumMatrix", "sumRegion", "update", "sumRegion"] [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]  
**Output:** [null, 8, null, 10]
