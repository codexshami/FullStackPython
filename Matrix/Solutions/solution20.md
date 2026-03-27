# Solution 20: Minimal Obstacle Bypass (Shortest Path in Binary Matrix)

## Approach Explanation
This is a shortest path problem in an unweighted grid, so BFS is the optimal approach. 8-directional movement is allowed.

## Step-by-Step Logic
1. If `grid[0][0] == 1` or `grid[n-1][n-1] == 1`, return -1.
2. Initialize `queue = deque([(0, 0, 1)])` (row, col, distance).
3. Mark `grid[0][0] = 1` (visited).
4. While queue is not empty:
   - Pop `(r, c, d)`.
   - If `(r, c)` is destination, return `d`.
   - Check all 8 neighbors:
     - If in bounds and `grid == 0`:
       - Mark `grid = 1` and append to queue with `d + 1`.
5. Return -1.

## Complexity
- **Time Complexity:** O(N^2).
- **Space Complexity:** O(N^2).

## Code
```python
from collections import deque

def shortest_path_binary_matrix(grid):
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]: return -1
    
    q = deque([(0, 0, 1)]) # row, col, dist
    grid[0][0] = 1 # Mark as visited
    
    while q:
        r, c, d = q.popleft()
        if r == n - 1 and c == n - 1:
            return d
            
        # 8 directions
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0: continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not grid[nr][nc]:
                    grid[nr][nc] = 1 # Mark visited
                    q.append((nr, nc, d + 1))
                    
    return -1
```
