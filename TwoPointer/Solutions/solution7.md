# Solution 7: Tricolor Segregation (Sort Colors)

## Approach Explanation
This is the Dutch National Flag problem. We use three pointers: `l` (boundary of 0s), `r` (boundary of 2s), and `i` (current element).

## Step-by-Step Logic
1. `l = 0`, `r = len(nums) - 1`, `i = 0`.
2. While `i <= r`:
   - If `nums[i] == 0`:
     - Swap `nums[l]` and `nums[i]`.
     - `l += 1`, `i += 1`.
   - Else if `nums[i] == 2`:
     - Swap `nums[r]` and `nums[i]`.
     - `r -= 1`. (Don't increment `i` as the swapped value needs checking).
   - Else (`nums[i] == 1`):
     - `i += 1`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def sort_colors(nums):
    l, r = 0, len(nums) - 1
    i = 0
    
    def swap(i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        
    while i <= r:
        if nums[i] == 0:
            swap(l, i)
            l += 1
            i += 1
        elif nums[i] == 2:
            swap(i, r)
            r -= 1
        else:
            i += 1
```
