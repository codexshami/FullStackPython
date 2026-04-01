# Solution 13: The Subset Sum Finder (Subset Sum Problem)

## Approach Explanation
We use backtracking to try including or excluding each element. We prune branches where the current sum exceeds the target.

## Step-by-Step Logic
1. Sort the array for easier pruning.
2. For each element, include it in the current subset and reduce the target.
3. If target becomes 0, save the subset.
4. If target goes negative, backtrack.
5. Skip to the next element to explore other subsets.

## Complexity
- **Time Complexity:** O(2^N).
- **Space Complexity:** O(N).

## Code
```python
def subset_sum(nums, target):
    result = []
    nums.sort()
    
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        for i in range(start, len(nums)):
            if nums[i] > remaining:
                break
            current.append(nums[i])
            backtrack(i + 1, current, remaining - nums[i])
            current.pop()
    
    backtrack(0, [], target)
    return result
```
