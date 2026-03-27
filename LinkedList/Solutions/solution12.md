# Solution 12: Bilateral Exchange

## Approach Explanation
We use a `dummy` node to simplify the head swapping logic. For each pair of nodes, we adjust their pointers to swap them and link them with the previous and next nodes.

## Step-by-Step Logic
1. Start with `dummy.next = head`.
2. Use a pointer `prev` initialized to `dummy`.
3. While `prev.next` and `prev.next.next` are not None:
   - Identify `first = prev.next` and `second = prev.next.next`.
   - Perform the swap:
     - `prev.next = second`
     - `first.next = second.next`
     - `second.next = first`
   - Move `prev = first`.
4. Return `dummy.next`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def swap_pairs(head):
    dummy = ListNode(0, head)
    prev = dummy
    
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        
        # Swapping
        prev.next = second
        first.next = second.next
        second.next = first
        
        # Advance
        prev = first
        
    return dummy.next
```
