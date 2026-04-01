# Solution 6: The Bracket Generator (Generate Parentheses)

## Approach Explanation
We build valid parentheses strings character by character. At each step, we can add `(` if we haven't used all opening brackets, and `)` if the count of `)` is less than `(`.

## Step-by-Step Logic
1. Track counts of open and close parentheses used so far.
2. If both counts equal `n`, save the string.
3. If open count < n, add `(` and recurse.
4. If close count < open count, add `)` and recurse.

## Complexity
- **Time Complexity:** O(4^N / sqrt(N)) — the N-th Catalan number.
- **Space Complexity:** O(N).

## Code
```python
def generate_parenthesis(n):
    result = []
    
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result
```
