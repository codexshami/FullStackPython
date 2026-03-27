# Solution 20: Literal Operator Evaluation

## Approach Explanation
We use a stack to handle parentheses and sign changes. For each opening parenthesis `(`, we push the current result and the sign onto the stack and reset the result for the expression inside the parentheses.

## Step-by-Step Logic
1. Initialize `res = 0`, `num = 0`, `sign = 1`, and an empty `stack`.
2. Iterate through characters:
   - If digit: update `num`.
   - If `+` or `-`: update `res` with the completed `num * sign`, reset `num`, and set the new `sign`.
   - If `(`: push current `res` and `sign` to stack, reset both for the sub-expression.
   - If `)`: complete the sub-expression, pop the sign and multiply, then add the popped result.
3. Add the last number to `res`.
4. Return `res`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
def calculate(s):
    stack = []
    res = 0
    num = 0
    sign = 1
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            res += sign * num
            num = 0
            sign = 1
        elif char == '-':
            res += sign * num
            num = 0
            sign = -1
        elif char == '(':
            # Push the results calculated so far
            stack.append(res)
            stack.append(sign)
            # Reset values
            res = 0
            sign = 1
        elif char == ')':
            res += sign * num
            num = 0
            # Pop sign, then pop previous result
            res *= stack.pop()
            res += stack.pop()
            
    return res + sign * num
```
