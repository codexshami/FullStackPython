# Solution 17: Allocation Capacity (Meeting Rooms II)

## Approach Explanation
We can use a Min-Heap to track the end times of meetings currently in progress. When a new meeting starts, we check if the earliest-ending meeting has already finished. If so, we reuse its room.

## Step-by-Step Logic
1. Sort `intervals` by `start` time.
2. Initialize an empty Min-Heap `rooms`.
3. For each `interval`:
   - If `rooms` is not empty and `rooms[0] <= interval[start]`:
     - A room has become free. Pop the oldest end time.
   - Push `interval[end]` onto the heap (new meeting occupies a room).
4. The size of the heap is the number of rooms required.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(N).

## Code
```python
import heapq

def min_meeting_rooms(intervals):
    if not intervals: return 0
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    # Heap stores end times of active meetings
    rooms = []
    
    for start, end in intervals:
        # If the earliest ending meeting is done, reuse the room
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
            
        heapq.heappush(rooms, end)
        
    return len(rooms)
```
