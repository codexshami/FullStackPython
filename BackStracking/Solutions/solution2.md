# Solution 2: The Maze Runner (Rat in a Maze)

## Approach Explanation
We use DFS with backtracking. Starting from `(0,0)`, we try all four directions. We mark visited cells to avoid revisiting and backtrack when a path fails.

## Step-by-Step Logic
1. Start at `(0, 0)`. The destination is `(N-1, N-1)`.
2. Try moving in all 4 directions: Down, Left, Right, Up (sorted for lexicographic order).
3. For each move, check bounds, if cell is open (`1`), and if not visited.
4. If destination is reached, save the path.
5. Backtrack: unmark the cell and remove the last direction.

## Complexity
- **Time Complexity:** O(4^(N^2)) in worst case.
- **Space Complexity:** O(N^2) for the visited matrix.

## Code
```python
def find_paths(maze):
    n = len(maze)
    result = []
    visited = [[False] * n for _ in range(n)]
    directions = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]
    
    def backtrack(r, c, path):
        if r == n - 1 and c == n - 1:
            result.append(path)
            return
        
        for dir_char, dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                backtrack(nr, nc, path + dir_char)
                visited[nr][nc] = False
    
    if maze[0][0] == 1:
        visited[0][0] = True
        backtrack(0, 0, "")
    return sorted(result)
```
