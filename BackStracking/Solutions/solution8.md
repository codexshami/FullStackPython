# Solution 8: The Word Forger (Word Search)

## Approach Explanation
We use DFS from every cell. For each cell matching the first character, we explore all 4 directions. We mark cells as visited during exploration and unmark during backtracking.

## Step-by-Step Logic
1. Iterate through every cell in the board.
2. If a cell matches the first character of the word, start DFS.
3. At each step, check bounds, if the cell matches the current character, and if it's not visited.
4. Temporarily mark the cell as visited (e.g., replace with '#').
5. Recurse in all 4 directions for the next character.
6. Restore the cell (backtrack).

## Complexity
- **Time Complexity:** O(M * N * 4^L) where L is word length.
- **Space Complexity:** O(L) for recursion stack.

## Code
```python
def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False
        
        temp = board[r][c]
        board[r][c] = '#'  # mark visited
        
        found = (dfs(r + 1, c, index + 1) or
                 dfs(r - 1, c, index + 1) or
                 dfs(r, c + 1, index + 1) or
                 dfs(r, c - 1, index + 1))
        
        board[r][c] = temp  # backtrack
        return found
    
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
```
