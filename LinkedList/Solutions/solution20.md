# Solution 20: Optimal Sequence Sorting

## Approach Explanation
We use Merge Sort. To handle linked lists without extra space, we recursively split the list into two halves using the fast and slow pointer technique, sort the halves, and then merge them.

## Step-by-Step Logic
1. Base case: If `head` is None or `head.next` is None, return `head`.
2. Find the middle node using `slow` and `fast` pointers.
3. Split the list: `left_half = head`, `right_half = slow.next`, `slow.next = None`.
4. Recursively sort both halves.
5. Merge the two sorted halves (reusing the logic from Problem 3).
6. Return the head of the merged list.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(log N) recursion depth.

## Code
```python
def sort_list(head):
    if not head or not head.next:
        return head
        
    # Split list into two halves
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    mid = slow.next
    slow.next = None # Break the list
    
    left = sort_list(head)
    right = sort_list(mid)
    
    # Merge sorted lists
    return merge(left, right)

def merge(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next
```
