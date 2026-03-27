# Solution 7: Minimal Consumption Rate

## Approach Explanation
We binary search over the possible values of speed `k`. The range for `k` is `[1, max(piles)]`. For each speed, we calculate the total hours needed.

## Step-by-Step Logic
1. Initialize `left = 1`, `right = max(piles)`.
2. While `left < right`:
   - `mid = (left + right) // 2`.
   - Calculate total hours `total_h = sum(ceil(p / mid) for p in piles)`.
   - If `total_h <= h`:
     - This speed is sufficient, try slower speeds. `right = mid`.
   - Else:
     - Speed is too slow. `left = mid + 1`.
3. Return `left`.

## Complexity
- **Time Complexity:** O(N * log(max(P))), where N is number of piles and P is max bananas.
- **Space Complexity:** O(1).

## Code
```python
import math

def min_eating_speed(piles, h):
    l, r = 1, max(piles)
    
    while l < r:
        mid = (l + r) // 2
        
        # Calculate hours needed for speed 'mid'
        hours = 0
        for p in piles:
            hours += math.ceil(p / mid)
            
        if hours <= h:
            r = mid
        else:
            l = mid + 1
            
    return l
```
