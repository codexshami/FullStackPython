# Solution 1: The Staircase Ascent (Climbing Stairs)

## Approach Explanation
This is essentially the Fibonacci sequence. `dp[i]` represents the number of ways to reach step `i`. We use bottom-up tabulation with O(1) space by only keeping the last two values.

## Step-by-Step Logic
1. Base cases: `dp[1] = 1`, `dp[2] = 2`.
2. For each step from 3 to n: `dp[i] = dp[i-1] + dp[i-2]`.
3. Optimize space by keeping only two variables.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def climb_stairs(n):
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1
```
