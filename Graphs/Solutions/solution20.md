# Solution 20: The Network Delay (Network Delay Time)

## Approach Explanation
This is a shortest path problem. We use Dijkstra's algorithm to find the shortest distance from the source node `k` to all other nodes. The answer is the maximum of these distances.

## Step-by-Step Logic
1. Build the adjacency list from the edge list.
2. Run Dijkstra from node `k`.
3. Find the maximum distance among all reachable nodes.
4. If any node is unreachable (distance = infinity), return -1.

## Complexity
- **Time Complexity:** O((V + E) log V).
- **Space Complexity:** O(V + E).

## Code
```python
import heapq
from collections import defaultdict

def network_delay_time(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0
    heap = [(0, k)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    
    max_dist = max(dist.values())
    return max_dist if max_dist < float('inf') else -1
```
