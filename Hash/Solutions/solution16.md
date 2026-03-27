# Solution 16: Grid Constraint Validation (Valid Sudoku - Hash Variant)

## Approach Explanation
We can use a single set to store "seen" strings for each row, column, and box. For example, "5 in row 0", "5 in col 1", and "5 in box 0-0".

## Step-by-Step Logic
1. Initialize `seen = set()`.
2. Iterate through `r` and `c` from 0 to 8:
   - If `board[r][c] != '.'`:
     - `val = board[r][c]`.
     - Create tokens: `f"{val} in row {r}"`, `f"{val} in col {c}"`, `f"{val} in box {r//3}-{c//3}"`.
     - If any token is already in `seen`, return False.
     - Add all tokens to `seen`.
3. Return True.

## Complexity
- **Time Complexity:** O(1) (fixed 9x9 board).
- **Space Complexity:** O(1).

## Code
```python
def is_valid_sudoku(board):
    seen = set()
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val != '.':
                if (val, 'r', r) in seen or \
                   (val, 'c', c) in seen or \
                   (val, 'b', r//3, c//3) in seen:
                    return False
                seen.add((val, 'r', r))
                seen.add((val, 'c', c))
                seen.add((val, 'b', r//3, c//3))
    return True
```
