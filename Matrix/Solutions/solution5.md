# Solution 5: Grid Constraints (Valid Sudoku)

## Approach Explanation
We use hash sets to track whether a digit has already appeared in a particular row, column, or 3x3 box.

## Step-by-Step Logic
1. Initialize 9 sets for rows, 9 for columns, and 9 for boxes.
2. Iterate through every cell `(r, c)` in the 9x9 board.
3. If value is not `.`:
   - Calculate box index: `(r // 3) * 3 + (c // 3)`.
   - Check if the value exists in `rows[r]`, `cols[c]`, or `boxes[idx]`.
   - If yes, return False.
   - Else, add it to all three sets.
4. If loop finishes, return True.

## Complexity
- **Time Complexity:** O(1) (since board size is fixed at 81 cells).
- **Space Complexity:** O(1).

## Code
```python
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".": continue
            
            box_idx = (r // 3) * 3 + (c // 3)
            
            if (val in rows[r] or 
                val in cols[c] or 
                val in boxes[box_idx]):
                return False
                
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)
            
    return True
```
