# Solution 2: Singularity Detection

## Approach Explanation
We use a hash map (or fixed-size array) to count the frequency of each character. Then, we re-traverse the string to find the first character with a frequency of 1.

## Step-by-Step Logic
1. Count character frequencies in `s` using a `Counter`.
2. Iterate through `s` using its index `i`.
3. If `count[s[i]] == 1`, return `i`.
4. If loop finishes, return -1.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1) (since the alphabet size is constant).

## Code
```python
from collections import Counter

def first_uniq_char(s):
    counts = Counter(s)
    for i, char in enumerate(s):
        if counts[char] == 1:
            return i
    return -1
```
