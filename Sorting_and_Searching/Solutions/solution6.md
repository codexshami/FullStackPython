# Solution 6: Local Extremum Detection

## Approach Explanation
We can use Binary Search based on the slope. If `nums[mid] < nums[mid+1]`, we are on an upward slope and there must be a peak to the right. Otherwise, there is a peak at `mid` or to the left.

## Step-by-Step Logic
1. Initialize `left = 0`, `right = len(nums) - 1`.
2. While `left < right`:
   - `mid = (left + right) // 2`.
   - If `nums[mid] < nums[mid + 1]`:
     - Upward slope, peak is in the right half. `left = mid + 1`.
   - Else:
     - Downward slope (or peak), peak is in the left half. `right = mid`.
3. Return `left`.

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(1).

## Code
```python
def find_peak_element(nums):
    l, r = 0, len(nums) - 1
    
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            r = mid
            
    return l
```
