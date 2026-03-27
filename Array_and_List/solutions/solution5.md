# Solution 5: Gravity Shift

## Approach Explanation
We use a two-pointer approach. One pointer `insert_pos` keeps track of where the next non-zero element should be placed. As we iterate through the array, every time we find a non-zero element, we swap it with the element at `insert_pos`.

## Step-by-Step Logic
1. Initialize `insert_pos = 0`.
2. Iterate through the array with `curr_idx`.
3. If `nums[curr_idx]` is not zero:
   - Swap `nums[insert_pos]` and `nums[curr_idx]`.
   - Increment `insert_pos`.
4. This effectively pushes all non-zero elements to the front and zeroes to the back.

## Complexity
- **Time Complexity:** O(N), single pass through the array.
- **Space Complexity:** O(1), in-place modification.

## Code
```python
def move_zeroes(nums):
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap current non-zero with the first available zero position
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
    return nums
```
