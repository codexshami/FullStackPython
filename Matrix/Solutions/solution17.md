# Solution 17: Territorial Enclosure (Surrounded Regions)

## Approach Explanation
An 'O' region is NOT surrounded if it is connected to an 'O' on the boundary.
1. Mark all 'O's on the boundary and their connected neighbors as "safe" (e.g., change to '#').
2. Iterate through the grid: rotate remaining 'O's to 'X's (since they are surrounded).
3. Change '#' back to 'O'.

## Step-by-Step Logic
1. For all boundary cells, if `board[r][c] == 'O'`, start DFS to mark the safe region.
2. After DFS, iterate through all cells:
   - If `board[r][c] == 'O'`, change to 'X'.
   - If `board[r][c] == '#'`, change to 'O'.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N).

## Code
```python
def solve(board):
    if not board: return
    
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c):
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            board[r][c] != 'O'):
            return
        board[r][c] = '#' # Mark as safe
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    # 1. Start DFS from boundary 'O's
    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)
        
    # 2. Capture and Restore
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == '#':
                board[r][c] = 'O'
```
