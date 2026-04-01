# Solution 3: The Treasure Heist (House Robber)

## Approach Explanation
At each house, we choose the maximum of: (1) robbing this house + best from two houses back, or (2) skipping this house and keeping the best from the previous house.

## Step-by-Step Logic
1. `dp[i]` = max money we can rob from houses 0..i.
2. `dp[0] = nums[0]`, `dp[1] = max(nums[0], nums[1])`.
3. For each house i >= 2: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`.
4. Return `dp[n-1]`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1) with space optimization.

## Code
```python
def rob(nums):
    if len(nums) == 1:
        return nums[0]
    
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current
    
    return prev1
```
