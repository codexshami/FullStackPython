# Solution 17: Binary Grid Maximum

## Approach Explanation
We treat each row as the base of a histogram. For each row, we maintain the heights of continuous '1's from top to bottom. Then, we apply the "Largest Rectangle in Histogram" logic to each row's heights.

## Step-by-Step Logic
1. If matrix is empty, return 0.
2. Initialize an array `heights` of size `cols`.
3. For each row in `matrix`:
   - Update `heights[j]`: increment if `matrix[row][j] == '1'`, else reset to 0.
   - Calculate the max rectangle area for this row using the histogram algorithm.
   - Update the global `max_area`.
4. Return `max_area`.

## Complexity
- **Time Complexity:** O(R * C), where R and C are rows and columns.
- **Space Complexity:** O(C).

## Code
```python
def maximal_rectangle(matrix):
    if not matrix or not matrix[0]: return 0
    
    cols = len(matrix[0])
    heights = [0] * (cols + 1) # Including sentinel
    max_area = 0
    
    for row in matrix:
        # Build histogram for current row
        for j in range(cols):
            heights[j] = heights[j] + 1 if row[j] == "1" else 0
            
        # Standard Largest Rectangle in Histogram logic
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
            
    return max_area
```
