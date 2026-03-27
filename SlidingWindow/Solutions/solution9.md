# Solution 9: Orchard Greedy Strategy (Fruit Into Baskets)

## Approach Explanation
This is equivalent to finding the "Longest Subarray with at most 2 Distinct Elements". We use a sliding window and a hash map to track the types of fruits in our baskets.

## Step-by-Step Logic
1. `l = 0`, `res = 0`, `count = {}`.
2. For each `r`:
   - `count[fruits[r]] = count.get(fruits[r], 0) + 1`.
   - While `len(count) > 2`:
     - `count[fruits[l]] -= 1`.
     - If `count[fruits[l]] == 0`, delete from map.
     - `l += 1`.
   - `res = max(res, r - l + 1)`.
3. Return `res`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1) (map of size 3).

## Code
```python
def total_fruit(fruits):
    count = {}
    l = 0
    res = 0
    for r in range(len(fruits)):
        count[fruits[r]] = 1 + count.get(fruits[r], 0)
        while len(count) > 2:
            count[fruits[l]] -= 1
            if count[fruits[l]] == 0:
                del count[fruits[l]]
            l += 1
        res = max(res, r - l + 1)
    return res
```
