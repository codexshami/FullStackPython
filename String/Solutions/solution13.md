# Solution 13: Minimum Inclusive Span (Minimum Window Substring)

## Approach Explanation
We use the Sliding Window technique with two pointers. We maintain a count of characters in the current window and compare it with the required counts from `t`.

## Step-by-Step Logic
1. Count frequencies of `t`.
2. `l = 0`, `r = 0`. Use a variable `have` to track how many unique characters in `t` are satisfied in the window.
3. Move `r` until the window contains all characters from `t`.
4. While the window is valid, move `l` to minimize the length.
5. Track the best `[l, r]` found.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(M), where M is number of unique characters.

## Code
```python
from collections import Counter

def min_window(s, t):
    if not t or not s: return ""
    
    dict_t = Counter(t)
    required = len(dict_t)
    
    l, r = 0, 0
    have = 0
    window_counts = {}
    
    # result: [length, l, r]
    ans = [float("inf"), None, None]
    
    while r < len(s):
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in dict_t and window_counts[char] == dict_t[char]:
            have += 1
            
        while have == required:
            # Update result
            if (r - l + 1) < ans[0]:
                ans = [r - l + 1, l, r]
            
            # Shrink from left
            char_l = s[l]
            window_counts[char_l] -= 1
            if char_l in dict_t and window_counts[char_l] < dict_t[char_l]:
                have -= 1
            l += 1
            
        r += 1
        
    return s[ans[1] : ans[2] + 1] if ans[0] != float("inf") else ""
```
