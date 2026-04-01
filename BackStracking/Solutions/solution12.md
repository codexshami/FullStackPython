# Solution 12: The Knight's Tour (Knight's Tour Problem)

## Approach Explanation
We use backtracking to move the knight across all cells. From each cell, the knight has up to 8 possible moves. We try each move, backtracking if a dead end is reached.

## Step-by-Step Logic
1. Initialize the board with -1 (unvisited).
2. Start from position (0, 0), mark it as move 0.
3. For each step, try all 8 possible knight moves.
4. If a move leads to a valid, unvisited cell, mark it and recurse.
5. If all cells are visited (step == N*N - 1), return True.
6. Backtrack by unmarking the cell.

## Complexity
- **Time Complexity:** O(8^(N^2)) in worst case.
- **Space Complexity:** O(N^2).

## Code
```python
def knights_tour(n):
    board = [[-1] * n for _ in range(n)]
    moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
    moves_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1
    
    def solve(x, y, move_count):
        if move_count == n * n:
            return True
        for i in range(8):
            nx, ny = x + moves_x[i], y + moves_y[i]
            if is_valid(nx, ny):
                board[nx][ny] = move_count
                if solve(nx, ny, move_count + 1):
                    return True
                board[nx][ny] = -1
        return False
    
    board[0][0] = 0
    if solve(0, 0, 1):
        return board
    return None
```
