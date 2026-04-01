# Solution 18: The Maximal Square (Maximal Square)

## Approach Explanation
`dp[i][j]` represents the side length of the largest square whose bottom-right corner is at `(i, j)`. If `matrix[i][j] == '1'`, we take the minimum of top, left, and top-left neighbors and add 1.

## Step-by-Step Logic
1. Create a DP table of same size as matrix.
2. Copy the first row and column from the matrix.
3. For each cell `(i, j)` where `matrix[i][j] == '1'`:
   - `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`.
4. Track the maximum value in the DP table.
5. Return `max_side^2`.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N).

## Code
```python
def maximal_square(matrix):
    if not matrix:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    
    return max_side ** 2
```
