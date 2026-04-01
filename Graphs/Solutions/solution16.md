# Solution 16: The Prim's Web (Prim's Minimum Spanning Tree)

## Approach Explanation
Prim's algorithm grows the MST one vertex at a time, always adding the cheapest edge connecting the MST to a non-MST vertex. We use a min-heap for efficiency.

## Step-by-Step Logic
1. Start from vertex 0. Add all its edges to the min-heap.
2. Pop the minimum weight edge from the heap.
3. If the vertex is already in MST, skip.
4. Otherwise, add the vertex to MST and push all its edges to the heap.
5. Repeat until all vertices are in MST.

## Complexity
- **Time Complexity:** O(E log V).
- **Space Complexity:** O(V + E).

## Code
```python
import heapq
from collections import defaultdict

def prim(V, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    visited = set()
    heap = [(0, 0)]  # (weight, vertex)
    mst_weight = 0
    
    while heap and len(visited) < V:
        w, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        mst_weight += w
        
        for weight, v in graph[u]:
            if v not in visited:
                heapq.heappush(heap, (weight, v))
    
    return mst_weight
```
