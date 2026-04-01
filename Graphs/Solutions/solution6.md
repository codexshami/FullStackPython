# Solution 6: The Topological Sorter (Topological Sort)

## Approach Explanation
We use Kahn's algorithm (BFS-based). We compute in-degrees for all vertices, start from 0-in-degree nodes, and progressively remove them, reducing in-degrees of their neighbors.

## Step-by-Step Logic
1. Compute in-degree for each vertex.
2. Add all vertices with in-degree 0 to a queue.
3. While the queue is not empty:
   - Dequeue a vertex, add to result.
   - Reduce in-degree of all its neighbors.
   - If any neighbor's in-degree becomes 0, enqueue it.
4. Return the result.

## Complexity
- **Time Complexity:** O(V + E).
- **Space Complexity:** O(V + E).

## Code
```python
from collections import deque, defaultdict

def topological_sort(V, adj):
    in_degree = [0] * V
    for u in adj:
        for v in adj[u]:
            in_degree[v] += 1
    
    queue = deque([i for i in range(V) if in_degree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in adj.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == V else []
```
