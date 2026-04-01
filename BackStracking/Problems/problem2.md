# Problem 2: The Maze Runner (Rat in a Maze)

## Problem Statement
Consider a rat placed at position `(0, 0)` in an `N x N` maze. The rat has to reach the destination at `(N-1, N-1)`. The rat can move in four directions: up, down, left, right. In the maze matrix, `1` means the block is open and `0` means the block is blocked. Find all possible paths that the rat can take to reach the destination. Return the paths as strings of 'U', 'D', 'L', 'R'.

## Input Format
- An N x N binary matrix `maze`.

## Example
**Input:** maze = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]  
**Output:** ["DDRDRR", "DRDDRR"]
