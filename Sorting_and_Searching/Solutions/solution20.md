# Solution 20: Stepped Matrix Search

## Approach Explanation
We start from the top-right corner of the matrix. At each step:
- If `target == curr`, return true.
- If `target < curr`, the target must be in a smaller column (move left).
- If `target > curr`, the target must be in a larger row (move down).
This works because the rows and columns are sorted.

## Step-by-Step Logic
1. Start at `row = 0`, `col = cols - 1`.
2. While `row < rows` and `col >= 0`:
   - If `matrix[row][col] == target`, return True.
   - If `matrix[row][col] > target`, `col -= 1`.
   - Else, `row += 1`.
3. If loop finishes, return False.

## Complexity
- **Time Complexity:** O(M + N).
- **Space Complexity:** O(1).

## Code
```python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]: return False
    
    rows, cols = len(matrix), len(matrix[0])
    r, c = 0, cols - 1
    
    while r < rows and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1
        else:
            r += 1
            
    return False
```
