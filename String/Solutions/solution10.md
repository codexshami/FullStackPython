# Solution 10: Recursive Expansion (Decode String)

## Approach Explanation
We use a stack to keep track of previous strings and repetition multipliers. When we see an opening bracket, we push the current context. When we see a closing bracket, we pop and reconstruct.

## Step-by-Step Logic
1. `stack = []`, `curr_str = ""`, `curr_num = 0`.
2. For each character `c` in `s`:
   - If `c` is digit: `curr_num = curr_num * 10 + int(c)`.
   - If `c == '['`:
     - Push `(curr_str, curr_num)` to stack.
     - Reset `curr_str = ""`, `curr_num = 0`.
   - If `c == ']'`:
     - `prev_str, num = stack.pop()`.
     - `curr_str = prev_str + num * curr_str`.
   - Else: `curr_str += c`.
3. Return `curr_str`.

## Complexity
- **Time Complexity:** O(total_length_of_output_string).
- **Space Complexity:** O(N) for the stack.

## Code
```python
def decode_string(s):
    stack = []
    curr_num = 0
    curr_str = ""
    
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
