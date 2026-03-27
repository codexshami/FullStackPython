# Solution 7: Minimal Contiguous Span (Minimum Size Subarray Sum)

## Approach Explanation
We use a sliding window with two pointers. We increment the right pointer to add elements until the sum >= target, then increment the left pointer to find the minimum length.

## Step-by-Step Logic
1. `l = 0`, `curr_sum = 0`, `res = float('inf')`.
2. For each `r`, `curr_sum += nums[r]`.
3. While `curr_sum >= target`:
   - `res = min(res, r - l + 1)`.
   - `curr_sum -= nums[l]`.
   - `l += 1`.
4. Return `res` if it was modified, else 0.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def min_sub_array_len(target, nums):
    l = 0
    curr_sum = 0
    res = float('inf')
    
    for r in range(len(nums)):
        curr_sum += nums[r]
        while curr_sum >= target:
            res = min(res, r - l + 1)
            curr_sum -= nums[l]
            l += 1
            
    return res if res != float('inf') else 0
```
