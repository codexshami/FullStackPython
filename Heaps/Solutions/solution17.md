# Solution 17: Equidistant Rearrangement

## Approach Explanation
This is a more general version of the "Reorganize String" problem (where `k=2`). We use a Max-Heap to pick the most frequent characters and a queue to enforce the distance `k`.

## Step-by-Step Logic
1. Count character frequencies.
2. Put all characters with frequency > 0 into a Max-Heap.
3. Use a queue `wait_queue` to store characters that are on cooldown.
4. While the Max-Heap is not empty:
   - Pop character `c`.
   - Append `c` to result.
   - Decrement frequency. Push `(freq, c)` to `wait_queue`.
   - If `len(wait_queue) >= k`:
     - Pop from `wait_queue`. If frequency > 0, push back to Max-Heap.
5. If result length != string length, return "".

## Complexity
- **Time Complexity:** O(N log A), where A is the alphabet size.
- **Space Complexity:** O(A).

## Code
```python
import heapq
from collections import Counter, deque

def rearrange_string(s, k):
    if k <= 1: return s
    
    counts = Counter(s)
    max_heap = [(-f, c) for c, f in counts.items()]
    heapq.heapify(max_heap)
    
    queue = deque()
    res = []
    
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        res.append(char)
        
        # Add to wait queue
        queue.append((freq + 1, char))
        
        # If queue is full, the wait is over for the front element
        if len(queue) == k:
            f, c = queue.popleft()
            if f < 0:
                heapq.heappush(max_heap, (f, c))
                
    return "".join(res) if len(res) == len(s) else ""
```
