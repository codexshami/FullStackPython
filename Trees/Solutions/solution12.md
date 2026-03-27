# Solution 12: Ancestral Reconstruction

## Approach Explanation
In preorder traversal, the first element is always the `root`. We find this element's position in the `inorder` traversal. All elements to the left in `inorder` are in the left subtree, and all elements to the right are in the right subtree.

## Step-by-Step Logic
1. Base case: If `preorder` or `inorder` is empty, return None.
2. `root_val = preorder[0]`.
3. Create `root = TreeNode(root_val)`.
4. Find index of `root_val` in `inorder` using a map for O(1) lookups.
5. Recursively build left and right subtrees:
   - Left subtree uses `inorder`[:index] and `preorder`[1:index+1].
   - Right subtree uses `inorder`[index+1:] and `preorder`[index+1:].

## Complexity
- **Time Complexity:** O(N), using a hash map to find indices.
- **Space Complexity:** O(N) to store the hash map and nodes.

## Code
```python
def build_tree(preorder, inorder):
    in_map = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0
    
    def helper(left, right):
        nonlocal pre_idx
        if left > right: return None
        
        root_val = preorder[pre_idx]
        root = TreeNode(root_val)
        pre_idx += 1
        
        # Root splits inorder into left and right subtrees
        mid = in_map[root_val]
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        
        return root
        
    return helper(0, len(inorder) - 1)
```
