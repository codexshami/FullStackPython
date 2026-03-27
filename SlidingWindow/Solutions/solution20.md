# Solution 20: Vowel Density Search (Maximum Number of Vowels in a Substring of Given Length)

## Approach Explanation
This is a straightforward fixed-size sliding window problem. We maintain a count of vowels in the current window of size `k`.

## Step-by-Step Logic
1. Vowels set: `{'a', 'e', 'i', 'o', 'u'}`.
2. Calculate vowels in the first `k` characters.
3. `res = count`.
4. Slide the window:
   - If incoming char is vowel, `count += 1`.
   - If outgoing char is vowel, `count -= 1`.
   - `res = max(res, count)`.
5. Return `res`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def max_vowels(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for i in range(k):
        if s[i] in vowels:
            count += 1
            
    res = count
    for i in range(k, len(s)):
        if s[i] in vowels:
            count += 1
        if s[i - k] in vowels:
            count -= 1
        res = max(res, count)
        
    return res
```
