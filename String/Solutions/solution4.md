# Solution 4: Mirror Constraint (Palindrome Number)

## Approach Explanation
We can solve this without converting the number to a string by reversing the digits of the integer (or half of it to avoid overflow).

## Step-by-Step Logic
1. If `x < 0` or (`x % 10 == 0` and `x != 0`), return False.
2. Initialize `rev = 0`.
3. While `x > rev`:
   - `rev = rev * 10 + x % 10`.
   - `x //= 10`.
4. Return `True` if `x == rev` (even length) or `x == rev // 10` (odd length).

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(1).

## Code
```python
def is_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
        
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
        
    return x == rev or x == rev // 10
```
