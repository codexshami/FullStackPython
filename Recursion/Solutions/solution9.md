# Solution 9: Zero-Sum Game Theory (Predict the Winner)

## Approach Explanation
We use recursion to find the maximum possible relative score (score1 - score2).
`f(i, j) = max(nums[i] - f(i+1, j), nums[j] - f(i, j-1))`.

## Step-by-Step Logic
1. `solve(l, r)`:
   - Base case: If `l == r`, return `nums[l]`.
   - Option 1: Pick `nums[l]`. Remaining score diff = `nums[l] - solve(l + 1, r)`.
   - Option 2: Pick `nums[r]`. Remaining score diff = `nums[r] - solve(l, r - 1)`.
   - Return `max(Option 1, Option 2)`.
2. Return True if `solve(0, len(nums) - 1) >= 0`.

## Complexity
- **Time Complexity:** O(2^N) without memoization, O(N^2) with.
- **Space Complexity:** O(N).

## Code
```python
def predict_the_winner(nums):
    memo = {}
    def solve(l, r):
        if l == r: return nums[l]
        if (l, r) in memo: return memo[(l, r)]
        
        # Diff between current player and next player
        res = max(nums[l] - solve(l + 1, r), 
                  nums[r] - solve(l, r - 1))
        memo[(l, r)] = res
        return res
        
    return solve(0, len(nums) - 1) >= 0
```
