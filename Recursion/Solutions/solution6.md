# Solution 6: Combinatorial Stairwell (Climbing Stairs)

## Approach Explanation
The number of ways to reach step `n` is the sum of ways to reach `n-1` and `n-2`. This is a Fibonacci-like recurrence. To avoid exponential time, we use a simple recursion with a dictionary for memoization.

## Step-by-Step Logic
1. `memo = {}`.
2. `solve(n)`:
   - Base case: If `n <= 2`, return `n`.
   - If `n` in `memo`, return `memo[n]`.
   - `memo[n] = solve(n - 1) + solve(n - 2)`.
   - Return `memo[n]`.

## Complexity
- **Time Complexity:** O(N) with memoization.
- **Space Complexity:** O(N).

## Code
```python
def climb_stairs(n):
    memo = {}
    def solve(n):
        if n <= 2: return n
        if n in memo: return memo[n]
        memo[n] = solve(n - 1) + solve(n - 2)
        return memo[n]
    return solve(n)
```
