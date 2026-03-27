# Solution 20: Identity Retrieval (Single Number II)

## Approach Explanation
To solve this in O(1) space, we can use Bit Manipulation to count the number of 1-bits at each position (0-31). Since every number appears 3 times except for one, the sum of bits at each position modulo 3 will reveal the bits of the single number.

## Step-by-Step Logic
1. Initialize `ans = 0`.
2. Iterate through `i` from 0 to 31:
   - `count = 0`.
   - For every `num` in `nums`:
     - If the `i`-th bit of `num` is 1, `count += 1`.
   - `count %= 3`.
   - If `count == 1`, set the `i`-th bit of `ans`.
3. Handle negative numbers (Python integers are infinite, so bits are tricky).

## Complexity
- **Time Complexity:** O(32 * N) = O(N).
- **Space Complexity:** O(1).

## Code
```python
def single_number(nums):
    ones, twos = 0, 0
    for n in nums:
        ones = (ones ^ n) & (~twos)
        twos = (twos ^ n) & (~ones)
    return ones
```
*(Note: The `ones`/`twos` approach is a more elegant bitwise state-machine version of the bit-counting logic).*
