# Solution 3: Homogenous Transformation (Longest Repeating Character Replacement)

## Approach Explanation
We use a sliding window. A window is valid if `(window_size - max_freq_char) <= k`.

## Step-by-Step Logic
1. `count = {}`, `max_f = 0`, `l = 0`, `res = 0`.
2. For `r` from 0 to `len(s)-1`:
   - `count[s[r]] = count.get(s[r], 0) + 1`.
   - `max_f = max(max_f, count[s[r]])`.
   - If `(r - l + 1) - max_f > k`:
     - `count[s[l]] -= 1`.
     - `l += 1`.
   - `res = max(res, r - l + 1)`.
3. Return `res`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1) (26 characters).

## Code
```python
def character_replacement(s, k):
    count = {}
    res = 0
    l = 0
    max_f = 0
    
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        max_f = max(max_f, count[s[r]])
        
        while (r - l + 1) - max_f > k:
            count[s[l]] -= 1
            l += 1
            
        res = max(res, r - l + 1)
        
    return res
```
