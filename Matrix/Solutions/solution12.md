# Solution 12: Morphological Reshaping (Matrix Reshape)

## Approach Explanation
First, check if the total number of elements `m * n` is equal to `r * c`. If not, return the original matrix. Otherwise, flatten the matrix and then rebuild it with new dimensions.

## Step-by-Step Logic
1. `m, n = len(mat), len(mat[0])`.
2. If `m * n != r * c`, return `mat`.
3. Initialize `res = [[0] * c for _ in range(r)]`.
4. Iterate through `m * n` elements using a single counter `k`:
   - Value is at `mat[k // n][k % n]`.
   - Place it at `res[k // c][k % c]`.
5. Return `res`.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(R * C) for the result.

## Code
```python
def matrix_reshape(mat, r, c):
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat
        
    res = [[0] * c for _ in range(r)]
    for k in range(m * n):
        res[k // c][k % c] = mat[k // n][k % n]
        
    return res
```
