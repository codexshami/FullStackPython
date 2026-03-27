# Solution 3: Cyclical Motion

## Approach Explanation
The most efficient way to rotate an array in-place is using the "Reverse" technique. If we reverse the whole array, then reverse the first `k` elements, and finally reverse the remaining elements, we get the rotated array.

## Step-by-Step Logic
1. Normalize `k` by taking `k % len(nums)` because rotating `len(nums)` times is equivalent to zero rotation.
2. Define a helper function `reverse(start, end)` to swap elements until pointers meet.
3. Reverse the entire array from index `0` to `n-1`.
4. Reverse the first part from index `0` to `k-1`.
5. Reverse the second part from index `k` to `n-1`.

## Complexity
- **Time Complexity:** O(N), as we visit each element a constant number of times.
- **Space Complexity:** O(1), as the rotation is done in-place.

## Code
```python
def rotate(nums, k):
    n = len(nums)
    k %= n
    
    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
    # Step 1: Reverse entire array
    reverse(0, n - 1)
    # Step 2: Reverse first k elements
    reverse(0, k - 1)
    # Step 3: Reverse the rest
    reverse(k, n - 1)
    
    return nums
```
