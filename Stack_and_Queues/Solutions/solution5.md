# Solution 5: Keypress Correction

## Approach Explanation
We use a stack to simulate the typing process. For every character, we push it onto the stack. For every `#`, we pop if the stack is not empty.

## Step-by-Step Logic
1. Define a helper function `build(string)`:
   - Initialize an empty stack.
   - For each char in the string:
     - If char is `#`, pop from stack if not empty.
     - Else, push char.
   - Return the joined string/stack.
2. Compare `build(s)` and `build(t)`.

## Complexity
- **Time Complexity:** O(N + M), where N and M are lengths of `s` and `t`.
- **Space Complexity:** O(N + M).

## Code
```python
def backspace_compare(s, t):
    def build(string):
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return "".join(stack)
        
    return build(s) == build(t)
```
