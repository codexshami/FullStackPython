# Solution 7: Targeted Segment Sum

## Approach Explanation
Since all elements are non-negative, we can use the sliding window (two-pointer) technique. We maintain a window `[start, end]` and its `current_sum`. If `current_sum` is less than `target`, we expand the window by moving `end`. If it's more, we contract it by moving `start`.

## Step-by-Step Logic
1. Initialize `start = 0` and `current_sum = 0`.
2. Iterate `end` from 0 to `n-1`:
   - Add `nums[end]` to `current_sum`.
   - While `current_sum > target` and `start < end`:
     - Subtract `nums[start]` from `current_sum`.
     - Increment `start`.
   - If `current_sum == target`:
     - Return `[start, end]`.
3. If loop ends without finding the target, return `[-1, -1]`.

## Complexity
- **Time Complexity:** O(N), as each element is added and removed from the window at most once.
- **Space Complexity:** O(1), only a few scalar variables.

## Code
```python
def subarray_sum(nums, target):
    start = 0
    current_sum = 0
    
    for end in range(len(nums)):
        current_sum += nums[end]
        
        while current_sum > target and start < end:
            current_sum -= nums[start]
            start += 1
            
        if current_sum == target:
            return [start, end]
            
    return [-1, -1]
```
