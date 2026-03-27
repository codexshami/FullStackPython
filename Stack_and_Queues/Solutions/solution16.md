# Solution 16: Columnar Capacity

## Approach Explanation
We use a monotonic increasing stack to store the indices of the bars. When we encounter a bar that is shorter than the one at the top of the stack, it means we can no longer expand the rectangle formed by the top bar. We then pop and calculate the area.

## Step-by-Step Logic
1. Add a bar of height 0 at the end of `heights` (as a sentinel).
2. Initialize an empty stack and `max_area = 0`.
3. Iterate through `heights` with index `i`:
   - While `stack` is not empty and `heights[i] < heights[stack[-1]]`:
     - `h = heights[stack.pop()]`
     - `w = i if not stack else i - stack[-1] - 1`
     - `max_area = max(max_area, h * w)`
   - Push current index `i`.
4. Return `max_area`.

## Complexity
- **Time Complexity:** O(N), every element is pushed and popped exactly once.
- **Space Complexity:** O(N).

## Code
```python
def largest_rectangle_area(heights):
    # Add a sentinel height to process remaining bars in stack
    heights.append(0)
    stack = []
    max_area = 0
    
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            # Width is determined by the distance between i and previous smaller element
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
        
    return max_area
```
