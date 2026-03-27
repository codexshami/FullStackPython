# Solution 1: Golden Ratio Sequence (Fibonacci Number)

## Approach Explanation
We use a simple recursive approach with base cases `F(0)` and `F(1)`. While O(2^N) is slow, it demonstrates the core concept of recursion.

## Step-by-Step Logic
1. Base case: If `n == 0`, return 0.
2. Base case: If `n == 1`, return 1.
3. Recursive step: Return `fib(n-1) + fib(n-2)`.

## Complexity
- **Time Complexity:** O(2^N).
- **Space Complexity:** O(N) (recursion stack).

## Code
```python
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)
```
*(Note: In real interviews, you should mention Memoization or Iterative approach to optimize this).*
