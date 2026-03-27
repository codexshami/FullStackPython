# Solution 15: Adaptive Insertion (Insert Interval)

## Approach Explanation
We process the intervals in three stages:
1. Intervals that end before the `newInterval` starts (no overlap).
2. Intervals that overlap with `newInterval` (merge them into `newInterval`).
3. Intervals that start after the (merged) `newInterval` ends (no overlap).

## Step-by-Step Logic
1. `res = []`, `i = 0`.
2. Phase 1 (Before): While `intervals[i][1] < newInterval[0]`, append to `res`.
3. Phase 2 (Merge): While `intervals[i][0] <= newInterval[1]`:
   - `newInterval[0] = min(newInterval[0], intervals[i][0])`
   - `newInterval[1] = max(newInterval[1], intervals[i][1])`
   - `i += 1`.
4. Append `newInterval` to `res`.
5. Phase 3 (After): Append the rest of `intervals` to `res`.
6. Return `res`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N) for the result.

## Code
```python
def insert_interval(intervals, newInterval):
    res = []
    i = 0
    n = len(intervals)
    
    # 1. Before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
        
    # 2. Merging overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)
    
    # 3. After newInterval
    while i < n:
        res.append(intervals[i])
        i += 1
        
    return res
```
