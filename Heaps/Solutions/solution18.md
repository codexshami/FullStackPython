# Solution 18: Algebraic Reconstitution

## Approach Explanation
We work backward from the `target` array to the `[1, 1, ..., 1]` array. In each step, the largest element must have been the sum of the previous array's elements. We can calculate the previous value of that element using the current sum.

## Step-by-Step Logic
1. Calculate the total sum of `target`.
2. Push all elements into a Max-Heap.
3. While the top of the heap is > 1:
   - Pop the largest element `max_val`.
   - Calculate the sum of other elements: `rest = total_sum - max_val`.
   - If `rest == 1`, return True (shortcut for [1, max_val] case).
   - If `rest == 0` or `max_val <= rest`, return False.
   - Calculate the "previous" value: `prev_val = max_val % rest`.
   - If `prev_val == 0`, return False unless `rest == 1`.
   - Update `total_sum = total_sum - max_val + prev_val`.
   - Push `prev_val` back to the heap.
4. Return True.

## Complexity
- **Time Complexity:** O(N log(max(target))), using modulo for optimization.
- **Space Complexity:** O(N).

## Code
```python
import heapq

def is_possible(target):
    if len(target) == 1:
        return target[0] == 1
        
    s = sum(target)
    h = [-t for t in target]
    heapq.heapify(h)
    
    while -h[0] > 1:
        mx = -heapq.heappop(h)
        rest = s - mx
        
        # If rest is 1, we can always reach 1 by repeatedly subtracting
        if rest == 1:
            return True
            
        if rest == 0 or mx <= rest:
            return False
            
        prev = mx % rest
        if prev == 0: # Case where prev should be rest
            return False
            
        s = s - mx + prev
        heapq.heappush(h, -prev)
        
    return True
```
