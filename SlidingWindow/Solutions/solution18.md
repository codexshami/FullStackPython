# Solution 18: Cognitive Temperance (Grumpy Bookstore Owner)

## Approach Explanation
We first calculate the customers satisfied regardless of the technique. Then we use a sliding window of size `minutes` to find which interval, if satisfied, adds the maximum "bonus" customers.

## Step-by-Step Logic
1. `satisfied = sum(customers[i] for i in if grumpy[i] == 0)`.
2. Initial `bonus = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)`.
3. `max_bonus = bonus`.
4. Slide the window from `minutes` to `n-1`:
   - If `grumpy[r] == 1`, `bonus += customers[r]`.
   - If `grumpy[l] == 1`, `bonus -= customers[l]`.
   - Update `max_bonus`.
5. Return `satisfied + max_bonus`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def max_satisfied(customers, grumpy, minutes):
    satisfied = 0
    for i in range(len(customers)):
        if grumpy[i] == 0:
            satisfied += customers[i]
            
    bonus = 0
    for i in range(minutes):
        if grumpy[i] == 1:
            bonus += customers[i]
            
    max_bonus = bonus
    for i in range(minutes, len(customers)):
        if grumpy[i] == 1:
            bonus += customers[i]
        if grumpy[i - minutes] == 1:
            bonus -= customers[i - minutes]
        max_bonus = max(max_bonus, bonus)
        
    return satisfied + max_bonus
```
