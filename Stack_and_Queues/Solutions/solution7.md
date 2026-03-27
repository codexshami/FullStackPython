# Solution 7: Seasonal Transition

## Approach Explanation
This is a variation of the Next Greater Element problem. We use a monotonic decreasing stack to store INDICES of the temperatures. When we find a warmer day, we calculate the difference between the current index and the index at the top of the stack.

## Step-by-Step Logic
1. Initialize `ans` array with zeros.
2. Initialize an empty stack `stack` to store indices.
3. Iterate through `temperatures` with index `i`:
   - While stack is not empty and `temperatures[i]` > `temperatures[stack[-1]]`:
     - `prev_index = stack.pop()`
     - `ans[prev_index] = i - prev_index`
   - Push current index `i` to stack.
4. Return `ans`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
def daily_temperatures(temperatures):
    n = len(temperatures)
    ans = [0] * n
    stack = [] # Stores indices
    
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx = stack.pop()
            ans[idx] = i - idx
        stack.append(i)
        
    return ans
```
