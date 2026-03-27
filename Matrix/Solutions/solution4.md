# Solution 4: Cellular Automaton (Game of Life)

## Approach Explanation
To update in-place, we use temporary state codes:
- `2`: Cell was dead (0), now live (1).
- `-1`: Cell was live (1), now dead (0).
When counting neighbors, absolute value of -1 is 1, so the original state is preserved.

## Step-by-Step Logic
1. For each cell `(i, j)`, count its 8 neighbors.
2. In neighbor count, consider original state 1 if value is `1` or `-1`.
3. Apply rules:
   - If `cell == 1` and `neighbors < 2 or > 3`, set `cell = -1`.
   - If `cell == 0` and `neighbors == 3`, set `cell = 2`.
4. After marking all cells, iterate and replace `2 -> 1` and `-1 -> 0`.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(1).

## Code
```python
def game_of_life(board):
    m, n = len(board), len(board[0])
    
    for i in range(m):
        for j in range(n):
            live_neighbors = 0
            for r in range(i - 1, i + 2):
                for c in range(j - 1, j + 2):
                    if r == i and c == j: continue
                    if 0 <= r < m and 0 <= c < n and abs(board[r][c]) == 1:
                        live_neighbors += 1
            
            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[i][j] = -1
            if board[i][j] == 0 and live_neighbors == 3:
                board[i][j] = 2
                
    for i in range(m):
        for j in range(n):
            if board[i][j] > 0:
                board[i][j] = 1
            else:
                board[i][j] = 0
```
