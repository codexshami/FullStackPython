# Solution 13: Trichromatic Sort (Sort Colors)

## Approach Explanation
This is the Dutch National Flag problem. We use three pointers: `low` (for 0s), `mid` (for 1s), and `high` (for 2s). We iterate through the array once and swap elements to their correct positions.

## Step-by-Step Logic
1. `low = 0`, `mid = 0`, `high = len(nums) - 1`.
2. While `mid <= high`:
   - If `nums[mid] == 0`:
     - Swap `nums[low]` and `nums[mid]`.
     - Increment `low` and `mid`.
   - If `nums[mid] == 1`:
     - Just increment `mid`.
   - If `nums[mid] == 2`:
     - Swap `nums[mid]` and `nums[high]`.
     - Decrement `high`. (Don't increment `mid` yet, as the swapped element needs to be checked).

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else: # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```
