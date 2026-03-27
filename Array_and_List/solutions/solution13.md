# Solution 13: Triple Sum Discovery

## Approach Explanation
We sort the array first. Then, we iterate through each number `nums[i]` and use a two-pointer approach (`left` and `right`) on the remainder of the array to find two numbers that sum to `-nums[i]`. To avoid duplicates, we skip identical elements.

## Step-by-Step Logic
1. Sort `nums` in ascending order.
2. Iterate `i` from 0 to `n-3`:
   - If `i > 0` and `nums[i] == nums[i-1]`, skip to avoid duplicates.
   - Set `left = i + 1`, `right = n - 1`.
   - While `left < right`:
     - Calculate `current_sum = nums[i] + nums[left] + nums[right]`.
     - If `current_sum == 0`:
       - Add `[nums[i], nums[left], nums[right]]` to result.
       - Move `left` forward and `right` backward.
       - Skip next `left` and `right` if they are identical to current ones.
     - Else if `current_sum < 0`, `left += 1`.
     - Else, `right -= 1`.
3. Return the result.

## Complexity
- **Time Complexity:** O(N^2), as we have a nested loop with two pointers.
- **Space Complexity:** O(log N) or O(N) depending on the sorting implementation.

## Code
```python
def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
                
    return result
```
