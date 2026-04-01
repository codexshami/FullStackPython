# Problem 11: The Color Map (Graph Coloring / M-Coloring Problem)

## Problem Statement
Given an undirected graph and a number `m`, determine if the graph can be colored with at most `m` colors such that no two adjacent vertices share the same color. Return one valid coloring if it exists.

## Input Format
- An adjacency matrix `graph` of size `V x V`.
- An integer `m` (number of colors).

## Example
**Input:** graph = [[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]], m = 3  
**Output:** [1, 2, 3, 2]
