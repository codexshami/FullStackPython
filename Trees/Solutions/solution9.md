# Solution 9: Integrity Audit

## Approach Explanation
A node is valid only if its value is strictly between a `min_value` and a `max_value`. When moving left, we update the `max_value`. When moving right, we update the `min_value`.

## Step-by-Step Logic
1. Define a helper function `validate(node, min_val, max_val)`.
2. If `node` is None, return True.
3. If `node.val` <= `min_val` or `node.val` >= `max_val`, return False.
4. Check subtrees:
   - `validate(node.left, min_val, node.val)`
   - `validate(node.right, node.val, max_val)`
5. Return the logical AND of these checks.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(H).

## Code
```python
def is_valid_bst(root):
    def validate(node, low=-float('inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        
        return (validate(node.left, low, node.val) and 
                validate(node.right, node.val, high))
                
    return validate(root)
```
