# Solution 6: Lexical Pathfinding (Word Search)

## Approach Explanation
We use Backtracking to explore all possible paths from each cell.

## Step-by-Step Logic
1. Iterate through each cell `(r, c)` in the board.
2. If `board[r][c] == word[0]`, start a recursive `dfs(r, c, index)`:
   - Base case 1: If `index == len(word)`, return True.
   - Base case 2: If `(r, c)` is out of bounds or `board[r][c] != word[index]`, return False.
   - Mark `board[r][c]` as visited (e.g., set to `#`).
   - Explore 4 neighbors: `dfs(r+1, c, index+1)`, etc.
   - Backtrack: Restore `board[r][c]` to original character.
   - return True if any neighbor returned True.
3. If no starting cell leads to finding the word, return False.

## Complexity
- **Time Complexity:** O(M * N * 4^L), where L is the length of the word.
- **Space Complexity:** O(L) for the recursion stack.

## Code
```python
def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            board[r][c] != word[i]):
            return False
            
        temp = board[r][c]
        board[r][c] = "#" # Mark visited
        
        found = (dfs(r + 1, c, i + 1) or 
                 dfs(r - 1, c, i + 1) or 
                 dfs(r, c + 1, i + 1) or 
                 dfs(r, c - 1, i + 1))
        
        board[r][c] = temp # Backtrack
        return found
        
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
```
