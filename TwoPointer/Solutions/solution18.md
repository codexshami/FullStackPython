# Solution 18: Subsequence Validation Span (Longest Word in Dictionary through Deleting)

## Approach Explanation
For each word in the dictionary, we check if it is a subsequence of `s` using Two Pointers. We update the result based on the length and lexicographical order.

## Step-by-Step Logic
1. `res = ""`.
2. For each `word` in `dictionary`:
   - `i = 0` (for `word`), `j = 0` (for `s`).
   - While `i < len(word)` and `j < len(s)`:
     - If `word[i] == s[j]`, `i += 1`.
     - `j += 1`.
   - If `i == len(word)` (subsequence found):
     - If `len(word) > len(res)` or (`len(word) == len(res)` and `word < res`):
       - `res = word`.
3. Return `res`.

## Complexity
- **Time Complexity:** O(N * M) where N is dictionary size and M is avg length of s.
- **Space Complexity:** O(1).

## Code
```python
def find_longest_word(s, dictionary):
    res = ""
    for word in dictionary:
        i = 0
        for char in s:
            if i < len(word) and word[i] == char:
                i += 1
        
        if i == len(word):
            if len(word) > len(res) or (len(word) == len(res) and word < res):
                res = word
                
    return res
```
