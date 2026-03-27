# Solution 5: Kinetic Attrition

## Approach Explanation
We use a Max-Heap to efficiently retrieve the two heaviest stones in each step.

## Step-by-Step Logic
1. Convert all stones to negative values and `heapify` them to create a Max-Heap.
2. While there is more than 1 stone:
   - Pop two stones `s1` and `s2`.
   - If `s1 != s2`, calculate the difference `s1 - s2` (or `abs(s1-s2)`) and push it back.
3. If one stone remains, return its absolute value; otherwise, return 0.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(N).

## Code
```python
import heapq

def last_stone_weight(stones):
    # Python uses min-heap, so negate values for max-heap
    h = [-s for s in stones]
    heapq.heapify(h)
    
    while len(h) > 1:
        s1 = heapq.heappop(h)
        s2 = heapq.heappop(h)
        # If they are different, push back the positive difference
        if s1 != s2:
            heapq.heappush(h, s1 - s2)
            
    return -h[0] if h else 0
```
