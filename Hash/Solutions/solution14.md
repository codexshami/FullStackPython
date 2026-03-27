# Solution 14: Quartic Combination (4Sum)

## Approach Explanation
We can solve this by sorting the array and using a nested loop for the first two numbers, then using Two-Pointer technique for the remaining two. This reduces O(N^4) to O(N^3).

## Step-by-Step Logic
1. Sort `nums`.
2. Iterate `i` from 0 to `n-1`. Skip duplicates.
3. Iterate `j` from `i+1` to `n-1`. Skip duplicates.
4. Set `left = j + 1`, `right = n - 1`.
5. While `left < right`:
   - Calculate current sum.
   - If `sum == target`, add to result and skip duplicates for `left` and `right`.
   - If `sum < target`, `left += 1`.
   - Else, `right -= 1`.

## Complexity
- **Time Complexity:** O(N^3).
- **Space Complexity:** O(1) (excluding result list).

## Code
```python
def four_sum(nums, target):
    nums.sort()
    n = len(nums)
    res = []
    
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]: continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j-1]: continue
            
            l, r = j + 1, n - 1
            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
    return res
```
