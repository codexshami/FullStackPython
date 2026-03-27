# Solution 1: Mirror Validation (Valid Palindrome)

## Approach Explanation
We use two pointers, one starting at the beginning (`l`) and one at the end (`r`). We move them towards the center, skipping non-alphanumeric characters and comparing values.

## Step-by-Step Logic
1. Initialize `l = 0`, `r = len(s) - 1`.
2. While `l < r`:
   - While `l < r` and `s[l]` is not alphanumeric, increment `l`.
   - While `l < r` and `s[r]` is not alphanumeric, decrement `r`.
   - If `s[l].lower() != s[r].lower()`, return False.
   - Increment `l`, decrement `r`.
3. Return True if the loop completes.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def is_palindrome(s):
    l, r = 0, len(s) - 1
    
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
            
        if s[l].lower() != s[r].lower():
            return False
            
        l += 1
        r -= 1
        
    return True
```
