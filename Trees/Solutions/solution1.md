# Solution 1: Systematic Exploration

## Approach Explanation
Inorder traversal (Left -> Root -> Right) can be implemented recursively or iteratively using a stack.

## Step-by-Step Logic
1. Initialize an empty `result` list.
2. Define a helper function `traverse(node)`:
   - If `node` is None, return.
   - `traverse(node.left)`
   - `result.append(node.val)`
   - `traverse(node.right)`
3. Call `traverse(root)`.
4. Return `result`.

## Complexity
- **Time Complexity:** O(N), where N is the number of nodes.
- **Space Complexity:** O(H), where H is the height of the tree (recursion stack).

## Code
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    res = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        res.append(node.val)
        helper(node.right)
        
    helper(root)
    return res
```
