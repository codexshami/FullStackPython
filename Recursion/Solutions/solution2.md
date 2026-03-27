# Solution 2: Logarithmic Divisibility (Power of Three)

## Approach Explanation
We recursively divide `n` by 3. If we reach 1, it's a power of three. If we reach a number not divisible by 3 (and not 1), it's not.

## Step-by-Step Logic
1. If `n <= 0`, return False.
2. If `n == 1`, return True.
3. If `n % 3 != 0`, return False.
4. Recursive step: Return `is_power_of_three(n // 3)`.

## Complexity
- **Time Complexity:** O(log3 N).
- **Space Complexity:** O(log3 N).

## Code
```python
def is_power_of_three(n):
    if n <= 0: return False
    if n == 1: return True
    return n % 3 == 0 and is_power_of_three(n // 3)
```
