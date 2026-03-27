# Solution 13: Linear Transformation

## Approach Explanation
We can solve this recursively by processing the tree in reverse pre-order (Right -> Left -> Root). We maintain a `prev` pointer that points to the previously processed node and attach it to the current node's right.

## Step-by-Step Logic
1. Initialize `prev = None`.
2. Define a helper `flatten(node)`:
   - If `node` is None, return.
   - Recurse on the right: `flatten(node.right)`.
   - Recurse on the left: `flatten(node.left)`.
   - Set `node.right = prev`.
   - Set `node.left = None`.
   - Update `prev = node`.
3. The main function calls `flatten(root)`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(H).

## Code
```python
def flatten(root):
    prev = None
    
    def helper(node):
        nonlocal prev
        if not node:
            return
        
        # Reverse preorder: Right, then Left, then Root
        helper(node.right)
        helper(node.left)
        
        node.right = prev
        node.left = None
        prev = node
        
    helper(root)
```
