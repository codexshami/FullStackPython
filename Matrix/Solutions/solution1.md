# Solution 1: Orbital Navigation (Spiral Matrix)

## Approach Explanation
We maintain four boundaries: `top`, `bottom`, `left`, and `right`. While the boundaries haven't crossed each other, we traverse the matrix in a clockwise spiral.

## Step-by-Step Logic
1. `top = 0`, `bottom = m - 1`, `left = 0`, `right = n - 1`.
2. While `top <= bottom` and `left <= right`:
   - Traverse from `left` to `right` along `top`. Increment `top`.
   - Traverse from `top` to `bottom` along `right`. Decrement `right`.
   - If `top <= bottom`:
     - Traverse from `right` to `left` along `bottom`. Decrement `bottom`.
   - If `left <= right`:
     - Traverse from `bottom` to `top` along `left`. Increment `left`.
3. Return the result list.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(1) (ignoring output array).

## Code
```python
def spiral_order(matrix):
    if not matrix: return []
    
    m, n = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, m - 1, 0, n - 1
    res = []
    
    while len(res) < m * n:
        # 1. Left to Right
        for j in range(left, right + 1):
            res.append(matrix[top][j])
        top += 1
        
        # 2. Top to Bottom
        if len(res) < m * n:
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
        # 3. Right to Left
        if len(res) < m * n:
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1
            
        # 4. Bottom to Top
        if len(res) < m * n:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
    return res
```
