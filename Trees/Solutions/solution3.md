# Solution 3: Mirror Transmutation

## Approach Explanation
We can use a recursive approach. For each node, we swap its left and right children and then recursively call the function for both.

## Step-by-Step Logic
1. If `root` is None, return None.
2. Swap `root.left` and `root.right`.
3. Recursively call `invert_tree(root.left)`.
4. Recursively call `invert_tree(root.right)`.
5. Return `root`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(H).

## Code
```python
def invert_tree(root):
    if not root:
        return None
        
    # Swap children
    root.left, root.right = root.right, root.left
    
    # Recurse
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root
```
