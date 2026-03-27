# Solution 6: Unique Grapheme Spans (Longest Substring Without Repeating Characters)

## Approach Explanation
We use the Sliding Window technique with two pointers and a hash map (or set) to track the indices of characters seen so far.

## Step-by-Step Logic
1. `start = 0`, `max_len = 0`.
2. `used = {}` (map char to last seen index).
3. For `end` from 0 to `len(s) - 1`:
   - If `s[end]` is in `used` and `used[s[end]] >= start`:
     - Move `start` to `used[s[end]] + 1`.
   - Update `max_len = max(max_len, end - start + 1)`.
   - Update `used[s[end]] = end`.
4. Return `max_len`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(min(M, N)), where M is the size of the charset.

## Code
```python
def length_of_longest_substring(s):
    used = {}
    max_len = start = 0
    
    for i, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_len = max(max_len, i - start + 1)
        used[char] = i
        
    return max_len
```
