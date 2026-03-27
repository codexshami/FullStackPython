# Solution 15: Weaving Levels

## Approach Explanation
We use BFS (Level Order Traversal) with a slight modification: we use a boolean flag `left_to_right` and reverse the level's values whenever the flag is false.

## Step-by-Step Logic
1. If `root` is None, return [].
2. Initialize `queue` with `root` and `left_to_right = True`.
3. While queue is not empty:
   - Get `size` of current level.
   - Collect `level_vals`.
   - If `not left_to_right`, reverse `level_vals`.
   - Append to result.
   - Toggle `left_to_right`.
4. Return `result`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(W).

## Code
```python
from collections import deque

def zigzag_level_order(root):
    if not root:
        return []
        
    res = []
    q = deque([root])
    left_to_right = True
    
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            
        if not left_to_right:
            level.reverse()
        res.append(level)
        left_to_right = not left_to_right
        
    return res
```
