# Solution 13: Maximal Greedy Partitioning (Partition Labels)

## Approach Explanation
We use a hash map to record the last occurrence of each character. Then we iterate through the string and maintain a `boundary` which is the furthest last occurrence of any character seen in the current partition.

## Step-by-Step Logic
1. `last = {char: i for i, char in enumerate(s)}`.
2. `start = 0`, `end = 0`, `res = []`.
3. For `i, char` in `enumerate(s)`:
   - `end = max(end, last[char])`.
   - If `i == end`:
     - Partition found! Append `end - start + 1` to `res`.
     - `start = i + 1`.
4. Return `res`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1) (size of alphabet).

## Code
```python
def partition_labels(s):
    last = {c: i for i, c in enumerate(s)}
    start = end = 0
    res = []
    
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            res.append(end - start + 1)
            start = i + 1
            
    return res
```
