# Solution 18: Shortest Stretch for Target

## Approach Explanation
We use the sliding window (two-pointer) technique. We expand the window from the right until the sum is greater than or equal to `target`. Then we shrink the window from the left as much as possible while maintaining the sum condition, updating the `min_length` at each step.

## Step-by-Step Logic
1. Initialize `left = 0`, `current_sum = 0`, and `min_len = infinity`.
2. Iterate `right` from 0 to `n-1`:
   - `current_sum += nums[right]`.
   - While `current_sum >= target`:
     - `min_len = min(min_len, right - left + 1)`.
     - `current_sum -= nums[left]`.
     - `left += 1`.
3. If `min_len` was never updated, return 0.
4. Return `min_len`.

## Complexity
- **Time Complexity:** O(N), as each pointer visits each element once.
- **Space Complexity:** O(1), no extra storage.

## Code
```python
def min_subarray_len(nums, target):
    left = 0
    current_sum = 0
    min_len = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= target:
            # Update minimum length
            min_len = min(min_len, right - left + 1)
            # Shrink from the left
            current_sum -= nums[left]
            left += 1
            
    return min_len if min_len != float('inf') else 0
```
