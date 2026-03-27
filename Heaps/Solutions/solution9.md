# Solution 9: Architectural Ascent

## Approach Explanation
We use a Min-Heap to keep track of the largest height differences where we used a ladder. If the number of height differences exceeds the number of ladders, we replace the smallest difference (using the ladder) with bricks.

## Step-by-Step Logic
1. Initialize a min-heap `h`.
2. For each building from `i = 0` to `len(heights) - 2`:
   - Calculate `diff = heights[i+1] - heights[i]`.
   - If `diff > 0`:
     - Push `diff` to the heap.
     - If `len(h) > ladders`:
       - Pop the smallest `diff` from the heap.
       - Subtract that `diff` from `bricks`.
     - If `bricks < 0`, return current index `i`.
3. If we finish the loop, return `len(heights) - 1`.

## Complexity
- **Time Complexity:** O(N log L), where L is the number of ladders.
- **Space Complexity:** O(L).

## Code
```python
import heapq

def furthest_building(heights, bricks, ladders):
    heap = []
    
    for i in range(len(heights) - 1):
        diff = heights[i+1] - heights[i]
        if diff > 0:
            heapq.heappush(heap, diff)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
                
    return len(heights) - 1
```
