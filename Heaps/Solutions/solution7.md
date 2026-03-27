# Solution 7: Strategic Scheduling

## Approach Explanation
We use a Max-Heap to always pick the task with the highest remaining frequency. We also use a queue to handle the cooldown period.

## Step-by-Step Logic
1. Count task frequencies.
2. Store frequencies in a Max-Heap.
3. Use a queue to store tasks that are in cooldown: `(new_freq, availability_time)`.
4. While heap or queue is not empty:
   - Increment `time`.
   - If heap is not empty, pop the most frequent task and decrement its frequency. If new frequency > 0, push to queue with `time + n`.
   - If queue front's `availability_time == time`, move it back to the heap.

## Complexity
- **Time Complexity:** O(T), where T is the total time (total tasks + idle time).
- **Space Complexity:** O(1), at most 26 unique tasks.

## Code
```python
import heapq
from collections import Counter, deque

def least_interval(tasks, n):
    counts = Counter(tasks)
    max_heap = [-cnt for cnt in counts.values()]
    heapq.heapify(max_heap)
    
    time = 0
    q = deque() # (neg_cnt, availability_time)
    
    while max_heap or q:
        time += 1
        
        if max_heap:
            cnt = 1 + heapq.heappop(max_heap) # pop, decrement (neg values)
            if cnt != 0:
                q.append((cnt, time + n))
        
        if q and q[0][1] == time:
            heapq.heappush(max_heap, q.popleft()[0])
            
    return time
```
