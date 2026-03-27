# Solution 6: Distributed Anagram Search (Find All Anagrams in a String)

## Approach Explanation
We use a sliding window of size `len(p)` and compare character counts. We can optimize by tracking the number of "matches" (character counts that are exactly equal).

## Step-by-Step Logic
1. If `len(p) > len(s)`, return [].
2. Count frequencies of `p` and the first `len(p)` chars of `s`.
3. Slide the window:
   - If window's `Counter` equals `p`'s `Counter`, add start index to result.
   - Update `Counter` by adding one character from right and removing one from left.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1) (26 characters).

## Code
```python
from collections import Counter

def find_anagrams(s, p):
    res = []
    ns, np = len(s), len(p)
    if np > ns: return res
    
    pCount = Counter(p)
    sCount = Counter(s[:np])
    
    if pCount == sCount:
        res.append(0)
        
    for i in range(1, ns - np + 1):
        sCount[s[i-1]] -= 1
        if sCount[s[i-1]] == 0:
            del sCount[s[i-1]]
        sCount[s[i+np-1]] += 1
        
        if pCount == sCount:
            res.append(i)
            
    return res
```
