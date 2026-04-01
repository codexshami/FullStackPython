# Solution 4: The Longest Common Thread (Longest Common Subsequence)

## Approach Explanation
We build a 2D DP table where `dp[i][j]` is the LCS length of `text1[:i]` and `text2[:j]`. If characters match, we extend the LCS by 1; otherwise, we take the max of excluding either character.

## Step-by-Step Logic
1. Create a `(m+1) x (n+1)` table initialized to 0.
2. For each pair `(i, j)`:
   - If `text1[i-1] == text2[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1`.
   - Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.
3. Return `dp[m][n]`.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N).

## Code
```python
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]
```
