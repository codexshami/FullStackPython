# Solution 19: Modular Summation (Subarray Sums Divisible by K)

## Approach Explanation
Similar to "Subarray Sum Equals K", but we track the remainder of the prefix sum when divided by `k`. If two prefix sums have the same remainder, the subarray between them is divisible by `k`.

## Step-by-Step Logic
1. Initialize `remainders = {0: 1}`, `curr_sum = 0`, `count = 0`.
2. For each `num` in `nums`:
   - `curr_sum += num`.
   - `rem = curr_sum % k`.
   - If `rem` in `remainders`:
     - `count += remainders[rem]`.
   - `remainders[rem] = remainders.get(rem, 0) + 1`.
3. Return `count`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(K).

## Code
```python
def subarrays_div_by_k(nums, k):
    res = 0
    prefix_sum = 0
    count = {0: 1}
    
    for n in nums:
        prefix_sum += n
        rem = prefix_sum % k
        if rem in count:
            res += count[rem]
        count[rem] = count.get(rem, 0) + 1
        
    return res
```
