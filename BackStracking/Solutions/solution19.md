# Solution 19: The Additive Split (Splitting String Into Descending Consecutive Values)

## Approach Explanation
We try every possible first number by taking prefixes of the string. Then we check if the rest of the string can be split into consecutive decreasing values.

## Step-by-Step Logic
1. For each possible first number (prefix of `s`):
2. Try to match the next consecutive value (first_num - 1) as the next substring.
3. Recurse with the remaining string and the next expected value.
4. If we reach the end of the string with at least 2 parts, return True.

## Complexity
- **Time Complexity:** O(N^2) in worst case.
- **Space Complexity:** O(N).

## Code
```python
def split_string(s):
    def backtrack(index, prev, count):
        if index == len(s):
            return count >= 2
        
        num = 0
        for i in range(index, len(s)):
            num = num * 10 + int(s[i])
            if num >= prev:
                break
            if prev - num == 1 or count == 0:
                if count == 0:
                    if backtrack(i + 1, num, 1):
                        return True
                elif prev - num == 1:
                    if backtrack(i + 1, num, count + 1):
                        return True
        return False
    
    # Try each possible first number
    num = 0
    for i in range(len(s) - 1):
        num = num * 10 + int(s[i])
        if backtrack(i + 1, num, 1):
            return True
    return False
```
