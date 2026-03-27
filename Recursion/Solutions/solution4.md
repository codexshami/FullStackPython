# Solution 4: Binary Decision Tree (Search in a Binary Search Tree)

## Approach Explanation
The property of BST (left < root < right) allows us to eliminate half of the tree in each recursive step.

## Step-by-Step Logic
1. Base case: If `root` is None or `root.val == val`, return `root`.
2. If `val < root.val`:
   - Search in the left subtree: `return searchBST(root.left, val)`.
3. Else:
   - Search in the right subtree: `return searchBST(root.right, val)`.

## Complexity
- **Time Complexity:** O(H) where H is tree height.
- **Space Complexity:** O(H).

## Code
```python
def search_bst(root, val):
    if not root or root.val == val:
        return root
    
    if val < root.val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)
```
