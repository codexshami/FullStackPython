# Solution 16: Interleaved Middle Find

## Approach Explanation
Since the requirement is O(log(m+n)), we use binary search. Instead of merging the arrays, we partition them such that the left half and right half have the same size and all elements in the left half are smaller than or equal to elements in the right half.

## Step-by-Step Logic
1. Ensure `nums1` is the shorter array.
2. Initialize `low = 0`, `high = len(nums1)`.
3. While `low <= high`:
   - `partition1 = (low + high) // 2`
   - `partition2 = (m + n + 1) // 2 - partition1`
   - Determine `max_left1`, `min_right1`, `max_left2`, `min_right2`.
   - If `max_left1 <= min_right2` and `max_left2 <= min_right1`:
     - If total elements are odd, return `max(max_left1, max_left2)`.
     - Else, return `(max(max_left1, max_left2) + min(min_right1, min_right2)) / 2`.
   - Else if `max_left1 > min_right2`, move `high = partition1 - 1`.
   - Otherwise, move `low = partition1 + 1`.

## Complexity
- **Time Complexity:** O(log(min(M, N))), where M and N are lengths of the arrays.
- **Space Complexity:** O(1), no extra storage.

## Code
```python
def find_median_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    
    while low <= high:
        partition1 = (low + high) // 2
        partition2 = (m + n + 1) // 2 - partition1
        
        max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float('inf') if partition1 == m else nums1[partition1]
        
        max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float('inf') if partition2 == n else nums2[partition2]
        
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            else:
                return max(max_left1, max_left2)
        elif max_left1 > min_right2:
            high = partition1 - 1
        else:
            low = partition1 + 1
```
