# Solution 2: The Golden Sequence Optimized (Fibonacci with DP)

## Approach Explanation
We use bottom-up tabulation to avoid the exponential time of naive recursion. We iterate from 0 to n, building the solution.

## Step-by-Step Logic
1. Create a `dp` array of size `n + 1`.
2. Set `dp[0] = 0`, `dp[1] = 1`.
3. For `i` from 2 to n: `dp[i] = dp[i-1] + dp[i-2]`.
4. Return `dp[n]`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1) with space optimization.

## Code
```python
def fib(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1
```
