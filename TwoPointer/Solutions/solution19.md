# Solution 19: Order Inversion Peak (Next Permutation)

## Approach Explanation
We find the first pair from the right where `nums[i] < nums[i+1]`. This `i` is the peak to be changed. Then find the smallest number in the right suffix that is larger than `nums[i]`, swap them, and reverse the suffix.

## Step-by-Step Logic
1. Find `i = len(nums) - 2` such that `nums[i] < nums[i+1]`.
2. If no such `i` (falling sequence), reverse the whole array.
3. If `i` exists:
   - Find `j = len(nums) - 1` such that `nums[j] > nums[i]`.
   - Swap `nums[i]` and `nums[j]`.
   - Reverse the suffix `nums[i+1:]`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def next_permutation(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
        
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        
    # Reverse suffix
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
```
