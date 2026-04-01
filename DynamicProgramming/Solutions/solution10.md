# Solution 10: The Unique Pathfinder (Unique Paths)

## Approach Explanation
`dp[i][j]` represents the number of unique paths to reach cell `(i, j)`. The robot can only move right or down, so `dp[i][j] = dp[i-1][j] + dp[i][j-1]`.

## Step-by-Step Logic
1. Create an `m x n` table.
2. Initialize first row and first column to 1 (only one way to reach any cell in these).
3. For each cell `(i, j)`: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`.
4. Return `dp[m-1][n-1]`.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N), reducible to O(N).

## Code
```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[m - 1][n - 1]
```
