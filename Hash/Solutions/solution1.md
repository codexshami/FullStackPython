# Solution 1: Constant-Time Identification (Two Sum)

## Approach Explanation
We use a hash map to store the values we've seen so far and their indices. For each number `x`, we check if `target - x` is already in the map.

## Step-by-Step Logic
1. Initialize `seen = {}`.
2. Iterate through `nums` with index `i`:
   - `complement = target - nums[i]`.
   - If `complement` is in `seen`, return `[seen[complement], i]`.
   - Otherwise, `seen[nums[i]] = i`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```
