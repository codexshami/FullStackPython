# Solution 8: Positional Summation

## Approach Explanation
We simulate the manual addition process from school. We iterate through both lists concurrently, adding the values along with any `carry` from the previous position.

## Step-by-Step Logic
1. Initialize a `dummy` node and `curr = dummy`.
2. Initialize `carry = 0`.
3. While `l1`, `l2` or `carry` is present:
   - `val1 = l1.val` if `l1` else 0.
   - `val2 = l2.val` if `l2` else 0.
   - `total = val1 + val2 + carry`.
   - `carry = total // 10`.
   - `curr.next = ListNode(total % 10)`.
   - Advance `curr`, `l1`, and `l2`.
4. Return `dummy.next`.

## Complexity
- **Time Complexity:** O(max(N, M)), where N and M are the lengths of the two lists.
- **Space Complexity:** O(max(N, M)) for the new linked list.

## Code
```python
def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        # Calculate sum and carry
        total = v1 + v2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        
        # Advance pointers
        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        
    return dummy.next
```
