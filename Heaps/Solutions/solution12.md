# Solution 12: Stream Integration

## Approach Explanation
We use a Min-Heap of size `k` to keep track of the smallest current element across all `k` lists. In each step, we pop the smallest element, add it to our merged list, and then push the next element from the same list into the heap.

## Step-by-Step Logic
1. Initialize a Min-Heap.
2. Push the first node of each list into the heap as `(node.val, i, node)`. (Include list index `i` to avoid comparison errors if values are equal).
3. Create a `dummy` node as the head of the result.
4. While heap is not empty:
   - Pop `(val, i, node)`.
   - Append `node` to the result list.
   - If `node.next` exists, push `(node.next.val, i, node.next)` into the heap.
5. Return `dummy.next`.

## Complexity
- **Time Complexity:** O(N log K), where N is the total number of nodes and K is the number of lists.
- **Space Complexity:** O(K) for the heap.

## Code
```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    h = []
    # Initialize heap with first node of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(h, (lst.val, i, lst))
            
    dummy = ListNode(0)
    curr = dummy
    
    while h:
        val, i, node = heapq.heappop(h)
        curr.next = ListNode(val)
        curr = curr.next
        
        if node.next:
            heapq.heappush(h, (node.next.val, i, node.next))
            
    return dummy.next
```
