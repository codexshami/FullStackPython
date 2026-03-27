# Solution 8: Prefix Sum Congruence (Subarray Sum Equals K)

## Approach Explanation
We use the concept of Prefix Sums. If the sum from index `0` to `i` is `S1` and the sum from index `0` to `j` is `S2`, then the sum of the subarray from `i+1` to `j` is `S2 - S1`. We want `S2 - S1 = k`, which means `S1 = S2 - k`. We use a hash map to store the frequencies of prefix sums.

## Step-by-Step Logic
1. Initialize `count = 0`, `curr_sum = 0`.
2. `prefix_sums = {0: 1}` (Base case: a sum of 0 has appeared 1 time).
3. Iterate through `nums`:
   - `curr_sum += num`.
   - If `curr_sum - k` is in `prefix_sums`:
     - `count += prefix_sums[curr_sum - k]`.
   - `prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1`.
4. Return `count`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
def subarray_sum(nums, k):
    count = 0
    curr_sum = 0
    prefix_sums = {0: 1}
    
    for n in nums:
        curr_sum += n
        if curr_sum - k in prefix_sums:
            count += prefix_sums[curr_sum - k]
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        
    return count
```
