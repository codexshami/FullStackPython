# Solution 8: Maximum Specular Span (Longest Palindromic Substring)

## Approach Explanation
We iterate through each character (and each gap between characters) and "expand around center" to find the longest palindrome centered there.

## Step-by-Step Logic
1. Initialize `start = 0`, `end = 0`.
2. For `i` from 0 to `len(s) - 1`:
   - `len1 = expand(i, i)` (odd length).
   - `len2 = expand(i, i + 1)` (even length).
   - `max_len = max(len1, len2)`.
   - If `max_len > end - start`:
     - Update `start = i - (max_len - 1) // 2`.
     - Update `end = i + max_len // 2`.
3. Return `s[start : end + 1]`.

## Complexity
- **Time Complexity:** O(N^2).
- **Space Complexity:** O(1).

## Code
```python
def longest_palindrome(s):
    if not s: return ""
    
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # Length is (r-1) - (l+1) + 1 = r - l - 1
        return r - l - 1
        
    res_start = res_end = 0
    for i in range(len(s)):
        l1 = expand(i, i)
        l2 = expand(i, i + 1)
        mx = max(l1, l2)
        if mx > res_end - res_start:
            res_start = i - (mx - 1) // 2
            res_end = i + mx // 2
            
    return s[res_start : res_end + 1]
```
