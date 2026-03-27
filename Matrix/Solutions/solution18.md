# Solution 18: Max Extent Analysis (Max Area of Island)

## Approach Explanation
Iterate through the grid. When a '1' is found, use DFS to calculate the size of that island and update the global `max_area`. To avoid revisiting, set visited cells to '0'.

## Step-by-Step Logic
1. `max_area = 0`.
2. For each cell `(r, c)`:
   - If `grid[r][c] == 1`:
     - `max_area = max(max_area, dfs(r, c))`.
3. `dfs(r, c)`:
   - If out of bounds or `grid[r][c] == 0`, return 0.
   - `grid[r][c] = 0`.
   - Return `1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)`.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N).

## Code
```python
def max_area_of_island(grid):
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c):
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            grid[r][c] == 0):
            return 0
            
        grid[r][c] = 0 # Mark visited
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
    mx = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                mx = max(mx, dfs(r, c))
    return mx
```
