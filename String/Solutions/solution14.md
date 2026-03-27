# Solution 14: Maximum Balanced Span (Longest Valid Parentheses)

## Approach Explanation
We can use a stack to store the indices of characters. We push the index of `(` and when we see `)`, we pop. The length is `current_index - stack[-1]`. We seed the stack with `-1` to handle the base starting case.

## Step-by-Step Logic
1. `stack = [-1]`, `max_len = 0`.
2. Iterate `i` from 0 to `len(s) - 1`:
   - If `s[i] == '('`: `stack.append(i)`.
   - Else (`s[i] == ')'`):
     - `stack.pop()`.
     - If `stack` is empty, this `)` is a breaker. Push current `i` as the new ground.
     - Else, current valid length is `i - stack[-1]`. Update `max_len`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
def longest_valid_parentheses(s):
    stack = [-1]
    max_len = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
                
    return max_len
```
