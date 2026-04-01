# Solution 5: The Knapsack Challenge (0/1 Knapsack)

## Approach Explanation
We use a 2D DP table where `dp[i][w]` represents the max value achievable using items 0..i-1 with knapsack capacity w. For each item, we either include it (if it fits) or skip it.

## Step-by-Step Logic
1. Create a `(n+1) x (W+1)` table initialized to 0.
2. For each item `i` and capacity `w`:
   - If `weights[i-1] <= w`: `dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])`.
   - Else: `dp[i][w] = dp[i-1][w]`.
3. Return `dp[n][W]`.

## Complexity
- **Time Complexity:** O(N * W).
- **Space Complexity:** O(N * W), reducible to O(W).

## Code
```python
def knapsack(W, weights, values):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
    
    return dp[n][W]
```
