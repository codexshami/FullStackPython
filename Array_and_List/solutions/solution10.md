# Solution 10: Peak Mountaineer

## Approach Explanation
We can use Binary Search to achieve O(log N). If the element at index `mid` is less than the element at `mid + 1`, a peak must exist on the right side. If it's greater, a peak exists on the left side (including `mid`).

## Step-by-Step Logic
1. Initialize `low = 0` and `high = n - 1`.
2. While `low < high`:
   - Calculate `mid = (low + high) // 2`.
   - If `nums[mid] < nums[mid + 1]`, move `low = mid + 1`.
   - Else, move `high = mid`.
3. Return `low` (or `high`), as they will point to the peak.

## Complexity
- **Time Complexity:** O(log N) due to binary search.
- **Space Complexity:** O(1), as we only use three scalar values.

## Code
```python
def find_peak_element(nums):
    low = 0
    high = len(nums) - 1
    
    while low < high:
        mid = (low + high) // 2
        
        if nums[mid] < nums[mid + 1]:
            # Peak is in the right half
            low = mid + 1
        else:
            # Peak is in the left half (including mid)
            high = mid
            
    return low
```
