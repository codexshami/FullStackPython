# Solution 14: Horizontal Linkage

## Approach Explanation
We use the already established `next` pointers from the level above to connect nodes in the current level. For a node `curr`, its left child's next is `curr.right`, and its right child's next is `curr.next.left` (if `curr.next` exists).

## Step-by-Step Logic
1. Start with `leftmost = root`.
2. While `leftmost.left` exists:
   - `curr = leftmost`
   - While `curr`:
     - `curr.left.next = curr.right`
     - If `curr.next`:
       - `curr.right.next = curr.next.left`
     - `curr = curr.next`
   - `leftmost = leftmost.left` (move to next level).
3. Return `root`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1), using only pointers.

## Code
```python
def connect(root):
    if not root:
        return root
        
    leftmost = root
    
    while leftmost.left:
        # Traverse the list of nodes at the current level
        curr = leftmost
        while curr:
            # Connection 1: children of same parent
            curr.left.next = curr.right
            # Connection 2: between children of adjacent parents
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
        # Move to the start of the next level
        leftmost = leftmost.left
        
    return root
```
