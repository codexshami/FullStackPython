# Problem 13: The Rotten Oranges (Rotting Oranges)

## Problem Statement
You are given an `m x n` grid where each cell can have one of three values: 0 (empty), 1 (fresh orange), 2 (rotten orange). Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes until no cell has a fresh orange. If impossible, return -1.

## Input Format
- A 2D grid of integers.

## Constraints
- 1 <= m, n <= 10

## Example
**Input:** grid = [[2,1,1],[1,1,0],[0,1,1]]  
**Output:** 4
