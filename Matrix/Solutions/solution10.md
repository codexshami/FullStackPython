# Solution 10: Angular Sweep (Diagonal Traverse)

## Approach Explanation
We use the property that along any anti-diagonal, the sum of indices `i + j` is constant. We can group elements by this sum and then reverse every other group to get the zigzag traversal.

## Step-by-Step Logic
1. Create a hash map `diagonals` where keys are `i + j` and values are lists of elements.
2. Iterate through the matrix and append `mat[i][j]` to `diagonals[i+j]`.
3. Iterate through keys from `0` to `m + n - 2`:
   - If key is even, reverse the list of elements for that key.
   - Append to result.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N).

## Code
```python
from collections import defaultdict

def find_diagonal_order(mat):
    if not mat: return []
    
    m, n = len(mat), len(mat[0])
    diagonals = defaultdict(list)
    
    for i in range(m):
        for j in range(n):
            diagonals[i + j].append(mat[i][j])
            
    res = []
    for k in range(m + n - 1):
        if k % 2 == 0:
            res.extend(diagonals[k][::-1])
        else:
            res.extend(diagonals[k])
            
    return res
```
