# Solution 6: Perpetual Ranker

## Approach Explanation
We maintain a Min-Heap of size `k`. The top of the heap is always the `kth` largest element in the stream.

## Step-by-Step Logic
1. `__init__`: Heapify the given `nums` and pop elements until the size is `k`.
2. `add(val)`: 
   - Push `val` to heap.
   - If size > k, pop.
   - Return `heap[0]`.

## Complexity
- **Time Complexity:** Init: O(N log N), Add: O(log K).
- **Space Complexity:** O(K).

## Code
```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
```
