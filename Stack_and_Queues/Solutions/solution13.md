# Solution 13: Numerical Pruning

## Approach Explanation
We use a monotonic increasing stack to store the digits. Whenever we see a digit that is smaller than the top of the stack, we pop the stack and decrement `k`. This ensures that larger digits at higher positional values are removed first.

## Step-by-Step Logic
1. Initialize an empty stack.
2. Iterate through each digit in `num`:
   - While `k > 0`, stack is not empty, and current digit < stack tip:
     - Pop stack and decrement `k`.
   - Push current digit onto stack.
3. If `k > 0` after the loop, remove the remaining `k` digits from the end of the stack.
4. Join the stack and strip leading zeros.
5. If the resulting string is empty, return "0".

## Complexity
- **Time Complexity:** O(N), where N is the length of the number.
- **Space Complexity:** O(N).

## Code
```python
def remove_k_digits(num, k):
    stack = []
    
    for digit in num:
        while k > 0 and stack and digit < stack[-1]:
            stack.pop()
            k -= 1
        stack.append(digit)
        
    # Remove remaining k from the end if necessary
    if k > 0:
        stack = stack[:-k]
        
    # Remove leading zeros and handle empty case
    result = "".join(stack).lstrip("0")
    return result if result else "0"
```
