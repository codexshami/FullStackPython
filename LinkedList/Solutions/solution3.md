# Solution 3: Confluential Sorting

## Approach Explanation
We use a "dummy" node to handle the head of the new list easily. We iterate through both lists, comparing values and attaching the smaller node to our merged list.

## Step-by-Step Logic
1. Create a `dummy` node and a `curr` pointer initialized to it.
2. While `l1` and `l2` are both not None:
   - If `l1.val <= l2.val`:
     - `curr.next = l1`
     - `l1 = l1.next`
   - Else:
     - `curr.next = l2`
     - `l2 = l2.next`
   - Move `curr = curr.next`.
3. If one list is exhausted, attach the remaining part of the other list: `curr.next = l1 or l2`.
4. Return `dummy.next`.

## Complexity
- **Time Complexity:** O(N + M), where N and M are the lengths of the two lists.
- **Space Complexity:** O(1), as we only rearrange existing nodes.

## Code
```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
        
    # Attach remaining nodes
    curr.next = l1 if l1 else l2
    
    return dummy.next
```
