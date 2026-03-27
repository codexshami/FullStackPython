# Solution 16: Volumetric Seepage

## Approach Explanation
We use a Min-Heap to process the cells starting from the outer boundaries of the grid. The heap helps us always process the cell with the lowest height that could potentially leak water.

## Step-by-Step Logic
1. If grid is small, return 0.
2. Initialize a Min-Heap and a `visited` set.
3. Add all boundary cells to the heap and mark them as visited.
4. While heap is not empty:
   - Pop cell `(h, r, c)`.
   - Check its 4 neighbors.
   - For each unvisited neighbor:
     - Water trapped += `max(0, h - neighbor_height)`.
     - Update neighbor's height for the heap: `max(neighbor_height, h)`.
     - Push updated neighbor and mark visited.
5. Return total water.

## Complexity
- **Time Complexity:** O(M * N * log(M * N)).
- **Space Complexity:** O(M * N).

## Code
```python
import heapq

def trap_rain_water(heightMap):
    if not heightMap or not heightMap[0]: return 0
    
    m, n = len(heightMap), len(heightMap[0])
    visited = [[False] * n for _ in range(m)]
    h = []
    
    # Add all boundaries to heap
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                heapq.heappush(h, (heightMap[i][j], i, j))
                visited[i][j] = True
    
    water = 0
    while h:
        height, r, c = heapq.heappop(h)
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                water += max(0, height - heightMap[nr][nc])
                heapq.heappush(h, (max(heightMap[nr][nc], height), nr, nc))
                visited[nr][nc] = True
                
    return water
```
