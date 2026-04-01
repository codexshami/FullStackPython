# Solution 12: The Triangle Descent (Triangle Minimum Path Sum)

## Approach Explanation
We work bottom-up, updating each cell with the minimum of the two adjacent cells below it, plus the cell's own value. The answer ends up at the top.

## Step-by-Step Logic
1. Start from the second-to-last row.
2. For each element: `triangle[r][c] += min(triangle[r+1][c], triangle[r+1][c+1])`.
3. After processing all rows, `triangle[0][0]` contains the answer.

## Complexity
- **Time Complexity:** O(N^2) where N is the number of rows.
- **Space Complexity:** O(1) (modify the input in place).

## Code
```python
def minimum_total(triangle):
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += min(triangle[row + 1][col], 
                                       triangle[row + 1][col + 1])
    return triangle[0][0]
```
