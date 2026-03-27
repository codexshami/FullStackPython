# Solution 1: Unique Grapheme Spans (Longest Substring Without Repeating Characters)

## Approach Explanation
We use a sliding window with two pointers (`left` and `right`) and a hash map to store the last seen index of each character.

## Step-by-Step Logic
1. `l = 0`, `res = 0`.
2. `char_map = {}`.
3. For `r` from 0 to `len(s)-1`:
   - If `s[r]` is in `char_map`:
     - Update `l = max(l, char_map[s[r]] + 1)`.
   - Update `res = max(res, r - l + 1)`.
   - `char_map[s[r]] = r`.
4. Return `res`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(min(N, M)) where M is the charset size.

## Code
```python
def length_of_longest_substring(s):
    l = 0
    res = 0
    char_map = {}
    
    for r in range(len(s)):
        if s[r] in char_map:
            l = max(l, char_map[s[r]] + 1)
        res = max(res, r - l + 1)
        char_map[s[r]] = r
        
    return res
```
