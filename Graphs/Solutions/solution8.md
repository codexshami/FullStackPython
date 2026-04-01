# Solution 8: The Connected Components (Number of Connected Components)

## Approach Explanation
We use Union-Find (Disjoint Set Union). Initially, each node is its own component. For each edge, we union the two nodes. The number of distinct roots at the end is the answer.

## Step-by-Step Logic
1. Initialize parent array where `parent[i] = i`.
2. For each edge, union the two nodes.
3. Count the number of unique roots.

## Complexity
- **Time Complexity:** O(E * α(N)) ≈ O(E) with path compression.
- **Space Complexity:** O(N).

## Code
```python
def count_components(n, edges):
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
    
    for u, v in edges:
        union(u, v)
    
    return len(set(find(i) for i in range(n)))
```
