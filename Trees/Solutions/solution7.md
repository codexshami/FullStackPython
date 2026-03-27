# Solution 7: Familial Nexus (BST)

## Approach Explanation
In a BST, the LCA is the first node whose value is between `p.val` and `q.val`. If both `p` and `q` are smaller than the root, the LCA must be in the left subtree. If both are larger, it's in the right subtree.

## Step-by-Step Logic
1. Start at the `root`.
2. While `curr` is not None:
   - If `p.val` and `q.val` are both smaller than `curr.val`, move `curr = curr.left`.
   - Else if `p.val` and `q.val` are both larger than `curr.val`, move `curr = curr.right`.
   - Otherwise, `curr` is the LCA. return `curr`.

## Complexity
- **Time Complexity:** O(H).
- **Space Complexity:** O(1).

## Code
```python
def lowest_common_ancestor_bst(root, p, q):
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr
```
