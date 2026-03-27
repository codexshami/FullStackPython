# Solution 5: Binomial Extraction (Pascal's Triangle II)

## Approach Explanation
We can generate the current row using the previous row. A row $N$ can be calculated from row $N-1$ by summing adjacent elements.

## Step-by-Step Logic
1. `getRow(n)`:
   - Base case: If `n == 0`, return `[1]`.
2. Recursive step: `prev_row = getRow(n - 1)`.
3. Create `curr_row` starting and ending with 1.
4. Intermediate elements: `curr_row[i] = prev_row[i-1] + prev_row[i]`.
5. Return `curr_row`.

## Complexity
- **Time Complexity:** O(N^2).
- **Space Complexity:** O(N).

## Code
```python
def get_row(rowIndex):
    if rowIndex == 0:
        return [1]
    
    prev_row = get_row(rowIndex - 1)
    res = [1]
    for i in range(1, len(prev_row)):
        res.append(prev_row[i-1] + prev_row[i])
    res.append(1)
    
    return res
```
