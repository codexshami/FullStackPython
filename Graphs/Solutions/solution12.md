# Solution 12: The Clone Graph (Clone Graph)

## Approach Explanation
We use BFS/DFS with a hash map to track already cloned nodes. For each node, we create a copy and recursively clone its neighbors.

## Step-by-Step Logic
1. Use a dictionary mapping original nodes to their clones.
2. Start DFS from the given node.
3. If a node is already cloned, return its clone.
4. Create a new node, clone all its neighbors recursively.

## Complexity
- **Time Complexity:** O(V + E).
- **Space Complexity:** O(V).

## Code
```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def clone_graph(node):
    if not node:
        return None
    
    cloned = {}
    
    def dfs(n):
        if n in cloned:
            return cloned[n]
        
        copy = Node(n.val)
        cloned[n] = copy
        
        for neighbor in n.neighbors:
            copy.neighbors.append(dfs(neighbor))
        
        return copy
    
    return dfs(node)
```
