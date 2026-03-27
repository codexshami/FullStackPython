# Solution 19: Minimal Fusion Cost

## Approach Explanation
This is a Dynamic Programming problem (specifically Interval DP). We define `dp[i][j]` as the minimum cost to merge piles from `i` to `j` into as few piles as possible. The number of piles will be reduced by `k-1` in each merge. For a set of `n` piles, they can be merged into one if `(n-1) % (k-1) == 0`.

## Step-by-Step Logic
1. Check if merge is possible: `(len(stones)-1) % (k-1) != 0`.
2. Use a prefix sum array for fast sum calculation of any range.
3. `dp[i][j]` is computed for all interval lengths.
4. For each interval `[i, j]`, we split it at `m` and compute `dp[i][m] + dp[m+1][j]`.
5. If the current interval `[i, j]` can be merged into one pile, add its total sum to `dp[i][j]`.

## Complexity
- **Time Complexity:** O(N^3 / K), where N is the number of piles.
- **Space Complexity:** O(N^2), for the DP table.

## Code
```python
def merge_stones(stones, k):
    n = len(stones)
    if (n - 1) % (k - 1) != 0:
        return -1
        
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        
    dp = [[0] * n for _ in range(n)]
    
    for length in range(k, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            # Split intervals
            for m in range(i, j, k - 1):
                dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j])
                
            # If current range can be merged into one pile
            if (length - 1) % (k - 1) == 0:
                dp[i][j] += prefix_sum[j + 1] - prefix_sum[i]
                
    return dp[0][n - 1]
```
