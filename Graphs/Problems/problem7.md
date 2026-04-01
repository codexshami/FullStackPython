# Problem 7: The Bipartite Checker (Is Graph Bipartite?)

## Problem Statement
There is an undirected graph with `n` nodes. Given the adjacency list, determine if the graph is bipartite. A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge connects a node in A to one in B.

## Input Format
- An adjacency list `graph`.

## Example
**Input:** graph = [[1,3],[0,2],[1,3],[0,2]]  
**Output:** True  
**Explanation:** Nodes can be split into {0,2} and {1,3}.

**Input:** graph = [[1,2,3],[0,2],[0,1,3],[0,2]]  
**Output:** False
