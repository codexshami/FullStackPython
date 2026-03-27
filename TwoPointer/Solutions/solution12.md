# Solution 12: End-to-Beginning Merging (Merge Sorted Array)

## Approach Explanation
Instead of merging from the beginning (which requires extra space or shifts), we merge from the ends of `nums1` and `nums2` into the end of `nums1`.

## Step-by-Step Logic
1. Initialize `p1 = m - 1`, `p2 = n - 1`, and `p = m + n - 1`.
2. While `p1 >= 0` and `p2 >= 0`:
   - If `nums1[p1] > nums2[p2]`:
     - `nums1[p] = nums1[p1]`, `p1 -= 1`.
   - Else:
     - `nums1[p] = nums2[p2]`, `p2 -= 1`.
   - `p -= 1`.
3. If `p2 >= 0`, fill the remaining `nums1` with the rest of `nums2`.

## Complexity
- **Time Complexity:** O(M + N).
- **Space Complexity:** O(1).

## Code
```python
def merge(nums1, m, nums2, n):
    p1, p2, p = m - 1, n - 1, m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
        
    nums1[:p2 + 1] = nums2[:p2 + 1]
```
