# Solution 8: Logistics Optimization

## Approach Explanation
We use Binary Search on the possible capacity of the ship. The range for capacity is `[max(weights), sum(weights)]`. For a given capacity `mid`, we check if it's possible to ship all packages within `days`.

## Step-by-Step Logic
1. `low = max(weights)`, `high = sum(weights)`.
2. While `low < high`:
   - `mid = (low + high) // 2`.
   - Calculate `count_days` needed for capacity `mid`:
     - Iterate through `weights`, maintaining `curr_weight`.
     - If `curr_weight + w > mid`, increment `count_days` and reset `curr_weight = w`.
     - Else, `curr_weight += w`.
   - If `count_days <= days`, `high = mid`.
   - Else, `low = mid + 1`.
3. Return `low`.

## Complexity
- **Time Complexity:** O(N * log(sum(W) - max(W))).
- **Space Complexity:** O(1).

## Code
```python
def ship_within_days(weights, days):
    l, r = max(weights), sum(weights)
    
    while l < r:
        mid = (l + r) // 2
        
        # Check if capacity 'mid' works
        curr_days = 1
        curr_w = 0
        for w in weights:
            if curr_w + w > mid:
                curr_days += 1
                curr_w = w
            else:
                curr_w += w
        
        if curr_days <= days:
            r = mid
        else:
            l = mid + 1
            
    return l
```
