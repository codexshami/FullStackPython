# Solution 3: The Cycle Detector (Detect Cycle in Undirected Graph)

## Approach Explanation
We use BFS/DFS. During traversal, if we find a visited neighbor that is not the parent of the current node, a cycle exists.

## Step-by-Step Logic
1. For each unvisited node, run DFS.
2. Track the parent of each node.
3. If we encounter a visited node that's not the parent → cycle detected.
4. If no cycle found after all nodes are processed, return False.

## Complexity
- **Time Complexity:** O(V + E).
- **Space Complexity:** O(V).

## Code
```python
def has_cycle(V, adj):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in adj.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    for i in range(V):
        if i not in visited:
            if dfs(i, -1):
                return True
    return False
```
