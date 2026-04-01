# Solution 10: The Partition Artist (Palindrome Partitioning)

## Approach Explanation
We try every possible prefix of the string. If it's a palindrome, we add it to the current partition and recurse on the remaining substring. We backtrack when we've exhausted the string.

## Step-by-Step Logic
1. Start from index 0 with an empty partition.
2. For each position, check all substrings starting from the current index.
3. If the substring is a palindrome, add it to the current partition.
4. Recurse on the remaining string.
5. When the index reaches the end, save the partition.

## Complexity
- **Time Complexity:** O(N * 2^N).
- **Space Complexity:** O(N).

## Code
```python
def partition(s):
    result = []
    
    def is_palindrome(sub):
        return sub == sub[::-1]
    
    def backtrack(start, current):
        if start == len(s):
            result.append(current[:])
            return
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                current.append(substring)
                backtrack(end, current)
                current.pop()
    
    backtrack(0, [])
    return result
```
