# Solution 3: Stack-Based Inversion (Reverse String - Recursive)

## Approach Explanation
We use a helper function with two pointers `l` and `r`. We swap `s[l]` and `s[r]` and then recurse for the inner part of the string.

## Step-by-Step Logic
1. Helper function `solve(l, r)`:
   - Base case: If `l >= r`, return.
   - Swap `s[l]` and `s[r]`.
   - `solve(l + 1, r - 1)`.
2. Call `solve(0, len(s) - 1)`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N) (stack).

## Code
```python
def reverse_string(s):
    def solve(l, r):
        if l >= r:
            return
        s[l], s[r] = s[r], s[l]
        solve(l + 1, r - 1)
        
    solve(0, len(s) - 1)
```
