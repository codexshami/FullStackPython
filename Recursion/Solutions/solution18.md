# Solution 18: The Permutation Machine (String Permutations)

## Approach Explanation
We fix each character at the first position and recursively compute permutations of the remaining characters. We collect all combinations.

## Step-by-Step Logic
1. Base case: If the string has length 1, return [s].
2. For each character in the string:
   - Remove it from the string.
   - Recursively find all permutations of the remaining string.
   - Prepend the removed character to each permutation.
3. Return all permutations.

## Complexity
- **Time Complexity:** O(N! * N).
- **Space Complexity:** O(N!) to store all permutations.

## Code
```python
def permutations(s):
    if len(s) == 1:
        return [s]
    
    result = []
    for i, char in enumerate(s):
        remaining = s[:i] + s[i+1:]
        for perm in permutations(remaining):
            result.append(char + perm)
    return result
```
