# Solution 20: Antiquated Numerology (Roman to Integer)

## Approach Explanation
We iterate through the string and add the value of each symbol to the total. If a smaller symbol appears before a larger one, we subtract it instead of adding it.

## Step-by-Step Logic
1. Map characters `I, V, X, L, C, D, M` to values.
2. Initialize `total = 0`, `prev_val = 0`.
3. Iterate through characters in reverse:
   - If `curr_val >= prev_val`, `total += curr_val`.
   - Else, `total -= curr_val`.
   - Update `prev_val`.
4. Return `total`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def roman_to_int(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev_val = 0
    
    for char in reversed(s):
        curr_val = d[char]
        if curr_val >= prev_val:
            res += curr_val
        else:
            res -= curr_val
        prev_val = curr_val
        
    return res
```
