# Solution 15: Nondeterministic Pattern Matcher (Regular Expression Matching)

## Approach Explanation
We use Dynamic Programming. `dp[i][j]` represents whether `s[i:]` matches `p[j:]`.

## Step-by-Step Logic
1. Use recursion with memoization (top-down DP).
2. Base Case: If `p` is empty, return `True` if `s` is also empty.
3. First Match: Check if `s[0]` matches `p[0]` (including `.` case).
4. If `p[1] == '*'`:
   - Case 1: Ignore `*` and preceding (zero occurrence): `match(s, p[2:])`.
   - Case 2: Use `*` once (if first match exists): `first_match and match(s[1:], p)`.
5. Else: Return `first_match and match(s[1:], p[1:])`.

## Complexity
- **Time Complexity:** O(N * M).
- **Space Complexity:** O(N * M).

## Code
```python
def is_match(s, p):
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo: return memo[(i, j)]
        if j == len(p): return i == len(s)
        
        first_match = i < len(s) and p[j] in {s[i], '.'}
        
        if j + 1 < len(p) and p[j + 1] == '*':
            ans = (dp(i, j + 2) or 
                   (first_match and dp(i + 1, j)))
        else:
            ans = first_match and dp(i + 1, j + 1)
            
        memo[(i, j)] = ans
        return ans
        
    return dp(0, 0)
```
