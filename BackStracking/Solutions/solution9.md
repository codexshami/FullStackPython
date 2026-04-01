# Solution 9: The Phone Decoder (Letter Combinations of Phone Number)

## Approach Explanation
We map each digit to its corresponding letters and use backtracking to generate all combinations by picking one letter from each digit's mapping.

## Step-by-Step Logic
1. Create a digit-to-letters mapping.
2. Start with an empty string and index 0.
3. For each digit, iterate through its letters.
4. Append a letter and recurse to the next digit.
5. When the combination length equals the digits length, save it.

## Complexity
- **Time Complexity:** O(4^N) where N is the number of digits.
- **Space Complexity:** O(N) for the recursion stack.

## Code
```python
def letter_combinations(digits):
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    result = []
    
    def backtrack(index, current):
        if index == len(digits):
            result.append(current)
            return
        for letter in phone_map[digits[index]]:
            backtrack(index + 1, current + letter)
    
    backtrack(0, '')
    return result
```
