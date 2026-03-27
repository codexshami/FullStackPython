# Solution 8: Nested Syntax Unrolling (Decode String - Recursive Edition)

## Approach Explanation
We process characters one by one. When we see a digit, we parse the full number `k`. When we see `[`, we recurse to decode the inner content. When we see `]`, we return from the current recursion.

## Step-by-Step Logic
1. Use an index pointer `i` that is shared or passed across recursion.
2. `solve()`:
   - Initialize `res = ""`.
   - While `i < len(s)` and `s[i] != ']'`:
     - If `s[i]` is not a digit: `res += s[i]`, `i += 1`.
     - If `s[i]` is a digit:
       - Parse `k`.
       - `i += 1` (skip `[`).
       - `inner_str = solve()`.
       - `i += 1` (skip `]`).
       - `res += inner_str * k`.
   - Return `res`.

## Complexity
- **Time Complexity:** O(N) where N is the length of decoded string.
- **Space Complexity:** O(N).

## Code
```python
def decode_string(s):
    def solve(i):
        res = ""
        while i < len(s) and s[i] != ']':
            if not s[i].isdigit():
                res += s[i]
                i += 1
            else:
                k = 0
                while i < len(s) and s[i].isdigit():
                    k = k * 10 + int(s[i])
                    i += 1
                i += 1 # skip '['
                inner, next_i = solve(i)
                i = next_i + 1 # skip ']'
                res += inner * k
        return res, i
        
    return solve(0)[0]
```
*(Alternative: Pass a list `[0]` as index to make it mutable).*
