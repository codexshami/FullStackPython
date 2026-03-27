# Solution 5: Consensus Prefix (Longest Common Prefix)

## Approach Explanation
We take the first string as our initial prefix and repeatedly prune it from the end whenever it doesn't match the start of the next string in the array.

## Step-by-Step Logic
1. If `strs` is empty, return "".
2. Set `prefix = strs[0]`.
3. For each string `s` in `strs[1:]`:
   - While `s` does not start with `prefix`:
     - Shorten `prefix` by removing the last character.
     - If `prefix` becomes empty, return "".
4. Return `prefix`.

## Complexity
- **Time Complexity:** O(S), where S is the sum of all characters in all strings.
- **Space Complexity:** O(1).

## Code
```python
def longest_common_prefix(strs):
    if not strs: return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix: return ""
            
    return prefix
```
