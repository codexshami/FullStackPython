# Solution 18: Linear Collinearity (Max Points on a Line)

## Approach Explanation
A line is defined by its slope and a point. For every point `i`, we calculate the slope to every other point `j`. We use a hash map to count the number of points for each slope.

## Step-by-Step Logic
1. For each point `p1` in `points`:
   - Initialize `slopes = {}`.
   - For every other point `p2`:
     - Calculate slope `(y2 - y1) / (x2 - x1)`.
     - To avoid floating point issues, use GCD: `dy / gcd, dx / gcd` as the key.
     - Special case for vertical lines.
     - Update `slopes[slope]`.
   - Track the maximum count for point `p1`.
2. Return global maximum.

## Complexity
- **Time Complexity:** O(N^2).
- **Space Complexity:** O(N).

## Code
```python
import math

def max_points(points):
    n = len(points)
    if n <= 2: return n
    
    res = 1
    for i in range(n):
        slopes = {}
        for j in range(i + 1, n):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            g = math.gcd(dx, dy)
            slope = (dx // g, dy // g)
            slopes[slope] = slopes.get(slope, 0) + 1
            res = max(res, slopes[slope] + 1)
            
    return res
```
