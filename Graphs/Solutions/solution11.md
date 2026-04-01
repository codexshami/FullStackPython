# Solution 11: The Flood Fill (Flood Fill Algorithm)

## Approach Explanation
We use DFS from the starting pixel. We change all connected pixels with the same original color to the new color.

## Step-by-Step Logic
1. Record the original color at `(sr, sc)`.
2. If the original color equals the new color, return (no-op).
3. DFS from `(sr, sc)`: change the pixel color and recurse on all 4 neighbors with the original color.

## Complexity
- **Time Complexity:** O(M * N).
- **Space Complexity:** O(M * N) for recursion stack.

## Code
```python
def flood_fill(image, sr, sc, color):
    original = image[sr][sc]
    if original == color:
        return image
    
    rows, cols = len(image), len(image[0])
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original:
            return
        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    dfs(sr, sc)
    return image
```
