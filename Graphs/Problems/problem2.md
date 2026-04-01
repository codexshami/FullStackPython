# Problem 2: The Depth Explorer (DFS Traversal)

## Problem Statement
Given an undirected graph represented as an adjacency list and a starting node, perform a Depth-First Search (DFS) traversal and return the order of visited nodes.

## Input Format
- An adjacency list `graph` (dictionary of lists).
- A starting node `start`.

## Example
**Input:** graph = {0: [1,2], 1: [0,3], 2: [0,4], 3: [1], 4: [2]}, start = 0  
**Output:** [0, 1, 3, 2, 4]
