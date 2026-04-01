# Solution 11: The Color Map (Graph Coloring / M-Coloring Problem)

## Approach Explanation
We assign colors to vertices one by one. Before assigning, we check if any adjacent vertex already has the same color. If no valid color exists, we backtrack.

## Step-by-Step Logic
1. Start with vertex 0 and try colors 1 through `m`.
2. Check if the color is safe (no adjacent vertex has the same color).
3. If safe, assign the color and recurse for the next vertex.
4. If all vertices are colored, return the solution.
5. If no color works, backtrack.

## Complexity
- **Time Complexity:** O(m^V) where V is the number of vertices.
- **Space Complexity:** O(V).

## Code
```python
def graph_coloring(graph, m):
    n = len(graph)
    colors = [0] * n
    
    def is_safe(vertex, color):
        for i in range(n):
            if graph[vertex][i] == 1 and colors[i] == color:
                return False
        return True
    
    def backtrack(vertex):
        if vertex == n:
            return True
        for color in range(1, m + 1):
            if is_safe(vertex, color):
                colors[vertex] = color
                if backtrack(vertex + 1):
                    return True
                colors[vertex] = 0
        return False
    
    if backtrack(0):
        return colors
    return []
```
