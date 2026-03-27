# Solution 4: Tracking the Intruder

## Approach Explanation
We treat the array as a linked list where `nums[i]` points to the index `nums[i]`. Since there's a duplicate, there must be a cycle in this linked list. We can use Floyd's Cycle-Finding Algorithm (Tortoise and Hare).

## Step-by-Step Logic
1. Initialize two pointers, `slow` and `fast`, both at `nums[0]`.
2. Move `slow` one step (`slow = nums[slow]`) and `fast` two steps (`fast = nums[nums[fast]]`) until they meet.
3. Once they meet, move `slow` back to `nums[0]`.
4. Move both `slow` and `fast` one step at a time. The point where they meet again is the start of the cycle, which corresponds to the duplicate number.

## Complexity
- **Time Complexity:** O(N), as we traverse the "list" a small number of times.
- **Space Complexity:** O(1), no extra space besides pointers.

## Code
```python
def find_duplicate(nums):
    # Phase 1: Finding the intersection point in the cycle
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
            
    # Phase 2: Finding the entrance to the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    return slow
```
