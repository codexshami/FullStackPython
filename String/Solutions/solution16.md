# Solution 16: Permissive Pattern Matcher (Wildcard Matching)

## Approach Explanation
This can be solved with DP or a greedy two-pointer approach with backtracking. The greedy approach is faster for wildcard matching.

## Step-by-Step Logic
1. `s_ptr = 0`, `p_ptr = 0`, `star_ptr = -1`, `s_tmp = -1`.
2. While `s_ptr < len(s)`:
   - If `p_ptr < len(p)` and `p[p_ptr]` is `s[s_ptr]` or `?`: Increment both.
   - Else if `p_ptr < len(p)` and `p[p_ptr]` is `*`: Mark `star = p_ptr`, `tmp_s = s_ptr`. Increment `p_ptr`.
   - Else if `star_ptr != -1`: (Mismatch but we saw a `*`): Backtrack `p_ptr = star_ptr + 1`, `s_tmp += 1`, `s_ptr = s_tmp`.
   - Else: return False.
3. Check remaining `p` characters: must all be `*`.

## Complexity
- **Time Complexity:** O(N * M) worst case, but near O(N + M) average.
- **Space Complexity:** O(1).

## Code
```python
def is_wildcard_match(s, p):
    s_ptr = p_ptr = 0
    star_idx = s_tmp_idx = -1
    
    while s_ptr < len(s):
        # Case 1: Match or ?
        if p_ptr < len(p) and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
            s_ptr += 1
            p_ptr += 1
        # Case 2: *
        elif p_ptr < len(p) and p[p_ptr] == '*':
            star_idx = p_ptr
            s_tmp_idx = s_ptr
            p_ptr += 1
        # Case 3: Mismatch, use last *
        elif star_idx != -1:
            p_ptr = star_idx + 1
            s_tmp_idx += 1
            s_ptr = s_tmp_idx
        else:
            return False
            
    # Trailing * in p
    return all(x == '*' for x in p[p_ptr:])
```
