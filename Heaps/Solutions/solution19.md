# Solution 19: Logistical Endurance

## Approach Explanation
This is a Greedy problem. We drive as far as we can with our current fuel. Along the way, we pass gas stations. We store the fuel available at these stations in a Max-Heap. If we run out of fuel before reaching the next station or the target, we pop the largest fuel amount from our heap (as if we had stopped at that station earlier).

## Step-by-Step Logic
1. Initialize a Max-Heap for station fuel.
2. Initialize `curr_dist = startFuel`, `stops = 0`, and `i = 0` (station index).
3. While `curr_dist < target`:
   - Add all stations that we have already passed or reached (`stations[i][0] <= curr_dist`) to the heap.
   - If the heap is empty, we cannot go further. Return -1.
   - Pop the largest fuel, add it to `curr_dist`, and increment `stops`.
4. Return `stops`.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(N).

## Code
```python
import heapq

def min_refuel_stops(target, startFuel, stations):
    # Max-heap for fuel amounts
    h = []
    res = 0
    curr = startFuel
    i = 0
    
    while curr < target:
        # Add all reachable stations to the heap
        while i < len(stations) and stations[i][0] <= curr:
            heapq.heappush(h, -stations[i][1])
            i += 1
            
        if not h:
            return -1
            
        # Refuel from the best station passed so far
        curr += -heapq.heappop(h)
        res += 1
        
    return res
```
