# Solution 4: Proximity Analysis

## Approach Explanation
We use a Max-Heap of size `k`. We store the squared distance `(x^2 + y^2)` and the point itself. By using a Max-Heap, we can always remove the point that is furthest from the origin among the current `k` points.

## Step-by-Step Logic
1. Initialize a max-heap.
2. For each `(x, y)` in `points`:
   - Calculate `dist = -(x*x + y*y)` (negative to simulate Max-Heap in Python).
   - Push `(dist, [x, y])` to the heap.
   - If heap size > k, pop the largest distance (the top).
3. Extract points from the heap and return.

## Complexity
- **Time Complexity:** O(N log K).
- **Space Complexity:** O(K).

## Code
```python
import heapq

def k_closest(points, k):
    max_heap = []
    
    for x, y in points:
        dist = x*x + y*y
        # Store negative distance for max-heap behavior
        heapq.heappush(max_heap, (-dist, [x, y]))
        
        if len(max_heap) > k:
            heapq.heappop(max_heap)
            
    return [p[1] for p in max_heap]
```
