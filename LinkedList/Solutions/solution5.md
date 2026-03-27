# Solution 5: Midpoint Equilibrium

## Approach Explanation
We use the Tortoise and Hare approach. Move `slow` by one step and `fast` by two steps. When `fast` reaches the end, `slow` will be at the middle.

## Step-by-Step Logic
1. Initialize `slow = head` and `fast = head`.
2. While `fast` and `fast.next` are not None:
   - `slow = slow.next`
   - `fast = fast.next.next`
3. Return `slow`.

## Complexity
- **Time Complexity:** O(N), single pass.
- **Space Complexity:** O(1), no extra space.

## Code
```python
def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```
