# Problem 17: Structural Weakness Analysis (Brick Wall)

## Problem Statement
There is a rectangular brick wall in front of you with `n` rows of bricks. The `i`-th row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.
You want to draw a vertical line from the top to the bottom and cross the least number of bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.
Given the 2D array `wall` that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

## Input Format
- A 2D integer matrix `wall`.

## Example
**Input:** wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]  
**Output:** 2
