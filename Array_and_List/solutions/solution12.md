# Solution 12: Railway Station Congestion

## Approach Explanation
We treat arrival and departure events as points on a timeline. By sorting both arrays, we can use two pointers to count how many trains are in the station at any point. When a train arrives, we increase the platform count; when a train departs, we decrease it.

## Step-by-Step Logic
1. Sort both `arrival` and `departure` arrays.
2. Initialize `platforms_needed = 0`, `max_platforms = 0`.
3. Initialize two pointers: `i = 0` (for arrival) and `j = 0` (for departure).
4. While `i < n`:
   - If `arrival[i] <= departure[j]`:
     - `platforms_needed += 1`
     - Update `max_platforms = max(max_platforms, platforms_needed)`
     - `i += 1`
   - Else:
     - `platforms_needed -= 1`
     - `j += 1`
5. Return `max_platforms`.

## Complexity
- **Time Complexity:** O(N log N) because of sorting.
- **Space Complexity:** O(1), assuming sorting is in-place or ignoring it.

## Code
```python
def min_platforms(arrival, departure):
    arrival.sort()
    departure.sort()
    
    n = len(arrival)
    i, j = 0, 0
    platforms_needed = 0
    max_platforms = 0
    
    while i < n:
        # If train is arriving before or at the time another train departs
        if arrival[i] <= departure[j]:
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:
            # Train departed, platform free
            platforms_needed -= 1
            j += 1
            
    return max_platforms
```
