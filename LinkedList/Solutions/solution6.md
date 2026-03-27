# Solution 6: Mirror Symmetry

## Approach Explanation
We can solve this in O(N) time and O(1) space. The idea is to find the middle of the list, reverse the second half, and then compare the first half with the reversed second half.

## Step-by-Step Logic
1. Find the middle of the linked list using fast and slow pointers.
2. Reverse the second half of the list starting from the middle.
3. Compare the elements of the first half and the reversed second half one by one.
4. (Optional but good practice) Restore the original list by reversing the second half back.
5. Return whether all elements matched.

## Complexity
- **Time Complexity:** O(N), three passes (find middle, reverse, compare).
- **Space Complexity:** O(1), in-place reversal.

## Code
```python
def is_palindrome(head):
    if not head or not head.next:
        return True
    
    # Step 1: Find the middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half
    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    # Step 3: Compare halves
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
        
    return True
```
