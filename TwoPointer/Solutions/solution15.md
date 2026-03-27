# Solution 15: Optimal Vessel Occupancy (Boats to Save People)

## Approach Explanation
To minimize boats, we should pair the heaviest person with the lightest person if possible. If the sum exceeds the limit, the heaviest person must go in a boat alone.

## Step-by-Step Logic
1. Sort `people`.
2. `l = 0`, `r = len(people) - 1`, `boats = 0`.
3. While `l <= r`:
   - If `people[l] + people[r] <= limit`:
     - `l += 1` (pair found).
   - `r -= 1` (heavy person always takes a boat).
   - `boats += 1`.
4. Return `boats`.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(1).

## Code
```python
def num_rescue_boats(people, limit):
    people.sort()
    l, r = 0, len(people) - 1
    boats = 0
    
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
        r -= 1
        boats += 1
        
    return boats
```
