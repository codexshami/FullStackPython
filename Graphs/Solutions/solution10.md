# Solution 10: The Minimum Spanning Tree (Kruskal's Algorithm)

## Approach Explanation
Kruskal's sorts all edges by weight, then greedily adds them to the MST if they don't form a cycle (checked using Union-Find).

## Step-by-Step Logic
1. Sort all edges by weight.
2. Initialize a Union-Find structure.
3. For each edge (in sorted order):
   - If the two vertices belong to different components, add the edge to MST and union them.
   - Skip if they're already connected (would form a cycle).
4. Return the total MST weight.

## Complexity
- **Time Complexity:** O(E log E).
- **Space Complexity:** O(V).

## Code
```python
def kruskal(V, edges):
    parent = list(range(V))
    rank = [0] * V
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    edges.sort(key=lambda x: x[2])
    mst_weight = 0
    mst_edges = 0
    
    for u, v, w in edges:
        if union(u, v):
            mst_weight += w
            mst_edges += 1
            if mst_edges == V - 1:
                break
    
    return mst_weight
```
