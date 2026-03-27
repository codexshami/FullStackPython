# Solution 11: Real-time Equilibrium

## Approach Explanation
We maintain two heaps: a Max-Heap for the lower half of the numbers and a Min-Heap for the upper half. The difference in size between the two heaps is at most 1.

## Step-by-Step Logic
1. `addNum(num)`:
   - Push `num` to max-heap (negate it).
   - Pop max-heap and push the value to min-heap (ensures upper half gets the correct element).
   - If `len(min_heap) > len(max_heap)`, pop min-heap and push to max-heap.
2. `findMedian()`:
   - If `len(max_heap) > len(min_heap)`, return the top of max-heap.
   - Else, return the average of the tops of both heaps.

## Complexity
- **Time Complexity:** addNum: O(log N), findMedian: O(1).
- **Space Complexity:** O(N).

## Code
```python
import heapq

class MedianFinder:
    def __init__(self):
        # max_heap stores the smaller half
        self.small = [] # Python min-heap, must negate values
        # min_heap stores the larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Push to small (max-heap)
        heapq.heappush(self.small, -num)
        
        # Step 2: Ensure small's values are <= large's values
        # Pop max from small and push to large
        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)
        
        # Step 3: Maintain size balance
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
```
