# Solution 17: The Decode Counter (Decode Ways)

## Approach Explanation
`dp[i]` represents the number of ways to decode `s[:i]`. At each position, we check if a single digit or a two-digit number forms a valid decoding.

## Step-by-Step Logic
1. If `s[0] == '0'`, return 0.
2. `dp[0] = 1`, `dp[1] = 1`.
3. For each position `i` from 2 to n:
   - If `s[i-1] != '0'`, add `dp[i-1]` (single digit decode).
   - If `10 <= int(s[i-2:i]) <= 26`, add `dp[i-2]` (two digit decode).
4. Return `dp[n]`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N), reducible to O(1).

## Code
```python
def num_decodings(s):
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]
    
    return dp[n]
```
