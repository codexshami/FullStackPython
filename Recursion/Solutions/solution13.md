# Solution 13: The String Reverser (Reverse String Recursively)

## Approach Explanation
We use recursion with two pointers (left and right) to swap characters from both ends, moving inward until they meet.

## Step-by-Step Logic
1. Define a helper function with `left` and `right` indices.
2. Base case: If `left >= right`, return.
3. Swap `s[left]` and `s[right]`.
4. Recurse with `left + 1` and `right - 1`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N) (recursion stack).

## Code
```python
def reverse_string(s):
    def helper(left, right):
        if left >= right:
            return
        s[left], s[right] = s[right], s[left]
        helper(left + 1, right - 1)
    
    helper(0, len(s) - 1)
```
