# Solution 6: Layered Perspective

## Approach Explanation
We use a Breadth-First Search (BFS) approach with a queue. For each level, we record the number of nodes currently in the queue to process that entire level before moving to the next.

## Step-by-Step Logic
1. If `root` is None, return an empty list.
2. Initialize a queue with the `root`.
3. While the queue is not empty:
   - Get the number of nodes at the current level.
   - Initialize an empty list `level_nodes`.
   - For `size` times:
     - Pop node from queue.
     - Add `node.val` to `level_nodes`.
     - Add children to queue if they exist.
   - Append `level_nodes` to the final `result`.
4. Return `result`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(W), where W is the maximum width of the tree.

## Code
```python
from collections import deque

def level_order(root):
    if not root:
        return []
        
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_vals = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_vals.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(level_vals)
        
    return result
```
