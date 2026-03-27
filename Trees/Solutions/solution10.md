# Solution 10: Profile Projection

## Approach Explanation
We can use BFS (Level Order Traversal). At each level, the last node processed is the one visible from the right side.

## Step-by-Step Logic
1. If `root` is None, return [].
2. Initialize `result = []` and `queue` with `root`.
3. While queue is not empty:
   - `level_size = len(queue)`
   - For `i` in range `level_size`:
     - Pop `node` from queue.
     - If `i == level_size - 1`, append `node.val` to `result`.
     - Add children to queue.
4. Return `result`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(W).

## Code
```python
from collections import deque

def right_side_view(root):
    if not root:
        return []
    
    res = []
    q = deque([root])
    
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            # If it's the rightmost node of the level
            if i == size - 1:
                res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            
    return res
```
