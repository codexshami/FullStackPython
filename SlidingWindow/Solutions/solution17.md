# Solution 17: Dissimilarity Quantile (Find K-th Smallest Pair Distance)

## Approach Explanation
We use Binary Search on the possible range of distances `[0, max(nums) - min(nums)]`. For a chosen distance `mid`, we count how many pairs have a distance `<= mid` using a sliding window.

## Step-by-Step Logic
1. Sort `nums`.
2. `low = 0`, `high = nums[-1] - nums[0]`.
3. While `low < high`:
   - `mid = (low + high) // 2`.
   - `count = 0`, `l = 0`.
   - For `r` from 0 to `n-1`:
     - While `nums[r] - nums[l] > mid`: `l += 1`.
     - `count += (r - l)`.
   - If `count >= k`: `high = mid`.
   - Else: `low = mid + 1`.
4. Return `low`.

## Complexity
- **Time Complexity:** O(N log N + N log(MaxDistance)).
- **Space Complexity:** O(1).

## Code
```python
def smallest_distance_pair(nums, k):
    nums.sort()
    n = len(nums)
    
    def count_less_equal(mid):
        count = 0
        l = 0
        for r in range(n):
            while nums[r] - nums[l] > mid:
                l += 1
            count += (r - l)
        return count
        
    low, high = 0, nums[-1] - nums[0]
    while low < high:
        mid = (low + high) // 2
        if count_less_equal(mid) >= k:
            high = mid
        else:
            low = mid + 1
            
    return low
```
