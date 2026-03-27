# Solution 13: Cyclical Displacement

## Approach Explanation
We first find the total length of the list and make it a circular list by connecting the tail to the head. Then, we find the new tail at position `(length - k % length - 1)` and break the circle there.

## Step-by-Step Logic
1. Handle edge cases (empty list, k=0).
2. Calculate length `n` and find the `tail`.
3. Connect `tail.next = head` to form a circle.
4. Calculate new break point: `steps_to_new_tail = n - (k % n) - 1`.
5. Traverse `steps_to_new_tail` steps from `head` to find `new_tail`.
6. Set `new_head = new_tail.next`.
7. Break the link: `new_tail.next = None`.
8. Return `new_head`.

## Complexity
- **Time Complexity:** O(N), two passes (one for length, one for break point).
- **Space Complexity:** O(1).

## Code
```python
def rotate_list(head, k):
    if not head or k == 0:
        return head
        
    # Find length
    n = 1
    tail = head
    while tail.next:
        tail = tail.next
        n += 1
        
    k %= n
    if k == 0: return head
    
    # Form a circle
    tail.next = head
    
    # Find new tail
    steps = n - k - 1
    new_tail = head
    for _ in range(steps):
        new_tail = new_tail.next
        
    # Break circle
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head
```
