# Solution 7: The Sudoku Solver (Solve Sudoku)

## Approach Explanation
We scan for empty cells and try digits 1-9. For each digit, we validate against Sudoku rules (row, column, 3x3 box). If valid, we place it and recurse. If no digit works, we backtrack.

## Step-by-Step Logic
1. Find the next empty cell (containing '.').
2. Try digits '1' through '9'.
3. Check if the digit is valid in the current row, column, and 3x3 box.
4. If valid, place the digit and recurse.
5. If recursion succeeds, return True.
6. Otherwise, reset the cell and try the next digit (backtrack).

## Complexity
- **Time Complexity:** O(9^(empty cells)) in worst case.
- **Space Complexity:** O(81) for the board.

## Code
```python
def solve_sudoku(board):
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False
            box_row, box_col = 3 * (row // 3) + i // 3, 3 * (col // 3) + i % 3
            if board[box_row][box_col] == num:
                return False
        return True
    
    def solve(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if solve(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True
    
    solve(board)
```
