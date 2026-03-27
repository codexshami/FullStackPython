# Solution 19: Watershed Convergence (Pacific Atlantic Water Flow)

## Approach Explanation
Instead of checking where water flows *to*, we check where water can flow *from* the oceans (reverse flow).
1. Start DFS from Pacific borders (top and left) and find all reachable cells.
2. Start DFS from Atlantic borders (bottom and right) and find all reachable cells.
3. The intersection of these two sets of reachable cells is the answer.

## Step-by-Step Logic
1. `pacific_reachable = set()`, `atlantic_reachable = set()`.
2. `dfs(r, c, reachable_set, prev_height)`:
   - If out of bounds or `(r, c)` already in set or `height < prev_height`, return.
   - Add `(r, c)` to set.
   - Recurse on 4 neighbors.
3. Call `dfs` for all boundary cells.
4. Return cells present in both sets.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N).

## Code
```python
def pacific_atlantic(heights):
    if not heights: return []
    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()
    
    def dfs(r, c, visit, prevH):
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            (r, c) in visit or 
            heights[r][c] < prevH):
            return
        visit.add((r, c))
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])
        
    for c in range(cols):
        dfs(0, c, pac, heights[0][c])
        dfs(rows - 1, c, atl, heights[rows-1][c])
        
    for r in range(rows):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, cols - 1, atl, heights[r][cols-1])
        
    res = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])
    return res
```
