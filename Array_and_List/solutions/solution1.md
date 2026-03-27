# Solution 1: Sum Pair Discovery

## Approach Explanation
We use a hash map (dictionary in Python) to store the value and its index as we iterate through the array. For each number, we calculate the `complement` (target - current_number). If the complement is already in our map, it means we found the pair.

## Step-by-Step Logic
1. Initialize an empty dictionary `seen`.
2. Iterate through the array using `enumerate` to get both index `i` and value `num`.
3. Calculate `complement = target - num`.
4. Check if `complement` exists in `seen`.
5. If it exists, return `[seen[complement], i]`.
6. Otherwise, add the current `num` to `seen` with its index: `seen[num] = i`.

## Complexity
- **Time Complexity:** O(N), where N is the number of elements in the array. We traverse the list only once.
- **Space Complexity:** O(N), as we store at most N elements in the hash map.

## Code
```python
def solve(nums, target):
    # Dictionary to store value: index
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        # If complement is found, return the indices
        if complement in seen:
            return [seen[complement], i]
        # Store index of the current number
        seen[num] = i
    
    return [] # Should not reach here based on problem constraints
```
