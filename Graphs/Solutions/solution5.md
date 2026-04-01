# Solution 5: The Shortest Route (Dijkstra's Algorithm)

## Approach Explanation
Dijkstra's finds the shortest path from a source to all vertices in a graph with non-negative weights. We use a min-heap (priority queue) to always process the vertex with the smallest known distance.

## Step-by-Step Logic
1. Initialize distances to infinity; source distance = 0.
2. Use a min-heap, starting with `(0, source)`.
3. Pop the vertex with the smallest distance.
4. For each neighbor, if a shorter path is found, update the distance and push to the heap.
5. Repeat until the heap is empty.

## Complexity
- **Time Complexity:** O((V + E) log V).
- **Space Complexity:** O(V + E).

## Code
```python
import heapq
from collections import defaultdict

def dijkstra(V, edges, src):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    
    dist = {i: float('inf') for i in range(V)}
    dist[src] = 0
    heap = [(0, src)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    
    return dist
```
