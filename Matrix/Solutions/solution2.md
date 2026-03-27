# Solution 2: Orthogonal Reorientation (Rotate Image)

## Approach Explanation
Rotating 90 degrees clockwise is equivalent to:
1. Reversing the matrix rows (vertical flip).
2. Transposing the matrix (swapping `matrix[i][j]` with `matrix[j][i]`).

## Step-by-Step Logic
1. Reverse the order of rows: `matrix.reverse()`.
2. Transpose the matrix:
   - Iterate for `i` from 0 to `n-1`.
   - Iterate for `j` from `i+1` to `n-1`.
   - Swap `matrix[i][j]` and `matrix[j][i]`.

## Complexity
- **Time Complexity:** O(N^2).
- **Space Complexity:** O(1).

## Code
```python
def rotate(matrix):
    # 1. Reverse up to down
    matrix.reverse()
    
    # 2. Transpose
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```
