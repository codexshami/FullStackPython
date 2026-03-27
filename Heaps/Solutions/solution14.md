# Solution 14: Dynamic Centrality

## Approach Explanation
We use two heaps (similar to the Median from Data Stream problem) but with an added challenge: we need to "remove" elements that are no longer in the sliding window. Since standard heaps don't support efficient removal, we use "lazy removal" by tracking the counts of elements to be removed in a hash map.

## Step-by-Step Logic
1. Maintain `small` (Max-Heap) and `large` (Min-Heap).
2. For each window:
   - Push new element (with balancing).
   - Get median.
   - Mark the element leaving the window for removal.
   - "Clean up" the tops of the heaps if they point to elements marked for removal.
   - Balance the sizes of the heaps.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(N).

## Code
```python
import heapq
from collections import defaultdict

class SlidingWindowMedian:
    def __init__(self, k):
        self.k = k
        self.small = [] # max_heap
        self.large = [] # min_heap
        self.num_to_remove = defaultdict(int)
        self.small_size = 0
        self.large_size = 0

    def _clean_heap(self, heap, is_small):
        while heap:
            val = -heap[0] if is_small else heap[0]
            if self.num_to_remove[val] > 0:
                self.num_to_remove[val] -= 1
                heapq.heappop(heap)
            else:
                break

    def get_medians(self, nums, k):
        res = []
        for i in range(k):
            self._add(nums[i])
        res.append(self._median())

        for i in range(k, len(nums)):
            self._remove(nums[i-k])
            self._add(nums[i])
            res.append(self._median())
        return res

    def _add(self, num):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
        self._balance()

    def _remove(self, num):
        self.num_to_remove[num] += 1
        if num <= -self.small[0]:
            self.small_size -= 1
        else:
            self.large_size -= 1
        self._clean_heap(self.small, True)
        self._clean_heap(self.large, False)
        self._balance()

    def _balance(self):
        if self.small_size > self.large_size + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
            self.small_size -= 1
            self.large_size += 1
            self._clean_heap(self.small, True)
        elif self.large_size > self.small_size:
            heapq.heappush(self.small, -heapq.heappop(self.large))
            self.large_size -= 1
            self.small_size += 1
            self._clean_heap(self.large, False)

    def _median(self):
        if self.k % 2 == 1:
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
```
