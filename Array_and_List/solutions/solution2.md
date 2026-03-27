# Solution 2: Maximum Wealth Subsegment

## Approach Explanation
We use Kadane's Algorithm. The idea is to maintain a `current_sum` that gathers the sum of the subarray and a `max_sum` that tracks the maximum found so far. If `current_sum` becomes negative, we reset it to zero because a negative sum will only decrease the sum of any subsequent subarray.

## Step-by-Step Logic
1. Initialize `max_so_far` to a very small number and `current_max` to 0.
2. Iterate through each `profit` in the `profits` array.
3. Add `profit` to `current_max`.
4. If `current_max > max_so_far`, update `max_so_far`.
5. If `current_max < 0`, reset `current_max` to 0.
6. Return `max_so_far`.

## Complexity
- **Time Complexity:** O(N), where N is the length of the array.
- **Space Complexity:** O(1), as we only use a few variables.

## Code
```python
def max_subarray_sum(profits):
    # Handle edge case where all numbers might be negative
    max_so_far = float('-inf')
    current_max = 0
    
    for profit in profits:
        current_max += profit
        
        if current_max > max_so_far:
            max_so_far = current_max
            
        if current_max < 0:
            current_max = 0
            
    return max_so_far
```
