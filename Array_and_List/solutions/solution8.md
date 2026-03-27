# Solution 8: Merging Overlaps

## Approach Explanation
We sort the intervals by their starting values. Then we iterate through the sorted list and check if the current interval overlaps with the last merged interval in our results. If it overlaps, we update the end of the last merged interval. If it doesn't, we add it as a new interval.

## Step-by-Step Logic
1. Sort `intervals` based on the first element of each interval.
2. Initialize `merged = []`.
3. Iterate through each `interval` in the sorted list.
4. If `merged` is empty or the last interval in `merged`'s end is less than the current `interval`'s start:
   - Add the current `interval` to `merged`.
5. Else (they overlap):
   - Update the end of the last interval in `merged` to be the maximum of its own end and the current `interval`'s end.
6. Return `merged`.

## Complexity
- **Time Complexity:** O(N log N) due to sorting, where N is the number of intervals.
- **Space Complexity:** O(N) to store the result, or O(log N) for sorting space.

## Code
```python
def merge_intervals(intervals):
    if not intervals:
        return []
        
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        last_start, last_end = merged[-1]
        curr_start, curr_end = intervals[i]
        
        # If the current interval overlaps with the last merged interval
        if curr_start <= last_end:
            # Update the end of the last merged interval
            merged[-1][1] = max(last_end, curr_end)
        else:
            # Otherwise, append the current interval
            merged.append([curr_start, curr_end])
            
    return merged
```
