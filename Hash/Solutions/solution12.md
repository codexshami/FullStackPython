# Solution 12: Frequency-Weighted Ordering (Sort Characters By Frequency)

## Approach Explanation
We count the frequencies of characters using a hash map, then sort the characters based on their values in the map in descending order.

## Step-by-Step Logic
1. `counts = Counter(s)`.
2. Get the unique characters and sort them by frequency (descending) and then lexicographically (to be consistent).
3. Build the result string by repeating each character its frequency times.

## Complexity
- **Time Complexity:** O(N + K log K), where K is number of unique characters.
- **Space Complexity:** O(N).

## Code
```python
from collections import Counter

def frequency_sort(s):
    count = Counter(s)
    # Sort characters by frequency (descending)
    sorted_chars = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    res = []
    for char, freq in sorted_chars:
        res.append(char * freq)
        
    return "".join(res)
```
