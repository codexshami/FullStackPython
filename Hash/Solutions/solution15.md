# Solution 15: Sliding Permutation Window (Find All Anagrams in a String)

## Approach Explanation
We use a sliding window of size `len(p)` and compare the character frequencies of the window with the frequencies of `p`.

## Step-by-Step Logic
1. Count frequencies of `p` in `pCount` map.
2. Maintain `sCount` for the current window in `s`.
3. As we slide the window:
   - Add the new char to `sCount`.
   - Remove the old char (leftmost) from `sCount`.
   - If `sCount == pCount`, add start index to result.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1) (alphabet size).

## Code
```python
from collections import Counter

def find_anagrams(s, p):
    ns, np = len(s), len(p)
    if ns < np: return []
    
    p_count = Counter(p)
    s_count = Counter(s[:np])
    
    res = []
    if s_count == p_count:
        res.append(0)
        
    for i in range(1, ns - np + 1):
        # Update window
        prev_char = s[i-1]
        new_char = s[i + np - 1]
        
        s_count[new_char] += 1
        s_count[prev_char] -= 1
        
        if s_count[prev_char] == 0:
            del s_count[prev_char]
            
        if s_count == p_count:
            res.append(i)
            
    return res
```
