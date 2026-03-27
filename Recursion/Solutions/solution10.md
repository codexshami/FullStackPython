# Solution 10: Eliminative Circular Logic (Josephus Problem)

## Approach Explanation
The problem can be solved recursively. If we know the position of the survivor for `n-1` people, we can map it back to the circle of `n` people by shifting by `k`.

## Step-by-Step Logic
1. Base case: If `n == 1`, return 0 (0-indexed).
2. Recursive step: `survivor_pos = (josephus(n - 1, k) + k) % n`.
3. Return `survivor_pos + 1` for 1-indexed result.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N) (stack).

## Code
```python
def find_the_winner(n, k):
    def solve(n, k):
        if n == 1:
            return 0
        return (solve(n - 1, k) + k) % n
        
    return solve(n, k) + 1
```
