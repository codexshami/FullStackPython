# Problem 6: The Topological Sorter (Topological Sort)

## Problem Statement
Given a Directed Acyclic Graph (DAG) with `V` vertices and `E` edges, find any topological ordering of the vertices. In topological sorting, for every directed edge `u → v`, vertex `u` comes before `v` in the ordering.

## Input Format
- Number of vertices `V`.
- An adjacency list `adj`.

## Example
**Input:** V = 6, adj = {5: [2,0], 4: [0,1], 2: [3], 3: [1], 0: [], 1: []}  
**Output:** [5, 4, 2, 3, 1, 0] (one valid ordering)
