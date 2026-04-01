# Solution 20: The Rod Cutter (Rod Cutting Problem)

## Approach Explanation
`dp[i]` represents the maximum revenue obtainable from a rod of length `i`. For each length, we try all possible first cuts and take the maximum.

## Step-by-Step Logic
1. Create `dp` array of size `n + 1`, initialized to 0.
2. For each length `i` from 1 to n:
   - For each cut length `j` from 1 to i:
     - `dp[i] = max(dp[i], price[j-1] + dp[i-j])`.
3. Return `dp[n]`.

## Complexity
- **Time Complexity:** O(N^2).
- **Space Complexity:** O(N).

## Code
```python
def rod_cutting(price, n):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], price[j - 1] + dp[i - j])
    
    return dp[n]
```
