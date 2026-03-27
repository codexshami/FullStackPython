# Solution 13: Diagonal Invariance (Toeplitz Matrix)

## Approach Explanation
An element `matrix[i][j]` belongs to the same diagonal as `matrix[i-1][j-1]`. We just need to check if each element is equal to its top-left neighbor.

## Step-by-Step Logic
1. Iterate through `i` from 1 to `m-1`.
2. Iterate through `j` from 1 to `n-1`.
3. If `matrix[i][j] != matrix[i-1][j-1]`, return False.
4. If loop finishes, return True.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(1).

## Code
```python
def is_toeplitz_matrix(matrix):
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False
    return True
```
