# Solution 2: The Depth Explorer (DFS Traversal)

## Approach Explanation
DFS explores as deep as possible along each branch before backtracking. We use recursion (or a stack) to achieve this.

## Step-by-Step Logic
1. Start at the given node, mark it as visited, add to result.
2. For each unvisited neighbor, recursively perform DFS.
3. Return when all reachable nodes are visited.

## Complexity
- **Time Complexity:** O(V + E).
- **Space Complexity:** O(V).

## Code
```python
def dfs(graph, start):
    visited = set()
    result = []
    
    def dfs_helper(node):
        visited.add(node)
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_helper(neighbor)
    
    dfs_helper(start)
    return result
```
