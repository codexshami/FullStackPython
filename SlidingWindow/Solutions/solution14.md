# Solution 14: Predicate Parity Count (Count Number of Nice Subarrays)

## Approach Explanation
This problem can be transformed into finding the number of subarrays with sum `k` by replacing odd numbers with 1 and even numbers with 0. However, a sliding window "At Most K" approach is more efficient.
`Exactly K = AtMost(K) - AtMost(K-1)`.

## Step-by-Step Logic
1. Define `at_most(k)`:
   - Use sliding window to find total subarrays with at most `k` odd numbers.
   - For every `r`, expand until `odds > k`. Shrink `l`.
   - `count += (r - l + 1)`.
2. Return `at_most(k) - at_most(k - 1)`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def count_nice_subarrays(nums, k):
    def at_most(goal):
        if goal < 0: return 0
        res = 0
        l = 0
        odds = 0
        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                odds += 1
            while odds > goal:
                if nums[l] % 2 != 0:
                    odds -= 1
                l += 1
            res += (r - l + 1)
        return res
        
    return at_most(k) - at_most(k - 1)
```
