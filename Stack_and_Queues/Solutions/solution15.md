# Solution 15: Sequence Verification

## Approach Explanation
We simulate the process using a real stack. For each element in `pushed`, we push it onto the stack and then immediately check if the top of the stack matches the next element in `popped`. If it matches, we pop and repeat.

## Step-by-Step Logic
1. Initialize an empty `stack`.
2. Initialize `i = 0` (index for `popped`).
3. For each `x` in `pushed`:
   - Push `x` to `stack`.
   - While `stack` is not empty and `stack[-1] == popped[i]`:
     - Pop from `stack`.
     - Increment `i`.
4. After pushing all elements, the stack should be empty if the sequence was valid.

## Complexity
- **Time Complexity:** O(N), where N is the number of elements.
- **Space Complexity:** O(N).

## Code
```python
def validate_stack_sequences(pushed, popped):
    stack = []
    i = 0
    for x in pushed:
        stack.append(x)
        while stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1
            
    return not stack
```
