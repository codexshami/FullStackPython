# Solution 17: Typographic Alignment (Text Justification)

## Approach Explanation
We process words line-by-line using a greedy approach. For each line, we calculate how many spaces are needed and distribute them according to the rules (even distribution, more on the left, or left-justified for the last line).

## Step-by-Step Logic
1. `res = []`, `curr_line = []`, `line_len = 0`.
2. For each `word` in `words`:
   - If `line_len + len(word) + len(curr_line) > maxWidth`:
     - Distribute spaces for `curr_line` and append to `res`.
     - Reset `curr_line = [word]`, `line_len = len(word)`.
   - Else:
     - `curr_line.append(word)`, `line_len += len(word)`.
3. Handle last line: left-justify and pad with trailing spaces.
4. Space Distribution (Normal Line):
   - Total spaces = `maxWidth - line_len`.
   - If only 1 word: left-justify with trailing spaces.
   - Else:
     - `spaces_between = total_spaces // (len(curr_line) - 1)`
     - `extra_spaces = total_spaces % (len(curr_line) - 1)`
     - Construct line by joining words with calculated spaces.

## Complexity
- **Time Complexity:** O(N), where N is total characters across all words.
- **Space Complexity:** O(N) for storing the result.

## Code
```python
def full_justify(words, maxWidth):
    res, curr, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(curr) > maxWidth:
            # Full justify the current line
            for i in range(maxWidth - num_of_letters):
                curr[i % (len(curr) - 1 or 1)] += ' '
            res.append("".join(curr))
            curr, num_of_letters = [], 0
        curr.append(w)
        num_of_letters += len(w)
        
    return res + [" ".join(curr).ljust(maxWidth)]
```
