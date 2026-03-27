# Solution 15: Chromatic Saturation (Flood Fill)

## Approach Explanation
We use DFS to visit all connected pixels of the same original color and change them to the new color.

## Step-by-Step Logic
1. Store the `start_color = image[sr][sc]`.
2. If `start_color == color`, return `image`.
3. Implement `dfs(r, c)`:
   - If `(r, c)` is out of bounds or `image[r][c] != start_color`, return.
   - Set `image[r][c] = color`.
   - Call `dfs` on 4 neighbors.
4. Call `dfs(sr, sc)` and return `image`.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N).

## Code
```python
def flood_fill(image, sr, sc, color):
    start_color = image[sr][sc]
    if start_color == color: return image
    
    rows, cols = len(image), len(image[0])
    
    def dfs(r, c):
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            image[r][c] != start_color):
            return
            
        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    dfs(sr, sc)
    return image
```
