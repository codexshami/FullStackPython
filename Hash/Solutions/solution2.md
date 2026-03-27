# Solution 2: Cycle Detection (Happy Number)

## Approach Explanation
We use a hash set to detect cycles. If we encounter a sum that we've seen before and it's not 1, the number will never reach 1.

## Step-by-Step Logic
1. Initialize `seen = set()`.
2. While `n != 1` and `n` not in `seen`:
   - `seen.add(n)`.
   - Calculate sum of squares of digits of `n`.
   - Update `n` with this sum.
3. Return `n == 1`.

## Complexity
- **Time Complexity:** O(log N) (finding digits and summing squares).
- **Space Complexity:** O(log N) (to store seen numbers).

## Code
```python
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1
```
