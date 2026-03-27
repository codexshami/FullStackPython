# Solution 20: Sorting Discordance (BST)

## Approach Explanation
An inorder traversal of a valid BST is sorted. If two nodes are swapped, there will be one or two locations where `curr.val < prev.val`. We find these "dropped" values and swap them back.

## Step-by-Step Logic
1. Initialize `first = None`, `second = None`, and `prev = TreeNode(-infinity)`.
2. Perform an inorder traversal (Recursive or Iterative).
3. In each step:
   - If `curr.val < prev.val`:
     - If `first` is None: `first = prev` (the first problematic node).
     - `second = curr` (the second problematic node).
   - `prev = curr`.
4. After traversal, swap values: `first.val, second.val = second.val, first.val`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(H).

## Code
```python
def recover_tree(root):
    first = second = prev = None
    
    def inorder(node):
        nonlocal first, second, prev
        if not node: return
        
        inorder(node.left)
        
        # Inorder property violation
        if prev and node.val < prev.val:
            if not first:
                first = prev
            second = node
        prev = node
        
        inorder(node.right)
        
    inorder(root)
    # Swap the values
    if first and second:
        first.val, second.val = second.val, first.val
```
