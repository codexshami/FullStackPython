# Solution 7: The Longest Rising Tide (Longest Increasing Subsequence)

## Approach Explanation
`dp[i]` is the length of the LIS ending at index `i`. For each element, we check all previous elements. If `nums[j] < nums[i]`, we can extend the LIS ending at `j`.

## Step-by-Step Logic
1. Initialize `dp` array with all 1s (each element is a subsequence of length 1).
2. For each `i`, check all `j < i`:
   - If `nums[j] < nums[i]`, update `dp[i] = max(dp[i], dp[j] + 1)`.
3. Return the maximum value in `dp`.

## Complexity
- **Time Complexity:** O(N^2). (Can be optimized to O(N log N) with binary search.)
- **Space Complexity:** O(N).

## Code
```python
def length_of_lis(nums):
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```
