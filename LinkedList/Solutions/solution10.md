# Solution 10: Cycle Entrance Node

## Approach Explanation
This is Phase 2 of Floyd's Cycle-Finding Algorithm. Once a meeting point is found inside the cycle, we reset one pointer to the head and move both at speed 1. They will meet at the start of the cycle.

## Step-by-Step Logic
1. Use `slow` and `fast` pointers to detect a cycle.
2. If no cycle is found, return `None`.
3. If a cycle is found, keep `fast` at the meeting point and move `slow` to `head`.
4. Move both `slow` and `fast` one step at a time.
5. The point where they meet is the entrance to the cycle.
6. Return that node.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def detect_cycle_entry(head):
    slow = fast = head
    
    # Phase 1: Detect presence of cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
        
    # Phase 2: Find entrance
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    return slow
```
