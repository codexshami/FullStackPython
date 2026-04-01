# Problem 14: The Bellman-Ford Explorer (Shortest Path with Negative Weights)

## Problem Statement
Given a weighted directed graph with `V` vertices, `E` edges, and a source vertex, find the shortest distances from the source to all other vertices using the Bellman-Ford algorithm. If a negative weight cycle is detected, report it.

## Input Format
- Number of vertices `V`.
- A list of edges `(u, v, weight)`.
- A source vertex `src`.

## Example
**Input:** V = 5, edges = [(0,1,-1),(0,2,4),(1,2,3),(1,3,2),(1,4,2),(3,2,5),(3,1,1),(4,3,-3)], src = 0  
**Output:** {0: 0, 1: -1, 2: 2, 3: -2, 4: 1}
