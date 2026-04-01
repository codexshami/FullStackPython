# Problem 5: The Shortest Route (Dijkstra's Algorithm)

## Problem Statement
Given a weighted, directed graph and a source vertex, find the shortest path from the source to all other vertices using Dijkstra's algorithm.

## Input Format
- Number of vertices `V`.
- A list of edges `(u, v, weight)`.
- A source vertex `src`.

## Example
**Input:** V = 5, edges = [(0,1,4),(0,2,1),(2,1,2),(1,3,1),(2,3,5),(3,4,3)], src = 0  
**Output:** {0: 0, 1: 3, 2: 1, 3: 4, 4: 7}
