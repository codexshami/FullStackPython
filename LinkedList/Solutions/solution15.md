# Solution 15: Odd-Even Interleaving

## Approach Explanation
We maintain two pointers, `odd` and `even`, to build the two lists simultaneously. The `even_head` is stored separately to link the end of the odd list to the start of the even list.

## Step-by-Step Logic
1. If `head` is None, return None.
2. Initialize `odd = head`, `even = head.next`, and `even_head = even`.
3. While `even` and `even.next` are not None:
   - `odd.next = even.next`
   - `odd = odd.next`
   - `even.next = odd.next`
   - `even = even.next`
4. Link: `odd.next = even_head`.
5. Return `head`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def odd_even_list(head):
    if not head: return None
    
    odd = head
    even = head.next
    even_head = even
    
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
        
    odd.next = even_head
    return head
```
