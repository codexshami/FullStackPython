# Solution 9: Efficient Dot Product (Sparse Matrix Multiplication)

## Approach Explanation
The standard O(M*K*N) multiplication can be optimized for sparse matrices by only iterating over non-zero elements.

## Step-by-Step Logic
1. Initialize `res` matrix of size `m x n` with 0s.
2. Iterate `i` from 0 to `m-1`.
3. Iterate `k` from 0 to `k-1`.
4. If `mat1[i][k] != 0`:
   - Only then iterate `j` from 0 to `n-1`.
   - If `mat2[k][j] != 0`:
     - `res[i][j] += mat1[i][k] * mat2[k][j]`.
This structure minimizes unnecessary multiplications.

## Complexity
- **Time Complexity:** O(M * K * N) worst case, but significantly faster for sparse matrices.
- **Space Complexity:** O(M * N) for the result.

## Code
```python
def multiply(mat1, mat2):
    m, k_dim = len(mat1), len(mat1[0])
    n = len(mat2[0])
    res = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for k in range(k_dim):
            if mat1[i][k] != 0:
                for j in range(n):
                    if mat2[k][j] != 0:
                        res[i][j] += mat1[i][k] * mat2[k][j]
                        
    return res
```
