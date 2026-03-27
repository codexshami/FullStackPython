# Solution 2: Vertical Span

## Approach Explanation
We use a recursive DFS approach. The depth of a node is `1 + max(depth of left child, depth of right child)`.

## Step-by-Step Logic
1. If `root` is None, return 0.
2. Calculate `left_depth = max_depth(root.left)`.
3. Calculate `right_depth = max_depth(root.right)`.
4. Return `max(left_depth, right_depth) + 1`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(H).

## Code
```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```
