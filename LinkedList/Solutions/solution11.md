# Solution 11: Dimensional Accordion

## Approach Explanation
We can solve this iteratively using a stack. Whenever we encounter a node with a child, we push its `next` node onto the stack and set the `child` as the new `next`.

## Step-by-Step Logic
1. Start from the `head` and traverse the list.
2. For each node `curr`:
   - If `curr.child` exists:
     - If `curr.next` exists, push `curr.next` onto a `stack`.
     - Set `curr.next = curr.child`.
     - `curr.next.prev = curr`.
     - `curr.child = None`.
   - If `curr.next` is None and `stack` is not empty:
     - Pop `node` from `stack`.
     - `curr.next = node`.
     - `node.prev = curr`.
3. Continue until the list and stack are exhausted.

## Complexity
- **Time Complexity:** O(N), where N is the total number of nodes in the multilevel structure.
- **Space Complexity:** O(K), where K is the depth of levels (stack size).

## Code
```python
def flatten(head):
    if not head:
        return head
    
    curr = head
    stack = []
    
    while curr:
        if curr.child:
            if curr.next:
                stack.append(curr.next)
            curr.next = curr.child
            curr.next.prev = curr
            curr.child = None
        
        if not curr.next and stack:
            next_node = stack.pop()
            curr.next = next_node
            next_node.prev = curr
            
        curr = curr.next
        
    return head
```
