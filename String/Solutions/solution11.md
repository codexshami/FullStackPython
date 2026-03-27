# Solution 11: Canonical Path Canonicalizer (Simplify Path)

## Approach Explanation
We split the path by `/` and use a stack to process the components. `..` pops from the stack, while `.` and empty strings are ignored.

## Step-by-Step Logic
1. Split `path` using `/`.
2. Initialize `stack = []`.
3. For each `part` in components:
   - If `part == '..'`, `pop()` from stack if not empty.
   - Else if `part` is not `.` and not empty, `push(part)`.
4. Return `'/' + '/'.join(stack)`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
def simplify_path(path):
    stack = []
    parts = path.split("/")
    
    for p in parts:
        if p == "..":
            if stack:
                stack.pop()
        elif p == "." or not p:
            continue
        else:
            stack.append(p)
            
    return "/" + "/".join(stack)
```
