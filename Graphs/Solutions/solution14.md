# Solution 14: The Bellman-Ford Explorer (Shortest Path with Negative Weights)

## Approach Explanation
Bellman-Ford relaxes all edges V-1 times. Unlike Dijkstra, it handles negative weights. An additional V-th pass detects negative weight cycles.

## Step-by-Step Logic
1. Initialize distances to infinity; source = 0.
2. Repeat V-1 times: for each edge (u, v, w), relax: if `dist[u] + w < dist[v]`, update `dist[v]`.
3. One more pass: if any edge can still be relaxed, a negative cycle exists.

## Complexity
- **Time Complexity:** O(V * E).
- **Space Complexity:** O(V).

## Code
```python
def bellman_ford(V, edges, src):
    dist = [float('inf')] * V
    dist[src] = 0
    
    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    # Check for negative weight cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return "Negative weight cycle detected"
    
    return {i: dist[i] for i in range(V)}
```
