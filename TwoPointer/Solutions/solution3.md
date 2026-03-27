# Solution 3: Triplet Nullification (3Sum)

## Approach Explanation
We sort the array and iterate through it. For each element `nums[i]`, we treat it as a fixed value and use the Two Pointer technique on the remaining part of the array to find pairs that sum to `-nums[i]`.

## Step-by-Step Logic
1. Sort `nums`.
2. Iterate `i` from 0 to `len(nums)-1`:
   - If `i > 0` and `nums[i] == nums[i-1]`, skip (to avoid duplicates).
   - `l = i + 1`, `r = len(nums) - 1`.
   - While `l < r`:
     - `s = nums[i] + nums[l] + nums[r]`.
     - If `s < 0`, `l += 1`.
     - Else if `s > 0`, `r -= 1`.
     - Else:
       - Append `[nums[i], nums[l], nums[r]]` to result.
       - Move `l` past duplicates of `nums[l]`.
       - Move `r` past duplicates of `nums[r]`.
       - Increment `l`, decrement `r`.

## Complexity
- **Time Complexity:** O(N^2).
- **Space Complexity:** O(log N) to O(N) depending on sorting implementation.

## Code
```python
def three_sum(nums):
    res = []
    nums.sort()
    
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
            
        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = a + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
```
