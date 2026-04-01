# Solution 14: The Unique Subset Collector (Subsets II — with Duplicates)

## Approach Explanation
Similar to Subsets I, but we sort the array first and skip duplicate elements at the same recursion level to avoid duplicate subsets.

## Step-by-Step Logic
1. Sort `nums` to group duplicates together.
2. Use the same backtracking approach as Subsets.
3. At each recursion level, skip an element if it equals the previous one (and the previous one was not included at this level).

## Complexity
- **Time Complexity:** O(N * 2^N).
- **Space Complexity:** O(N).

## Code
```python
def subsets_with_dup(nums):
    result = []
    nums.sort()
    
    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue  # skip duplicates
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
```
