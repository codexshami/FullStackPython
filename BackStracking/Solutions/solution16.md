# Solution 16: The Unique Permutation Generator (Permutations II)

## Approach Explanation
We sort the array and use a `used` array to track which elements are in the current permutation. To avoid duplicates, we skip an element if it's the same as the previous one and the previous one hasn't been used at the current level.

## Step-by-Step Logic
1. Sort `nums`.
2. Use a boolean `used` array.
3. At each position, try each unused element.
4. Skip if `nums[i] == nums[i-1]` and `used[i-1]` is False (avoids duplicate permutations).
5. Add element, mark used, recurse, then backtrack.

## Complexity
- **Time Complexity:** O(N! * N).
- **Space Complexity:** O(N).

## Code
```python
def permute_unique(nums):
    result = []
    nums.sort()
    used = [False] * len(nums)
    
    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            current.append(nums[i])
            backtrack(current)
            current.pop()
            used[i] = False
    
    backtrack([])
    return result
```
