# Solution 9: Set-Equivalence Bucketing (Group Anagrams)

## Approach Explanation
We use a hash map where the key is the sorted version of a string (or a character frequency tuple). All anagrams will have the same key.

## Step-by-Step Logic
1. Initialize a hash map `ans = defaultdict(list)`.
2. For each string `s` in `strs`:
   - Create a key: `sorted_s = "".join(sorted(s))`.
   - Append `s` to `ans[sorted_s]`.
3. Return `ans.values()`.

## Complexity
- **Time Complexity:** O(N * K log K), where K is the max length of a string.
- **Space Complexity:** O(N * K).

## Code
```python
from collections import defaultdict

def group_anagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        ans[key].append(s)
    return list(ans.values())
```
