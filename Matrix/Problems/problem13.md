# Problem 13: Diagonal Invariance (Toeplitz Matrix)

## Problem Statement
Given an `m x n` matrix, return `true` if the matrix is Toeplitz. Otherwise, return `false`.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

## Input Format
- A 2D integer matrix `matrix`.

## Example
**Input:** matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]  
**Output:** True
**Explanation:** Diagonals are [9], [5, 5], [1, 1, 1], [2, 2, 2], [3, 3], [4]. All have identical numbers.
