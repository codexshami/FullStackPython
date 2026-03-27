# Solution 7: Bimodal Continuity (Longest Harmonic Subsequence)

## Approach Explanation
A harmonic subsequence consists of only two numbers `x` and `x+1`. We can count the frequency of each number using a hash map and then find the maximum `count(x) + count(x+1)`.

## Step-by-Step Logic
1. Count frequencies of all numbers in `nums` using `Counter`.
2. `max_len = 0`.
3. For each `x` in the counter:
   - If `x + 1` is also in the counter:
     - `max_len = max(max_len, count[x] + count[x+1])`.
4. Return `max_len`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
from collections import Counter

def find_lhs(nums):
    counts = Counter(nums)
    max_len = 0
    for x in counts:
        if x + 1 in counts:
            max_len = max(max_len, counts[x] + counts[x + 1])
    return max_len
```
