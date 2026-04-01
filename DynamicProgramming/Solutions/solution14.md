# Solution 14: The Partition Equalizer (Partition Equal Subset Sum)

## Approach Explanation
This reduces to a subset sum problem: can we find a subset that sums to `total_sum / 2`? We use a 1D boolean DP array where `dp[j]` indicates whether sum `j` is achievable.

## Step-by-Step Logic
1. If total sum is odd, return False.
2. Set target = total_sum // 2.
3. Create a boolean `dp` array of size `target + 1`.
4. `dp[0] = True`.
5. For each number, iterate from target down to the number:
   - `dp[j] = dp[j] or dp[j - num]`.
6. Return `dp[target]`.

## Complexity
- **Time Complexity:** O(N * target).
- **Space Complexity:** O(target).

## Code
```python
def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]
```
