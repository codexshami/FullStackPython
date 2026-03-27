# Solution 6: Unique Intersection (Intersection of Two Arrays)

## Approach Explanation
We can use hash sets to find the intersection efficiently. Convert both arrays to sets and find their common elements.

## Step-by-Step Logic
1. Convert `nums1` to set `s1`.
2. Convert `nums2` to set `s2`.
3. Return the list of elements present in both `s1` and `s2`.

## Complexity
- **Time Complexity:** O(N + M).
- **Space Complexity:** O(N + M).

## Code
```python
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
```
