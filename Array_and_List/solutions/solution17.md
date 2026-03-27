# Solution 17: Infinite Loop Wealth

## Approach Explanation
The maximum sum can either be a normal subarray (found by Kadane) or a circular subarray. A circular subarray's sum is roughly `Total Sum - Minimum Subarray Sum`. We calculate both and take the maximum. Note: if all numbers are negative, the "Total Sum - Min Sum" would result in 0, which is incorrect, so we handle that case.

## Step-by-Step Logic
1. Calculate `max_kadane` using normal Kadane's algorithm.
2. Calculate `min_kadane` by either using Kadane on `-nums` or modifying it to find the minimum.
3. Calculate `total_sum` of the array.
4. If `total_sum == min_kadane`, return `max_kadane`.
5. Otherwise, return `max(max_kadane, total_sum - min_kadane)`.

## Complexity
- **Time Complexity:** O(N), single pass (or two passes) through the array.
- **Space Complexity:** O(1), no extra space.

## Code
```python
def max_circular_sum(nums):
    def kadane(arr):
        max_s = float('-inf')
        curr_s = 0
        for x in arr:
            curr_s += x
            max_s = max(max_s, curr_s)
            if curr_s < 0:
                curr_s = 0
        return max_s

    def min_kadane(arr):
        min_s = float('inf')
        curr_s = 0
        for x in arr:
            curr_s += x
            min_s = min(min_s, curr_s)
            if curr_s > 0:
                curr_s = 0
        return min_s

    total_sum = sum(nums)
    max_normal = kadane(nums)
    min_normal = min_kadane(nums)
    
    # If all elements are negative
    if total_sum == min_normal:
        return max_normal
        
    return max(max_normal, total_sum - min_normal)
```
