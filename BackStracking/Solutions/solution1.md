# Solution 1: The Queen's Dominion (N-Queens)

## Approach Explanation
We place queens one row at a time. For each row, we try every column. Before placing, we check if the column, the main diagonal, and the anti-diagonal are safe. We backtrack if a placement leads to no valid solution.

## Step-by-Step Logic
1. Use sets to track occupied columns, diagonals (`row - col`), and anti-diagonals (`row + col`).
2. For each row, try placing a queen at each column.
3. If valid, place the queen, update sets, and recurse to the next row.
4. When all rows are filled, save the board configuration.
5. Backtrack by removing the queen and updating sets.

## Complexity
- **Time Complexity:** O(N!).
- **Space Complexity:** O(N^2).

## Code
```python
def solve_n_queens(n):
    results = []
    board = [['.' ] * n for _ in range(n)]
    cols = set()
    diag = set()       # row - col
    anti_diag = set()  # row + col
    
    def backtrack(row):
        if row == n:
            results.append([''.join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag or (row + col) in anti_diag:
                continue
            board[row][col] = 'Q'
            cols.add(col)
            diag.add(row - col)
            anti_diag.add(row + col)
            backtrack(row + 1)
            board[row][col] = '.'
            cols.remove(col)
            diag.remove(row - col)
            anti_diag.remove(row + col)
    
    backtrack(0)
    return results
```
