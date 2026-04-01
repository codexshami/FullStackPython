# Solution 8: The Edit Distance (Edit Distance / Levenshtein Distance)

## Approach Explanation
We build a 2D DP table where `dp[i][j]` is the minimum operations to convert `word1[:i]` to `word2[:j]`. Transitions: insert, delete, or replace.

## Step-by-Step Logic
1. Create a `(m+1) x (n+1)` table.
2. Base cases: `dp[i][0] = i` (delete all), `dp[0][j] = j` (insert all).
3. For each `(i, j)`:
   - If characters match: `dp[i][j] = dp[i-1][j-1]`.
   - Else: `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`.
4. Return `dp[m][n]`.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N).

## Code
```python
def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # delete
                                   dp[i][j - 1],      # insert
                                   dp[i - 1][j - 1])  # replace
    
    return dp[m][n]
```
