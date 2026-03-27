# Solution 19: Vertical Alignment

## Approach Explanation
We perform a DFS traversal and record the `(row, col, value)` of each node. We store these in a list, then sort the list primarily by `col`, then by `row`, then by `value`. Finally, we group them by `col`.

## Step-by-Step Logic
1. Perform DFS with coordinates: `(node, row, col)`.
2. Store every node as `(col, row, val)` in a list.
3. Sort the list.
4. Iterate through the sorted list and group nodes with the same `col` into sub-lists.
5. Return the list of groups.

## Complexity
- **Time Complexity:** O(N log N) due to sorting.
- **Space Complexity:** O(N).

## Code
```python
def vertical_traversal(root):
    nodes = [] # Store (col, row, val)
    
    def dfs(node, r, c):
        if not node: return
        nodes.append((c, r, node.val))
        dfs(node.left, r + 1, c - 1)
        dfs(node.right, r + 1, c + 1)
        
    dfs(root, 0, 0)
    nodes.sort()
    
    res = []
    if not nodes: return res
    
    # Group by col
    curr_col = nodes[0][0]
    curr_group = []
    for c, r, v in nodes:
        if c == curr_col:
            curr_group.append(v)
        else:
            res.append(curr_group)
            curr_group = [v]
            curr_col = c
    res.append(curr_group)
    
    return res
```
