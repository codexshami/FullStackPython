# Solution 1: Priority Selection

## Approach Explanation
We use a Min-Heap of size `k`. We iterate through the array and push elements onto the heap. If the heap size exceeds `k`, we pop the smallest element. After processing all elements, the top of the Min-Heap will be the `kth` largest element.

## Step-by-Step Logic
1. Initialize an empty min-heap.
2. For each number in `nums`:
   - Push it to the heap.
   - If `len(heap) > k`, pop the smallest element.
3. Return the top of the heap.

## Complexity
- **Time Complexity:** O(N log K).
- **Space Complexity:** O(K).

## Code
```python
import heapq

def find_kth_largest(nums, k):
    # Min-heap to store the k largest elements
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
            
    return heap[0]
```
