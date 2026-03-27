# Solution 7: Adversarial Grid Logic (Tic-Tac-Toe Design)

## Approach Explanation
To check the win condition in O(1) time per move, we don't need a full grid. Instead, we track the sum of values for each row, column, and the two diagonals. Let Player 1 add 1 and Player 2 subtract 1. If any sum reaches `n` or `-n`, that player wins.

## Step-by-Step Logic
1. `__init__`: Create arrays `rows` and `cols` of size `n`, and two integers `diag` and `anti_diag`.
2. `move(row, col, player)`:
   - `val = 1` if `player == 1` else `-1`.
   - `rows[row] += val`.
   - `cols[col] += val`.
   - If `row == col`, `diag += val`.
   - If `row + col == n - 1`, `anti_diag += val`.
   - If `abs(rows[row]) == n` or `abs(cols[col]) == n` or `abs(diag) == n` or `abs(anti_diag) == n`, return `player`.
   - Else, return 0.

## Complexity
- **Time Complexity:** O(1) per move.
- **Space Complexity:** O(N).

## Code
```python
class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        val = 1 if player == 1 else -1
        
        self.rows[row] += val
        self.cols[col] += val
        if row == col:
            self.diag += val
        if row + col == self.n - 1:
            self.anti_diag += val
            
        if (abs(self.rows[row]) == self.n or 
            abs(self.cols[col]) == self.n or 
            abs(self.diag) == self.n or 
            abs(self.anti_diag) == self.n):
            return player
            
        return 0
```
