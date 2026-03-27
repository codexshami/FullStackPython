# Solution 1: Character Inversion

## Approach Explanation
We use two pointers, `left` and `right`, starting at the ends of the array and swap them until they meet in the middle.

## Step-by-Step Logic
1. `l = 0`, `r = len(s) - 1`.
2. While `l < r`:
   - Swap `s[l]` and `s[r]`.
   - `l += 1`, `r -= 1`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def reverse_string(s):
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
```
