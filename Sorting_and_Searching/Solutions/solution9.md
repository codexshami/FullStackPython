# Solution 9: Integrated Median Analysis

## Approach Explanation
We use a binary search to partition the two arrays such that the number of elements on the left side of the partition is equal to (or one more than) the number of elements on the right side. We binary search on the shorter array to optimize time.

## Step-by-Step Logic
1. Ensure `nums1` is the shorter array.
2. Initialize `low = 0`, `high = m`.
3. Total elements `half = (m + n + 1) // 2`.
4. While `low <= high`:
   - `i = (low + high) // 2` (partition for `nums1`).
   - `j = half - i` (partition for `nums2`).
   - Boundary checks:
     - `L1 = nums1[i-1]` if `i > 0` else `-inf`.
     - `R1 = nums1[i]` if `i < m` else `inf`.
     - `L2 = nums2[j-1]` if `j > 0` else `-inf`.
     - `R2 = nums2[j]` if `j < n` else `inf`.
   - If `L1 <= R2 and L2 <= R1`:
     - Found correct partition.
     - If total is odd, return `max(L1, L2)`.
     - If total is even, return `(max(L1, L2) + min(R1, R2)) / 2`.
   - Else if `L1 > R2`, move `i` left (`high = i - 1`).
   - Else, move `i` right (`low = i + 1`).

## Complexity
- **Time Complexity:** O(log(min(M, N))).
- **Space Complexity:** O(1).

## Code
```python
def find_median_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        
    m, n = len(nums1), len(nums2)
    l, r = 0, m
    half = (m + n + 1) // 2
    
    while l <= r:
        i = (l + r) // 2
        j = half - i
        
        l1 = nums1[i-1] if i > 0 else -float('inf')
        r1 = nums1[i] if i < m else float('inf')
        l2 = nums2[j-1] if j > 0 else -float('inf')
        r2 = nums2[j] if j < n else float('inf')
        
        if l1 <= r2 and l2 <= r1:
            if (m + n) % 2:
                return float(max(l1, l2))
            return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            r = i - 1
        else:
            l = i + 1
```
