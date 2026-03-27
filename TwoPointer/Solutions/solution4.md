# Solution 4: Maximum Volumetric Boundary (Container With Most Water)

## Approach Explanation
We use two pointers at the ends of the array. The area is `min(h[l], h[r]) * (r - l)`. To find a larger area, we must move the pointer that is shorter, as the width only decreases.

## Step-by-Step Logic
1. Initialize `l = 0`, `r = len(height) - 1`, `res = 0`.
2. While `l < r`:
   - `area = (r - l) * min(height[l], height[r])`.
   - `res = max(res, area)`.
   - If `height[l] < height[r]`, `l += 1`.
   - Else, `r -= 1`.
3. Return `res`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def max_area(height):
    l, r = 0, len(height) - 1
    res = 0
    
    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)
        
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
            
    return res
```
