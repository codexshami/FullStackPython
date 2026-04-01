# Solution 4: The Island Counter (Number of Islands)

## Approach Explanation
We treat the grid as a graph. For each unvisited '1', we start a DFS/BFS to mark all connected land cells as visited, incrementing the island count.

## Step-by-Step Logic
1. Iterate through every cell.
2. When we find a '1', increment the island count and run DFS to mark all connected '1's as '0' (visited).
3. DFS explores all 4 directions.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N) in worst case for recursion.

## Code
```python
def num_islands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # mark visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    
    return count
```
