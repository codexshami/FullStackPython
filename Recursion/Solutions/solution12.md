# Solution 12: Stairway to Summit (Climbing Stairs)

## Approach Explanation
At each step, we can take 1 or 2 steps. The total ways to reach step `n` is the sum of ways to reach step `n-1` and step `n-2`. We use memoization to avoid redundant computation.

## Step-by-Step Logic
1. Base cases: If `n == 1`, return 1. If `n == 2`, return 2.
2. Recursive step: Return `climb(n-1) + climb(n-2)`.
3. Use a memo dictionary to cache results.

## Complexity
- **Time Complexity:** O(N) with memoization.
- **Space Complexity:** O(N) (memo + recursion stack).

## Code
```python
def climb_stairs(n, memo={}):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in memo:
        return memo[n]
    
    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    return memo[n]
```
