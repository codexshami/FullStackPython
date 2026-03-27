# Solution 12: Range-Bounded Count (Number of Subarrays with Bounded Maximum)

## Approach Explanation
The number of subarrays where `max(subarray) <= target` is easier to calculate.
The answer is `count(right) - count(left - 1)`.
`count(bound)` counts subarrays where no element exceeds `bound`.

## Step-by-Step Logic
1. Define `count_under(bound)`:
   - Use a sliding window or a simple counter to find contiguous segments where elements are `<= bound`.
   - For a segment of length `L`, there are `L*(L+1)//2` subarrays.
2. Return `count_under(right) - count_under(left - 1)`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def num_subarray_bounded_max(nums, left, right):
    def count(bound):
        res = 0
        curr = 0
        for x in nums:
            if x <= bound:
                curr += 1
                res += curr
            else:
                curr = 0
        return res
        
    return count(right) - count(left - 1)
```
