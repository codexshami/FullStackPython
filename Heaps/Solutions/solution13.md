# Solution 13: Minimal Domain Covering

## Approach Explanation
We maintain a window of size `k` containing one element from each list using a Min-Heap. We also track the maximum value currently in the heap. The current range is `[heap[0].val, current_max]`.

## Step-by-Step Logic
1. For each list, maintain an index (initially 0).
2. Store the first element of each list in a Min-Heap: `(value, list_index, index_in_list)`.
3. Track the `max_val` across all elements in the heap.
4. While the heap size is `k`:
   - Calculate current range `[heap_min, max_val]`. Update if smaller.
   - Pop the smallest element.
   - If that list has more elements, push the next one and update `max_val`.
   - If one list is exhausted, we cannot form a range with all lists anymore.

## Complexity
- **Time Complexity:** O(N log K).
- **Space Complexity:** O(K).

## Code
```python
import heapq

def smallest_range(nums):
    # Min-heap to find the minimum of the k pointers
    h = []
    max_val = -float('inf')
    
    # Init with first element of every list
    for i in range(len(nums)):
        heapq.heappush(h, (nums[i][0], i, 0))
        max_val = max(max_val, nums[i][0])
        
    ans = [-10**5, 10**5]
    
    while True:
        min_val, list_idx, val_idx = heapq.heappop(h)
        
        # Update range if current is smaller
        if max_val - min_val < ans[1] - ans[0]:
            ans = [min_val, max_val]
            
        # Move forward in the list we just popped from
        if val_idx + 1 < len(nums[list_idx]):
            nxt_val = nums[list_idx][val_idx + 1]
            heapq.heappush(h, (nxt_val, list_idx, val_idx + 1))
            max_val = max(max_val, nxt_val)
        else:
            # Cannot form any more ranges including all lists
            break
            
    return ans
```
