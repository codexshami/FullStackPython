# Solution 19: Vernacular Transcription (Integer to English Words)

## Approach Explanation
We process the number in groups of three digits (billions, millions, thousands, and hundreds). For each group, we use helper functions to convert the number to words.

## Step-by-Step Logic
1. Create word mappings for `LESS_THAN_20`, `TENS`, and `THOUSANDS`.
2. Implement `helper(n)` which handles numbers < 1000.
3. In main function:
   - Handle 0.
   - For `THOUSANDS` indices (0 to 3):
     - If `num % 1000 != 0`, calculate `helper(num % 1000) + label + result`.
     - `num //= 1000`.
4. Return trimmed result.

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(log N).

## Code
```python
def number_to_words(num):
    if num == 0: return "Zero"
    
    less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]
    
    def helper(n):
        if n == 0: return ""
        elif n < 20: return less_than_20[n] + " "
        elif n < 100: return tens[n // 10] + " " + helper(n % 10)
        else: return less_than_20[n // 100] + " Hundred " + helper(n % 100)
        
    res = ""
    for i in range(len(thousands)):
        if num % 1000 != 0:
            res = helper(num % 1000) + thousands[i] + " " + res
        num //= 1000
        
    return res.strip()
```
