# Solution 16: Topographical Connectivity (Number of Islands)

## Approach Explanation
We iterate through each cell. When we find a '1', we increment our island count and use DFS (or BFS) to "sink" the entire island (set all connected '1's to '0').

## Step-by-Step Logic
1. Initialize `count = 0`.
2. Iterate through `r` and `c`.
3. If `grid[r][c] == "1"`:
   - `count += 1`.
   - Call `dfs(r, c)` to sink the island.
4. `dfs(r, c)`:
   - If out of bounds or `grid[r][c] == "0"`, return.
   - `grid[r][c] = "0"`.
   - Recurse on 4 neighbors.
5. Return `count`.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N) for recursion stack.

## Code
```python
def num_islands(grid):
    if not grid: return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            grid[r][c] == "0"):
            return
            
        grid[r][c] = "0" # Sink it
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
                
    return count
```
