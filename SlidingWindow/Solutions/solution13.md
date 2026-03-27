# Solution 13: Parity Equivalence Span (Replace the Substring for Balanced String)

## Approach Explanation
We want to find the shortest window such that the characters *outside* the window do not exceed `n/4` for any character 'Q', 'W', 'E', 'R'.

## Step-by-Step Logic
1. Count the initial frequencies of 'Q', 'W', 'E', 'R' in `s`.
2. Target frequency `target = n // 4`.
3. If all frequencies `<= target`, return 0.
4. Use a sliding window `[l, r]`:
   - "Remove" `s[r]` from the counts of characters outside.
   - While all counts outside are `<= target`:
     - Update minimum length `r - l + 1`.
     - "Add" `s[l]` back to the counts outside and increment `l`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
from collections import Counter

def balanced_string(s):
    n = len(s)
    count = Counter(s)
    target = n // 4
    
    # Check if already balanced
    if all(count[c] <= target for c in "QWER"):
        return 0
        
    res = n
    l = 0
    for r in range(n):
        count[s[r]] -= 1
        while l < n and all(count[c] <= target for c in "QWER"):
            res = min(res, r - l + 1)
            count[s[l]] += 1
            l += 1
            
    return res
```
