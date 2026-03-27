# Solution 7: Binary Exponentiation (Pow(x, n))

## Approach Explanation
We use Divide and Conquer. $x^n = (x^{n/2})^2$. Handle negative powers by taking the reciprocal.

## Step-by-Step Logic
1. `solve(x, n)`:
   - Base case: If `n == 0`, return 1.
   - `half = solve(x, n // 2)`.
   - If `n` is even: return `half * half`.
   - If `n` is odd: return `half * half * x`.
2. In the main function, if `n < 0`: return `1 / solve(x, -n)`.

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(log N).

## Code
```python
def my_pow(x, n):
    def solve(x, n):
        if n == 0: return 1
        half = solve(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
            
    if n < 0:
        return 1 / solve(x, abs(n))
    return solve(x, n)
```
