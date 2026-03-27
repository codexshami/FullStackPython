# Solution 8: Universal Ancestry (Binary Tree)

## Approach Explanation
We use a post-order traversal (bottom-up). If a node is `p` or `q`, we return it. If a node receives non-null values from both its left and right children, it must be the LCA.

## Step-by-Step Logic
1. Base case: If `root` is None, or `root` is `p` or `q`, return `root`.
2. Recursively search in the left subtree: `left = lca(root.left, p, q)`.
3. Recursively search in the right subtree: `right = lca(root.right, p, q)`.
4. If both `left` and `right` are not None:
   - This means `p` and `q` are in different subtrees, so `root` is the LCA.
5. If only one is not None, return that non-null value (the found `p` or `q`).
6. If both are None, return None.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(H).

## Code
```python
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
        
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
        
    return left if left else right
```
