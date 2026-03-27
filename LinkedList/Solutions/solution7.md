# Solution 7: Path Convergence

## Approach Explanation
We use two pointers, `pA` and `pB`, initialized to the heads of `listA` and `listB`. Both pointers traverse their respective lists. When a pointer reaches the end of its list, we redirect it to the head of the *other* list.

## Step-by-Step Logic
1. Initialize `pA = headA` and `pB = headB`.
2. While `pA != pB`:
   - `pA = pA.next` if `pA` is not None, else `pA = headB`.
   - `pB = pB.next` if `pB` is not None, else `pB = headA`.
3. If they intersect, they will meet at the intersection node after (at most) `m + n` steps.
4. If they don't intersect, they will both become `None` at the same time and exit the loop.
5. Return `pA`.

## Complexity
- **Time Complexity:** O(M + N), as each pointer travels at most both lists.
- **Space Complexity:** O(1), no extra storage.

## Code
```python
def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
        
    pA, pB = headA, headB
    
    while pA != pB:
        # Redirect pointer to the other list's head if it hits None
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
        
    return pA
```
