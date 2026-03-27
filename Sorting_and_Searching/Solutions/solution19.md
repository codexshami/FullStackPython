# Solution 19: Planar Quadrant Update

## Approach Explanation
Since we have frequent updates, a standard prefix-sum array would take O(R*C) per update. Instead, we use a 2D Binary Indexed Tree (Fenwick Tree) to achieve O(log R * log C) for both update and query.

## Step-by-Step Logic
1. `__init__`: Create a 2D array `bit` of size `(M+1, N+1)`. Call `update` for every cell in the original matrix.
2. `update(r, c, val)`: Calculate the `diff = val - original_val`. Propagate this `diff` up the Fenwick tree.
3. `query(r, c)`: Get the prefix sum from `(0,0)` to `(r,c)` by iterating down the Fenwick tree.
4. `sumRegion(r1, c1, r2, c2)`: Calculate as `query(r2, c2) - query(r1-1, c2) - query(r2, c1-1) + query(r1-1, c1-1)`.

## Complexity
- **Time Complexity:** O(log M * log N) per query/update.
- **Space Complexity:** O(M * N).

## Code
```python
class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]: return
        self.M, self.N = len(matrix), len(matrix[0])
        self.mat = [[0] * self.N for _ in range(self.M)]
        self.bit = [[0] * (self.N + 1) for _ in range(self.M + 1)]
        for r in range(self.M):
            for c in range(self.N):
                self.update(r, c, matrix[r][c])

    def update(self, row, col, val):
        diff = val - self.mat[row][col]
        self.mat[row][col] = val
        i = row + 1
        while i <= self.M:
            j = col + 1
            while j <= self.N:
                self.bit[i][j] += diff
                j += j & (-j)
            i += i & (-i)

    def _query(self, row, col):
        res = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                res += self.bit[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return res

    def sumRegion(self, r1, c1, r2, c2):
        return (self._query(r2, c2) - self._query(r1 - 1, c2) - 
                self._query(r2, c1 - 1) + self._query(r1 - 1, c1 - 1))
```
