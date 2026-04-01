# Solution 15: The All-Pairs Shortest Path (Floyd-Warshall Algorithm)

## Approach Explanation
Floyd-Warshall considers every vertex as an intermediate point. For each pair `(i, j)`, we check if going through vertex `k` gives a shorter path.

## Step-by-Step Logic
1. Initialize the distance matrix from the input graph.
2. For each intermediate vertex `k`:
   - For each pair `(i, j)`:
     - `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`.
3. Return the distance matrix.

## Complexity
- **Time Complexity:** O(V^3).
- **Space Complexity:** O(V^2).

## Code
```python
def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]  # deep copy
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist
```
