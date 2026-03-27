# Solution 14: Liquid Capture Potential

## Approach Explanation
We use two pointers, one at the beginning and one at the end. At each step, we calculate the area and update the `max_area`. We then move the pointer that points to the shorter line, as moving the longer line's pointer can only decrease the width without potentially increasing the height significantly enough to compensate.

## Step-by-Step Logic
1. Initialize `left = 0`, `right = n - 1`, and `max_area = 0`.
2. While `left < right`:
   - `width = right - left`.
   - `current_height = min(height[left], height[right])`.
   - `max_area = max(max_area, width * current_height)`.
   - If `height[left] < height[right]`, `left += 1`.
   - Else, `right -= 1`.
3. Return `max_area`.

## Complexity
- **Time Complexity:** O(N), single pass through the array.
- **Space Complexity:** O(1), no extra data structures.

## Code
```python
def max_area(height):
    left, right = 0, len(height) - 1
    maximum_area = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        h = min(height[left], height[right])
        current_area = width * h
        
        maximum_area = max(maximum_area, current_area)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return maximum_area
```
