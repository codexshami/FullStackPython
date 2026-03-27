# Solution 14: Temporal Union (Merge Intervals)

## Approach Explanation
We sort the intervals by their start times. Then, we iterate through the sorted intervals and merge current interval with the last merged interval if they overlap.

## Step-by-Step Logic
1. Sort `intervals` by `start`.
2. Initialize `merged = [intervals[0]]`.
3. For each `interval` from index 1:
   - `last_start, last_end = merged[-1]`
   - `curr_start, curr_end = interval`
   - If `curr_start <= last_end`:
     - Overlap! Update `merged[-1][1] = max(last_end, curr_end)`.
   - Else:
     - No overlap. Add `interval` to `merged`.
4. Return `merged`.

## Complexity
- **Time Complexity:** O(N log N) due to sorting.
- **Space Complexity:** O(N) for the result.

## Code
```python
def merge_intervals(intervals):
    if not intervals: return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        # If overlap
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
            
    return merged
```
