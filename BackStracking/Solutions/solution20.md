# Solution 20: The Expression Builder (Expression Add Operators)

## Approach Explanation
We try inserting `+`, `-`, or `*` between digits. We track the current value and the last operand (needed for multiplication precedence). We avoid numbers with leading zeros.

## Step-by-Step Logic
1. At each position, try all possible operand lengths (1 to remaining).
2. Skip numbers with leading zeros (except "0" itself).
3. For the first number, just set it as the value.
4. For subsequent numbers, try +, -, *.
5. For multiplication, undo the last addition/subtraction and apply `* current`.
6. If we reach the end and value == target, save the expression.

## Complexity
- **Time Complexity:** O(4^N).
- **Space Complexity:** O(N).

## Code
```python
def add_operators(num, target):
    result = []
    
    def backtrack(index, expression, value, last):
        if index == len(num):
            if value == target:
                result.append(expression)
            return
        
        for i in range(index, len(num)):
            # Skip numbers with leading zeros
            if i > index and num[index] == '0':
                break
            
            current = int(num[index:i + 1])
            
            if index == 0:
                backtrack(i + 1, str(current), current, current)
            else:
                backtrack(i + 1, expression + '+' + str(current),
                         value + current, current)
                backtrack(i + 1, expression + '-' + str(current),
                         value - current, -current)
                backtrack(i + 1, expression + '*' + str(current),
                         value - last + last * current, last * current)
    
    backtrack(0, '', 0, 0)
    return result
```
