# Solution 4: Parity Singularity (Single Number)

## Approach Explanation
While the hash-based approach (using a frequency map or set) is intuitive, the constraint of O(1) space suggests using Bit Manipulation (XOR).
Property of XOR: `a ^ a = 0` and `a ^ 0 = a`.

## Step-by-Step Logic
1. Initialize `res = 0`.
2. For every `num` in `nums`:
   - `res ^= num`.
3. Return `res`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def single_number(nums):
    res = 0
    for n in nums:
        res ^= n
    return res
```
