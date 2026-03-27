# Solution 9: Genetic Blueprint Duplication

## Approach Explanation
We use a three-step process to avoid extra space:
1. Create interleaved nodes: for each node `A`, create its copy `A'` and insert it as `A -> A' -> B`.
2. Connect random pointers: `A'.random = A.random.next` (if `A.random` exists).
3. Extract the copy: Separate the interleaved list into original and copy lists.

## Step-by-Step Logic
1. Iterate through the list and for each node, create a copy and insert it after the original node.
2. Iterate again and set `curr.next.random = curr.random.next` if `curr.random` is not None.
3. Iterate a third time to separate the lists: `curr.next` pointers are updated to restore the original list and build the copy.
4. Return the head of the copy list.

## Complexity
- **Time Complexity:** O(N), three passes.
- **Space Complexity:** O(1), ignoring the storage of the copy list itself.

## Code
```python
def copy_random_list(head):
    if not head:
        return None
        
    # Step 1: Interleave Copy nodes
    curr = head
    while curr:
        new_node = Node(curr.val, curr.next)
        curr.next = new_node
        curr = new_node.next
        
    # Step 2: Assign random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
        
    # Step 3: Separate the lists
    curr = head
    copy_head = head.next
    while curr:
        copy_node = curr.next
        curr.next = copy_node.next
        if copy_node.next:
            copy_node.next = copy_node.next.next
        curr = curr.next
        
    return copy_head
```
