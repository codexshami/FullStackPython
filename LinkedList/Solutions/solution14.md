# Solution 14: Bifurcated Streams

## Approach Explanation
We maintain two separate linked lists (using dummy heads): one for nodes less than `x` and another for nodes greater than or equal to `x`. After traversing the main list, we connect the end of the "less than" list to the head of the "greater than" list.

## Step-by-Step Logic
1. Initialize `dummy1` and `dummy2` for the two partitions.
2. Maintain `p1` and `p2` pointers for the ends of these lists.
3. Traverse the original list:
   - If `node.val < x`: `p1.next = node`, `p1 = p1.next`.
   - Else: `p2.next = node`, `p2 = p2.next`.
4. `p2.next = None` to avoid cycles.
5. Connect: `p1.next = dummy2.next`.
6. Return `dummy1.next`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1), as we only change pointers.

## Code
```python
def partition(head, x):
    less_head = ListNode(0)
    greater_head = ListNode(0)
    
    p1, p2 = less_head, greater_head
    curr = head
    
    while curr:
        if curr.val < x:
            p1.next = curr
            p1 = p1.next
        else:
            p2.next = curr
            p2 = p2.next
        curr = curr.next
        
    p2.next = None
    p1.next = greater_head.next
    
    return less_head.next
```
