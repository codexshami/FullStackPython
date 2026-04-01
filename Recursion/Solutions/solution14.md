# Solution 14: The Palindrome Detective (Check Palindrome Recursively)

## Approach Explanation
We compare characters from both ends of the string, recursing inward. If all paired characters match, the string is a palindrome.

## Step-by-Step Logic
1. Clean the string: keep only alphanumeric characters, convert to lowercase.
2. Define a helper with `left` and `right` indices.
3. Base case: If `left >= right`, return True.
4. If characters at `left` and `right` don't match, return False.
5. Recurse with `left + 1` and `right - 1`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N) (recursion stack + cleaned string).

## Code
```python
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    def helper(left, right):
        if left >= right:
            return True
        if cleaned[left] != cleaned[right]:
            return False
        return helper(left + 1, right - 1)
    
    return helper(0, len(cleaned) - 1)
```
