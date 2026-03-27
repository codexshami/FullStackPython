# Solution 5: Reflection Check

## Approach Explanation
A tree is symmetric if its left and right subtrees are mirrors of each other. We use a helper function that takes two nodes and checks if they are mirror images.

## Step-by-Step Logic
1. Define `is_mirror(t1, t2)`:
   - If both are None, return True.
   - If one is None or values differ, return False.
   - Return `is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)`.
2. Return `is_mirror(root.left, root.right)`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(H).

## Code
```python
def is_symmetric(root):
    if not root:
        return True
        
    def is_mirror(node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2 or node1.val != node2.val:
            return False
            
        return is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)
        
    return is_mirror(root.left, root.right)
```
