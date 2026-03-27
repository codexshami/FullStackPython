# Solution 10: Retroactive Erasure (Backspace String Compare)

## Approach Explanation
To achieve O(1) space, we iterate through the strings from the end. We keep track of the number of backspaces ('#') encountered to determine which characters effectively exist.

## Step-by-Step Logic
1. Define a helper function to find the next valid character index by scanning backwards and accounting for `#`.
2. Start pointers `i` and `j` at the ends of `s` and `t`.
3. In a loop:
   - Find next valid char in `s` and `t`.
   - If one string ends and other doesn't, return False.
   - If both characters are valid and differ, return False.
   - Decrement pointers.
4. Return True.

## Complexity
- **Time Complexity:** O(N + M).
- **Space Complexity:** O(1).

## Code
```python
def backspace_compare(s, t):
    def get_next_valid_index(string, index):
        backspace = 0
        while index >= 0:
            if string[index] == '#':
                backspace += 1
            elif backspace > 0:
                backspace -= 1
            else:
                break
            index -= 1
        return index

    i, j = len(s) - 1, len(t) - 1
    while i >= 0 or j >= 0:
        i = get_next_valid_index(s, i)
        j = get_next_valid_index(t, j)

        if i < 0 and j < 0:
            return True
        if i < 0 or j < 0 or s[i] != t[j]:
            return False
            
        i -= 1
        j -= 1
    return True
```
