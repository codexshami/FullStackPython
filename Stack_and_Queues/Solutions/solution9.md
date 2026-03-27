# Solution 9: Absolute Path Normalizer

## Approach Explanation
We split the path by `/` and use a stack to process each component. 

## Step-by-Step Logic
1. Split the string by `/`.
2. Iterate through components:
   - If component is `..`: pop from stack if stack is not empty (go up).
   - If component is `.` or empty: do nothing.
   - Else: push the component onto the stack.
3. Join the stack elements with `/` and prepend `/`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
def simplify_path(path):
    stack = []
    components = path.split("/")
    
    for c in components:
        if c == "..":
            if stack:
                stack.pop()
        elif c == "." or not c:
            continue
        else:
            stack.append(c)
            
    return "/" + "/".join(stack)
```
