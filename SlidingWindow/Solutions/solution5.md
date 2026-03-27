# Solution 5: Permutation Subsequence (Permutation in String)

## Approach Explanation
We use a sliding window of size `len(s1)` and compare character counts. We can optimize by tracking the number of "matches" (character counts that are exactly equal).

## Step-by-Step Logic
1. If `len(s1) > len(s2)`, return False.
2. Count frequencies of `s1` and the first `len(s1)` chars of `s2`.
3. Calculate initial `matches` (count of positions where `s1_count[i] == s2_count[i]`).
4. Slide the window:
   - Add new char: update matches.
   - Remove old char: update matches.
   - If `matches == 26`, return True.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1) (size 26 arrays).

## Code
```python
def check_inclusion(s1, s2):
    if len(s1) > len(s2): return False
    
    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1
        
    matches = 0
    for i in range(26):
        if s1Count[i] == s2Count[i]:
            matches += 1
            
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26: return True
        
        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1
            
        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1
        
    return matches == 26
```
