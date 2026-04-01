# Problem 18: The Strongly Connected (Kosaraju's Algorithm)

## Problem Statement
Given a directed graph with `V` vertices and `E` edges, find the number of Strongly Connected Components (SCCs) using Kosaraju's algorithm. A SCC is a maximal set of vertices where every vertex is reachable from every other vertex.

## Input Format
- Number of vertices `V`.
- An adjacency list `adj`.

## Example
**Input:** V = 5, adj = {0: [2,3], 1: [0], 2: [1], 3: [4], 4: []}  
**Output:** 3  
**Explanation:** SCCs: {0,1,2}, {3}, {4}.
