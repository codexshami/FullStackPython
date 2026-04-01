# Solution 13: The Word Breaker (Word Break)

## Approach Explanation
`dp[i]` is True if `s[:i]` can be segmented into dictionary words. For each position `i`, we check all possible previous positions `j` where `dp[j]` is True and `s[j:i]` is in the dictionary.

## Step-by-Step Logic
1. Create a boolean `dp` array of size `n + 1`, with `dp[0] = True`.
2. For each position `i` from 1 to n:
   - For each `j` from 0 to i: if `dp[j]` is True and `s[j:i]` is in `wordDict`, set `dp[i] = True`.
3. Return `dp[n]`.

## Complexity
- **Time Complexity:** O(N^2 * M) where M is the max word length.
- **Space Complexity:** O(N).

## Code
```python
def word_break(s, word_dict):
    word_set = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[n]
```
