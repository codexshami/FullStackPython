# Solution 8: Postfix Computation

## Approach Explanation
We use a stack to store operands. When we encounter an operator, we pop the top two operands, apply the operator, and push the result back onto the stack.

## Step-by-Step Logic
1. Initialize an empty stack.
2. Iterate through each token in the input:
   - If token is an operator:
     - Pop `b` (the second operand).
     - Pop `a` (the first operand).
     - Perform the operation `a operator b`.
     - Push the result back to stack. (For division, use `int(a / b)` to truncate towards zero).
   - Else (operand):
     - Push the integer value of the token.
3. Return the only element remaining in the stack.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
def eval_rpn(tokens):
    stack = []
    
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                # Truncate towards zero
                stack.append(int(a / b))
        else:
            stack.append(int(token))
            
    return stack[0]
```
