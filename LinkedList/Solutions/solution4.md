# Solution 4: Targeted Extraction

## Approach Explanation
We use two pointers, `fast` and `slow`, with a gap of `n` nodes between them. When the `fast` pointer reaches the end, the `slow` pointer will be just before the node to be removed.

## Step-by-Step Logic
1. Create a `dummy` node pointing to `head` (to handle cases where the head itself is removed).
2. Initialize `fast` and `slow` pointers at the `dummy` node.
3. Move `fast` pointer `n + 1` steps forward.
4. Move both `fast` and `slow` pointers one step at a time until `fast` becomes None.
5. The `slow` pointer is now right before the node to be deleted. Change `slow.next = slow.next.next`.
6. Return `dummy.next`.

## Complexity
- **Time Complexity:** O(N), single pass through the list.
- **Space Complexity:** O(1), constant extra space.

## Code
```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    
    # Create the gap
    for _ in range(n + 1):
        fast = fast.next
        
    # Move until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next
        
    # Remove the node
    slow.next = slow.next.next
    
    return dummy.next
```
