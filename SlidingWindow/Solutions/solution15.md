# Solution 15: Cardinality Constraint (Subarrays with K Different Integers)

## Approach Explanation
Finding "Exactly K" directly is hard. We use `Exactly K = AtMost(K) - AtMost(K-1)`.

## Step-by-Step Logic
1. Define `at_most(k)`:
   - Use a sliding window and a hash map to keep track of frequency of characters.
   - `while len(count) > k`: shrink the window from left.
   - `res += r - l + 1`.
2. Return `at_most(k) - at_most(k - 1)`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(K).

## Code
```python
from collections import Counter

def subarrays_with_k_distinct(nums, k):
    def at_most(goal):
        count = Counter()
        res = 0
        l = 0
        for r in range(len(nums)):
            if count[nums[r]] == 0:
                goal -= 1
            count[nums[r]] += 1
            
            while goal < 0:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    goal += 1
                l += 1
            res += (r - l + 1)
        return res
        
    return at_most(k) - at_most(k - 1)
```
