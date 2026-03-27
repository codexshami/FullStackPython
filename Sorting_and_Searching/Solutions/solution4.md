# Solution 4: Inflection Point Discovery

## Approach Explanation
In a rotated sorted array, the minimum element is the only element that is smaller than the element before it. We can use binary search by comparing the middle element with the rightmost element.

## Step-by-Step Logic
1. Initialize `left = 0`, `right = len(nums) - 1`.
2. While `left < right`:
   - `mid = (left + right) // 2`.
   - If `nums[mid] > nums[right]`:
     - This means the minimum is in the right half (since it's rotated). Set `left = mid + 1`.
   - If `nums[mid] <= nums[right]`:
     - This means the right half is sorted normally, and the minimum is at `mid` or to its left. Set `right = mid`.
3. Return `nums[left]`.

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(1).

## Code
```python
def find_min(nums):
    l, r = 0, len(nums) - 1
    
    while l < r:
        mid = (l + r) // 2
        # If mid > right, min is in the right half
        if nums[mid] > nums[right]:
            l = mid + 1
        else:
            # mid <= right, min is in the left half including mid
            r = mid
            
    return nums[l]
```
