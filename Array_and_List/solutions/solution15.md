# Solution 15: Strategic Leapfrog

## Approach Explanation
This can be solved using a greedy approach. We maintain a variable `max_reachable` that keeps track of the farthest index we can reach. If at any point the current index is greater than `max_reachable`, we can't move forward and return `False`.

## Step-by-Step Logic
1. Initialize `max_reachable = 0`.
2. Iterate through index `i` and value `jump` in `nums`:
   - If `i > max_reachable`, it means we can't reach this index, so return `False`.
   - Update `max_reachable = max(max_reachable, i + jump)`.
   - If `max_reachable` is already at or past the last index, return `True`.
3. Return `True` if the loop completes (though it usually returns within the loop).

## Complexity
- **Time Complexity:** O(N), single pass through the array.
- **Space Complexity:** O(1), only one extra variable.

## Code
```python
def can_jump(nums):
    max_reachable = 0
    n = len(nums)
    
    for i in range(n):
        # If the current index is unreachable
        if i > max_reachable:
            return False
            
        # Update the farthest index we can reach
        max_reachable = max(max_reachable, i + nums[i])
        
        # If we can already reach the end
        if max_reachable >= n - 1:
            return True
            
    return True
```
