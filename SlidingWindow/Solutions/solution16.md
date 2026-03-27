# Solution 16: Sequential Inclusion Span (Minimum Window Subsequence)

## Approach Explanation
We use a two-pointer approach with a "backwards check" optimization. When we find a valid subsequence in `s1` ending at `r`, we move backwards from `r` to find the best (rightmost) starting `l` for that subsequence. This helps find the minimum window.

## Step-by-Step Logic
1. `s1_ptr = 0`, `s2_ptr = 0`, `min_len = float('inf')`, `res = ""`.
2. Iterate `s1_ptr` through `s1`:
   - If `s1[s1_ptr] == s2[s2_ptr]`, increment `s2_ptr`.
   - If `s2_ptr == len(s2)` (found a valid subsequence):
     - Start a `back_ptr` at `s1_ptr` and move `s2_ptr` backwards from `len(s2)-1` to `0`.
     - Find the starting index `l` in `s1`.
     - Update `min_len` and `res`.
     - Reset `s1_ptr = l + 1`, `s2_ptr = 0`.
3. Return `res`.

## Complexity
- **Time Complexity:** O(N * M) worst case, but efficient in practice.
- **Space Complexity:** O(1).

## Code
```python
def min_window(s1, s2):
    n1, n2 = len(s1), len(s2)
    s1_idx = 0
    s2_idx = 0
    res = ""
    min_len = float('inf')
    
    while s1_idx < n1:
        if s1[s1_idx] == s2[s2_idx]:
            s2_idx += 1
            if s2_idx == n2:
                # Found a valid end. Go backward to find best start.
                end = s1_idx
                s2_idx -= 1
                while s2_idx >= 0:
                    if s1[s1_idx] == s2[s2_idx]:
                        s2_idx -= 1
                    s1_idx -= 1
                s1_idx += 1
                
                # Check min_len
                if end - s1_idx + 1 < min_len:
                    min_len = end - s1_idx + 1
                    res = s1[s1_idx : end + 1]
                    
                s2_idx = 0
        s1_idx += 1
        
    return res
```
