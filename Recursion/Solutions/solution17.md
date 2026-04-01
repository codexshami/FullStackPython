# Solution 17: The Greatest Divider (GCD using Recursion)

## Approach Explanation
We apply the Euclidean algorithm: `GCD(a, b) = GCD(b, a % b)`. The recursion terminates when `b == 0`, at which point `a` is the GCD.

## Step-by-Step Logic
1. Base case: If `b == 0`, return `a`.
2. Recursive step: Return `gcd(b, a % b)`.

## Complexity
- **Time Complexity:** O(log(min(a, b))).
- **Space Complexity:** O(log(min(a, b))) (recursion stack).

## Code
```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
```
