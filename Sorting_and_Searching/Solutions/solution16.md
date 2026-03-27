# Solution 16: Conflict Minimization

## Approach Explanation
This is equivalent to finding the maximum number of non-overlapping intervals (the Interval Scheduling Problem). We use a Greedy approach: sort the intervals by their END times and always pick the interval that ends earliest.

## Step-by-Step Logic
1. Sort `intervals` by `end`.
2. Initialize `count = 0` and `last_end = -inf`.
3. For each `interval`:
   - If `interval[start] >= last_end`:
     - This interval can be included! Update `last_end = interval[end]`.
   - Else:
     - This interval overlaps with the optimal set, so it must be removed. Increment `count`.
4. Return `count`.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(1).

## Code
```python
def erase_overlap_intervals(intervals):
    if not intervals: return 0
    
    # Greedy: Sort by end time
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    last_end = -float('inf')
    
    for start, end in intervals:
        if start >= last_end:
            # No overlap, keep it
            last_end = end
        else:
            # Overlap, remove it
            count += 1
            
    return count
```
