# Solution 19: Atmospheric Catchment

## Approach Explanation
We use a monotonic decreasing stack to store the indices of the bars. When we see a bar higher than the bar on top of the stack, it means we have found a "valley" that can trap water. We pop the valley bar and calculate the area between the new top of the stack and the current bar.

## Step-by-Step Logic
1. Initialize an empty `stack` and `total_water = 0`.
2. Iterate through `height` with index `curr`:
   - While `stack` is not empty and `height[curr] > height[stack[-1]]`:
     - `valley_idx = stack.pop()`
     - If `stack` is empty: break (no left boundary).
     - `left_idx = stack[-1]`
     - `h = min(height[curr], height[left_idx]) - height[valley_idx]`
     - `w = curr - left_idx - 1`
     - `total_water += h * w`
   - Push `curr`.
3. Return `total_water`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
def trap_water_stack(height):
    stack = []
    water = 0
    
    for curr in range(len(height)):
        while stack and height[curr] > height[stack[-1]]:
            valley = stack.pop()
            if not stack: break
            
            left = stack[-1]
            dist = curr - left - 1
            # Water trapped is limited by the shorter boundary
            h = min(height[curr], height[left]) - height[valley]
            water += h * dist
            
        stack.append(curr)
        
    return water
```
