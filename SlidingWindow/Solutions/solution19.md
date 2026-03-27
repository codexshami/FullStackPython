# Solution 19: Boundary Selection Strategy (Maximum Points You Can Obtain from Cards)

## Approach Explanation
Taking `k` cards from the ends is equivalent to leaving a contiguous subarray of size `n - k` in the middle! To maximize the sum of `k` cards, we must minimize the sum of the `n - k` cards left in the middle.

## Step-by-Step Logic
1. `n = len(cardPoints)`, `window_size = n - k`.
2. If `k == n`, return `sum(cardPoints)`.
3. Total sum of all cards.
4. Use sliding window to find the minimum sum of any subarray of size `window_size`.
5. Return `total_sum - min_subarray_sum`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def max_score(cardPoints, k):
    n = len(cardPoints)
    window_size = n - k
    
    curr = sum(cardPoints[:window_size])
    min_sum = curr
    total = sum(cardPoints)
    
    for i in range(window_size, n):
        curr += cardPoints[i] - cardPoints[i - window_size]
        min_sum = min(min_sum, curr)
        
    return total - min_sum
```
