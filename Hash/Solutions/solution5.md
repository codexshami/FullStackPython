# Solution 5: Proximity Constraint (Contains Duplicate II)

## Approach Explanation
We use a hash map to store the index of each number. Every time we encounter a number that is already in the map, we check if the difference between current index and stored index is `<= k`.

## Step-by-Step Logic
1. Initialize `seen = {}`.
2. For `i, num` in `enumerate(nums)`:
   - If `num` in `seen` and `i - seen[num] <= k`:
     - Return True.
   - `seen[num] = i`.
3. Return False.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
def contains_nearby_duplicate(nums, k):
    seen = {}
    for i, n in enumerate(nums):
        if n in seen and i - seen[n] <= k:
            return True
        seen[n] = i
    return False
```
