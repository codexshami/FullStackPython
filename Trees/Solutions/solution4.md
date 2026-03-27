# Solution 4: Identical Blueprints

## Approach Explanation
We compare the roots and then recursively compare their left and right subtrees.

## Step-by-Step Logic
1. If both `p` and `q` are None, they are the same (True).
2. If only one is None or their values differ, they are not the same (False).
3. Return `is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(H).

## Code
```python
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
        
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
```
