# Solution 18: The Target Sum Path (Path Sum II)

## Approach Explanation
We traverse the tree using DFS. At each node, we add it to the current path and subtract its value from the target. If we reach a leaf with target == 0, we save the path. We backtrack by removing the node.

## Step-by-Step Logic
1. DFS from the root, maintaining the current path and remaining sum.
2. At each node, add it to the path and subtract from remaining.
3. If it's a leaf and remaining is 0, save the path.
4. Recurse on left and right children.
5. Backtrack by removing the node from the path.

## Complexity
- **Time Complexity:** O(N^2) in worst case (skewed tree).
- **Space Complexity:** O(N).

## Code
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def path_sum(root, target_sum):
    result = []
    
    def dfs(node, remaining, path):
        if not node:
            return
        path.append(node.val)
        
        if not node.left and not node.right and remaining == node.val:
            result.append(path[:])
        
        dfs(node.left, remaining - node.val, path)
        dfs(node.right, remaining - node.val, path)
        path.pop()  # backtrack
    
    dfs(root, target_sum, [])
    return result
```
