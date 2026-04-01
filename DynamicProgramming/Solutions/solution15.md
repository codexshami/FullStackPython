# Solution 15: The Matrix Chain (Matrix Chain Multiplication)

## Approach Explanation
We use interval DP. `dp[i][j]` stores the minimum multiplications needed to compute matrices `i` through `j`. We try every possible split point `k` between `i` and `j`.

## Step-by-Step Logic
1. Create a 2D table of size `n x n` (where n = len(p) - 1).
2. Diagonals represent base cases (single matrices, cost = 0).
3. For chain lengths 2 to n:
   - For each starting index `i`:
     - For each split `k`: compute cost and keep the minimum.
4. Return `dp[1][n-1]`.

## Complexity
- **Time Complexity:** O(N^3).
- **Space Complexity:** O(N^2).

## Code
```python
def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):  # chain length
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]
```
