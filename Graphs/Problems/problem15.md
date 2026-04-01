# Problem 15: The All-Pairs Shortest Path (Floyd-Warshall Algorithm)

## Problem Statement
Given a weighted directed graph represented as an adjacency matrix, find the shortest distances between every pair of vertices using the Floyd-Warshall algorithm. If no path exists, the distance is infinity.

## Input Format
- A 2D adjacency matrix `graph` of size `V x V`.

## Example
**Input:** graph = [[0,3,INF,7],[8,0,2,INF],[5,INF,0,1],[2,INF,INF,0]]  
**Output:** [[0,3,5,6],[5,0,2,3],[3,6,0,1],[2,5,7,0]]
