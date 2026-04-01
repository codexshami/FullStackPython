# Solution 7: The Bipartite Checker (Is Graph Bipartite?)

## Approach Explanation
We use BFS coloring. We try to color the graph with two colors such that no adjacent nodes share the same color. If we find a conflict, the graph is not bipartite.

## Step-by-Step Logic
1. Initialize a color array with -1 (uncolored).
2. For each uncolored node, start BFS.
3. Color the start node with 0, and its neighbors with 1, alternating.
4. If a neighbor already has the same color as the current node → not bipartite.

## Complexity
- **Time Complexity:** O(V + E).
- **Space Complexity:** O(V).

## Code
```python
from collections import deque

def is_bipartite(graph):
    n = len(graph)
    color = [-1] * n
    
    for start in range(n):
        if color[start] != -1:
            continue
        queue = deque([start])
        color[start] = 0
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
    
    return True
```
