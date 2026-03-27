# Solution 16: Multi-way Merging

## Approach Explanation
We use a Min-Heap to efficiently find the smallest node among the heads of all `k` lists. We extract the smallest node, attach it to our result list, and then push the next node from the same list into the heap.

## Step-by-Step Logic
1. Initialize a `dummy` node and `curr = dummy`.
2. Initialize a Min-Heap `heap`.
3. Push the `head` of each non-empty list into the heap along with its index (to handle same-value nodes).
4. While the heap is not empty:
   - Pop the smallest `node` from the heap.
   - `curr.next = node`.
   - `curr = curr.next`.
   - If `node.next` exists, push `node.next` into the heap.
5. Return `dummy.next`.

## Complexity
- **Time Complexity:** O(N log k), where N is the total number of nodes and k is the number of lists.
- **Space Complexity:** O(k), storage in the heap.

## Code
```python
import heapq

def merge_k_lists(lists):
    dummy = ListNode(0)
    curr = dummy
    heap = []
    
    # Initialize heap with heads of all lists
    for i in range(len(lists)):
        if lists[i]:
            # Store (value, list_index, node)
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
            
    while heap:
        val, idx, node = heapq.heappop(heap)
        
        curr.next = node
        curr = curr.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))
            
    return dummy.next
```
