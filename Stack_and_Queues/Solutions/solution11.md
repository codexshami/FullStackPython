# Solution 11: Pattern Expander

## Approach Explanation
We use two stacks: one to store the multipliers (numbers) and another to store the previous strings. When we encounter `[`, we push the current string and current number onto their respective stacks. When we encounter `]`, we pop and reconstruct.

## Step-by-Step Logic
1. Initialize `curr_str = ""` and `curr_num = 0`.
2. Iterate through characters:
   - If digit: update `curr_num`.
   - If `[`: push `curr_str` and `curr_num` to stacks, reset both.
   - If `]`: pop `num` and `prev_str`, then `curr_str = prev_str + num * curr_str`.
   - Else (char): add to `curr_str`.
3. Return `curr_str`.

## Complexity
- **Time Complexity:** O(N), where N is the length of the final decoded string.
- **Space Complexity:** O(N).

## Code
```python
def decode_string(s):
    stack = []
    curr_str = ""
    curr_num = 0
    
    for char in s:
        if char == '[':
            stack.append((curr_str, curr_num))
            curr_str = ""
            curr_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + num * curr_str
        elif char.isdigit():
            curr_num = curr_num * 10 + int(char)
        else:
            curr_str += char
            
    return curr_str
```
