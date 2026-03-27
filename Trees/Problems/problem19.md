# Problem 19: Vertical Alignment

## Problem Statement
Given the `root` of a binary tree, return the vertical order traversal of its nodes' values. For each node at position `(row, col)`, its left child will be at `(row + 1, col - 1)` and its right child will be at `(row + 1, col + 1)`. Report nodes from top to bottom, sorted by col then by row, then by value if multiple nodes are at the same (row, col).

## Input Format
- The `root` of a binary tree.

## Example
**Input:** root = [3, 9, 20, null, null, 15, 7]  
**Output:** [[9], [3, 15], [20], [7]]
