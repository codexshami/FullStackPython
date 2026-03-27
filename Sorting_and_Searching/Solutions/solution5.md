# Solution 5: Search in Disrupted Continuum

## Approach Explanation
Even in a rotated array, at least one half (left or right) of any range split by `mid` will be sorted. We identify which half is sorted and check if the `target` lies within that sorted range.

## Step-by-Step Logic
1. Initialize `left = 0`, `right = len(nums) - 1`.
2. While `left <= right`:
   - `mid = (left + right) // 2`.
   - If `nums[mid] == target`, return `mid`.
   - **Check if Left Half is Sorted:** `nums[left] <= nums[mid]`
     - If `target` is within `[nums[left], nums[mid]]`, set `right = mid - 1`.
     - Else, set `left = mid + 1`.
   - **Else (Right Half must be Sorted):**
     - If `target` is within `[nums[mid], nums[right]]`, set `left = mid + 1`.
     - Else, set `right = mid - 1`.
3. Return -1.

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(1).

## Code
```python
def search_rotated(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
            
        # Left sorted half
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        # Right sorted half
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
                
    return -1
```
