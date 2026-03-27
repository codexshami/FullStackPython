# Solution 11: Reservoir Capacity

## Approach Explanation
We use a two-pointer approach starting from both ends. For any position, the amount of water it can hold is `min(max_left, max_right) - height[i]`. By moving pointers towards each other based on which side is lower, we can calculate this without pre-computing all left and right maxima.

## Step-by-Step Logic
1. Initialize `left = 0`, `right = n - 1`, `left_max = 0`, `right_max = 0`, and `water = 0`.
2. While `left < right`:
   - If `height[left] < height[right]`:
     - If `height[left] >= left_max`, update `left_max`.
     - Else, `water += left_max - height[left]`.
     - Move `left` pointer.
   - Else:
     - If `height[right] >= right_max`, update `right_max`.
     - Else, `water += right_max - height[right]`.
     - Move `right` pointer.
3. Return `water`.

## Complexity
- **Time Complexity:** O(N), single pass through the array.
- **Space Complexity:** O(1), no extra arrays used.

## Code
```python
def trap_water(height):
    if not height:
        return 0
        
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
            
    return water
```
