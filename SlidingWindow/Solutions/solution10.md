# Solution 10: Bitwise Maximal Span (Longest Subarray of 1's After Deleting One Element)

## Approach Explanation
Find the longest window that contains at most one `0`. The answer will be `window_size - 1` (since we must delete one element).

## Step-by-Step Logic
1. `l = 0`, `zeros = 0`, `res = 0`.
2. For each `r`:
   - If `nums[r] == 0`, `zeros += 1`.
   - While `zeros > 1`:
     - If `nums[l] == 0`, `zeros -= 1`.
     - `l += 1`.
   - `res = max(res, r - l)`. (Note: r - l + 1 - 1 = r - l).
3. Return `res`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def longest_subarray(nums):
    l = 0
    zeros = 0
    res = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            zeros += 1
        while zeros > 1:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        res = max(res, r - l)
    return res
```
