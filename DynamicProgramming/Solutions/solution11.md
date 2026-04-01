# Solution 11: The Palindromic Core (Longest Palindromic Substring)

## Approach Explanation
We use the "expand around center" technique. For each character (and each pair of characters), we expand outward while the substring remains a palindrome, tracking the longest one found.

## Step-by-Step Logic
1. For each index `i`, try expanding from `(i, i)` (odd length) and `(i, i+1)` (even length).
2. Expand while characters at both ends match.
3. Track the start and length of the longest palindrome found.

## Complexity
- **Time Complexity:** O(N^2).
- **Space Complexity:** O(1).

## Code
```python
def longest_palindrome(s):
    start, max_len = 0, 1
    
    def expand(left, right):
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1
    
    for i in range(len(s)):
        expand(i, i)       # odd length
        expand(i, i + 1)   # even length
    
    return s[start:start + max_len]
```
