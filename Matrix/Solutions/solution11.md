# Solution 11: Linear Serialization (Search a 2D Matrix)

## Approach Explanation
Because of the matrix properties, it can be treated as a single sorted 1D array of size `m * n`. We can perform standard Binary Search.

## Step-by-Step Logic
1. `m, n = len(matrix), len(matrix[0])`.
2. `low = 0`, `high = m * n - 1`.
3. While `low <= high`:
   - `mid = (low + high) // 2`.
   - Convert `mid` back to matrix coordinates: `r = mid // n`, `c = mid % n`.
   - If `matrix[r][c] == target`, return True.
   - If `matrix[r][c] < target`, `low = mid + 1`.
   - Else, `high = mid - 1`.
4. Return False.

## Complexity
- **Time Complexity:** O(log(M * N)).
- **Space Complexity:** O(1).

## Code
```python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]: return False
    
    m, n = len(matrix), len(matrix[0])
    l, r = 0, m * n - 1
    
    while l <= r:
        mid = (l + r) // 2
        # Map 1D index to 2D coordinates
        val = matrix[mid // n][mid % n]
        
        if val == target:
            return True
        elif val < target:
            l = mid + 1
        else:
            r = mid - 1
            
    return False
```
