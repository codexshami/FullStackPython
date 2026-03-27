# Solution 6: Lexicographical Decimation (Remove Duplicates from Sorted Array)

## Approach Explanation
We use a slow pointer (`l`) and a fast pointer (`r`). The slow pointer tracks the position of the last unique element, while the fast pointer iterates through the array.

## Step-by-Step Logic
1. If `len(nums) == 0`, return 0.
2. Initialize `l = 1`.
3. For `r` from 1 to `len(nums)-1`:
   - If `nums[r] != nums[r-1]`:
     - `nums[l] = nums[r]`.
     - `l += 1`.
4. Return `l`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def remove_duplicates(nums):
    if not nums: return 0
    
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
            
    return l
```
