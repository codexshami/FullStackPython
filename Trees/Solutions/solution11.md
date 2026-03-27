# Solution 11: Path Manifest

## Approach Explanation
We use DFS to explore all paths. We keep track of the `current_path` and the `remaining_sum`. When we reach a leaf, we check if the `remaining_sum` equals the leaf's value.

## Step-by-Step Logic
1. Define a helper `dfs(node, current_path, current_sum)`.
2. If `node` is None, return.
3. Add `node.val` to `current_path`.
4. If `node` is a leaf and sum matches:
   - Add a copy of `current_path` to `result`.
5. Else:
   - Recurse left: `dfs(node.left, current_path, targetSum - node.val)`.
   - Recurse right: `dfs(node.right, current_path, targetSum - node.val)`.
6. **Backtrack:** Remove `node.val` from `current_path` before returning to parent.

## Complexity
- **Time Complexity:** O(N^2) in worst case (skewed tree and many valid paths) because of path copying.
- **Space Complexity:** O(H).

## Code
```python
def path_sum(root, targetSum):
    res = []
    
    def dfs(node, path, s):
        if not node:
            return
            
        path.append(node.val)
        
        # Leaf node check
        if not node.left and not node.right and s == node.val:
            res.append(list(path)) # Copy current path
            
        dfs(node.left, path, s - node.val)
        dfs(node.right, path, s - node.val)
        
        # Backtrack
        path.pop()
        
    dfs(root, [], targetSum)
    return res
```
