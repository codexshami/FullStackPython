# Solution 5: Pluvial Accumulation (Trapping Rain Water)

## Approach Explanation
We use two pointers at the ends and track the maximum height seen from the left (`leftMax`) and the right (`rightMax`). The water trapped at any point is determined by the lower of the two maximums.

## Step-by-Step Logic
1. Initialize `l = 0`, `r = n - 1`, `leftMax = height[0]`, `rightMax = height[n-1]`, `res = 0`.
2. While `l < r`:
   - If `leftMax < rightMax`:
     - `l += 1`.
     - `leftMax = max(leftMax, height[l])`.
     - `res += leftMax - height[l]`.
   - Else:
     - `r -= 1`.
     - `rightMax = max(rightMax, height[r])`.
     - `res += rightMax - height[r]`.
3. Return `res`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def trap(height):
    if not height: return 0
    
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
            
    return res
```
