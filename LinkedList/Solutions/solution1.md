# Solution 1: Eternal Reversal

## Approach Explanation
We use an iterative approach with three pointers: `prev`, `curr`, and `next_node`. As we traverse the list, we change the `next` pointer of the current node to point to the previous node.

## Step-by-Step Logic
1. Initialize `prev = None` and `curr = head`.
2. While `curr` is not None:
   - Save the next node: `next_node = curr.next`.
   - Reverse the link: `curr.next = prev`.
   - Move `prev` to `curr`.
   - Move `curr` to `next_node`.
3. Return `prev` as the new head.

## Complexity
- **Time Complexity:** O(N), where N is the number of nodes.
- **Space Complexity:** O(1), in-place reversal.

## Code
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    return prev
```
