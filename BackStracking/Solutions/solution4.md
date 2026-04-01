# Solution 4: The Combination Lock (Combination Sum)

## Approach Explanation
We use backtracking to explore all combinations. Since the same number can be reused, we don't increment the index when we include a candidate. We prune branches where the remaining target becomes negative.

## Step-by-Step Logic
1. Sort candidates to enable early termination.
2. Start with an empty combination and the full target.
3. For each candidate from the current index, subtract it from the target.
4. If target becomes 0, save the combination.
5. If target goes negative, break (since candidates are sorted).
6. Recurse with the same index (allowing reuse).

## Complexity
- **Time Complexity:** O(N^(T/M)) where T is target, M is minimum candidate.
- **Space Complexity:** O(T/M) for recursion depth.

## Code
```python
def combination_sum(candidates, target):
    result = []
    candidates.sort()
    
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])
            current.pop()
    
    backtrack(0, [], target)
    return result
```
