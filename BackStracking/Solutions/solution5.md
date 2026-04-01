# Solution 5: The Arrangement Engine (Permutations)

## Approach Explanation
We build permutations by choosing each unused element at every position. We use a `used` boolean array to track which elements have already been placed.

## Step-by-Step Logic
1. If the current permutation length equals `n`, save it.
2. Iterate through all elements in `nums`.
3. Skip elements already in the current permutation (tracked by `used` array).
4. Add the element, mark as used, recurse.
5. Backtrack: remove the element and unmark.

## Complexity
- **Time Complexity:** O(N! * N).
- **Space Complexity:** O(N).

## Code
```python
def permute(nums):
    result = []
    
    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        for num in nums:
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()
    
    backtrack([])
    return result
```
