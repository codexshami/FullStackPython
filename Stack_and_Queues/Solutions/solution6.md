# Solution 6: Nearest Superior Element

## Approach Explanation
We use a monotonic stack to precompute all next greater elements in `nums2`. We store these results in a hash map. Then, we simply query the map for each element in `nums1`.

## Step-by-Step Logic
1. Initialize an empty stack and a dictionary `mapping`.
2. Iterate through each `num` in `nums2`:
   - While stack is not empty and `num` > top of stack:
     - `temp = stack.pop()`
     - `mapping[temp] = num`
   - Push `num` to stack.
3. For values remaining in stack, set their `mapping` value to -1.
4. Build the result for `nums1` using the `mapping`.

## Complexity
- **Time Complexity:** O(N + M), where N, M are lengths of `nums1` and `nums2`. Each element in `nums2` is pushed and popped exactly once.
- **Space Complexity:** O(M) for map and stack.

## Code
```python
def next_greater_element(nums1, nums2):
    mapping = {}
    stack = []
    
    for num in nums2:
        while stack and num > stack[-1]:
            mapping[stack.pop()] = num
        stack.append(num)
        
    while stack:
        mapping[stack.pop()] = -1
        
    return [mapping[num] for num in nums1]
```
