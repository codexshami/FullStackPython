# Solution 15: The Combination Picker (Combinations)

## Approach Explanation
We build combinations by picking elements from left to right. Starting from 1, at each step we either pick the current number or skip it, always moving forward.

## Step-by-Step Logic
1. Start with an empty combination and the number 1.
2. Add the current number and recurse for the next.
3. When the combination has `k` elements, save it.
4. Backtrack by removing the last number.

## Complexity
- **Time Complexity:** O(C(n, k) * k).
- **Space Complexity:** O(k).

## Code
```python
def combine(n, k):
    result = []
    
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        for i in range(start, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(1, [])
    return result
```
