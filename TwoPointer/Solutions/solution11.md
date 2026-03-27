# Solution 11: Dual-Pointer Intersection (Intersection of Two Arrays II)

## Approach Explanation
While a hash map is a common solution, the Two Pointer approach is extremely efficient if the arrays are sorted. We sort both arrays and use two pointers to find common elements.

## Step-by-Step Logic
1. Sort `nums1` and `nums2`.
2. Initialize `i = 0`, `j = 0`, `res = []`.
3. While `i < len(nums1)` and `j < len(nums2)`:
   - If `nums1[i] < nums2[j]`, increment `i`.
   - Else if `nums1[i] > nums2[j]`, increment `j`.
   - Else:
     - Append `nums1[i]` to `res`.
     - Increment `i` and `j`.
4. Return `res`.

## Complexity
- **Time Complexity:** O(N log N + M log M) due to sorting.
- **Space Complexity:** O(N + M).

## Code
```python
def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    
    i = j = 0
    res = []
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1
            
    return res
```
