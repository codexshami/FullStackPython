# Solution 13: The Rotten Oranges (Rotting Oranges)

## Approach Explanation
This is a multi-source BFS problem. All initially rotten oranges are sources. We process them level by level (each level = 1 minute), spreading rot to adjacent fresh oranges.

## Step-by-Step Logic
1. Add all rotten oranges (value 2) to the queue. Count fresh oranges.
2. BFS level by level:
   - For each rotten orange, rot all adjacent fresh oranges.
   - Decrement fresh count.
3. If fresh count reaches 0, return the number of minutes. Otherwise, return -1.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N).

## Code
```python
from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    
    if fresh == 0:
        return 0
    
    minutes = 0
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
        minutes += 1
    
    return minutes - 1 if fresh == 0 else -1
```
