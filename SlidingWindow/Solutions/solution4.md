# Solution 4: Peak Element Tracking (Sliding Window Maximum)

## Approach Explanation
We use a Monotonic Deque to store indices of potential maxima. The deque will maintain indices in decreasing order of their corresponding values in `nums`.

## Step-by-Step Logic
1. Initialize `q = deque()`, `output = []`.
2. Iterate `r` from 0 to `len(nums)-1`:
   - While `q` is not empty and `nums[q[-1]] < nums[r]`, `q.pop()`.
   - `q.append(r)`.
   - If `l > q[0]`, `q.popleft()` (out of window).
   - If `r + 1 >= k`, `output.append(nums[q[0]])`, increment `l`.
3. Return `output`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(K).

## Code
```python
from collections import deque

def max_sliding_window(nums, k):
    output = []
    q = deque() # indices
    l = r = 0
    
    while r < len(nums):
        # pop smaller values from q
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)
        
        # remove left val from window
        if l > q[0]:
            q.popleft()
            
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
        
    return output
```
