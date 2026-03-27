# Solution 3: Null Propagation (Set Matrix Zeroes)

## Approach Explanation
To use O(1) space, we use the first row and first column as markers for whether that row/column should be set to zero. We need separate flags to track if the first row or first column themselves should be zeroed.

## Step-by-Step Logic
1. Check if the first row and first column should be zero.
2. Iterate through the rest of the matrix (from `(1,1)`), marking `matrix[i][0] = 0` and `matrix[0][j] = 0` if `matrix[i][j] == 0`.
3. Use these markers to zero out the inner matrix.
4. Finally, zero out the first row and first column if their flags are set.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(1).

## Code
```python
def set_zeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))
    
    # Mark in first row/col
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    # Fill based on marks
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
                
    # Handle first row/col
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
```
