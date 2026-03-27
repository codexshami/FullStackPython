# Solution 2: Dominant Occurrences

## Approach Explanation
1. Count the frequency of each element using a hash map.
2. Use a min-heap to keep track of the `k` elements with the highest frequencies. The heap stores tuples of `(frequency, element)`.

## Step-by-Step Logic
1. Use `collections.Counter` to get frequencies.
2. Initialize a min-heap.
3. For each `(num, freq)` pair in the counter:
   - Push `(freq, num)` to the heap.
   - If heap size > k, pop the smallest frequency element.
4. Extract the `num` from each tuple in the heap and return as a list.

## Complexity
- **Time Complexity:** O(N log K), where N is the number of unique elements.
- **Space Complexity:** O(N) for the count map.

## Code
```python
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    counts = Counter(nums)
    # Min-heap of size k to keep track of top frequencies
    heap = []
    
    for val, freq in counts.items():
        heapq.heappush(heap, (freq, val))
        if len(heap) > k:
            heapq.heappop(heap)
            
    return [item[1] for item in heap]
```
