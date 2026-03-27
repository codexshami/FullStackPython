# Solution 18: Arithmetic Expression Parser (Basic Calculator II)

## Approach Explanation
We use a stack to process the expression. We maintain the current number and the last operator seen. When we encounter a new operator (or the end of the string), we perform the "last operator" operation on the current number and push the result to the stack.

## Step-by-Step Logic
1. `num = 0`, `last_op = '+'`, `stack = []`.
2. Iterate through string `s`:
   - If char is digit, update `num`.
   - If char is operator or end of string:
     - If `last_op == '+'`: `stack.append(num)`.
     - If `last_op == '-'`: `stack.append(-num)`.
     - If `last_op == '*'`: `stack.append(stack.pop() * num)`.
     - If `last_op == '/'`: `stack.append(int(stack.pop() / num))`.
     - Update `last_op = char`, `num = 0`.
3. Return `sum(stack)`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
def calculate(s):
    if not s: return 0
    stack, num, sign = [], 0, "+"
    s += "+" # dummy to trigger last op
    for char in s:
        if char == " ": continue
        if char.isdigit():
            num = num * 10 + int(char)
        else:
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            elif sign == "/":
                top = stack.pop()
                stack.append(int(top / num))
            sign = char
            num = 0
    return sum(stack)
```
