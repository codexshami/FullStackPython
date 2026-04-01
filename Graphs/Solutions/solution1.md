# Solution 1: The Breadth Explorer (BFS Traversal)

## Approach Explanation
BFS uses a queue to explore nodes level by level. We start from the source, visit all neighbors, then their neighbors, and so on.

## Step-by-Step Logic
1. Initialize a queue with the start node and a visited set.
2. While the queue is not empty:
   - Dequeue a node, add it to the result.
   - Enqueue all unvisited neighbors, marking them as visited.

## Complexity
- **Time Complexity:** O(V + E).
- **Space Complexity:** O(V).

## Code
```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result
```
