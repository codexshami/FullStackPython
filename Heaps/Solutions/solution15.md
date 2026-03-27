# Solution 15: Venture Capital (IPO)

## Approach Explanation
We use a Min-Heap to store all projects sorted by their capital requirement. We also use a Max-Heap to store the profits of projects that we can afford with our current capital.

## Step-by-Step Logic
1. Create a list of pairs `(capital, profit)` and sort it by capital.
2. Maintain a Max-Heap for available profits.
3. For `k` iterations:
   - Add all projects whose capital requirement is <= current capital `w` into the Max-Heap.
   - If the Max-Heap is empty, we can't do any more projects. Break.
   - Pop the largest profit from the Max-Heap and add it to `w`.
4. Return `w`.

## Complexity
- **Time Complexity:** O(N log N + K log N).
- **Space Complexity:** O(N).

## Code
```python
import heapq

def find_max_capital(k, w, profits, capital):
    # Min-heap for capital requirements
    n = len(profits)
    projects = sorted(zip(capital, profits))
    max_profit_heap = []
    
    i = 0
    for _ in range(k):
        # Move all projects we can afford into max_profit_heap
        while i < n and projects[i][0] <= w:
            heapq.heappush(max_profit_heap, -projects[i][1])
            i += 1
            
        if not max_profit_heap:
            break
            
        # Select the project with the highest profit
        w += -heapq.heappop(max_profit_heap)
        
    return w
```
