# Solution 3: Insertion Point Prediction

## Approach Explanation
We use Binary Search. The insertion point is the same as the index of the first element that is greater than or equal to the target.

## Step-by-Step Logic
1. Initialize `left = 0`, `right = len(nums) - 1`.
2. While `left <= right`:
   - `mid = (left + right) // 2`.
   - If `nums[mid] == target`, return `mid`.
   - If `nums[mid] < target`, `left = mid + 1`.
   - If `nums[mid] > target`, `right = mid - 1`.
3. If search finishes without finding target, `left` will be at the correct insertion index.

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(1).

## Code
```python
def search_insert(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
            
    return l
```
