# Solution 14: Resource Balancing Strategy (Bag of Tokens)

## Approach Explanation
We should use power on the smallest tokens (face up) to gain score, and use score on the largest tokens (face down) to gain the most power. This greedy approach works perfectly with Two Pointers on a sorted array.

## Step-by-Step Logic
1. Sort `tokens`.
2. `l = 0`, `r = len(tokens) - 1`, `score = 0`, `max_score = 0`.
3. While `l <= r`:
   - If `power >= tokens[l]`:
     - `power -= tokens[l]`, `score += 1`, `l += 1`, `max_score = max(max_score, score)`.
   - Else if `score > 0`:
     - `power += tokens[r]`, `score -= 1`, `r -= 1`.
   - Else:
     - Break.
4. Return `max_score`.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(1).

## Code
```python
def bag_of_tokens_score(tokens, power):
    tokens.sort()
    l, r = 0, len(tokens) - 1
    score = 0
    res = 0
    
    while l <= r:
        if power >= tokens[l]:
            power -= tokens[l]
            score += 1
            l += 1
            res = max(res, score)
        elif score > 0:
            power += tokens[r]
            score -= 1
            r -= 1
        else:
            break
            
    return res
```
