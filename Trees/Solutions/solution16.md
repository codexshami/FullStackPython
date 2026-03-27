# Solution 16: Maximal Segment Sum

## Approach Explanation
We use DFS to calculate the maximum gain from each subtree. For each node, the "maximum path passing through it" is `node.val + left_gain + right_gain`. We update the global maximum using this value. However, the node returns only `node.val + max(left_gain, right_gain)` to its parent.

## Step-by-Step Logic
1. Initialize `max_sum = -infinity`.
2. Define `get_gain(node)`:
   - If `node` is None, return 0.
   - `left_gain = max(get_gain(node.left), 0)` (ignore negative gains).
   - `right_gain = max(get_gain(node.right), 0)`.
   - `curr_path_sum = node.val + left_gain + right_gain`.
   - Update `max_sum = max(max_sum, curr_path_sum)`.
   - Return `node.val + max(left_gain, right_gain)`.
3. Call `get_gain(root)`.
4. Return `max_sum`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(H).

## Code
```python
def max_path_sum(root):
    ans = -float('inf')
    
    def get_gain(node):
        nonlocal ans
        if not node:
            return 0
            
        # Only consider positive gains
        left_gain = max(get_gain(node.left), 0)
        right_gain = max(get_gain(node.right), 0)
        
        # This node is the "highest" point of the path
        curr_sum = node.val + left_gain + right_gain
        ans = max(ans, curr_sum)
        
        # Return the best path starting from this node downwards
        return node.val + max(left_gain, right_gain)
        
    get_gain(root)
    return ans
```
