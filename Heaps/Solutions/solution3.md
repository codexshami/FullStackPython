# Solution 3: Weighted Rearrangement

## Approach Explanation
We count frequencies and then use a Max-Heap to extract characters in decreasing order of frequency.

## Step-by-Step Logic
1. Count frequencies.
2. Use a Max-Heap (Python's `heapq` with negative frequencies) to store `(-freq, char)`.
3. While the heap is not empty:
   - Pop the character with the highest frequency.
   - Append it `freq` times to the result string.
4. Return the string.

## Complexity
- **Time Complexity:** O(N log U), where U is the number of unique characters.
- **Space Complexity:** O(N).

## Code
```python
import heapq
from collections import Counter

def frequency_sort(s):
    counts = Counter(s)
    # Use max-heap (negative values for heapq)
    max_heap = [(-freq, char) for char, freq in counts.items()]
    heapq.heapify(max_heap)
    
    res = []
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        res.append(char * (-freq))
        
    return "".join(res)
```
