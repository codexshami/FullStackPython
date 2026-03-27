# Solution 11: Binary Maximal Gap (Max Consecutive Ones III)

## Approach Explanation
We use a sliding window of which the zeroes count is at most `k`. We expand the right pointer and shrink the left pointer as needed.

## Step-by-Step Logic
1. `l = 0`, `zeros = 0`, `res = 0`.
2. For each `r`:
   - If `nums[r] == 0`, `zeros += 1`.
   - While `zeros > k`:
     - If `nums[l] == 0`, `zeros -= 1`.
     - `l += 1`.
   - `res = max(res, r - l + 1)`.
3. Return `res`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def longest_ones(nums, k):
    l = 0
    zeros = 0
    res = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            zeros += 1
        while zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        res = max(res, r - l + 1)
    return res
```
