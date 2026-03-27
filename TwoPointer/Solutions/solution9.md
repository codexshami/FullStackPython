# Solution 9: Quadruplet Nullification (4Sum)

## Approach Explanation
We use Two Pointer technique nested within two loops. Sorting handles duplicates.

## Step-by-Step Logic
1. Sort `nums`.
2. For `i` in `range(n)`:
   - Skip duplicate `nums[i]`.
   - For `j` in `range(i+1, n)`:
     - Skip duplicate `nums[j]`.
     - `l = j + 1`, `r = n - 1`.
     - While `l < r`:
       - Calculate sum. If sum == target, add to result and skip duplicates of `l` and `r`.
       - Adjust pointers.

## Complexity
- **Time Complexity:** O(N^3).
- **Space Complexity:** O(N).

## Code
```python
def four_sum(nums, target):
    nums.sort()
    res, quad = [], []

    def kSum(k, start, target):
        if k != 2:
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()
            return

        # base case, two sum
        l, r = start, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                res.append(quad + [nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    
    kSum(4, 0, target)
    return res
```
*(Note: Used a recursive generalization of the Two Pointer approach for better scalability to k-Sum).*
