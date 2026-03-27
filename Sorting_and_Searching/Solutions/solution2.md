# Solution 2: Regression Point Analysis

## Approach Explanation
This is a binary search problem where the search space is `[1, n]`. We want to find the smallest version `v` such that `isBadVersion(v)` is true.

## Step-by-Step Logic
1. Initialize `left = 1`, `right = n`.
2. While `left < right`:
   - `mid = left + (right - left) // 2`.
   - If `isBadVersion(mid)` is true, the first bad version is either `mid` or before it. Set `right = mid`.
   - If `isBadVersion(mid)` is false, all versions up to `mid` are good. Set `left = mid + 1`.
3. Return `left`.

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(1).

## Code
```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def first_bad_version(n):
    l, r = 1, n
    while l < r:
        mid = l + (r - l) // 2
        if isBadVersion(mid):
            r = mid
        else:
            l = mid + 1
    return l
```
