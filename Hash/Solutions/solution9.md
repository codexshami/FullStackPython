# Solution 9: Set-Equivalence Bucketing (Group Anagrams)

## Approach Explanation
We use a hash map where the key is either the sorted version of the string or a frequency tuple.

## Step-by-Step Logic
1. Initialize `ans = defaultdict(list)`.
2. For each string `s` in `strs`:
   - Count character frequencies (a-z) into a tuple of size 26.
   - Use this tuple as a key in `ans` and append `s` to the list.
3. Return `ans.values()`.

## Complexity
- **Time Complexity:** O(N * K), where K is the length of the string.
- **Space Complexity:** O(N * K).

## Code
```python
from collections import defaultdict

def group_anagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return list(ans.values())
```
