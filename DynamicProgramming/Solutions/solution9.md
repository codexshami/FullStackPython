# Solution 9: The Maximum Subarray (Kadane's Algorithm)

## Approach Explanation
At each position, we decide: start a new subarray here, or extend the current one. We track the maximum sum seen so far. This is a classic DP problem disguised as a greedy algorithm.

## Step-by-Step Logic
1. Initialize `current_sum = nums[0]` and `max_sum = nums[0]`.
2. For each element from index 1:
   - `current_sum = max(nums[i], current_sum + nums[i])`.
   - `max_sum = max(max_sum, current_sum)`.
3. Return `max_sum`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def max_subarray(nums):
    current_sum = max_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```
