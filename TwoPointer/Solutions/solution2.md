# Solution 2: Sorted Target Sum (Two Sum II - Input Array Is Sorted)

## Approach Explanation
Since the array is sorted, we can use two pointers at the ends. If the sum is too high, we move the right pointer left. If it's too low, we move the left pointer right.

## Step-by-Step Logic
1. Initialize `l = 0`, `r = len(numbers) - 1`.
2. While `l < r`:
   - Calculate `curr_sum = numbers[l] + numbers[r]`.
   - If `curr_sum == target`, return `[l + 1, r + 1]`.
   - If `curr_sum < target`, `l += 1`.
   - Else, `r -= 1`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def two_sum(numbers, target):
    l, r = 0, len(numbers) - 1
    
    while l < r:
        curr = numbers[l] + numbers[r]
        if curr == target:
            return [l + 1, r + 1]
        elif curr < target:
            l += 1
        else:
            r -= 1
```
