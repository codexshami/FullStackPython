# Solution 17: Structural Weakness Analysis (Brick Wall)

## Approach Explanation
Crossing the least number of bricks is equivalent to crossing the most number of edges. We use a hash map to count the frequencies of the vertical edges (positions) across all rows.

## Step-by-Step Logic
1. Initialize `edges = {0: 0}`.
2. For each `row` in `wall`:
   - `curr_pos = 0`.
   - Iterate through bricks in `row` (except the last one):
     - `curr_pos += brick_width`.
     - `edges[curr_pos] = edges.get(curr_pos, 0) + 1`.
3. The number of rows is `len(wall)`.
4. Max edges found is `max(edges.values())`.
5. Minimum crossed bricks = `total_rows - max_edges`.

## Complexity
- **Time Complexity:** O(N), where N is total bricks.
- **Space Complexity:** O(W), where W is the width of the wall (or number of unique edge positions).

## Code
```python
def least_bricks(wall):
    edges = {0: 0} # map position to edge count
    for row in wall:
        pos = 0
        for brick in row[:-1]:
            pos += brick
            edges[pos] = edges.get(pos, 0) + 1
            
    return len(wall) - max(edges.values())
```
