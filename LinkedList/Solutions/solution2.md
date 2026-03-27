# Solution 2: Circular Entrapment

## Approach Explanation
We use Floyd's Cycle-Finding Algorithm (Tortoise and Hare). We have two pointers moving at different speeds. If there is a cycle, the fast pointer will eventually catch up to the slow pointer.

## Step-by-Step Logic
1. Initialize `slow = head` and `fast = head`.
2. While `fast` and `fast.next` are not None:
   - Move `slow` by one step: `slow = slow.next`.
   - Move `fast` by two steps: `fast = fast.next.next`.
   - If `slow == fast`, return `True` (cycle detected).
3. If the loop ends, return `False`.

## Complexity
- **Time Complexity:** O(N), where N is the number of nodes.
- **Space Complexity:** O(1), no extra space.

## Code
```python
def has_cycle(head):
    if not head:
        return False
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
            
    return False
```
