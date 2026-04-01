# Solution 16: The Binary Decoder (Decimal to Binary)

## Approach Explanation
We repeatedly divide the number by 2 and build the binary string from the remainders using recursion.

## Step-by-Step Logic
1. Base case: If `n == 0`, return "0". If `n == 1`, return "1".
2. Recursive step: Return `decimal_to_binary(n // 2)` + `str(n % 2)`.

## Complexity
- **Time Complexity:** O(log N).
- **Space Complexity:** O(log N) (recursion stack).

## Code
```python
def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)
```
