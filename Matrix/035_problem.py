#Find the number of island in binary matrix
def num_islands(grid):
    if not grid:
        return 0
    
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # Mark the cell as visited
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':  # Found an island
                count += 1
                dfs(i, j)  # Mark the entire island as visited
    
    return count
# Get input for the binary matrix
rows = int(input("Enter the number of rows for the binary matrix: "))
cols = int(input("Enter the number of columns for the binary matrix: "))
grid = []
print("Enter the elements of the binary matrix (0 or 1):")
for i in range(rows):
    row = input().split()
    grid.append(row)
# Find the number of islands and print the result
result = num_islands(grid)
print("The number of islands in the binary matrix is:", result)
#time complexity: O(n*m) where n is the number of rows and m is the number of columns in the grid, because we need to visit each cell of the grid at most once. The space complexity is O(n*m) in the worst case when the grid is filled with land (1s), because we may need to store all cells in the call stack during the depth-first search.