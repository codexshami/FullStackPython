# Solution 7: Lexical Integer Extraction (atoi)

## Approach Explanation
We process the string step-by-step: trimming, checking sign, and then accumulating digits while checking for overflow.

## Step-by-Step Logic
1. `s = s.lstrip()`. If empty, return 0.
2. Check first character for `+` or `-`. Set `sign`.
3. Iterate through characters:
   - If character is a digit, add to `res`.
   - If not a digit, stop.
4. Apply `sign`.
5. Clamp result to `[-2^31, 2^31 - 1]`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def my_atoi(s):
    s = s.strip()
    if not s: return 0
    
    sign = 1
    i = 0
    if s[0] == '-':
        sign = -1
        i = 1
    elif s[0] == '+':
        i = 1
        
    res = 0
    while i < len(s) and s[i].isdigit():
        res = res * 10 + int(s[i])
        i += 1
        
    res *= sign
    
    # Clamping
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if res > INT_MAX: return INT_MAX
    if res < INT_MIN: return INT_MIN
    
    return res
```
