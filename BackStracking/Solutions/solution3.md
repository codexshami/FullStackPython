# Solution 3: The Subset Architect (Subsets)

## Approach Explanation
We build subsets by deciding, for each element, whether to include it or not. This is a classic backtracking pattern where we recursively explore both choices.

## Step-by-Step Logic
1. Start with an empty subset and index 0.
2. At each index, we have two choices: include `nums[index]` or skip it.
3. When the index reaches the end of the array, save the current subset.
4. Backtrack by removing the last added element.

## Complexity
- **Time Complexity:** O(N * 2^N).
- **Space Complexity:** O(N) for the recursion stack.

## Code
```python
def subsets(nums):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
```
