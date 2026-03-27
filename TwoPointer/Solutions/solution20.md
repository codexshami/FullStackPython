# Solution 20: Zero Gravitational Shift (Move Zeroes)

## Approach Explanation
We use a `slow` pointer to track where the next non-zero element should be placed and a `fast` pointer to find the next non-zero element.

## Step-by-Step Logic
1. `l = 0`.
2. For `r` from 0 to `len(nums)-1`:
   - If `nums[r] != 0`:
     - Swap `nums[l]` and `nums[r]`.
     - `l += 1`.
3. The remaining elements from `l` to end are already zeroes (or will be swapped into place).

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def move_zeroes(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
```
