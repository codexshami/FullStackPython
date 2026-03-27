# Solution 8: Non-Adjacent Sequence

## Approach Explanation
Similar to the Task Scheduler, we use a Max-Heap to always pick the most frequent character. We keep track of the previously used character to avoid placing it again immediately.

## Step-by-Step Logic
1. Count frequencies.
2. Store `(-freq, char)` in a Max-Heap.
3. Initialize `prev = None`.
4. While heap is not empty:
   - Pop character `c`.
   - Append `c` to result.
   - If `prev` exists, push it back to the heap.
   - Decrement frequency of `c`. If still > 0, set `prev = (new_freq, c)`. Else `prev = None`.
5. If the resulting string length != input string length, return "".

## Complexity
- **Time Complexity:** O(N log K), where K is the alphabet size.
- **Space Complexity:** O(K).

## Code
```python
import heapq
from collections import Counter

def reorganize_string(s):
    counts = Counter(s)
    max_heap = [(-f, c) for c, f in counts.items()]
    heapq.heapify(max_heap)
    
    prev = None
    res = []
    
    while max_heap or prev:
        # If heap is empty but prev exists, it's impossible
        if not max_heap and prev:
            return ""
            
        freq, char = heapq.heappop(max_heap)
        res.append(char)
        
        # After using prev, it's safe to put it back
        if prev:
            heapq.heappush(max_heap, prev)
            prev = None
            
        # Update current char and set as prev
        if freq + 1 < 0:
            prev = (freq + 1, char)
            
    return "".join(res)
```
