# Solution 8: Approximate Triplet Sum (3Sum Closest)

## Approach Explanation
Similar to 3Sum, we sort the array and use Two Pointers. Instead of looking for exactly 0, we track the sum with the minimum absolute difference from the target.

## Step-by-Step Logic
1. Sort `nums`.
2. `best_sum = float('inf')`.
3. For `i` in `range(len(nums))`:
   - `l = i + 1`, `r = len(nums) - 1`.
   - While `l < r`:
     - `curr_sum = nums[i] + nums[l] + nums[r]`.
     - If `abs(target - curr_sum) < abs(target - best_sum)`: `best_sum = curr_sum`.
     - If `curr_sum < target`, `l += 1`.
     - Else if `curr_sum > target`, `r -= 1`.
     - Else, return `target`.
4. Return `best_sum`.

## Complexity
- **Time Complexity:** O(N^2).
- **Space Complexity:** O(log N) to O(N).

## Code
```python
def three_sum_closest(nums, target):
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    
    for i in range(len(nums)):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(s - target) < abs(res - target):
                res = s
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return res
    return res
```
