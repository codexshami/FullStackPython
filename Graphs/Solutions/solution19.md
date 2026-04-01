# Solution 19: The Surrounded Regions (Surrounded Regions)

## Approach Explanation
Instead of finding surrounded regions, we find non-surrounded ones. Any 'O' connected to the border cannot be captured. We DFS from all border 'O's, mark them, then flip the rest.

## Step-by-Step Logic
1. DFS from all 'O's on the border, marking them as safe (e.g., 'S').
2. Iterate through the board:
   - Change remaining 'O's to 'X' (they're surrounded).
   - Change 'S' back to 'O' (they're safe).

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N) for recursion.

## Code
```python
def solve(board):
    if not board:
        return
    
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        board[r][c] = 'S'  # mark as safe
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    # Mark border-connected O's
    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)
    
    # Flip
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'S':
                board[r][c] = 'O'
```
