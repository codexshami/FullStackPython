# Solution 18: The Strongly Connected (Kosaraju's Algorithm)

## Approach Explanation
Kosaraju's algorithm works in 3 steps: (1) DFS on original graph to get finish order, (2) transpose the graph, (3) DFS on transposed graph in reverse finish order — each DFS tree is an SCC.

## Step-by-Step Logic
1. Perform DFS on the original graph, pushing vertices to a stack by finish time.
2. Create a transposed graph (reverse all edges).
3. Pop vertices from the stack and perform DFS on the transposed graph.
4. Each DFS call on the transposed graph gives one SCC.

## Complexity
- **Time Complexity:** O(V + E).
- **Space Complexity:** O(V + E).

## Code
```python
from collections import defaultdict

def kosaraju(V, adj):
    # Step 1: Fill stack with finish order
    visited = set()
    stack = []
    
    def dfs1(node):
        visited.add(node)
        for neighbor in adj.get(node, []):
            if neighbor not in visited:
                dfs1(neighbor)
        stack.append(node)
    
    for i in range(V):
        if i not in visited:
            dfs1(i)
    
    # Step 2: Transpose the graph
    transposed = defaultdict(list)
    for u in adj:
        for v in adj[u]:
            transposed[v].append(u)
    
    # Step 3: DFS on transposed graph
    visited.clear()
    scc_count = 0
    
    def dfs2(node):
        visited.add(node)
        for neighbor in transposed.get(node, []):
            if neighbor not in visited:
                dfs2(neighbor)
    
    while stack:
        node = stack.pop()
        if node not in visited:
            dfs2(node)
            scc_count += 1
    
    return scc_count
```
