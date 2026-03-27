# Solution 1: Half-Interval Search

## Approach Explanation
We use the standard Binary Search algorithm. We maintain two pointers, `left` and `right`, and repeatedly check the middle element.

## Step-by-Step Logic
1. Initialize `left = 0`, `right = len(nums) - 1`.
2. While `left <= right`:
   - Calculate `mid = left + (right - left) // 2`.
   - If `nums[mid] == target`, return `mid`.
   - If `nums[mid] < target`, move `left = mid + 1`.
   - If `nums[mid] > target`, move `right = mid - 1`.
3. If not found, return -1.

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(1).

## Code
```python
def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
            
    return -1
```
