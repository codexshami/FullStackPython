# Solution 17: Fractal Reversal

## Approach Explanation
We process the list in chunks of size `k`. First, we check if there are at least `k` nodes. If yes, we reverse them and recursively call the function for the remaining part.

## Step-by-Step Logic
1. Count if there are `k` nodes available. If not, return `head`.
2. Reverse the first `k` nodes manually (similar to standard reversal).
3. After reversing `k` nodes, the original `head` is now the `tail` of this group.
4. Set `head.next = reverse_k_group(next_head, k)` where `next_head` is the start of the next group.
5. Return the new head of this reversed group.

## Complexity
- **Time Complexity:** O(N), each node is visited twice (once for counting, once for reversing).
- **Space Complexity:** O(N/k) recursion stack space.

## Code
```python
def reverse_k_group(head, k):
    # Check if we have k nodes
    curr = head
    for _ in range(k):
        if not curr: return head
        curr = curr.next
        
    # Reverse k nodes
    prev = None
    curr = head
    for _ in range(k):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    # Recursively handle the next group
    head.next = reverse_k_group(curr, k)
    
    return prev
```
