# Solution 14: Geometric Boundary (Island Perimeter)

## Approach Explanation
For each land cell, it contributes 4 to the perimeter. However, if a land cell has a neighbor that is also land, those two share an edge, and we must subtract 2 from the total perimeter (1 for each cell).

## Step-by-Step Logic
1. Initialize `perimeter = 0`.
2. Iterate through each cell `(i, j)`:
   - If `grid[i][j] == 1`:
     - `perimeter += 4`.
     - Check neighbor to the left: if `grid[i][j-1] == 1`, `perimeter -= 2`.
     - Check neighbor above: if `grid[i-1][j] == 1`, `perimeter -= 2`.
3. Return `perimeter`.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(1).

## Code
```python
def island_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                # Check top neighbor
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                # Check left neighbor
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2
                    
    return perimeter
```
