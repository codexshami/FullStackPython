# Solution 11: The Digital Root (Sum of Digits)

## Approach Explanation
We recursively sum the digits of the number. If the result is a single digit, return it. Otherwise, recurse again on the sum.

## Step-by-Step Logic
1. Base case: If `num < 10`, return `num`.
2. Compute digit sum by taking `num % 10` (last digit) + recursive call on `num // 10`.
3. If the digit sum is >= 10, recurse on the digit sum.

## Complexity
- **Time Complexity:** O(log N) per pass, O(log N) passes in worst case.
- **Space Complexity:** O(log N) (recursion stack).

## Code
```python
def digital_root(num):
    if num < 10:
        return num
    
    def digit_sum(n):
        if n == 0:
            return 0
        return n % 10 + digit_sum(n // 10)
    
    return digital_root(digit_sum(num))
```
