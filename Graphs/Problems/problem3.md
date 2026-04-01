# Problem 3: The Cycle Detector (Detect Cycle in Undirected Graph)

## Problem Statement
Given an undirected graph with `V` vertices and `E` edges, check whether the graph contains any cycle or not.

## Input Format
- Number of vertices `V`.
- An adjacency list `adj`.

## Example
**Input:** V = 5, adj = {0: [1], 1: [0,2,4], 2: [1,3], 3: [2,4], 4: [1,3]}  
**Output:** True (cycle exists: 1-2-3-4-1)
