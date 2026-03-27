# Solution 18: Crest Tracking

## Approach Explanation
We use a Monotonic Deque (Double-ended Queue) to store the indices of the elements in the window. We want the deque to store indices such that the corresponding values are in decreasing order. The front of the deque will always have the index of the maximum element.

## Step-by-Step Logic
1. Initialize an empty `deque` and `ans` list.
2. Iterate through `nums` with index `i`:
   - Remove indices from the back of the `deque` that point to values smaller than `nums[i]`.
   - Add `i` to the back.
   - If the index at the front of the `deque` is outside the current window (`i - k`), remove it from the front.
   - If the window size is reached (`i >= k - 1`), append `nums[deque[0]]` to `ans`.
3. Return `ans`.

## Complexity
- **Time Complexity:** O(N), every element is added and removed from the deque at most once.
- **Space Complexity:** O(k) for the deque.

## Code
```python
from collections import deque

def max_sliding_window(nums, k):
    q = deque() # Stores indices
    res = []
    
    for i, n in enumerate(nums):
        # Remove smaller elements from the back
        while q and nums[q[-1]] <= n:
            q.pop()
        q.append(i)
        
        # Remove index if it's out of window
        if q[0] == i - k:
            q.popleft()
            
        # Add to result if window is full
        if i >= k - 1:
            res.append(nums[q[0]])
            
    return res
```
