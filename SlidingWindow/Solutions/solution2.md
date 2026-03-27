# Solution 2: Minimum Inclusive Span (Minimum Window Substring)

## Approach Explanation
We use a sliding window where `r` expands the window and `l` shrinks it once the window is valid (contains all characters of `t`).

## Step-by-Step Logic
1. Count characters in `t`.
2. `l = 0`, `r = 0`. `have = 0`, `need = len(t_count)`.
3. Expand `r`:
   - Update window counts. If char count matches `t_count`, `have += 1`.
   - While `have == need`:
     - Update min window result.
     - Shrink `l`. update counts. If count drops below `t_count`, `have -= 1`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(M).

## Code
```python
from collections import Counter

def min_window(s, t):
    if not t: return ""
    
    count_t, window = Counter(t), {}
    have, need = 0, len(count_t)
    res, res_len = [-1, -1], float("infinity")
    l = 0
    
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        
        if c in count_t and window[c] == count_t[c]:
            have += 1
            
        while have == need:
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1
            
            window[s[l]] -= 1
            if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                have -= 1
            l += 1
            
    l, r = res
    return s[l : r + 1] if res_len != float("infinity") else ""
```
