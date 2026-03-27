# Solution 3: Multi-set Equivalence (Valid Anagram)

## Approach Explanation
Two strings are anagrams if they have the same character counts.

## Step-by-Step Logic
1. If lengths of `s` and `t` are different, return False.
2. Count characters in `s` and `t` using `Counter` (or hash maps).
3. If the counts are equal, return True.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1) (alphabet size).

## Code
```python
from collections import Counter

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
```
