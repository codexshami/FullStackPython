# Solution 17: Selective Phoneme Inversion (Reverse Vowels of a String)

## Approach Explanation
We use two pointers `l` and `r` at the ends of the string. We skip non-vowel characters and swap the vowels at `l` and `r`.

## Step-by-Step Logic
1. Convert string to list `s_list`.
2. `l = 0`, `r = len(s) - 1`.
3. `vowels = set("aeiouAEIOU")`.
4. While `l < r`:
   - While `l < r` and `s_list[l]` not in `vowels`: `l += 1`.
   - While `l < r` and `s_list[r]` not in `vowels`: `r -= 1`.
   - Swap `s_list[l]` and `s_list[r]`.
   - `l += 1`, `r -= 1`.
5. Return `"`.join(s_list)`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N) (due to list conversion).

## Code
```python
def reverse_vowels(s):
    vowels = set("aeiouAEIOU")
    s = list(s)
    l, r = 0, len(s) - 1
    
    while l < r:
        if s[l] not in vowels:
            l += 1
        elif s[r] not in vowels:
            r -= 1
        else:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            
    return "".join(s)
```
