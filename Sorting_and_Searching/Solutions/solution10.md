# Solution 10: Partition Optimization

## Approach Explanation
We binary search for the minimum possible "largest sum". The range is `[max(nums), sum(nums)]`. For each value, we check if we can partition the array into `k` or fewer subarrays with each subarray sum <= `mid`.

## Step-by-Step Logic
1. `low = max(nums)`, `high = sum(nums)`.
2. While `low < high`:
   - `mid = (low + high) // 2`.
   - Calculate how many subarrays are needed for `limit = mid`:
     - Iterate through `nums`, keeping `curr_sum`.
     - If `curr_sum + n > limit`, start new subarray: `sub_count += 1`, `curr_sum = n`.
     - Else, `curr_sum += n`.
   - If `sub_count <= k`, `high = mid`.
   - Else, `low = mid + 1`.
3. Return `low`.

## Complexity
- **Time Complexity:** O(N * log(sum(nums))).
- **Space Complexity:** O(1).

## Code
```python
def split_array(nums, k):
    l, r = max(nums), sum(nums)
    
    while l < r:
        limit = (l + r) // 2
        
        # Greedy count of subarrays
        count = 1
        curr = 0
        for n in nums:
            if curr + n > limit:
                count += 1
                curr = n
            else:
                curr += n
                
        if count <= k:
            r = limit
        else:
            l = limit + 1
            
    return l
```
