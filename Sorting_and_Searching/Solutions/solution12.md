# Solution 12: Pivot-Based Partitioning

## Approach Explanation
1. Pick a pivot (e.g., the last element).
2. Partition: Reorder the array so that all elements smaller than pivot are on the left, and larger ones are on the right.
3. Recursively apply to sub-arrays.

## Step-by-Step Logic
1. `quick_sort(nums, low, high)`:
   - If `low < high`:
     - `p = partition(nums, low, high)`
     - `quick_sort(nums, low, p - 1)`
     - `quick_sort(nums, p + 1, high)`
2. `partition(nums, low, high)`:
   - `pivot = nums[high]`
   - `i = low - 1`
   - For `j` from `low` to `high - 1`:
     - If `nums[j] < pivot`, increment `i` and swap `nums[i], nums[j]`.
   - Swap `nums[i + 1], nums[high]`.
   - Return `i + 1`.

## Complexity
- **Time Complexity:** O(N log N) Average, O(N^2) Worst Case.
- **Space Complexity:** O(log N) for recursion stack.

## Code
```python
import random

def quick_sort(nums):
    def sort(l, r):
        if l >= r: return
        
        # Partition
        pivot_idx = random.randint(l, r)
        nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
        pivot = nums[r]
        
        i = l
        for j in range(l, r):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        
        sort(l, i - 1)
        sort(i + 1, r)
        
    sort(0, len(nums) - 1)
    return nums
```
