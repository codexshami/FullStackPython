# Solution 8: Logarithmic Product Window (Subarray Product Less Than K)

## Approach Explanation
If the product of elements from `l` to `r` is `< k`, then all subarrays ending at `r` starting between `l` and `r` also satisfy the condition. The number of such subarrays is `r - l + 1`.

## Step-by-Step Logic
1. If `k <= 1`, return 0.
2. `l = 0`, `prod = 1`, `res = 0`.
3. For each `r`, `prod *= nums[r]`.
4. While `prod >= k` (and `l <= r`):
   - `prod /= nums[l]`.
   - `l += 1`.
5. `res += (r - l + 1)`.
6. Return `res`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def num_subarray_product_less_than_k(nums, k):
    if k <= 1: return 0
    res = 0
    prod = 1
    l = 0
    for r in range(len(nums)):
        prod *= nums[r]
        while prod >= k:
            prod /= nums[l]
            l += 1
        res += (r - l + 1)
    return res
```
